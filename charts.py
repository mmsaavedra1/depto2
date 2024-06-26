from depto2_gui import Ui_MainWindow
from PySide6.QtGui import Qt, QIcon, QFont, QDesktopServices, QPen, QColor
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QUrl
from PySide6 import QtCharts

from utils.calculo_metricas import *
from os import listdir
import json

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
        self.cae.setText('5.5')
        self.ggoo.setText('1000000')

        self.cae_calculadora.setText('5.5')
        self.plazo_calculadora.setText('30')
        self.ggoo_calculadora.setText('1000000')
        self.financiamiento_calculadora.setText('80')

        self.uf.setText(str(obtener_uf_actualizada(ruta='db/uf_historica.json')))

        # Seteo de la tabla proyectos
        self.tabla_proyectos.setColumnWidth(0, 170)
        header = self.tabla_proyectos.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignLeft)

        # Doble Click y abrir hipervinculo
        self.tabla_proyectos.cellDoubleClicked.connect(self.cell_double_clicked)

        # Seteo de opciones avanzadas de calculadora
        self.avanzado.stateChanged.connect(self.switch_avanced)
        self.frame_avanzado.hide()

        # Habilitar los comboBox de comunas
        self.comuna_1.stateChanged.connect(self.bloqueo_comuna_1)
        self.comuna_2.stateChanged.connect(self.bloqueo_comuna_2)
        self.comuna_3.stateChanged.connect(self.bloqueo_comuna_3)

        # Seteo de la tabla de dfl2
        self.tabla_dfl2.setRowCount(2)
        self.tabla_dfl2.itemChanged.connect(self.actualizar_tabla_dfl2_segun_anio)

        # Logica de boton amoblado
        self.esta_amoblado.stateChanged.connect(self.switch_amoblado)

        # Seteo de las regiones/comunas proyectos
        regiones = sorted(obtener_regiones('db/Proyectos'))

        self.lista_regiones.addItems(regiones)
        self.lista_regiones.currentIndexChanged.connect(self.actualizar_comunas)

        comunas = sorted(obtener_comunas(f'db/Proyectos/{self.lista_regiones.currentText()}'))

        self.lista_comunas.addItems(comunas)
        self.lista_comunas.currentIndexChanged.connect(self.actualizar_plusvalia_comunas)

        self.lista_regiones_2.addItems(regiones)
        self.lista_regiones_2.currentIndexChanged.connect(self.actualizar_comunas_2)

        comunas_2 = sorted(obtener_comunas(f'db/Proyectos/{self.lista_regiones_2.currentText()}'))

        self.lista_comunas_2.addItems(comunas_2)
        self.lista_comunas_2.currentIndexChanged.connect(self.actualizar_plusvalia_comunas_2)
        self.lista_comunas_3.addItems(comunas_2)
        self.lista_comunas_3.currentIndexChanged.connect(self.actualizar_plusvalia_comunas_3)
        self.lista_comunas_4.addItems(comunas_2)
        self.lista_comunas_4.currentIndexChanged.connect(self.actualizar_plusvalia_comunas_4)

        self.plusvalia_1.setText(obtener_plusvalia(self.lista_comunas.currentText()))
        self.plusvalia_2.setText(obtener_plusvalia(self.lista_comunas_2.currentText()))
        self.plusvalia_3.setText(obtener_plusvalia(self.lista_comunas_3.currentText()))
        self.plusvalia_4.setText(obtener_plusvalia(self.lista_comunas_4.currentText()))

       

        # Botones de cabecera
        self.boton_evaluacion.clicked.connect(self.switch_to_evaluacion)
        self.boton_proyectos.clicked.connect(self.switch_to_proyectos)
        
        # Bonton Listar Proyectos
        self.boton_generar_proyectos.clicked.connect(self.actualizar_tabla_proyectos)

        # Boton Generar Evaluacion
        self.boton_generar_evaluacion.clicked.connect(self.actualizar_grafico_dfl2)
        self.boton_generar_evaluacion.clicked.connect(self.actualizar_tabla_dfl2_boton_generar)

        # Revisa que se seleccione un proyecto para evaluar
        self.boton_evaluar_proyecto.clicked.connect(self.evaluar_proyecto)


    # Metodos que mueven las diferente paginas del stack
    def switch_to_evaluacion(self):
        self.widget_pila.setCurrentIndex(0)


    def switch_to_proyectos(self):
        self.widget_pila.setCurrentIndex(1)

    # Metodo que actualiza el ComboBox
    def actualizar_comunas(self):
        self.lista_comunas.clear()
    
        comunas = sorted(obtener_comunas(f'db/Proyectos/{self.lista_regiones.currentText()}'))
        self.lista_comunas.addItems(comunas)


    def actualizar_comunas_2(self):
        self.lista_comunas_2.clear()
        self.lista_comunas_3.clear()
        self.lista_comunas_4.clear()

        comunas = sorted(obtener_comunas(f'db/Proyectos/{self.lista_regiones_2.currentText()}'))
        self.lista_comunas_2.addItems(comunas)
        self.lista_comunas_3.addItems(comunas)
        self.lista_comunas_4.addItems(comunas)


    # Metodo que actualiza las plsuvalias
    def actualizar_plusvalia_comunas(self):
        self.plusvalia_1.setText(obtener_plusvalia(self.lista_comunas.currentText()))
    def actualizar_plusvalia_comunas_2(self):
        self.plusvalia_2.setText(obtener_plusvalia(self.lista_comunas_2.currentText()))
    def actualizar_plusvalia_comunas_3(self):
        self.plusvalia_3.setText(obtener_plusvalia(self.lista_comunas_3.currentText()))
    def actualizar_plusvalia_comunas_4(self):
        self.plusvalia_4.setText(obtener_plusvalia(self.lista_comunas_4.currentText()))


    # Metodos que bloquean combo box de comuna
    def bloqueo_comuna_1(self, state):
        if state == 2:  # Si el checkbox está seleccionado
            self.lista_comunas_2.setEnabled(True)
        else:  # Si el checkbox no está seleccionado
            self.lista_comunas_2.setEnabled(False)


    # Metodos que bloquean combo box de comuna
    def bloqueo_comuna_2(self, state):
        if state == 2:  # Si el checkbox está seleccionado
            self.lista_comunas_3.setEnabled(True)
        else:  # Si el checkbox no está seleccionado
            self.lista_comunas_3.setEnabled(False)


    # Metodos que bloquean combo box de comuna
    def bloqueo_comuna_3(self, state):
        if state == 2:  # Si el checkbox está seleccionado
            self.lista_comunas_4.setEnabled(True)
        else:  # Si el checkbox no está seleccionado
            self.lista_comunas_4.setEnabled(False)


    # Metodos que despliegan los calculos avanzados
    def switch_avanced(self, state):
        if state == 2:  # Si el checkbox está seleccionado
            self.frame_avanzado.show()
        else:  # Si el checkbox no está seleccionado
            self.frame_avanzado.hide()

    # Metodo que deshabilitada arriendo amoblado
    def switch_amoblado(self, state):
        if state == 2:  # Si el checkbox está seleccionado
            self.arriendo_proyecto.setEnabled(False)
            self.arriendo_amoblado.setEnabled(True)
            self.gastos_amoblado.setEnabled(True)
        else:  # Si el checkbox no está seleccionado
            self.arriendo_proyecto.setEnabled(True)
            self.arriendo_amoblado.setEnabled(False)        
            self.gastos_amoblado.setEnabled(False)

    # Metodo que reacciona al doble click sobre las celdas
    def cell_double_clicked(self, row, column):
        url = self.tabla_proyectos.item(row, column).text()
        if column == 9:
            QDesktopServices.openUrl(QUrl(url))


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
            self.arriendo_proyecto.setText(valores_fila_seleccionada[7].strip('$').replace('.',''))
            self.nombre_proyecto.setText(valores_fila_seleccionada[0])
            self.lista_regiones.setCurrentText(self.lista_regiones_2.currentText())
            self.lista_comunas.setCurrentText(valores_fila_seleccionada[1])
            self.plusvalia_1.setText(obtener_plusvalia(valores_fila_seleccionada[1]))
            self.gastos_amoblado.setText(valores_fila_seleccionada[6].strip('$').replace('.',''))
            self.arriendo_amoblado.setText(valores_fila_seleccionada[10].strip('$').replace('.',''))

            self.actualizar_grafico_dfl2()
            self.actualizar_tabla_dfl2_boton_generar()  # La borra y vuelve a cargar
            
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona una fila completa para continuar.")


    # Crear tabla de proyectos segun comunas
    def actualizar_tabla_proyectos(self):

        # Limpiar la tabla
        self.tabla_proyectos.setRowCount(0)

        # Filtrar comunas
        comunas = set()

        # Obtener diccionario de amoblados
        ruta ='db/gastos_amoblado.json'
        with open(ruta, 'r') as file:
            datos_amoblado = json.load(file)

        # Obtener comunas habilitadas
        if self.comuna_1.isChecked() == True:
            comuna_1 = self.lista_comunas_2.currentText()
            comunas.add(comuna_1)
        if self.comuna_2.isChecked() == True:
            comuna_2 = self.lista_comunas_3.currentText()
            comunas.add(comuna_2)
        if self.comuna_3.isChecked() == True:
            comuna_3 = self.lista_comunas_4.currentText()
            comunas.add(comuna_3)

        for comuna_ in comunas:
            if f'{comuna_}_dpto_ventas_resumen_comuna_2024-05.xlsx' in listdir(f'db/Proyectos/{self.lista_regiones_2.currentText()}'):
                df_comuna = pd.read_excel(f'db/Proyectos/{self.lista_regiones_2.currentText()}/{comuna_}_dpto_ventas_resumen_comuna_2024-05.xlsx')
                for row in range(df_comuna.shape[0]):
                    titulo = df_comuna.loc[row, 'Titulo']
                    comuna = comuna_
                    direccion = df_comuna.loc[row, 'Direccion']
                    superficie = " ".join(df_comuna.loc[row, 'Superficie Útil'].split(' ')[:2])
                    tipologia = f"{df_comuna.loc[row, 'Habitaciones'].split(' ')[0]}D+{df_comuna.loc[row, 'Banos'].split(' ')[0]}B"
                    precio = f"UF{df_comuna.loc[row, 'Precio [UF]']:,.0f}".replace(',','.')
                    arriendo = f"${df_comuna.loc[row, 'Precio Arriendo Manual - IA Ponderado']:,.0f}".replace(',','.')
                    arriendo_amoblado = f"${df_comuna.loc[row, 'Arriendo Amoblado Manual - IA Ponderado']:,.0f}".replace(',','.')
                    #cap_rate = f"%{df_comuna.loc[row, 'Cap Rate Manual - IA Ponderado']:,.2f}".replace(".", ',')
                    url = df_comuna.loc[row, 'url']

                    ########## Proceso de calculo de rentabilidades ########## 
                
                    # Calcular la maxima rentabilidad
                    roi_con_venta, max_ano_venta = self.crear_datos_dfl2_listado(
                        precio_compra=int(precio.strip('UF').replace('.','')), 
                        porcentaje_pie=100-int(self.financiamiento_calculadora.text()), 
                        cae=self.cae_calculadora.text(),
                        plazo_credito=int(self.plazo_calculadora.text()),
                        plusvalia_hist=obtener_plusvalia(comuna),
                        ggoo=int(self.ggoo_calculadora.text()),
                        arriendo_proyecto=arriendo.strip('$').replace('.','')
                    )

                    # Calcular la maxima rentabilidad amoblado
                    roi_con_venta_amo, max_ano_venta_amo = self.crear_datos_dfl2_listado(
                        precio_compra=int(precio.strip('UF').replace('.','')), 
                        porcentaje_pie=100-int(self.financiamiento_calculadora.text()), 
                        cae=self.cae_calculadora.text(),
                        plazo_credito=int(self.plazo_calculadora.text()),
                        plusvalia_hist=obtener_plusvalia(comuna),
                        ggoo=int(self.ggoo_calculadora.text())+datos_amoblado[tipologia],
                        arriendo_proyecto=arriendo_amoblado.strip('$').replace('.','')
                    )

                    # Castear datos
                    max_rent = f"%{roi_con_venta*100:,.2f}".replace(".", ',')
                    max_ano_venta = f"{max_ano_venta}"

                    # Castear datos amoblado
                    gastos_amoblado = f"${datos_amoblado[tipologia]:,.0f}".replace(",", '.')
                    max_rent_amo = f"%{roi_con_venta_amo*100:,.2f}".replace(".", ',')
                    max_ano_venta_amo = f"{max_ano_venta_amo}"
                    ########## Proceso de calculo de rentabilidades ########## 

                    # Filtro rango de precios
                    precio_min = 0 if self.precio_3.text() == "" else int(self.precio_3.text())
                    precio_max = 99999999 if self.precio_4.text() == "" else int(self.precio_4.text())
                    precio_ = int(df_comuna.loc[row, 'Precio [UF]'])
                    
                    if precio_min <= precio_ and precio_ <= precio_max:
                        fila_tabla = self.tabla_proyectos.rowCount()
                        self.tabla_proyectos.insertRow(fila_tabla)

                        self.tabla_proyectos.setItem(fila_tabla, 0, QTableWidgetItem(titulo))
                        self.tabla_proyectos.setItem(fila_tabla, 1, QTableWidgetItem(comuna))
                        self.tabla_proyectos.setItem(fila_tabla, 2, QTableWidgetItem(direccion))
                        self.tabla_proyectos.setItem(fila_tabla, 3, QTableWidgetItem(superficie))
                        self.tabla_proyectos.setItem(fila_tabla, 4, QTableWidgetItem(tipologia))
                        self.tabla_proyectos.setItem(fila_tabla, 5, QTableWidgetItem(precio))
                        self.tabla_proyectos.setItem(fila_tabla, 6, QTableWidgetItem(gastos_amoblado))
                        self.tabla_proyectos.setItem(fila_tabla, 7, QTableWidgetItem(arriendo)) 
                        self.tabla_proyectos.setItem(fila_tabla, 8, QTableWidgetItem(max_rent))
                        self.tabla_proyectos.setItem(fila_tabla, 9, QTableWidgetItem(max_ano_venta))
                        self.tabla_proyectos.setItem(fila_tabla, 10, QTableWidgetItem(arriendo_amoblado))
                        self.tabla_proyectos.setItem(fila_tabla, 11, QTableWidgetItem(max_rent_amo))
                        self.tabla_proyectos.setItem(fila_tabla, 12, QTableWidgetItem(max_ano_venta_amo))
                        #self.tabla_proyectos.setItem(fila_tabla, 8, QTableWidgetItem(cap_rate))
                        self.tabla_proyectos.setItem(fila_tabla, 13, QTableWidgetItem(url))


    # Crear valores para desplegar en grafico
    def crear_datos_dfl2(self, cae=None):
        """
        Funcion que calcula las rentabilidades para un proyecto inmobiliario particular
        """
       # Valores ingresado por el usuario
        precio_compra = int(self.precio_2.text())
        porcentaje_pie = self.pie.text()
        cae = self.cae.text() if cae is None else cae
        plazo_credito = int(self.plazo.text())

        if self.uf.text() == "":
            self.uf.setText(str(obtener_uf_actualizada(ruta='db/uf_historica.json')))
        uf = int(self.uf.text())
        
        # Logica en funcion si está amoblado o no
        ggoo = int(self.ggoo.text())/uf
        if self.esta_amoblado.isChecked():
            ggoo += int(self.gastos_amoblado.text())/uf

        plusvalia_hist = self.plusvalia_1.text()

        # 0º calcular el pie
        pie = calcular_pie(precio_compra, porcentaje_pie)
        # 1º calcular el dividendo si no fue entregado
        dividendo = calcular_dividendo(precio_compra, porcentaje_pie, cae, plazo_credito)
        self.dividendo.setText(f"{round(dividendo*uf):,.0f}".replace(',', '.'))
        
        # 2º definir el capital inicial del inversionista
        capital = pie + ggoo
        # 3º calcaular la tabla de amortizacion 
        tabla_amortizacion = calcular_tabla_amortizacion(precio_compra, porcentaje_pie, cae, plazo_credito)
        # 4º calcular arriendo del proyecto
        if self.esta_amoblado.isChecked():
            arriendo_mercado_ia = int(self.arriendo_amoblado.text())/uf
        else:
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
    

    def crear_datos_dfl2_listado(self, precio_compra: int, porcentaje_pie: str, cae: str, plazo_credito:int, plusvalia_hist:str, ggoo:int, arriendo_proyecto:str):
        """
        Funcion que calcula las rentabilidades para cada proeycto del listado inicial
        """
        if self.uf.text() == "":
            self.uf.setText(str(obtener_uf_actualizada(ruta='db/uf_historica.json')))
        uf = int(self.uf.text())

        # 0º calcular el pie
        pie = calcular_pie(precio_compra, porcentaje_pie)
        # 1º calcular el dividendo si no fue entregado
        dividendo = calcular_dividendo(precio_compra, porcentaje_pie, cae, plazo_credito)
        self.dividendo.setText(f"{round(dividendo*uf):,.0f}".replace(',', '.'))        
        # 2º definir el capital inicial del inversionista
        ggoo = ggoo/uf
        capital = pie + ggoo
        # 3º calcaular la tabla de amortizacion 
        tabla_amortizacion = calcular_tabla_amortizacion(precio_compra, porcentaje_pie, cae, plazo_credito)
        # 4º calcular arriendo del proyecto
        arriendo_mercado_ia = int(arriendo_proyecto)/uf
        # 5º calcular el caprate del proyecto
        cap_rate = obtener_cap_rate(arriendo_mercado_ia, precio_compra)
        # 6º calcular el gap de arriendo y dividendo
        gap_mensual = obtener_gap_arriendo_dividendo(arriendo_mercado_ia, dividendo, 'UF', uf)

        #### Esta parte es para construir el grafico de venta
        max_ano_rentabilidad = 0
        max_rentabilidad = 0

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

            if roi_con_venta > max_rentabilidad:
                max_ano_rentabilidad = i
                max_rentabilidad = roi_con_venta
        
        return max_rentabilidad, max_ano_rentabilidad


    
    # Obtener valores segun el año de analisis
    def actualizar_tabla_dfl2_segun_anio(self, item):
        # Desconecta la señal para evitar recursion
        self.tabla_dfl2.itemChanged.disconnect(self.actualizar_tabla_dfl2_segun_anio)

        if item.row() == 1 and item.column() == 0:
            indice = self.tabla_dfl2.item(1, 0).text()
            if indice != "":
                self.actualizar_tabla_dfl2(indice=indice)

        # Conecta la señal para la futura ejecucion
        self.tabla_dfl2.itemChanged.connect(self.actualizar_tabla_dfl2_segun_anio)


    # Actualizar tabla DFL2 si se aprieta el boton
    def actualizar_tabla_dfl2_boton_generar(self):
        # Actualizar la tabla dfl2 a cero
        for row in range(2):
            for column in range(self.tabla_dfl2.columnCount()):
                self.tabla_dfl2.setItem(row, column, QTableWidgetItem(""))

        self.actualizar_tabla_dfl2(indice=None)


    # Obtener valores de recomendacion de venta
    def actualizar_tabla_dfl2(self, indice=None):
        values, cap_rate = self.crear_datos_dfl2()
        plazo_venta, rentabilidad_flujos, rentabilidad_plusvalia, rentabilidad_amortizacion, roi_sin_venta, roi_con_venta, utilidad_venta = zip(*values)

        if indice==None:
            indice_max = roi_con_venta.index(max(roi_con_venta))
            row = 0
        else:
            indice_max = int(indice)-1
            row = 1

        max_ano_venta = plazo_venta[indice_max]
        max_rent_total = roi_con_venta[indice_max]
        max_rent_flujo = rentabilidad_flujos[indice_max]
        max_rent_plusvalia = rentabilidad_plusvalia[indice_max]
        max_rent_amortizacion = rentabilidad_amortizacion[indice_max]
        max_utilidad = utilidad_venta[indice_max]

        self.tabla_dfl2.setItem(row, 0, QTableWidgetItem(str(max_ano_venta)))
        self.tabla_dfl2.setItem(row, 1, QTableWidgetItem(f"%{round(cap_rate*100,2)}"))
        self.tabla_dfl2.setItem(row, 2, QTableWidgetItem(f"%{round(max_rent_total*100,2)}"))
        self.tabla_dfl2.setItem(row, 3, QTableWidgetItem(f"%{round(max_rent_flujo*100,2)}"))
        self.tabla_dfl2.setItem(row, 4, QTableWidgetItem(f"%{round(max_rent_plusvalia*100,2)}"))
        self.tabla_dfl2.setItem(row, 5, QTableWidgetItem(f"%{round(max_rent_amortizacion*100,2)}"))
        self.tabla_dfl2.setItem(row, 6, QTableWidgetItem(f"UF{round(max_utilidad)}"))

    
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

        # Hacer mas gruesa la linea
        grosor = 4
        pen_1 = QPen(QColor(32, 159, 223))
        pen_1.setWidth(grosor)
        rentabilidad_total_venta_series.setPen(pen_1)

        pen_2 = QPen(QColor(153, 202, 83))
        pen_2.setWidth(grosor)
        rentabilidad_total_sin_venta_series.setPen(pen_2)

        pen_3 = QPen(QColor(246, 166, 37))
        pen_3.setWidth(grosor)
        rentabilidad_plusvalia_series.setPen(pen_3)

        pen_4 = QPen(QColor(109, 95, 213))
        pen_4.setWidth(grosor)
        rentabilidad_amortizacion_series.setPen(pen_4)

        pen_5 = QPen(QColor(191, 89, 62))
        pen_5.setWidth(grosor)
        rentabilidad_flujos_series.setPen(pen_5)

        axis_y_min = 0
        axis_y_max = 0

        for plazo_venta, rentabilidad_flujos, rentabilidad_plusvalia, rentabilidad_amortizacion, roi_sin_venta, roi_con_venta, _ in values:
            rentabilidad_total_venta_series.append(plazo_venta, roi_con_venta*100)
            rentabilidad_total_sin_venta_series.append(plazo_venta, roi_sin_venta*100)
            rentabilidad_plusvalia_series.append(plazo_venta, rentabilidad_plusvalia*100)
            rentabilidad_amortizacion_series.append(plazo_venta, rentabilidad_amortizacion*100)
            rentabilidad_flujos_series.append(plazo_venta, rentabilidad_flujos*100)
            years.append(str(plazo_venta))
            axis_y_min =  min(roi_con_venta*100, roi_sin_venta*100, rentabilidad_plusvalia*100, rentabilidad_amortizacion*100, rentabilidad_flujos*100, axis_y_min)
            axis_y_max =  max(roi_con_venta*100, roi_sin_venta*100, rentabilidad_plusvalia*100, rentabilidad_amortizacion*100, rentabilidad_flujos*100, axis_y_max)


        # Buscar el maximo valor para la vertical
        plazo_venta, _, _, _, _, roi_con_venta, _ = zip(*values)
        indice_max = roi_con_venta.index(max(roi_con_venta))
        max_ano_venta = float(plazo_venta[indice_max])

        vertical_line = QtCharts.QLineSeries()
        vertical_line.setName("Año Venta")

        vertical_pen = QPen(Qt.red)
        vertical_pen.setStyle(Qt.DashLine)
        vertical_pen.setWidth(grosor-1)
        vertical_line.setPen(vertical_pen)

        vertical_line.append(max_ano_venta, axis_y_min-2)
        vertical_line.append(max_ano_venta, axis_y_max+2)

        # Añadir las series de datos al grafico
        chart.addSeries(rentabilidad_total_venta_series)
        chart.addSeries(rentabilidad_total_sin_venta_series)
        chart.addSeries(rentabilidad_plusvalia_series)
        chart.addSeries(rentabilidad_amortizacion_series)
        chart.addSeries(rentabilidad_flujos_series)
        chart.addSeries(vertical_line)
        
        # Crear ejes verticales y horizontales
        axis_x = QtCharts.QValueAxis()
        axis_x.setLabelFormat("%.0f")
        axis_x.setRange(float(years[0]), float(years[-1]))
        chart.addAxis(axis_x, Qt.AlignBottom)

        axis_y = QtCharts.QValueAxis()
        axis_y.setLabelFormat("%.0f%%")
        axis_y.setRange(-2+axis_y_min, axis_y_max+2)
        chart.addAxis(axis_y, Qt.AlignLeft)


        # Ajustar datos al eje que corresponde
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

        vertical_line.attachAxis(axis_x)
        vertical_line.attachAxis(axis_y)

        # Añadir datos a la vista de Grafico
        self.grafico_dfl2.setChart(chart)

