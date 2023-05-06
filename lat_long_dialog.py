# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CalculadoraDialog
                                 A QGIS plugin
 Este plugin es una calculadora
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-05-04
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Mitcy
        email                : arielisaibonilla@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from math import modf  #Vamos a utilizar la libreria de python math

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'lat_long_dialog_base.ui'))


class CalculadoraDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(CalculadoraDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        #Disparadores para el resultado
        self.spGra.valueChanged.connect(self.latDMSaDD)
        self.spMin.valueChanged.connect(self.latDMSaDD)
        self.cmb1.currentTextChanged.connect(self.latDMSaDD)
        self.spDD.valueChanged.connect(self.latDDaDMS)

    def latDMSaDD(self):
        grados=self.spGra.value()
        minutos=self.spMin.value()
        segundos=self.spSeg.value()

        latH = self.cmb1.currentText()
        dDD =float(grados) + minutos/60 + segundos/3600

        if latH == "S":
            dDD = dDD * -1 
        
        self.spRes1.setValue(dDD)

    
    def latDDaDMS(self):
        gDMS = self.spDD.value()
        dato=modf(gDMS)
        grados=dato[1]
        x=dato[0]
        dato=modf(x)
        minutos=dato[1]
        segundos=dato[0]*60
        resultado=[grados, minutos, segundos]
        self.txtLatDMS.setValue(resultado +'°'+ resultado[1]+'´'+resultado[2]+'"')




