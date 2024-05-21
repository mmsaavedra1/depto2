from depto2_gui import Ui_MainWindow
from PySide6.QtGui import Qt, QIcon, QFont
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PySide6 import QtCharts

from utils.calculo_metricas import *
from os import listdir

class Depto2App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Depto2 App")
        self.setWindowIcon(QIcon("/images/Logo.png"))
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.setFixedSize(self.size())

        #Seteo de parametros
        self.pie.setText('20')
        self.plazo.setText('30')
        self.cae.setText('5')
        self.uf.setText(str(obtener_uf_actualizada(ruta='db/uf_historica.json')))

        # Seteo de la tabla proyectos
        self.tabla_proyectos.setColumnWidth(0, 170)
        header = self.tabla_proyectos.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignLeft)

        # Seteo de las comunas proyectos
        comunas = sorted(obtener_comunas('db/'))
        self.lista_comunas_2.addItems(comunas)
        self.lista_comunas_3.addItems(comunas)
        self.lista_comunas_4.addItems(comunas)

        # Seteo de las comunas evaluacion
        self.lista_comunas.addItems(comunas)

        self.boton_evaluacion.clicked.connect(self.switch_to_evaluacion)
        self.boton_proyectos.clicked.connect(self.switch_to_proyectos)
        self.boton_generar_proyectos.clicked.connect(self.actualizar_tabla_proyectos)
        self.boton_generar_evaluacion.clicked.connect(self.actualizar_grafico_dfl2)
        self.boton_generar_evaluacion.clicked.connect(self.actualizar_tabla_dfl2)

        # Revisa que se seleccione un proyecto para evaluar
        self.boton_evaluar_proyecto.clicked.connect(self.evaluar_proyecto)


     # Metodos que mueven las diferente paginas del stack
    def switch_to_evaluacion(self):
        self.widget_pila.setCurrentIndex(0)

    def switch_to_proyectos(self):
        self.widget_pila.setCurrentIndex(1)


    # Metodo que evalua un proyecto seleccionado
    def evaluar_proyecto(self):
        rango_seleccionados = self.tabla_proyectos.selectedRanges()
        fila_seleccionada = False
        valores_fila_seleccionada = []

        for rango_seleccionado in rango_seleccionados:
            if rango_seleccionado.columnCount() == self.tabla_proyectos.columnCount():
                fila_seleccionada = True
                selected_row = rango_seleccionado.topRow()
                valores_fila_seleccionada = [
                    self.tabla_proyectos.item(selected_row, column).text() 
                    for column in range(self.tabla_proyectos.columnCount())
                ]
                break

        if fila_seleccionada:
            self.widget_pila.setCurrentIndex(0)
            self.boton_proyectos.setChecked(False)
            self.boton_evaluacion.setChecked(True)

            self.precio_2.setText(valores_fila_seleccionada[5].strip('UF').replace('.',''))
            self.arriendo_proyecto.setText(valores_fila_seleccionada[6].strip('$').replace('.',''))
            self.nombre_proyecto.setText(valores_fila_seleccionada[0])
            self.lista_comunas.setCurrentText(valores_fila_seleccionada[1])

            self.actualizar_grafico_dfl2()
            self.actualizar_tabla_dfl2()
            
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona una fila completa para continuar.")


    # Crear tabla de proyectos segun comunas
    def actualizar_tabla_proyectos(self):

        # Limpiar la tabla
        self.tabla_proyectos.setRowCount(0)
        
        # Filtrar comunas
        comunas = set([
            self.lista_comunas_2.currentText(),
            self.lista_comunas_3.currentText(),
            self.lista_comunas_4.currentText()])

        for comuna_ in comunas:

            if f'{comuna_}_dpto_ventas_resumen_2024-05.xlsx' in listdir('db'):
                df_comuna = pd.read_excel(f'db/{comuna_}_dpto_ventas_resumen_2024-05.xlsx')

                for row in range(df_comuna.shape[0]):
                    titulo = df_comuna.loc[row, 'Titulo']
                    comuna = comuna_
                    direccion = df_comuna.loc[row, 'Direccion']
                    superficie = " ".join(df_comuna.loc[row, 'Superficie Útil'].split(' ')[:2])
                    tipologia = f"{df_comuna.loc[row, 'Habitaciones'].split(' ')[0]}D+{df_comuna.loc[row, 'Banos'].split(' ')[0]}B"
                    precio = f"UF{df_comuna.loc[row, 'precio [UF]']:,.0f}".replace(',','.')
                    arriendo = f"${df_comuna.loc[row, 'Precio Arriendo Manual - IA Ponderado']:,.0f}".replace(',','.')
                    arriendo_amoblado = f"${df_comuna.loc[row, 'Arriendo Amoblado Manual - IA Ponderado']:,.0f}".replace(',','.')
                    cap_rate = f"%{df_comuna.loc[row, 'Cap Rate Manual - IA Ponderado']:,.2f}".replace(".", ',')
                    
                    # Filtro rango de precios
                    precio_min = 0 if self.precio_3.text() == "" else int(self.precio_3.text())
                    precio_max = 99999999 if self.precio_4.text() == "" else int(self.precio_4.text())
                    precio_ = int(df_comuna.loc[row, 'precio [UF]'])
                    
                    if precio_min <= precio_ and precio_ <= precio_max:
                        fila_tabla = self.tabla_proyectos.rowCount()
                        self.tabla_proyectos.insertRow(fila_tabla)

                        self.tabla_proyectos.setItem(fila_tabla, 0, QTableWidgetItem(titulo))
                        self.tabla_proyectos.setItem(fila_tabla, 1, QTableWidgetItem(comuna))
                        self.tabla_proyectos.setItem(fila_tabla, 2, QTableWidgetItem(direccion))
                        self.tabla_proyectos.setItem(fila_tabla, 3, QTableWidgetItem(superficie))
                        self.tabla_proyectos.setItem(fila_tabla, 4, QTableWidgetItem(tipologia))
                        self.tabla_proyectos.setItem(fila_tabla, 5, QTableWidgetItem(precio))
                        self.tabla_proyectos.setItem(fila_tabla, 6, QTableWidgetItem(arriendo)) 
                        self.tabla_proyectos.setItem(fila_tabla, 7, QTableWidgetItem(arriendo_amoblado))
                        self.tabla_proyectos.setItem(fila_tabla, 8, QTableWidgetItem(cap_rate))


    # Crear valores para desplegar en grafico
    def crear_datos_dfl2(self):
       # Valores ingresado por el usuario
        precio_compra = int(self.precio_2.text())
        porcentaje_pie = self.pie.text()
        cae = self.cae.text()
        plazo_credito = int(self.plazo.text())

        if self.uf.text() == "":
            self.uf.setText(str(obtener_uf_actualizada(ruta='db/uf_historica.json')))
        uf = int(self.uf.text())
        
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
        arriendo_mercado_ia = int(self.arriendo_proyecto.text())/uf
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
            # 13º anualizar los valores
            rentabilidad_flujos = anualizar_tasa(rentabilidad_flujos, plazo_venta)
            rentabilidad_plusvalia = anualizar_tasa(rentabilidad_plusvalia, plazo_venta)
            rentabilidad_amortizacion = anualizar_tasa(rentabilidad_amortizacion, plazo_venta)
            roi_sin_venta = anualizar_tasa(roi_sin_venta, plazo_venta)
            roi_con_venta = anualizar_tasa(roi_con_venta, plazo_venta)  

            # guardar valores historicos para graficar
            datos.append([plazo_venta, rentabilidad_flujos, rentabilidad_plusvalia, rentabilidad_amortizacion, roi_sin_venta, roi_con_venta, utilidad_venta])

        return datos, cap_rate


    # Obtener valores de recomendacion de venta
    def actualizar_tabla_dfl2(self):
        values, cap_rate = self.crear_datos_dfl2()
        plazo_venta, rentabilidad_flujos, rentabilidad_plusvalia, rentabilidad_amortizacion, roi_sin_venta, roi_con_venta, utilidad_venta = zip(*values)

        indice_max = roi_con_venta.index(max(roi_con_venta))

        max_ano_venta = plazo_venta[indice_max]
        max_rent_total = roi_con_venta[indice_max]
        max_rent_flujo = rentabilidad_flujos[indice_max]
        max_rent_plusvalia = rentabilidad_plusvalia[indice_max]
        max_rent_amortizacion = rentabilidad_amortizacion[indice_max]
        max_utilidad = utilidad_venta[indice_max]

        self.tabla_dfl2.insertRow(self.tabla_dfl2.rowCount())
        self.tabla_dfl2.setItem(0, 0, QTableWidgetItem(str(max_ano_venta)))
        self.tabla_dfl2.setItem(0, 1, QTableWidgetItem(f"%{round(cap_rate*100,2)}"))
        self.tabla_dfl2.setItem(0, 2, QTableWidgetItem(f"%{round(max_rent_total*100,2)}"))
        self.tabla_dfl2.setItem(0, 3, QTableWidgetItem(f"%{round(max_rent_flujo*100,2)}"))
        self.tabla_dfl2.setItem(0, 4, QTableWidgetItem(f"%{round(max_rent_plusvalia*100,2)}"))
        self.tabla_dfl2.setItem(0, 5, QTableWidgetItem(f"%{round(max_rent_amortizacion*100,2)}"))
        self.tabla_dfl2.setItem(0, 6, QTableWidgetItem(f"UF{round(max_utilidad)}"))
        
    
    # Manejar el grafico de torta
    def actualizar_grafico_dfl2(self):
        chart = QtCharts.QChart()
        chart.setTitle("Rentabilidades Proyectadas - DFL2")
        chart_font = QFont()
        chart_font.setPointSize(15)
        chart_font.setBold(True)
        chart.setTitleFont(chart_font)

        values, _ = self.crear_datos_dfl2()

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

        axis_y_min = 0
        axis_y_max = 0


        #plazo_venta, rentabilidad_flujos, rentabilidad_plusvalia, rentabilidad_amortizacion, roi_sin_venta, roi_con_venta, _ = zip(*values)
        for plazo_venta, rentabilidad_flujos, rentabilidad_plusvalia, rentabilidad_amortizacion, roi_sin_venta, roi_con_venta, _ in values:
            rentabilidad_total_venta_series.append(plazo_venta, roi_con_venta*100)
            rentabilidad_total_sin_venta_series.append(plazo_venta, roi_sin_venta*100)
            rentabilidad_plusvalia_series.append(plazo_venta, rentabilidad_plusvalia*100)
            rentabilidad_amortizacion_series.append(plazo_venta, rentabilidad_amortizacion*100)
            rentabilidad_flujos_series.append(plazo_venta, rentabilidad_flujos*100)
            years.append(str(plazo_venta))
            axis_y_min =  min(roi_con_venta*100, roi_sin_venta*100, rentabilidad_plusvalia*100, rentabilidad_amortizacion*100, rentabilidad_flujos*100, axis_y_min)
            axis_y_max =  max(roi_con_venta*100, roi_sin_venta*100, rentabilidad_plusvalia*100, rentabilidad_amortizacion*100, rentabilidad_flujos*100, axis_y_max)
        
        #rentabilidad_total_venta_series.append(zip(plazo_venta, roi_con_venta))
        #rentabilidad_total_sin_venta_series.append(zip(plazo_venta, roi_sin_venta))
        #rentabilidad_plusvalia_series.append(zip(plazo_venta, rentabilidad_plusvalia))
        #rentabilidad_amortizacion_series.append(zip(plazo_venta, rentabilidad_amortizacion))
        #rentabilidad_flujos_series.append(zip(plazo_venta, rentabilidad_flujos))
        #years = [str(x) for x in plazo_venta]
        #axis_y_min =  min(roi_con_venta + roi_sin_venta + rentabilidad_plusvalia + rentabilidad_amortizacion + rentabilidad_flujos)
        #axis_y_max =  max(roi_con_venta + roi_sin_venta + rentabilidad_plusvalia + rentabilidad_amortizacion + rentabilidad_flujos)

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
        axis_y.setLabelFormat("%.0f%%")
        axis_y.setRange(-2+axis_y_min, axis_y_max+2)
        chart.addAxis(axis_y, Qt.AlignLeft)

        rentabilidad_total_venta_series.attachAxis(axis_x)
        rentabilidad_total_venta_series.attachAxis(axis_y)

        rentabilidad_total_sin_venta_series.attachAxis(axis_x)
        rentabilidad_total_sin_venta_series.attachAxis(axis_y)
        
        rentabilidad_plusvalia_series.attachAxis(axis_x)
        rentabilidad_plusvalia_series.attachAxis(axis_y)
        
        rentabilidad_amortizacion_series.attachAxis(axis_x)
        rentabilidad_amortizacion_series.attachAxis(axis_y)
        
        rentabilidad_flujos_series.attachAxis(axis_x)
        rentabilidad_flujos_series.attachAxis(axis_y)

        self.grafico_dfl2.setChart(chart)


