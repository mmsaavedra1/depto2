# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Depto2 GUI v3.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStackedWidget,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(511, 687)
        font = QFont()
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.titulo = QLabel(self.centralwidget)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(115, 20, 361, 20))
        font1 = QFont()
        font1.setPointSize(17)
        font1.setBold(True)
        self.titulo.setFont(font1)
        self.subtitulo = QLabel(self.centralwidget)
        self.subtitulo.setObjectName(u"subtitulo")
        self.subtitulo.setGeometry(QRect(115, 40, 321, 20))
        font2 = QFont()
        font2.setPointSize(13)
        self.subtitulo.setFont(font2)
        self.subsubtitulo = QLabel(self.centralwidget)
        self.subsubtitulo.setObjectName(u"subsubtitulo")
        self.subsubtitulo.setGeometry(QRect(115, 60, 271, 16))
        self.widget_botones = QWidget(self.centralwidget)
        self.widget_botones.setObjectName(u"widget_botones")
        self.widget_botones.setGeometry(QRect(40, 90, 431, 44))
        self.widget_botones.setStyleSheet(u"QWidget{\n"
"	background-color: #E6E9E7;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	height: 30px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #0056D2;\n"
"	color: white;\n"
"	font-weight: bold;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget_botones)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.boton_proyectos = QPushButton(self.widget_botones)
        self.boton_proyectos.setObjectName(u"boton_proyectos")
        icon = QIcon()
        icon.addFile(u":/images/dashboardsmall2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/dashboardsmall1.png", QSize(), QIcon.Normal, QIcon.On)
        self.boton_proyectos.setIcon(icon)
        self.boton_proyectos.setCheckable(True)
        self.boton_proyectos.setChecked(True)
        self.boton_proyectos.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.boton_proyectos)

        self.boton_evaluacion = QPushButton(self.widget_botones)
        self.boton_evaluacion.setObjectName(u"boton_evaluacion")
        icon1 = QIcon()
        icon1.addFile(u":/images/financessmall2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/images/financessmall1.png", QSize(), QIcon.Normal, QIcon.On)
        self.boton_evaluacion.setIcon(icon1)
        self.boton_evaluacion.setCheckable(True)
        self.boton_evaluacion.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.boton_evaluacion)

        self.widget_pila = QStackedWidget(self.centralwidget)
        self.widget_pila.setObjectName(u"widget_pila")
        self.widget_pila.setGeometry(QRect(0, 140, 511, 531))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.widget_datos_evaluacion = QFrame(self.page)
        self.widget_datos_evaluacion.setObjectName(u"widget_datos_evaluacion")
        self.widget_datos_evaluacion.setGeometry(QRect(40, 380, 451, 141))
        self.widget_datos_evaluacion.setFrameShape(QFrame.NoFrame)
        self.etiq_lista_comunas = QLabel(self.widget_datos_evaluacion)
        self.etiq_lista_comunas.setObjectName(u"etiq_lista_comunas")
        self.etiq_lista_comunas.setGeometry(QRect(10, 5, 111, 16))
        font3 = QFont()
        font3.setBold(True)
        self.etiq_lista_comunas.setFont(font3)
        self.lista_comunas = QComboBox(self.widget_datos_evaluacion)
        self.lista_comunas.addItem("")
        self.lista_comunas.addItem("")
        self.lista_comunas.addItem("")
        self.lista_comunas.addItem("")
        self.lista_comunas.setObjectName(u"lista_comunas")
        self.lista_comunas.setGeometry(QRect(10, 31, 215, 20))
        self.etiq_precio_2 = QLabel(self.widget_datos_evaluacion)
        self.etiq_precio_2.setObjectName(u"etiq_precio_2")
        self.etiq_precio_2.setGeometry(QRect(10, 55, 131, 16))
        self.etiq_precio_2.setFont(font3)
        self.precio_2 = QLineEdit(self.widget_datos_evaluacion)
        self.precio_2.setObjectName(u"precio_2")
        self.precio_2.setGeometry(QRect(130, 55, 91, 21))
        self.etiq_anios_venta = QLabel(self.widget_datos_evaluacion)
        self.etiq_anios_venta.setObjectName(u"etiq_anios_venta")
        self.etiq_anios_venta.setGeometry(QRect(10, 80, 91, 16))
        self.etiq_anios_venta.setFont(font3)
        self.anios_venta = QComboBox(self.widget_datos_evaluacion)
        self.anios_venta.addItem("")
        self.anios_venta.addItem("")
        self.anios_venta.addItem("")
        self.anios_venta.addItem("")
        self.anios_venta.addItem("")
        self.anios_venta.addItem("")
        self.anios_venta.addItem("")
        self.anios_venta.addItem("")
        self.anios_venta.addItem("")
        self.anios_venta.addItem("")
        self.anios_venta.addItem("")
        self.anios_venta.addItem("")
        self.anios_venta.setObjectName(u"anios_venta")
        self.anios_venta.setGeometry(QRect(130, 80, 91, 21))
        self.plazo = QLineEdit(self.widget_datos_evaluacion)
        self.plazo.setObjectName(u"plazo")
        self.plazo.setGeometry(QRect(330, 51, 81, 20))
        self.cae = QLineEdit(self.widget_datos_evaluacion)
        self.cae.setObjectName(u"cae")
        self.cae.setGeometry(QRect(330, 70, 81, 20))
        self.pie = QLineEdit(self.widget_datos_evaluacion)
        self.pie.setObjectName(u"pie")
        self.pie.setGeometry(QRect(330, 30, 81, 21))
        self.etiq_plazo = QLabel(self.widget_datos_evaluacion)
        self.etiq_plazo.setObjectName(u"etiq_plazo")
        self.etiq_plazo.setGeometry(QRect(240, 50, 81, 20))
        font4 = QFont()
        font4.setBold(False)
        self.etiq_plazo.setFont(font4)
        self.titutlo = QLabel(self.widget_datos_evaluacion)
        self.titutlo.setObjectName(u"titutlo")
        self.titutlo.setGeometry(QRect(240, 5, 191, 16))
        self.titutlo.setFont(font3)
        self.etiq_pie = QLabel(self.widget_datos_evaluacion)
        self.etiq_pie.setObjectName(u"etiq_pie")
        self.etiq_pie.setGeometry(QRect(240, 30, 71, 16))
        self.etiq_pie.setFont(font4)
        self.etiq_cae = QLabel(self.widget_datos_evaluacion)
        self.etiq_cae.setObjectName(u"etiq_cae")
        self.etiq_cae.setGeometry(QRect(240, 70, 71, 16))
        self.etiq_cae.setFont(font4)
        self.boton_generar_evaluacion = QPushButton(self.widget_datos_evaluacion)
        self.boton_generar_evaluacion.setObjectName(u"boton_generar_evaluacion")
        self.boton_generar_evaluacion.setGeometry(QRect(10, 110, 431, 31))
        self.boton_generar_evaluacion.setStyleSheet(u"QPushButton{\n"
"	background-color: #0056D2;\n"
"	color: white;\n"
"	border:none;\n"
"	height: 30px;\n"
"	font-weight:bold;\n"
"	border-radius:10px;\n"
"}")
        self.boton_generar_evaluacion.setCheckable(True)
        self.tabla_evaluacion = QTableWidget(self.page)
        if (self.tabla_evaluacion.columnCount() < 6):
            self.tabla_evaluacion.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_evaluacion.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_evaluacion.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_evaluacion.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_evaluacion.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_evaluacion.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_evaluacion.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tabla_evaluacion.setObjectName(u"tabla_evaluacion")
        self.tabla_evaluacion.setGeometry(QRect(30, 330, 460, 51))
        self.tabla_evaluacion.horizontalHeader().setMinimumSectionSize(19)
        self.tabla_evaluacion.horizontalHeader().setDefaultSectionSize(76)
        self.grafico_evaluacion = QChartView(self.page)
        self.grafico_evaluacion.setObjectName(u"grafico_evaluacion")
        self.grafico_evaluacion.setGeometry(QRect(0, 0, 511, 321))
        self.widget_pila.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.comunas_2 = QFrame(self.page_2)
        self.comunas_2.setObjectName(u"comunas_2")
        self.comunas_2.setGeometry(QRect(40, 330, 441, 201))
        self.comunas_2.setFrameShape(QFrame.NoFrame)
        self.etiq_lista_comunas_2 = QLabel(self.comunas_2)
        self.etiq_lista_comunas_2.setObjectName(u"etiq_lista_comunas_2")
        self.etiq_lista_comunas_2.setGeometry(QRect(20, 80, 111, 16))
        self.etiq_lista_comunas_2.setFont(font3)
        self.lista_comunas_2 = QComboBox(self.comunas_2)
        self.lista_comunas_2.addItem("")
        self.lista_comunas_2.addItem("")
        self.lista_comunas_2.addItem("")
        self.lista_comunas_2.addItem("")
        self.lista_comunas_2.setObjectName(u"lista_comunas_2")
        self.lista_comunas_2.setGeometry(QRect(90, 80, 341, 21))
        self.etiq_lista_comunas_3 = QLabel(self.comunas_2)
        self.etiq_lista_comunas_3.setObjectName(u"etiq_lista_comunas_3")
        self.etiq_lista_comunas_3.setGeometry(QRect(20, 105, 111, 16))
        self.etiq_lista_comunas_3.setFont(font3)
        self.lista_comunas_3 = QComboBox(self.comunas_2)
        self.lista_comunas_3.addItem("")
        self.lista_comunas_3.addItem("")
        self.lista_comunas_3.addItem("")
        self.lista_comunas_3.addItem("")
        self.lista_comunas_3.setObjectName(u"lista_comunas_3")
        self.lista_comunas_3.setGeometry(QRect(90, 105, 341, 21))
        self.lista_comunas_4 = QComboBox(self.comunas_2)
        self.lista_comunas_4.addItem("")
        self.lista_comunas_4.addItem("")
        self.lista_comunas_4.addItem("")
        self.lista_comunas_4.addItem("")
        self.lista_comunas_4.setObjectName(u"lista_comunas_4")
        self.lista_comunas_4.setGeometry(QRect(90, 130, 341, 21))
        self.etiq_lista_comunas_4 = QLabel(self.comunas_2)
        self.etiq_lista_comunas_4.setObjectName(u"etiq_lista_comunas_4")
        self.etiq_lista_comunas_4.setGeometry(QRect(20, 130, 71, 16))
        self.etiq_lista_comunas_4.setFont(font3)
        self.credito_hip_2 = QFrame(self.comunas_2)
        self.credito_hip_2.setObjectName(u"credito_hip_2")
        self.credito_hip_2.setGeometry(QRect(130, 20, 201, 51))
        self.credito_hip_2.setFrameShape(QFrame.NoFrame)
        self.etiq_cae_2 = QLabel(self.credito_hip_2)
        self.etiq_cae_2.setObjectName(u"etiq_cae_2")
        self.etiq_cae_2.setGeometry(QRect(10, 20, 31, 16))
        self.etiq_cae_2.setFont(font4)
        self.etiq_precio_3 = QLabel(self.credito_hip_2)
        self.etiq_precio_3.setObjectName(u"etiq_precio_3")
        self.etiq_precio_3.setGeometry(QRect(30, 0, 141, 20))
        self.etiq_precio_3.setFont(font3)
        self.precio_3 = QLineEdit(self.credito_hip_2)
        self.precio_3.setObjectName(u"precio_3")
        self.precio_3.setGeometry(QRect(35, 20, 61, 21))
        self.precio_4 = QLineEdit(self.credito_hip_2)
        self.precio_4.setObjectName(u"precio_4")
        self.precio_4.setGeometry(QRect(100, 20, 61, 21))
        self.etiq_cae_3 = QLabel(self.credito_hip_2)
        self.etiq_cae_3.setObjectName(u"etiq_cae_3")
        self.etiq_cae_3.setGeometry(QRect(170, 20, 31, 16))
        self.etiq_cae_3.setFont(font4)
        self.boton_generar_proyectos = QPushButton(self.page_2)
        self.boton_generar_proyectos.setObjectName(u"boton_generar_proyectos")
        self.boton_generar_proyectos.setGeometry(QRect(50, 490, 431, 31))
        self.boton_generar_proyectos.setStyleSheet(u"QPushButton{\n"
"	background-color: #0056D2;\n"
"	color: white;\n"
"	border:none;\n"
"	height: 30px;\n"
"	font-weight:bold;\n"
"	border-radius:10px;\n"
"}")
        self.boton_generar_proyectos.setCheckable(True)
        self.widget_pila.addWidget(self.page_2)
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setEnabled(True)
        self.logo.setGeometry(QRect(40, 15, 71, 71))
        self.logo.setPixmap(QPixmap(u":/images/Logo.png"))
        self.logo.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 511, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.widget_pila.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"Depto2 - Departamento para todo inversionista", None))
        self.subtitulo.setText(QCoreApplication.translate("MainWindow", u"Mediante IA ahorramos tiempo en la toma de decisiones", None))
        self.subsubtitulo.setText(QCoreApplication.translate("MainWindow", u"Elige una opci\u00f3n para revisar inversiones:", None))
        self.boton_proyectos.setText(QCoreApplication.translate("MainWindow", u"Proyectos de Inversion", None))
        self.boton_evaluacion.setText(QCoreApplication.translate("MainWindow", u"Evaluaci\u00f3n de proyecto", None))
        self.etiq_lista_comunas.setText(QCoreApplication.translate("MainWindow", u"Comuna", None))
        self.lista_comunas.setItemText(0, QCoreApplication.translate("MainWindow", u"\u00d1u\u00f1oa", None))
        self.lista_comunas.setItemText(1, QCoreApplication.translate("MainWindow", u"Las Condes", None))
        self.lista_comunas.setItemText(2, QCoreApplication.translate("MainWindow", u"Providencia", None))
        self.lista_comunas.setItemText(3, QCoreApplication.translate("MainWindow", u"Quinta Normal", None))

        self.etiq_precio_2.setText(QCoreApplication.translate("MainWindow", u"Precio Proyecto", None))
        self.etiq_anios_venta.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o de Venta", None))
        self.anios_venta.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.anios_venta.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.anios_venta.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.anios_venta.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.anios_venta.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.anios_venta.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.anios_venta.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.anios_venta.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.anios_venta.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.anios_venta.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.anios_venta.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.anios_venta.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))

        self.etiq_plazo.setText(QCoreApplication.translate("MainWindow", u"Plazo (A\u00f1os)", None))
        self.titutlo.setText(QCoreApplication.translate("MainWindow", u"Datos de cr\u00e9dito hipotecario", None))
        self.etiq_pie.setText(QCoreApplication.translate("MainWindow", u"Pie (%)", None))
        self.etiq_cae.setText(QCoreApplication.translate("MainWindow", u"CAE (%)", None))
        self.boton_generar_evaluacion.setText(QCoreApplication.translate("MainWindow", u"Generar Informaci\u00f3n", None))
        ___qtablewidgetitem = self.tabla_evaluacion.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o Venta", None));
        ___qtablewidgetitem1 = self.tabla_evaluacion.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"R. Total", None));
        ___qtablewidgetitem2 = self.tabla_evaluacion.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"R. Flujo", None));
        ___qtablewidgetitem3 = self.tabla_evaluacion.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"R. Amortizacion", None));
        ___qtablewidgetitem4 = self.tabla_evaluacion.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"R. Flujo", None));
        ___qtablewidgetitem5 = self.tabla_evaluacion.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Utilidades", None));
        self.etiq_lista_comunas_2.setText(QCoreApplication.translate("MainWindow", u"Comuna 1", None))
        self.lista_comunas_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u00d1u\u00f1oa", None))
        self.lista_comunas_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Las Condes", None))
        self.lista_comunas_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Providencia", None))
        self.lista_comunas_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Quinta Normal", None))

        self.etiq_lista_comunas_3.setText(QCoreApplication.translate("MainWindow", u"Comuna 2", None))
        self.lista_comunas_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Las Condes", None))
        self.lista_comunas_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Providencia", None))
        self.lista_comunas_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Quinta Normal", None))
        self.lista_comunas_3.setItemText(3, QCoreApplication.translate("MainWindow", u"\u00d1u\u00f1oa", None))

        self.lista_comunas_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Quinta Normal", None))
        self.lista_comunas_4.setItemText(1, QCoreApplication.translate("MainWindow", u"\u00d1u\u00f1oa", None))
        self.lista_comunas_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Las Condes", None))
        self.lista_comunas_4.setItemText(3, QCoreApplication.translate("MainWindow", u"Providencia", None))

        self.etiq_lista_comunas_4.setText(QCoreApplication.translate("MainWindow", u"Comuna 3", None))
        self.etiq_cae_2.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.etiq_precio_3.setText(QCoreApplication.translate("MainWindow", u"Precios de Proyectos", None))
        self.etiq_cae_3.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.boton_generar_proyectos.setText(QCoreApplication.translate("MainWindow", u"Generar Informaci\u00f3n", None))
        self.logo.setText("")
    # retranslateUi

