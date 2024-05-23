# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Depto2 GUI.ui'
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
        MainWindow.resize(1132, 703)
        font = QFont()
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.titulo = QLabel(self.centralwidget)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(435, 10, 361, 20))
        font1 = QFont()
        font1.setPointSize(17)
        font1.setBold(True)
        self.titulo.setFont(font1)
        self.subtitulo = QLabel(self.centralwidget)
        self.subtitulo.setObjectName(u"subtitulo")
        self.subtitulo.setGeometry(QRect(435, 30, 321, 20))
        font2 = QFont()
        font2.setPointSize(13)
        self.subtitulo.setFont(font2)
        self.subsubtitulo = QLabel(self.centralwidget)
        self.subsubtitulo.setObjectName(u"subsubtitulo")
        self.subsubtitulo.setGeometry(QRect(435, 50, 271, 16))
        self.widget_botones = QWidget(self.centralwidget)
        self.widget_botones.setObjectName(u"widget_botones")
        self.widget_botones.setGeometry(QRect(360, 80, 431, 44))
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
        self.widget_pila.setGeometry(QRect(0, 130, 1121, 541))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.widget_datos_evaluacion = QFrame(self.page)
        self.widget_datos_evaluacion.setObjectName(u"widget_datos_evaluacion")
        self.widget_datos_evaluacion.setGeometry(QRect(260, 390, 681, 151))
        self.widget_datos_evaluacion.setFrameShape(QFrame.NoFrame)
        self.etiq_lista_comunas = QLabel(self.widget_datos_evaluacion)
        self.etiq_lista_comunas.setObjectName(u"etiq_lista_comunas")
        self.etiq_lista_comunas.setGeometry(QRect(10, 50, 81, 16))
        font3 = QFont()
        font3.setBold(False)
        self.etiq_lista_comunas.setFont(font3)
        self.lista_comunas = QComboBox(self.widget_datos_evaluacion)
        self.lista_comunas.setObjectName(u"lista_comunas")
        self.lista_comunas.setGeometry(QRect(100, 50, 121, 20))
        self.etiq_precio_2 = QLabel(self.widget_datos_evaluacion)
        self.etiq_precio_2.setObjectName(u"etiq_precio_2")
        self.etiq_precio_2.setGeometry(QRect(10, 70, 81, 16))
        self.etiq_precio_2.setFont(font3)
        self.precio_2 = QLineEdit(self.widget_datos_evaluacion)
        self.precio_2.setObjectName(u"precio_2")
        self.precio_2.setGeometry(QRect(100, 70, 121, 21))
        self.plazo = QLineEdit(self.widget_datos_evaluacion)
        self.plazo.setObjectName(u"plazo")
        self.plazo.setGeometry(QRect(350, 51, 81, 20))
        self.cae = QLineEdit(self.widget_datos_evaluacion)
        self.cae.setObjectName(u"cae")
        self.cae.setGeometry(QRect(350, 70, 81, 20))
        self.pie = QLineEdit(self.widget_datos_evaluacion)
        self.pie.setObjectName(u"pie")
        self.pie.setGeometry(QRect(350, 30, 81, 21))
        self.etiq_plazo = QLabel(self.widget_datos_evaluacion)
        self.etiq_plazo.setObjectName(u"etiq_plazo")
        self.etiq_plazo.setGeometry(QRect(260, 50, 81, 20))
        self.etiq_plazo.setFont(font3)
        self.titutlo = QLabel(self.widget_datos_evaluacion)
        self.titutlo.setObjectName(u"titutlo")
        self.titutlo.setGeometry(QRect(260, 10, 191, 16))
        font4 = QFont()
        font4.setBold(True)
        self.titutlo.setFont(font4)
        self.etiq_pie = QLabel(self.widget_datos_evaluacion)
        self.etiq_pie.setObjectName(u"etiq_pie")
        self.etiq_pie.setGeometry(QRect(260, 30, 71, 16))
        self.etiq_pie.setFont(font3)
        self.etiq_cae = QLabel(self.widget_datos_evaluacion)
        self.etiq_cae.setObjectName(u"etiq_cae")
        self.etiq_cae.setGeometry(QRect(260, 70, 71, 16))
        self.etiq_cae.setFont(font3)
        self.boton_generar_evaluacion = QPushButton(self.widget_datos_evaluacion)
        self.boton_generar_evaluacion.setObjectName(u"boton_generar_evaluacion")
        self.boton_generar_evaluacion.setGeometry(QRect(10, 120, 431, 31))
        self.boton_generar_evaluacion.setStyleSheet(u"QPushButton{\n"
"	background-color: #0056D2;\n"
"	color: white;\n"
"	border:none;\n"
"	height: 30px;\n"
"	font-weight:bold;\n"
"	border-radius:10px;\n"
"}")
        self.boton_generar_evaluacion.setCheckable(True)
        self.etiq_precio_4 = QLabel(self.widget_datos_evaluacion)
        self.etiq_precio_4.setObjectName(u"etiq_precio_4")
        self.etiq_precio_4.setGeometry(QRect(10, 90, 81, 16))
        self.etiq_precio_4.setFont(font3)
        self.arriendo_proyecto = QLineEdit(self.widget_datos_evaluacion)
        self.arriendo_proyecto.setObjectName(u"arriendo_proyecto")
        self.arriendo_proyecto.setGeometry(QRect(100, 90, 121, 21))
        self.etiq_precio_5 = QLabel(self.widget_datos_evaluacion)
        self.etiq_precio_5.setObjectName(u"etiq_precio_5")
        self.etiq_precio_5.setGeometry(QRect(10, 30, 81, 16))
        self.etiq_precio_5.setFont(font3)
        self.nombre_proyecto = QLineEdit(self.widget_datos_evaluacion)
        self.nombre_proyecto.setObjectName(u"nombre_proyecto")
        self.nombre_proyecto.setGeometry(QRect(100, 30, 121, 21))
        self.titutlo_2 = QLabel(self.widget_datos_evaluacion)
        self.titutlo_2.setObjectName(u"titutlo_2")
        self.titutlo_2.setGeometry(QRect(10, 10, 191, 16))
        self.titutlo_2.setFont(font4)
        self.etiq_cae_4 = QLabel(self.widget_datos_evaluacion)
        self.etiq_cae_4.setObjectName(u"etiq_cae_4")
        self.etiq_cae_4.setGeometry(QRect(470, 30, 71, 16))
        self.etiq_cae_4.setFont(font3)
        self.uf = QLineEdit(self.widget_datos_evaluacion)
        self.uf.setObjectName(u"uf")
        self.uf.setGeometry(QRect(540, 30, 81, 20))
        self.dividendo = QLineEdit(self.widget_datos_evaluacion)
        self.dividendo.setObjectName(u"dividendo")
        self.dividendo.setEnabled(False)
        self.dividendo.setGeometry(QRect(350, 90, 81, 20))
        self.etiq_cae_5 = QLabel(self.widget_datos_evaluacion)
        self.etiq_cae_5.setObjectName(u"etiq_cae_5")
        self.etiq_cae_5.setGeometry(QRect(260, 90, 71, 16))
        self.etiq_cae_5.setFont(font3)
        self.tabla_dfl2 = QTableWidget(self.page)
        if (self.tabla_dfl2.columnCount() < 7):
            self.tabla_dfl2.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_dfl2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_dfl2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_dfl2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_dfl2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_dfl2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_dfl2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_dfl2.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_dfl2.setObjectName(u"tabla_dfl2")
        self.tabla_dfl2.setGeometry(QRect(10, 340, 551, 51))
        self.tabla_dfl2.horizontalHeader().setMinimumSectionSize(19)
        self.tabla_dfl2.horizontalHeader().setDefaultSectionSize(76)
        self.grafico_dfl2 = QChartView(self.page)
        self.grafico_dfl2.setObjectName(u"grafico_dfl2")
        self.grafico_dfl2.setGeometry(QRect(10, 0, 551, 321))
        self.grafico_27bis = QChartView(self.page)
        self.grafico_27bis.setObjectName(u"grafico_27bis")
        self.grafico_27bis.setGeometry(QRect(580, 0, 551, 321))
        self.tabla_27bis = QTableWidget(self.page)
        if (self.tabla_27bis.columnCount() < 7):
            self.tabla_27bis.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_27bis.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_27bis.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_27bis.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_27bis.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_27bis.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_27bis.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_27bis.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        self.tabla_27bis.setObjectName(u"tabla_27bis")
        self.tabla_27bis.setGeometry(QRect(580, 340, 551, 51))
        self.tabla_27bis.horizontalHeader().setMinimumSectionSize(19)
        self.tabla_27bis.horizontalHeader().setDefaultSectionSize(76)
        self.titutlo_3 = QLabel(self.page)
        self.titutlo_3.setObjectName(u"titutlo_3")
        self.titutlo_3.setGeometry(QRect(10, 323, 561, 16))
        self.titutlo_3.setFont(font4)
        self.titutlo_4 = QLabel(self.page)
        self.titutlo_4.setObjectName(u"titutlo_4")
        self.titutlo_4.setGeometry(QRect(580, 323, 271, 16))
        self.titutlo_4.setFont(font4)
        self.widget_pila.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.comunas_2 = QFrame(self.page_2)
        self.comunas_2.setObjectName(u"comunas_2")
        self.comunas_2.setGeometry(QRect(350, 340, 451, 201))
        self.comunas_2.setFrameShape(QFrame.NoFrame)
        self.etiq_lista_comunas_2 = QLabel(self.comunas_2)
        self.etiq_lista_comunas_2.setObjectName(u"etiq_lista_comunas_2")
        self.etiq_lista_comunas_2.setGeometry(QRect(20, 80, 111, 16))
        self.etiq_lista_comunas_2.setFont(font4)
        self.lista_comunas_2 = QComboBox(self.comunas_2)
        self.lista_comunas_2.setObjectName(u"lista_comunas_2")
        self.lista_comunas_2.setGeometry(QRect(90, 80, 341, 21))
        self.lista_comunas_2.setEditable(False)
        self.etiq_lista_comunas_3 = QLabel(self.comunas_2)
        self.etiq_lista_comunas_3.setObjectName(u"etiq_lista_comunas_3")
        self.etiq_lista_comunas_3.setGeometry(QRect(20, 105, 111, 16))
        self.etiq_lista_comunas_3.setFont(font4)
        self.lista_comunas_3 = QComboBox(self.comunas_2)
        self.lista_comunas_3.setObjectName(u"lista_comunas_3")
        self.lista_comunas_3.setGeometry(QRect(90, 105, 341, 21))
        self.lista_comunas_3.setEditable(False)
        self.lista_comunas_4 = QComboBox(self.comunas_2)
        self.lista_comunas_4.setObjectName(u"lista_comunas_4")
        self.lista_comunas_4.setGeometry(QRect(90, 130, 341, 21))
        self.lista_comunas_4.setEditable(False)
        self.etiq_lista_comunas_4 = QLabel(self.comunas_2)
        self.etiq_lista_comunas_4.setObjectName(u"etiq_lista_comunas_4")
        self.etiq_lista_comunas_4.setGeometry(QRect(20, 130, 71, 16))
        self.etiq_lista_comunas_4.setFont(font4)
        self.credito_hip_2 = QFrame(self.comunas_2)
        self.credito_hip_2.setObjectName(u"credito_hip_2")
        self.credito_hip_2.setGeometry(QRect(130, 20, 201, 51))
        self.credito_hip_2.setFrameShape(QFrame.NoFrame)
        self.etiq_cae_2 = QLabel(self.credito_hip_2)
        self.etiq_cae_2.setObjectName(u"etiq_cae_2")
        self.etiq_cae_2.setGeometry(QRect(10, 20, 31, 16))
        self.etiq_cae_2.setFont(font3)
        self.etiq_precio_3 = QLabel(self.credito_hip_2)
        self.etiq_precio_3.setObjectName(u"etiq_precio_3")
        self.etiq_precio_3.setGeometry(QRect(30, 0, 141, 20))
        self.etiq_precio_3.setFont(font4)
        self.precio_3 = QLineEdit(self.credito_hip_2)
        self.precio_3.setObjectName(u"precio_3")
        self.precio_3.setGeometry(QRect(35, 20, 61, 21))
        self.precio_3.setAlignment(Qt.AlignCenter)
        self.precio_4 = QLineEdit(self.credito_hip_2)
        self.precio_4.setObjectName(u"precio_4")
        self.precio_4.setGeometry(QRect(100, 20, 61, 21))
        self.precio_4.setAlignment(Qt.AlignCenter)
        self.etiq_cae_3 = QLabel(self.credito_hip_2)
        self.etiq_cae_3.setObjectName(u"etiq_cae_3")
        self.etiq_cae_3.setGeometry(QRect(170, 20, 31, 16))
        self.etiq_cae_3.setFont(font3)
        self.boton_generar_proyectos = QPushButton(self.page_2)
        self.boton_generar_proyectos.setObjectName(u"boton_generar_proyectos")
        self.boton_generar_proyectos.setGeometry(QRect(370, 510, 201, 31))
        self.boton_generar_proyectos.setStyleSheet(u"QPushButton{\n"
"	background-color: #0056D2;\n"
"	color: white;\n"
"	border:none;\n"
"	height: 30px;\n"
"	font-weight:bold;\n"
"	border-radius:10px;\n"
"}")
        self.boton_generar_proyectos.setCheckable(True)
        self.tabla_proyectos = QTableWidget(self.page_2)
        if (self.tabla_proyectos.columnCount() < 9):
            self.tabla_proyectos.setColumnCount(9)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabla_proyectos.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabla_proyectos.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabla_proyectos.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabla_proyectos.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabla_proyectos.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tabla_proyectos.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tabla_proyectos.setHorizontalHeaderItem(6, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tabla_proyectos.setHorizontalHeaderItem(7, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tabla_proyectos.setHorizontalHeaderItem(8, __qtablewidgetitem22)
        self.tabla_proyectos.setObjectName(u"tabla_proyectos")
        self.tabla_proyectos.setGeometry(QRect(200, 10, 801, 321))
        self.tabla_proyectos.setShowGrid(True)
        self.tabla_proyectos.setGridStyle(Qt.SolidLine)
        self.tabla_proyectos.setSortingEnabled(True)
        self.tabla_proyectos.setRowCount(0)
        self.tabla_proyectos.horizontalHeader().setMinimumSectionSize(19)
        self.tabla_proyectos.horizontalHeader().setDefaultSectionSize(76)
        self.tabla_proyectos.horizontalHeader().setProperty("showSortIndicator", True)
        self.boton_evaluar_proyecto = QPushButton(self.page_2)
        self.boton_evaluar_proyecto.setObjectName(u"boton_evaluar_proyecto")
        self.boton_evaluar_proyecto.setGeometry(QRect(580, 510, 201, 31))
        self.boton_evaluar_proyecto.setStyleSheet(u"QPushButton{\n"
"	background-color: #0056D2;\n"
"	color: white;\n"
"	border:none;\n"
"	height: 30px;\n"
"	font-weight:bold;\n"
"	border-radius:10px;\n"
"}")
        self.boton_evaluar_proyecto.setCheckable(True)
        self.widget_pila.addWidget(self.page_2)
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setEnabled(True)
        self.logo.setGeometry(QRect(360, 5, 71, 71))
        self.logo.setPixmap(QPixmap(u":/images/Logo.png"))
        self.logo.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1132, 21))
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
        self.etiq_precio_2.setText(QCoreApplication.translate("MainWindow", u"Precio [UF]", None))
        self.etiq_plazo.setText(QCoreApplication.translate("MainWindow", u"Plazo (A\u00f1os)", None))
        self.titutlo.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9dito Hipotecario", None))
        self.etiq_pie.setText(QCoreApplication.translate("MainWindow", u"Pie (%)", None))
        self.etiq_cae.setText(QCoreApplication.translate("MainWindow", u"CAE (%)", None))
        self.boton_generar_evaluacion.setText(QCoreApplication.translate("MainWindow", u"Generar Evaluaci\u00f3n", None))
        self.etiq_precio_4.setText(QCoreApplication.translate("MainWindow", u"Arriendo [$]", None))
        self.etiq_precio_5.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.nombre_proyecto.setText("")
        self.titutlo_2.setText(QCoreApplication.translate("MainWindow", u"Datos Proyecto", None))
        self.etiq_cae_4.setText(QCoreApplication.translate("MainWindow", u"UF/CLP", None))
        self.uf.setText("")
        self.etiq_cae_5.setText(QCoreApplication.translate("MainWindow", u"Dividendo", None))
        ___qtablewidgetitem = self.tabla_dfl2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None));
        ___qtablewidgetitem1 = self.tabla_dfl2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Cap Rate", None));
        ___qtablewidgetitem2 = self.tabla_dfl2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"R. Total", None));
        ___qtablewidgetitem3 = self.tabla_dfl2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"R. Flujo", None));
        ___qtablewidgetitem4 = self.tabla_dfl2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"R. Plusvalia", None));
        ___qtablewidgetitem5 = self.tabla_dfl2.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"R. Amortizacion", None));
        ___qtablewidgetitem6 = self.tabla_dfl2.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Utilidades", None));
        ___qtablewidgetitem7 = self.tabla_27bis.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None));
        ___qtablewidgetitem8 = self.tabla_27bis.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Cap Rate", None));
        ___qtablewidgetitem9 = self.tabla_27bis.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"R. Total", None));
        ___qtablewidgetitem10 = self.tabla_27bis.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"R. Flujo", None));
        ___qtablewidgetitem11 = self.tabla_27bis.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"R. Plusvalia", None));
        ___qtablewidgetitem12 = self.tabla_27bis.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"R. Amortizacion", None));
        ___qtablewidgetitem13 = self.tabla_27bis.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Utilidades", None));
        self.titutlo_3.setText(QCoreApplication.translate("MainWindow", u"Detalle de venta, m\u00e1xima utilidad [DFL2]", None))
        self.titutlo_4.setText(QCoreApplication.translate("MainWindow", u"Detalle de venta, m\u00e1xima utilidad [27BIS]", None))
        self.etiq_lista_comunas_2.setText(QCoreApplication.translate("MainWindow", u"Comuna 1", None))
        self.etiq_lista_comunas_3.setText(QCoreApplication.translate("MainWindow", u"Comuna 2", None))
        self.etiq_lista_comunas_4.setText(QCoreApplication.translate("MainWindow", u"Comuna 3", None))
        self.etiq_cae_2.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.etiq_precio_3.setText(QCoreApplication.translate("MainWindow", u"Precios de Proyectos", None))
        self.etiq_cae_3.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.boton_generar_proyectos.setText(QCoreApplication.translate("MainWindow", u"Listar Proyectos", None))
        ___qtablewidgetitem14 = self.tabla_proyectos.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem15 = self.tabla_proyectos.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Comuna", None));
        ___qtablewidgetitem16 = self.tabla_proyectos.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Direccion", None));
        ___qtablewidgetitem17 = self.tabla_proyectos.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Superficie", None));
        ___qtablewidgetitem18 = self.tabla_proyectos.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Tipologia", None));
        ___qtablewidgetitem19 = self.tabla_proyectos.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Precio [UF]", None));
        ___qtablewidgetitem20 = self.tabla_proyectos.horizontalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Arriendo [$]", None));
        ___qtablewidgetitem21 = self.tabla_proyectos.horizontalHeaderItem(7)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Arriendo Amoblado[$]", None));
        ___qtablewidgetitem22 = self.tabla_proyectos.horizontalHeaderItem(8)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cap Rate", None));
        self.boton_evaluar_proyecto.setText(QCoreApplication.translate("MainWindow", u"Generar Evaluaci\u00f3n", None))
        self.logo.setText("")
    # retranslateUi

