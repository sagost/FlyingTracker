# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FlyingTracker
                                 A QGIS plugin
 Aerial survey tracker
                             -------------------
        begin                : 2015-03-09
        copyright            : (C) 2015 by Salvatore Agosta / SAL Engineering
        email                : sagost@katamail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load FlyingTracker class from file FlyingTracker.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .flying_tracker import FlyingTracker
    return FlyingTracker(iface)
