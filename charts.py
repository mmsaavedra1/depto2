from depto2_gui import Ui_MainWindow
from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import QMainWindow
from PySide6 import QtCharts

from utils.calculo_metricas import *

class Depto2App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Depto2 App")
        self.setWindowIcon(QIcon("/images/Logo.png"))

        self.boton_evaluacion.clicked.connect(self.switch_to_evaluacion)
        self.boton_proyectos.clicked.connect(self.switch_to_proyectos)
        self.boton_generar_evaluacion.clicked.connect(self.update_linegraph)

    # Metodos que mueven las diferente paginas del stack
    def switch_to_evaluacion(self):
        self.widget_pila.setCurrentIndex(0)

    def switch_to_proyectos(self):
        self.widget_pila.setCurrentIndex(1)

    # Crear valores para desplegar en grafico
    def create_linegraph_values(self):
       # Valores ingresado por el usuario
        precio_compra = int(self.precio_2.text())
        porcentaje_pie = self.pie.text()
        cae = self.cae.text()
        plazo_credito = int(self.plazo.text())
        uf = 37000  # obtener_uf_actualizada()
        ggoo = 1e6/uf
        plusvalia_hist = '3.5'

        # 0º calcular el pie
        pie = calcular_pie(precio_compra, porcentaje_pie)
        # 1º calcular el dividendo si no fue entregado
        dividendo = calcular_dividendo(precio_compra, porcentaje_pie, cae, plazo_credito)
        # 2º definir el capital inicial del inversionista
        capital = pie + ggoo
        # 3º calcaular la tabla de amortizacion 
        tabla_amortizacion = calcular_tabla_amortizacion(precio_compra, porcentaje_pie, cae, plazo_credito)
        # 4º calcular arriendo del proyecto
        arriendo_mercado_ia = precio_compra/12
        # 5º calcular el caprate del proyecto
        cap_rate = obtener_cap_rate(arriendo_mercado_ia, precio_compra)
        # 6º calcular el gap de arriendo y dividendo
        gap_mensual = obtener_gap_arriendo_dividendo(arriendo_mercado_ia, dividendo, 'UF', uf)

        #### Esta parte es para construir el grafico de venta
        datos = []
        for i in range(1, plazo_credito):
            plazo_venta = i
            # 7º calcular rentabilidad por flujos
            rentabilidad_flujos = obtener_rentabilidad_flujo(plazo_venta, gap_mensual*12, capital)
            # 8º calcular rentabilidad por plusvalia
            rentabilidad_plusvalia = obtener_rentabilidad_plusvalia(plazo_venta, plusvalia_hist, precio_compra, capital)
            # 9º calcular rentabilidad por amortizacion
            rentabilidad_amortizacion = obtener_rentabilidad_amortizacion(precio_compra, porcentaje_pie, plazo_venta, tabla_amortizacion, capital)
            # 10º calcular utilidad sin venta
            utilidad_no_venta = obtener_utilidades_no_venta(capital, rentabilidad_flujos, rentabilidad_plusvalia, rentabilidad_amortizacion)
            # 11º calcular utilidad con venta
            utilidad_venta = obtener_utilidades_venta(precio_compra, capital, rentabilidad_flujos, rentabilidad_plusvalia, rentabilidad_amortizacion)
            # 11º calcular ROI sin venta
            roi_sin_venta = obtener_roi(utilidad_no_venta, capital)
            # 12º calcular ROI con venta
            roi_con_venta = obtener_roi(utilidad_venta, capital)       

            # guardar valores historicos para graficar
            datos.append([plazo_venta, rentabilidad_flujos, rentabilidad_plusvalia, rentabilidad_amortizacion, roi_sin_venta, roi_con_venta])

        return datos

    
    # Manejar el grafico de torta
    def update_linegraph(self):
        chart = QtCharts.QChart()
        chart.setTitle("Rentabilidades Proyectadas En El Tiempo")

        values = self.create_linegraph_values()

        years = []
        rentabilidad_total_venta_series = QtCharts.QLineSeries()
        rentabilidad_total_sin_venta_series = QtCharts.QLineSeries()
        rentabilidad_plusvalia_series = QtCharts.QLineSeries()
        rentabilidad_amortizacion_series = QtCharts.QLineSeries()
        rentabilidad_flujos_series = QtCharts.QLineSeries()

        rentabilidad_total_venta_series.setName('ROI Con Venta')
        rentabilidad_total_sin_venta_series.setName('ROI Sin Venta')
        rentabilidad_plusvalia_series.setName('R. Plusvalia')
        rentabilidad_amortizacion_series.setName('R. Amortizacion')
        rentabilidad_flujos_series.setName('R. Flujos')
        
        for plazo_venta, rentabilidad_flujos, rentabilidad_plusvalia, rentabilidad_amortizacion, roi_sin_venta, roi_con_venta in values:
            rentabilidad_total_venta_series.append(plazo_venta, roi_con_venta)
            rentabilidad_total_sin_venta_series.append(plazo_venta, roi_sin_venta)
            rentabilidad_plusvalia_series.append(plazo_venta, rentabilidad_plusvalia)
            rentabilidad_amortizacion_series.append(plazo_venta, rentabilidad_amortizacion)
            rentabilidad_flujos_series.append(plazo_venta, rentabilidad_flujos)
            years.append(str(plazo_venta))
        
        chart.addSeries(rentabilidad_total_venta_series)
        chart.addSeries(rentabilidad_total_sin_venta_series)
        chart.addSeries(rentabilidad_plusvalia_series)
        chart.addSeries(rentabilidad_amortizacion_series)
        chart.addSeries(rentabilidad_flujos_series)

        axis_x = QtCharts.QValueAxis()
        axis_x.setLabelFormat("%.0f")
        axis_x.setRange(float(years[0]), float(years[-1]))
        chart.addAxis(axis_x, Qt.AlignBottom)

        axis_y = QtCharts.QValueAxis()

        rentabilidad_total_venta_series.attachAxis(axis_x)
        rentabilidad_total_sin_venta_series.attachAxis(axis_x)
        rentabilidad_plusvalia_series.attachAxis(axis_x)
        rentabilidad_amortizacion_series.attachAxis(axis_x)
        rentabilidad_flujos_series.attachAxis(axis_x)

        self.grafico_evaluacion.setChart(chart)


