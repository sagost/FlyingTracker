# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FlyingTrackerDialog
								 A QGIS plugin
 Aerial survey tracker
							 -------------------
		begin				: 2015-03-09
		git sha			  : $Format:%H$
		copyright			: (C) 2015 by Salvatore Agosta / SAL Engineering
		email				: sagost@katamail.com
 ***************************************************************************/

/***************************************************************************
 *																		 *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or	 *
 *   (at your option) any later version.								   *
 *																		 *
 ***************************************************************************/
"""

import os
import glob

import serial
from qgis.core import QgsPoint, QgsRectangle, QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsMapLayerRegistry, QgsMapLayer, QgsGeometry, QgsVectorLayer, QgsField, QgsFeature 
from CanvasMarkers import PositionMarker
from PyQt4 import QtCore, QtGui, uic
from qgis.gui import QgsRubberBand , QgsVertexMarker
from geographiclib.geodesic import Geodesic
from geopy.distance import vincenty
import geopy
from geopy import Point
from threading import Thread
import re
import platform
import math


FORM_CLASS, _ = uic.loadUiType(os.path.join(
	os.path.dirname(__file__), 'flying_tracker_dialog_base.ui'))


class FlyingTrackerDialog(QtGui.QDockWidget, FORM_CLASS):
	def __init__(self,iface, parent=None):
		"""Constructor."""
		super(FlyingTrackerDialog, self).__init__(parent)
		
		self.setupUi(self)
		self.iface = iface
		
		self.course_comboBox.clear()
		self.lcdNumberWpt.display (1)
		
		self.GpsFixlcdNumber.display(0)
		self.SatelliteslcdNumber.display(0)
		
		self.pushButtonDisconnect.hide()		   
		self.pushButtonConnect.clicked.connect(self.Connect)
		self.pushButtonDisconnect.clicked.connect(self.Disconnect)
		self.pushCloseButton.clicked.connect(self.Close)
		self.LoadtoolButton.clicked.connect(self.FillComboBox)
		self.wptplus_toolButton.clicked.connect(self.NextWpt)
		self.wptmin_toolButton.clicked.connect(self.BackWpt)
		QtCore.QObject.connect(self.wptplus_toolButton, QtCore.SIGNAL("valueChanged(int)"), self.AdjNxtWpt)
		QtCore.QObject.connect(self.wptmin_toolButton, QtCore.SIGNAL("valueChanged(int)"), self.AdjNxtWpt)
		self.ZoomIntoolButton.clicked.connect(self.ZoomIn)
		self.ZoomOuttoolButton.clicked.connect(self.ZoomOut)
		
		shortcut = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_S), self.iface.mainWindow())
		shortcut.setContext(QtCore.Qt.ApplicationShortcut)
		shortcut.activated.connect(self.ZoomIn)
		shortcut2 = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_A), self.iface.mainWindow())
		shortcut2.setContext(QtCore.Qt.ApplicationShortcut)
		shortcut2.activated.connect(self.ZoomOut)
		shortcut3 = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_X), self.iface.mainWindow())
		shortcut3.setContext(QtCore.Qt.ApplicationShortcut)
		shortcut3.activated.connect(self.NextWpt)
		shortcut4 = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Z), self.iface.mainWindow())
		shortcut4.setContext(QtCore.Qt.ApplicationShortcut)
		shortcut4.activated.connect(self.BackWpt)
		
		self.timer = QtCore.QTimer()
		QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.SendSerial)
		
		self.NxtWptRubber = False
		self.PositionMarker = False
		self.RubberBand = False
		self.WptVertexSignal = False
		
		self.trackCounter = 4
			
			
	def AdjNxtWpt(self):	
		
		if self.WptVertexSignal == True:
			self.iface.mapCanvas().scene().removeItem(self.WptVertex)
			del self.WptVertex
			self.WptVertexSignal = False
		
		if self.NxtWptRubber == True:
			self.iface.mapCanvas().scene().removeItem(self.rdue)
			del self.rdue
			self.iface.mapCanvas().scene().removeItem(self.rtre)
			del self.rtre
			self.NxtWptRubber = False
			
		canvas = self.iface.mapCanvas()
		mapRenderer = canvas.mapRenderer()
		crsSrc = QgsCoordinateReferenceSystem(4326)    	# NMEA is in WGS 84
		crsDest = mapRenderer.destinationCrs()		
		xform = QgsCoordinateTransform(crsSrc, crsDest)
		
		WptValue = int(self.lcdNumberWpt.value())
		
		try:
			Wpt = self.pts[WptValue - 1]
				
		except IndexError:
			return
		
		self.WptVertex = QgsVertexMarker(self.iface.mapCanvas())
		self.WptVertex.setIconSize(20)
		self.WptVertex.setIconType(QgsVertexMarker.ICON_X)
		self.WptVertex.setPenWidth(20)
		self.WptVertex.setCenter(xform.transform(Wpt))
		self.WptVertexSignal = True

		if WptValue != 1:
			
			Wpt2 = self.pts[WptValue -2]
			self.rdue = QgsRubberBand(self.iface.mapCanvas(), False)          # False = not a polygon
			pointsdue = [xform.transform(Wpt), xform.transform(Wpt2)]
			
			self.rdue.setColor(QtGui.QColor(255,0,0))
			self.rdue.setWidth(8)
			self.rdue.setLineStyle(QtCore.Qt.PenStyle(QtCore.Qt.DotLine))
			self.rdue.setToGeometry(QgsGeometry.fromPolyline(pointsdue), None)                                  #creation of NextWayPoint rubberband
			
			
			self.rtre = QgsRubberBand(self.iface.mapCanvas(), False) 
			pointstre = self.pts[0:WptValue-1]
			
			for i in xrange(len(pointstre)):
					pointstre[i] = xform.transform(pointstre[i])
													
			
			self.rtre.setColor(QtGui.QColor(127,0,255))
			self.rtre.setWidth(8)
			self.rtre.setLineStyle(QtCore.Qt.PenStyle(QtCore.Qt.DotLine))
			self.rtre.setToGeometry(QgsGeometry.fromPolyline(pointstre), None)
			
			self.NxtWptRubber = True
			
				
	def Connect(self):
		
		try:
			
			self.positionMarker = PositionMarker(self.iface.mapCanvas())
			self.PositionMarker = True
			portName = self.comboBox.currentText()
			self.ser = serial.Serial(portName , 38400)
			layername = self.course_comboBox.itemData(self.course_comboBox.currentIndex())
			RouteLayer = QgsMapLayerRegistry.instance().mapLayer(layername)
			RouteLayer.selectAll()
			feats = RouteLayer.selectedFeatures()
			RouteLayer.removeSelection()
			feat = feats[0]
			geom = feat.geometry()
			self.pts = geom.asPolyline()
			SourceIntCRS = int(RouteLayer.crs().authid().split(':')[1])
			
			if SourceIntCRS != 4326:
				SourceIntCRS = int(RouteLayer.crs().authid().split(':')[1])
				SourceCRS = QgsCoordinateReferenceSystem(SourceIntCRS)
				DestCRS = QgsCoordinateReferenceSystem(4326)
				xformRouteLayer = QgsCoordinateTransform(SourceCRS, DestCRS)
				for i in xrange(len(self.pts)):
					x = self.pts[i][0]
					y = self.pts[i][1]														#if track layer is not in WGS84 Geographic every coordinate is transformed
					TmpPoint = QgsPoint(x,y)
					Tmp2Point = xformRouteLayer.transform(TmpPoint)
					self.pts[i] = Tmp2Point
			
				
			
			self.TrackLayer = QgsVectorLayer("Point?crs=epsg:4326&index=yes", "Flight_track", "memory")
			self.TrackLayerProvider = self.TrackLayer.dataProvider()
			self.TrackLayerProvider.addAttributes( [ QgsField("id", QtCore.QVariant.Int),
                                  QgsField('Time', QtCore.QVariant.String),
                                  QgsField('Ele', QtCore.QVariant.String),
                                   ] )
			
			QgsMapLayerRegistry.instance().addMapLayer( self.TrackLayer )       
			symbols = self.TrackLayer.rendererV2().symbols()
			symbol = symbols[0]
			symbol.setColor(QtGui.QColor(0,255,0))
			self.iface.legendInterface().refreshLayerSymbology(self.TrackLayer)
			
			if self.lcdNumberWpt.value() == 0:
				self.lcdNumberWpt.display(1)
				
			elif self.lcdNumberWpt.value() > len(self.pts):
				self.lcdNumberWpt.display(1)
				
			self.InRouteTolerance = float(self.DTrack_spinBox.value())      #if we are distant from route less than this value path become green, otherwise red
			self.CompassTolerance = self.DCompass_spinBox.value()       #if compass to next wpt confront to actual compass diverge less than this value projection of direction become green, otherwise red
			self.WptArrivedTolerance = float(self.DWpt_spinBox.value())   #if we pass near a wpt less than this value (in meters) the program will set the next wpt
			self.EleTolerance = float(self.DHeightspinBox.value())         #if our elevation diverge from planned elevation more than this value our cursor will be red, otherwise green
			
			canvas = self.iface.mapCanvas()
			mapRenderer = canvas.mapRenderer()
			crsSrc = QgsCoordinateReferenceSystem(4326)	# NMEA is in WGS 84
			crsDest = mapRenderer.destinationCrs()
				
			self.backxform = QgsCoordinateTransform(crsDest, crsSrc)
						
			self.xform = QgsCoordinateTransform(crsSrc, crsDest) #usage: xform.transform(QgsPoint) 
			self.AdjNxtWpt()	
			self.timer.start(1000)
			
		except:
			pass
		
		
	def SendSerial(self):
		thread = Thread(target = self.ReadSerial)
		thread.start()
		thread.join()
		
		
		
	def Disconnect(self,serialPort):
		
		self.timer.stop()
		self.lcdNumberSpeed.display(0)
		self.lcdNumberCompass.display(0)
		try:
			self.iface.mapCanvas().scene().removeItem(self.WptVertex)
			self.ser.close()
			self.iface.mapCanvas().scene().removeItem(self.r)
			self.iface.mapCanvas().scene().removeItem(self.runo)
			self.iface.mapCanvas().scene().removeItem(self.positionMarker)
			del self.WptVertex
			del self.r
			del self.runo
		except:
			pass
		
		
		self.iface.mapCanvas().setRotation(0)

		self.RubberBand = False
		
		if self.NxtWptRubber == True:
			self.iface.mapCanvas().scene().removeItem(self.rdue)
			self.iface.mapCanvas().scene().removeItem(self.rtre)
			del self.rdue
			del self.rtre
			self.NxtWptRubber = False
			
		else:
			pass
		
		self.WptVertexSignal = False
		self.lcdNumberHeights.display(0)
		self.lcdNumberSpeed.display(0)
		self.lcdNumberCompass.display(0)
		self.lcdCompassWpt.display(0)
		self.GpsFixlcdNumber.display(0)
		self.SatelliteslcdNumber.display(0)

		
	def FillComboBox(self):
		try:
			self.comboBox.clear()
			portlist = []
			system_name = platform.system()
			if system_name == "Windows":
			# Scan for available ports.
				available = []
				for i in range(256):
					try:
						s = serial.Serial(i)
						available.append(i)
						s.close()
					except serial.SerialException:										#Search for active serial port 
						pass
				#print available
				list1 = available
			elif system_name == "Darwin":
			# Mac
				#print glob.glob('/dev/tty*') + glob.glob('/dev/cu*')
				list1 = glob.glob('/dev/tty*') + glob.glob('/dev/cu*')
			else:
				# Assume Linux or something else
				#print glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*')
				list1 = glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*')
			for i in list1:
				try:
					serial.Serial(i).close()
					portlist.append(i)
				except IOError:
					pass
	
			for x in portlist:
				self.comboBox.addItem(x)
				
			self.course_comboBox.clear()
			
			LayerRegistryItem = QgsMapLayerRegistry.instance().mapLayers()
			for id, layer in LayerRegistryItem.iteritems():
				if layer.type() == QgsMapLayer.VectorLayer:
					self.course_comboBox.addItem(layer.name(), id)   
					
			layername = self.course_comboBox.itemData(self.course_comboBox.currentIndex())
			RouteLayer = QgsMapLayerRegistry.instance().mapLayer(layername)
			RouteLayer.selectAll()
			RouteLayer.featureCount()
			feats = RouteLayer.selectedFeatures()
			RouteLayer.removeSelection()
			feat = feats[0]
			geom = feat.geometry()
			self.pts = geom.asPolyline()
			SourceIntCRS = int(RouteLayer.crs().authid().split(':')[1])
			
			if SourceIntCRS != 4326:
				SourceIntCRS = int(RouteLayer.crs().authid().split(':')[1])
				SourceCRS = QgsCoordinateReferenceSystem(SourceIntCRS)
				DestCRS = QgsCoordinateReferenceSystem(4326)
				xformRouteLayer = QgsCoordinateTransform(SourceCRS, DestCRS)
				for i in xrange(len(self.pts)):
					x = self.pts[i][0]
					y = self.pts[i][1]														#if track layer is not in WGS84 Geographic every coordinate is transformed
					TmpPoint = QgsPoint(x,y)
					Tmp2Point = xformRouteLayer.transform(TmpPoint)
					self.pts[i] = Tmp2Point
			
			self.AdjNxtWpt()
		except:
			pass
		
	
	
	def Close (self):
		
		self.timer.stop()
		self.lcdNumberHeights.display(0)
		self.lcdNumberSpeed.display(0)
		self.lcdNumberCompass.display(0)
		self.lcdCompassWpt.display(0)
		
		self.course_comboBox.clear()
		if self.PositionMarker == True:
			self.iface.mapCanvas().scene().removeItem(self.positionMarker)
		
		
		if self.NxtWptRubber == True:
			self.iface.mapCanvas().scene().removeItem(self.rdue)
			self.iface.mapCanvas().scene().removeItem(self.rtre)
			del self.rdue
			del self.rtre
			self.NxtWptRubber = False
			
		else:
			pass
		
		if self.WptVertexSignal == True:
			self.iface.mapCanvas().scene().removeItem(self.WptVertex)
			del self.WptVertex
			self.WptVertexSignal = False
				
		self.close()


	def ZoomIn(self):
		self.iface.mapCanvas().zoomIn()
		
		
	def ZoomOut(self):	
		self.iface.mapCanvas().zoomOut()
	
	
	def NextWpt(self):
		try:
			currentValue = self.lcdNumberWpt.value()
			if currentValue == len(self.pts):
				pass
			else:
				self.lcdNumberWpt.display(currentValue + 1)
				self.AdjNxtWpt()
		except:
			pass
	
	
	def BackWpt(self):
		try:
			currentValue = self.lcdNumberWpt.value()
			if currentValue >= 2:
				self.lcdNumberWpt.display(currentValue - 1)
				self.AdjNxtWpt()
		except:
			pass
	
	
	def ReadSerial(self):
		
		if self.trackCounter > 5:
			self.trackCounter = 4
		self.trackCounter = self.trackCounter + 1      # when it arrive to 5 a gps point is painted (default is 4)

		GPGGA = 0
		GPVTG = 0
		
		data = self.ser.read(1)
		n = self.ser.inWaiting()
		if n:
			data = data + self.ser.read(n)


		if re.search("\r\n", data):
			# Since we found a CRLF, split it out
			data2 = data.split("\r\n")
		
			for i in range( len(data2)):
				
				if data2[i][0:6] == '$GPGGA':
					GPGGA = data2[i].split(',')
					#print GPGGA
			
				elif data2[i][0:6] == '$GPVTG':
					GPVTG = data2[i].split(',')
					#print GPRMC
						
			if GPGGA == 0:
				#print 'mancato'
				return

			elif GPVTG == 0:
				#print 'mancato'
				return
		
			else:
				
				decimalsLat = (float (GPGGA[2][2:]))   / 60
				degreeLat = float(GPGGA[2][0:2])
				decimalsLon = (float (GPGGA[4][3:]))   / 60
				degreeLon = float(GPGGA[4][0:3])
				
				Lat = degreeLat + decimalsLat
				Lon = degreeLon + decimalsLon
				
				if GPGGA[5]=='W':
					Lon = - Lon
				if GPGGA[3]=='S':
					Lat = - Lat

				Ele = float(GPGGA[9])
				Compass = float(GPVTG[1])
				Speed = (float(GPVTG[7]))                      # in Km/h
				GpsFix = int(GPGGA[6])
				GpsSatellites = int(GPGGA[7])
			
				self.ser.flushInput()
				self.ser.flushOutput()
				
				self.GpsFixlcdNumber.display(GpsFix)
				self.SatelliteslcdNumber.display(GpsSatellites)
				
				if self.RubberBand == True:
					self.iface.mapCanvas().scene().removeItem(self.r)
					del self.r
					
					self.RubberBand = False
				
				Point = QgsPoint()
				Point.set(Lon, Lat)
				 
				TransfPoint = self.xform.transform(Point)
				
				
				canvas = self.iface.mapCanvas()
				if Compass <= 180:
						#canvas.setRotation(-(Compass-self.rotation))
					canvas.setRotation(-Compass)										# set canvas rotation according to:  UP of the map = Compass Direction
				else:
					Compass = 360 - Compass
					canvas.setRotation(Compass)
				
				canvas.setCenter(TransfPoint)
				
				self.positionMarker.newCoords(TransfPoint)						# Put the arrow on screen
				#self.positionMarker.angle = 0.0
				
				WptValue = int(self.lcdNumberWpt.value())
				WptE = self.pts[WptValue - 1][0]
				WptN = self.pts[WptValue - 1][1]
					
				GeodesicAircraftToWpt = Geodesic.WGS84.Inverse(Lat, Lon, WptN, WptE)
				distance = GeodesicAircraftToWpt['s12']	
				azim = GeodesicAircraftToWpt['azi1']																									 #determine azimuth from next wpt
				if azim < 0:
					azim += 360
				
				if distance <= self.WptArrivedTolerance:					# tolerance in meter for next wpt
					self.NextWpt()
					
					
				#feetEle = Ele * 3.2808399            #meters to feet
				
				if self.comboBox_2.currentText() == 'ft.':
					feetEle = Ele * 3.2808399									#Convert if needed
					self.lcdNumberHeights.display(feetEle)
				else:
					self.lcdNumberHeights.display(Ele)
				
				
				
				if self.comboBox_3.currentText() != 'km/h':
					Speed = Speed * 0.53995694												#Convert if needed
					self.lcdNumberSpeed.display(float(Speed))
				else:
					self.lcdNumberSpeed.display(float(Speed))	
					
					
					
				self.lcdNumberCompass.display(float(Compass))
				self.lcdCompassWpt.display(azim)
				
				
				canvasInPixel = canvas.getCoordinateTransform()
				ExtentHeightInPixel = canvasInPixel.mapHeight()
				ExtentWidthInPixel = canvasInPixel.mapWidth()
				
				LocateCompassProjectionEndInMapUnit = canvasInPixel.toMapPoint(ExtentWidthInPixel/2.0,ExtentHeightInPixel-(ExtentHeightInPixel*0.95))
				
				self.r = QgsRubberBand(self.iface.mapCanvas(), False)  # False = not a polygon
		
				#points = [TransfPoint, QgsPoint(x,y)]							#creazione della proiezione della prua su mappa
				points = [TransfPoint, LocateCompassProjectionEndInMapUnit]	
				self.r.setWidth(8)
				self.r.setToGeometry(QgsGeometry.fromPolyline(points), None)
				
				if abs(Compass - azim) <= self.CompassTolerance:                 #Compass tolerance
					self.r.setColor(QtGui.QColor(0,255,0))
				else:
					self.r.setColor(QtGui.QColor(255,0,0))
					
				self.RubberBand = True
				
				try:
					self.iface.mapCanvas().scene().removeItem(self.runo)              # remove track for first waypoint
				except:
					pass
				
				if WptValue != 1:
					
					
					#DistanceFromLineTolerance = 100   #meter      set distance from route 

					BackwardLat = self.rdue.asGeometry().asPolyline()[1][1]         #start to design a QgsRectangle buffer around current route to confront to Point
					BackwardLon = self.rdue.asGeometry().asPolyline()[1][0]
					BackwardPoint = QgsPoint(BackwardLon, BackwardLat)
					
					BackwardPointTransformed = self.backxform.transform(BackwardPoint)

					GeodesicWptWpt = Geodesic.WGS84.Inverse(BackwardPointTransformed.y(), BackwardPointTransformed.x(), WptN, WptE)
					#GeodesicWptWpt = Geodesic.WGS84.Inverse(BackwardLat, BackwardLon, WptN, WptE)
					WptWptCompass = GeodesicWptWpt['azi1']
					
					if WptWptCompass < 0:
						WptWptCompass += 360
					#print WptWptCompass
						
					WptWptCompassRight = WptWptCompass + 90
					if WptWptCompassRight > 360:
						WptWptCompassRight = WptWptCompassRight - 360
					#print WptWptCompassRight
					
					WptWptCompassLeft = WptWptCompass - 90
					if WptWptCompassLeft < 0:
						WptWptCompassLeft += 360
					#print WptWptCompassLeft
							
					origin = geopy.Point(WptN, WptE)
					URBufferVertex = vincenty(meters=self.InRouteTolerance).destination(origin, WptWptCompassRight)
					URBufferVertexPoint = QgsPoint(URBufferVertex.longitude,URBufferVertex.latitude)
					
					ULBufferVertex = vincenty(meters= self.InRouteTolerance).destination(origin, WptWptCompassLeft)
					ULBufferVertexPoint = QgsPoint(ULBufferVertex.longitude,ULBufferVertex.latitude)
					del origin
					
					origin = geopy.Point(BackwardPointTransformed.y(), BackwardPointTransformed.x())
					DRBufferVertex = vincenty(meters=self.InRouteTolerance).destination(origin, WptWptCompassRight)
					DRBufferVertexPoint = QgsPoint(DRBufferVertex.longitude,DRBufferVertex.latitude)
					
					DLBufferVertex = vincenty(meters= self.InRouteTolerance).destination(origin, WptWptCompassLeft)
					DLBufferVertexPoint = QgsPoint(DLBufferVertex.longitude,DLBufferVertex.latitude)
					del origin
					
					gPolygon = QgsGeometry.fromPolygon([[URBufferVertexPoint, ULBufferVertexPoint, DLBufferVertexPoint, DRBufferVertexPoint]])

					if not gPolygon.contains(Point):
						self.rdue.setColor(QtGui.QColor(255,0,0))
						#print 'noncontiene'
					else:
						self.rdue.setColor(QtGui.QColor(0,255,0))
						#print 'contiene'
				else:
					self.runo = QgsRubberBand(self.iface.mapCanvas(), False)
					points = [TransfPoint, self.xform.transform(self.pts[0])]													# draw track for first waypoint
					self.runo.setColor(QtGui.QColor(255,0,0))
					self.runo.setWidth(6)
					self.runo.setLineStyle(QtCore.Qt.PenStyle(QtCore.Qt.DotLine))
					self.runo.setToGeometry(QgsGeometry.fromPolyline(points), None)
					
				
				#if abs(float((self.fixedHeightspinBox.value()/ 3.2808399)) - (feetEle/ 3.2808399)) <= self.EleTolerance:         #ele tolerance expressed in meters
				if abs(self.fixedHeightspinBox.value() - Ele) <= self.EleTolerance:
						self.positionMarker.setHasPosition(True)   #True or False to change color
				else:
					self.positionMarker.setHasPosition(False)
					
				if self.trackCounter == 5:
					#pass
					fc = int(self.TrackLayerProvider.featureCount())
					time = str(GPGGA[1])[0:2] + ':' + str(GPGGA[1])[2:4] + ':' + str(GPGGA[1])[4:6]             # timestamp for GPX layer

				
					feature = QgsFeature()
					feature.setGeometry(QgsGeometry.fromPoint(Point))
					feature.setAttributes([fc,time,Ele])
					self.TrackLayer.startEditing()
					self.TrackLayer.addFeature(feature, True)
					self.TrackLayer.commitChanges()
					self.TrackLayer.setCacheImage(None)
					self.TrackLayer.triggerRepaint()
					self.trackCounter = 0
						
				return

	

			
		
