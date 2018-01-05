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




from PyQt4 import QtCore, QtGui
from qgis.core import *
from qgis.gui import *


class PositionMarker(QgsMapCanvasItem):
	""" marker for current GPS position """

	def __init__(self, canvas, alpha=255):
		QgsMapCanvasItem.__init__(self, canvas)
		self.pos = None
		self.hasPosition = False
		self.d = 20
		self.angle = 0
		self.setZValue(100) # must be on top
		self.alpha=alpha
		
	def newCoords(self, pos):
		if self.pos != pos:
			self.pos = QgsPoint(pos) # copy
			self.updatePosition()
			
	def setHasPosition(self, has):
		if self.hasPosition != has:
			self.hasPosition = has
			self.update()
		
	def updatePosition(self):
		if self.pos:
			self.setPos(self.toCanvasCoordinates(self.pos))
			self.update()
			
	def paint(self, p, xxx, xxx2):
		if not self.pos:
			return
		
		
		path = QtGui.QPainterPath()
		path.moveTo(0,-30)
		path.lineTo(30,30)
		path.lineTo(0,15)
		path.lineTo(-30,30)
		path.lineTo(0,-30)
		
		
		# render position with angle
		p.save()
		p.setRenderHint(QtGui.QPainter.Antialiasing)
		if self.hasPosition:
			p.setBrush(QtGui.QBrush(QtGui.QColor(0,255,0, self.alpha)))
		else:
			p.setBrush(QtGui.QBrush(QtGui.QColor(0,0,0, self.alpha)))
		p.setPen(QtGui.QColor(0,0,0, self.alpha))
		p.rotate(self.angle)
		p.drawPath(path)
		p.restore()
			
	#def boundingRect(self):
		#return QtCore.QRectF(-self.d,-self.d, self.d*2, self.d*2)
