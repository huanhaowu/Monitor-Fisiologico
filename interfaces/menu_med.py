# Librerias de Tkinter
import tkinter as tk
from tkinter import Canvas, Entry, Button, PhotoImage, ttk, Label, StringVar, messagebox

# Modelos de datos
from modelos.parametros_fisiologicos import ParametrosFisiologicos
from modelos.medicion_parametro import MedicionParametro
from modelos.mediciones_sujeto import MedicionesSujeto

# Libreria para utilizar funciones del sistema
import os
from pathlib import Path



class MenuMed(tk.Frame):
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#FFFFFF')
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"assets/menu_med")
        
        self.controller = controller
        
        
    def crear_elementos_formulario(self):
        self.controller.title("Menu de Mediciones")

        
        #Canvas de la ventana principal
        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 725,
            width = 1260,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)

        #Imagen del logo (HEARTBEAT)
        self.imagen_logo_app = PhotoImage(file=self.relative_to_assets("logo.png"))
        
        self.logo_app = self.canvas.create_image(
            640.0,
            61.0,
            image=self.imagen_logo_app
        )         
       
        #region // Botón Regresar
        self.imagen_btn_regresar = PhotoImage(
            file=self.relative_to_assets("btn_regresar.png"))

        self.btn_volver = Button(
            self,
            image=self.imagen_btn_regresar,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.confirmar_regreso(),
            relief="flat",
            bg = "White"
        )
        self.btn_volver.place(
            x=21.0,
            y=26.0,
            width=61.0,
            height=60.0
        )
        
        #endregion

        #region // Botón Comenzar (Comienza el proceso de una medicion)
        
        self.imagen_btn_comenzar = PhotoImage(
            file=self.relative_to_assets("btn_comenzar.png"))
        
        self.btn_comenzar = Button(
            self,
            image=self.imagen_btn_comenzar,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.validar(self.validar_caso),
            relief="flat",
            bg = "White"
        )

        self.btn_comenzar.place(
            x=1060.0,
            y=488.0,
            width=61.65789794921875,
            height=66.0
        )

        #endregion

        #region // Botón Limpiar Textos en Pantalla (Limpia los datos de la medición actual y sus respectivas instrucciones)
        self.imagen_btn_limpiar_textos_en_pantalla = PhotoImage(
            file=self.relative_to_assets("btn_limpiar.png"))
        self.btn_limpiar_textos_en_pantalla = Button(
            self,
            image=self.imagen_btn_limpiar_textos_en_pantalla,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.habilitar_botones(),
            relief="flat",
            bg = "White",  
        )
        self.btn_limpiar_textos_en_pantalla.place(
            x=1122.0,
            y=491.0,
            width=67.0,
            height=71.71826171875
        )
        #endregion

        #region // Botón Temperatura (Boton para elegir la medición de temperatura)
        self.imagen_btn_temperatura = PhotoImage(
            file=self.relative_to_assets("btn_temperatura.png"))
        self.btn_temperatura = Button(
            self,
            image=self.imagen_btn_temperatura,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.elegir_parametro("Temperatura","a"),
            relief="flat",
            bg = "White", 
        )
        self.btn_temperatura.place(
            x=-25.0,
            y=180.0,
            width=518.0,
            height=93.0
        )

        #endregion

      
        #region // Botón Saturación de Oxígeno (Boton para elegir la medición de saturación de oxígeno)
        self.imagen_btn_saturacion_oxigeno = PhotoImage(
            file=self.relative_to_assets("btn_sat_oxigeno.png"))
        
        self.btn_saturacion_oxigeno = Button(
            self,
            image=self.imagen_btn_saturacion_oxigeno,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.elegir_parametro("Saturacion de Oxigeno","b"),
            relief="flat",
            bg = "White", 
        )
        self.btn_saturacion_oxigeno.place(
            x=-10.0,
            y=289.0,
            width=483.0,
            height=90.0
        )

        #endregion

        #region // Botón Presión Arterial (Boton para elegir la medición de presión arterial)
        self.imagen_btn_presion_arterial = PhotoImage(
            file=self.relative_to_assets("btn_presion.png"))
        self.btn_presion_arterial = Button(
            self,
            image=self.imagen_btn_presion_arterial,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.elegir_parametro("Presion Arterial","c"),
            relief="flat",
            bg = "White",
        )
        self.btn_presion_arterial.place(
            x=-10.0,
            y=405.0,
            width=484.0,
            height=97.0
        )
    
        #endregion

        #region // Botón Frecuencia Cardíaca (Boton para elegir la medición de frecuencia cardíaca)
        self.imagen_btn_frecuencia_cardiaca = PhotoImage(
            file=self.relative_to_assets("btn_frecuencia.png"))

        self.btn_frecuencia_cardiaca = Button(
            self,
            image=self.imagen_btn_frecuencia_cardiaca,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.elegir_parametro("Frecuencia Cardiaca","d"),
            relief="flat",
            bg = "White", 
        )

        self.btn_frecuencia_cardiaca.place(
            x=-10.0,
            y=522.0,
            width=471.0,
            height=92.0
        )
        #endregion

        #region // Botón Generar Informe (Boton para pasar a la pantalla de generar el reporte de meficion)
        self.imagen_btn_generar_reporte = PhotoImage(
            file=self.relative_to_assets("btn_reporte.png"))

        self.btn_generar_reporte = Button(
            self,
            image=self.imagen_btn_generar_reporte,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.abrir_reporte(), 
            relief="flat",
            bg = "White", 
        )
        self.btn_generar_reporte.place(
            x=838.0,
            y=646.0,
            width=424.0,
            height=91.0
        )
        
        #endregion

        #Variable de texto para ir cambiando las instrucciones para las mediciones
        self.texto_pantalla = StringVar()
        self.texto_pantalla.set("")

        #Label que muestra las instrucciones en pantalla para las mediciones
        self.lbl_pantalla = Label(
            self,
            borderwidth=2, 
            relief="groove", 
            bg = "white",
            textvariable = self.texto_pantalla, 
            anchor="nw", #Se coloca el texto hacia arriba y hacia la izquierda
            justify="left", #justificar el texto a la izquierda
            font = ("Arial", 12)
            )

        self.lbl_pantalla.place(
            x = 561.0,
            y = 280.0,
            width = 630.0,
            height = 200.0  
            )
        
        # region // Texbox de la altura
        self.canvas.create_text(
            720.0,
            177.0,
            anchor="nw",
            text="Altura",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )
        
        self.txb_altura = Entry(
            self,
            bd=1,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0, 
            font=("Arial", 16)
        )

        #Enlaza la función evitar_espacio a la txb_altura cada vez que se presiona una tecla en la entrada.
        self.txb_altura.bind('<Key>', self.evitar_espacio)

        self.txb_altura.place(
            x=610.0,
            y=233.0,
            width=165.0,
            height=35.0
        )

        # endregion


        # region // Combobox unidad de medida de la altura (si esta dada en Metros o Pies)
        self.cb_altura = ttk.Combobox(
        self,
        state = "readonly",
        values = ["Metros","Pies"], 
        font=("Arial", 16)
        )
      
        self.cb_altura.place(
            x=790.0,
            y=234.0,
            width=90.0,
            height=35.0
        )

        self.cb_altura.config(font=("Arial", 16))

        self.cb_altura.current(0)

        #endregion 
        
        #region // Textbox del Peso
        self.canvas.create_text(
            990.0,
            177.0,
            anchor="nw",
            text="Peso",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )

        self.txb_peso = Entry(
            self,
            bd=1,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 16)
        )
        
        #Enlaza la función evitar_espacio a la txb_peso cada vez que se presiona una tecla en la entrada.
        self.txb_peso.bind('<Key>', self.evitar_espacio) 

        self.txb_peso.place(
            x=900.0,
            y=234.0,
            width=178.0,
            height=34.0
        )

        # endregion

        # region // Combobox unidad de medida del peso (si esta dado en lb o kg)

        self.cb_peso = ttk.Combobox(
        self,
        state = "readonly",
        values = ["Kg","Lb"], 
        font=("Arial", 16)
        )

        self.cb_peso.place(
            x=1090.0,
            y=234.0,
            width=59.0,
            height=35.0
        )

        #Estableciendo por defecto el primer elemento de la lista del combobox del peso
        self.cb_peso.current(0)
        
        #endregion 

        # region // Label de la medida obtenida
        
        #Variable de texto para ir cambiando la medida de los parametro medidos
        self.texto_parametro = StringVar()
        #Inicializando la variable
        self.texto_parametro.set("")
        
        self.lbl_parametro = Label(
            self,
            borderwidth=2, 
            relief="groove", 
            bg = "white",
            textvariable= self.texto_parametro, 
            anchor="center", #se coloca el texto hacia arriba y hacia la izquierda
            font = ("Arial", 18)
        )

        self.lbl_parametro.place(
            x=561.0,
            y=554.0,
            width=289.0,
            height=55.0 
        )

        # endregion

        # region // Label con el parametro medido
        
        #Variable de texto para ir cambiando el label de los parametro medidos
        self.texto_parametro_medido = StringVar()
        
        self.texto_parametro_medido.set("Parametro medido:")

        self.lbl_parametro_medido = Label(
            self,
            borderwidth=0,
            relief="groove", 
            bg = "white",
            textvariable= self.texto_parametro_medido, 
            anchor="center", #se coloca el texto hacia arriba y hacia la izquierda
            font = ("Arial", 18)
        )

        self.lbl_parametro_medido.place(
            x = 570.0,
            y = 510.0
        )

        #endregion

        self.validar_medicion()
        
        self.validar_caso = " " #variable que funciona para validar cual es el caso que se encuentra activo, esta inicializada en " " debido a que es el caso por defecto
        
        self.deshabilitar_botones("", "")
        
        self.mostrar_instrucciones("", "") #Colocar el texto por defecto al iniciar la interfaz en la pantalla
            

    # Funcion para abrir el registro del sujeto nuevamente
    def abrir_registro(self):
        del self.controller.medicion
        self.controller.show_frame("RegistroSujeto")


    # Funcion para abrir el reporte de la medicion
    def abrir_reporte(self):
        from interfaces.reporte_med import ReporteMed
        import datetime
        medicion_sujeto = MedicionesSujeto()
        medicion_sujeto.guardar_medicion(
            self.controller.sujeto, 
            self.convertir_peso(float(self.txb_peso.get())), 
            self.convertir_altura(float(self.txb_altura.get())), 
            datetime.date.today(), 
            self.controller.medicion.parametros_medidos, 
            self.controller.medicion.id_medicion
        )
        self.controller.medicion = medicion_sujeto
        
        self.controller.show_frame("ReporteMed")


    # Funcion para desabilitar botones segun el parametro seleccionado
    def deshabilitar_botones(self, boton:str, instruccion:str):

        def case_a(): #Caso a es para la temperatura
            self.btn_limpiar_textos_en_pantalla.config(state = 'normal')
            self.btn_saturacion_oxigeno.config(state = 'disabled')
            self.btn_presion_arterial.config(state = 'disabled')
            self.btn_frecuencia_cardiaca.config(state = 'disabled')
            self.btn_temperatura.config(state = 'normal')
            self.btn_generar_reporte.config(state = 'normal')
            self.btn_limpiar_textos_en_pantalla.config(state = "normal")
            self.btn_comenzar.config(state = "normal")
            self.btn_generar_reporte.config(state = "disabled")
            self.mostrar_instrucciones("a",instruccion)


        def case_b(): #Caso b es para la saturacion de oxigeno  
            self.btn_limpiar_textos_en_pantalla.config(state = 'normal')
            self.btn_saturacion_oxigeno.config(state = 'normal')
            self.btn_presion_arterial.config(state = 'disabled')
            self.btn_frecuencia_cardiaca.config(state = 'disabled')
            self.btn_temperatura.config(state = 'disabled')
            self.btn_generar_reporte.config(state = 'normal')
            self.btn_limpiar_textos_en_pantalla.config(state = "normal")
            self.btn_comenzar.config(state = "normal")
            self.btn_generar_reporte.config(state = "disabled")
            self.mostrar_instrucciones("b",instruccion)


        def case_c(): #Caso c es para la presion arterial 
            self.btn_limpiar_textos_en_pantalla.config(state = 'normal')
            self.btn_saturacion_oxigeno.config(state = 'disabled')
            self.btn_presion_arterial.config(state = 'normal')
            self.btn_frecuencia_cardiaca.config(state = 'disabled')
            self.btn_temperatura.config(state = 'disabled')
            self.btn_generar_reporte.config(state = 'normal')
            self.btn_limpiar_textos_en_pantalla.config(state = "normal")
            self.btn_comenzar.config(state = "normal")
            self.btn_generar_reporte.config(state = "disabled")
            self.mostrar_instrucciones("c",instruccion)


        def case_d(): #Caso e es para la frecuencia cardiaca 
            self.btn_limpiar_textos_en_pantalla.config(state = 'normal')
            self.btn_saturacion_oxigeno.config(state = 'disabled')
            self.btn_presion_arterial.config(state = 'disabled')
            self.btn_frecuencia_cardiaca.config(state = 'normal')
            self.btn_temperatura.config(state = 'disabled')
            self.btn_generar_reporte.config(state = 'normal')
            self.btn_limpiar_textos_en_pantalla.config(state = "normal")
            self.btn_comenzar.config(state = "normal")
            self.btn_generar_reporte.config(state = "disabled")
            self.mostrar_instrucciones("d",instruccion)

      
        def case_default():
            self.btn_limpiar_textos_en_pantalla.config(state = 'disabled')
            self.btn_saturacion_oxigeno.config(state = 'disabled')
            self.btn_presion_arterial.config(state = 'disabled')
            self.btn_frecuencia_cardiaca.config(state = 'disabled')
            self.btn_temperatura.config(state = 'disabled')
            self.btn_generar_reporte.config(state = 'disabled')
            self.mostrar_instrucciones("", "")

        switch_case = {
            "Temperatura": case_a,
            "Saturacion de Oxigeno": case_b,
            "Presion Arterial": case_c,
            "Frecuencia Cardiaca": case_d,            
        }
        switch_case.get(boton, case_default)()
    

    # Funcion para ir cambiando las instrucciones en pantalla       
    def mostrar_instrucciones(self,caso:str,instrucciones:str):
        def case_a(): #Caso a es para las instrucciones de temperatura 
            self.texto_pantalla.set(instrucciones) 
        def case_b(): #Caso b es para las instrucciones de la  saturacion de oxigeno
            self.texto_pantalla.set(instrucciones) 
        def case_c(): #Caso c es para las instrucciones de la saturacion de presion arterial 
            self.texto_pantalla.set(instrucciones) 
        def case_d(): #Caso e es para las instrucciones de la frecuencia cardiaca 
            self.texto_pantalla.set(instrucciones) 
        def case_default():
            self.texto_pantalla.set("\n\t\t\t INSTRUCCIONES: \n 1) Digite su peso y altura. \n\n 2) Haga click en el boton verde para validar sus datos") 


        switch_case = {
            "a": case_a,
            "b": case_b,
            "c": case_c,
            "d": case_d,            
        }
        
        switch_case.get(caso, case_default)()

    # Funcion para evitar espacios dentro de los lblbox de altura y peso
    def evitar_espacio(self, event):
        if event.keysym == 'space':
            return 'break'      

    # Funcion para validar que el punto decimal dle peso o la altura no este ni al principio ni al final
    def validar_punto_decimal(self, altura_sujeto:float, peso_sujeto:float):
        if (altura_sujeto.find('.') !=0 and altura_sujeto.find('.') != len(altura_sujeto) - 1) and (peso_sujeto.find('.') !=0 and peso_sujeto.find('.') != len(peso_sujeto) - 1 ):
            return True
        else:
            return False

    # Funcion para validar navegacion hacia registro
    def confirmar_regreso(self):
        if(messagebox.askokcancel("Confirmación de navegación","¿Estás seguro de volver hacia atrás? \n\n No se conservarán las mediciones actuales.") == True):
            self.abrir_registro()


    # Funcion para validar que la altura y peso introducidos por el sujeto de estudio esten correctamente
    def comprobar_altura_peso(self, altura_sujeto:float, peso_sujeto:float):
        if (altura_sujeto.replace('.', '', 1).isdigit() and peso_sujeto.replace('.', '', 1).isdigit() and self.validar_punto_decimal(altura_sujeto, peso_sujeto)):
           if(messagebox.askokcancel("Confirmación de información","¿Ha confirmado por completo sus datos?") == True):
                self.habilitar_botones()

        elif altura_sujeto == "" or peso_sujeto=="":
            messagebox.showwarning("ALERTA", "¡Recuerde ingresar su peso y altura antes de comenzar!")
            self.txb_altura.focus_set()
            self.txb_peso.focus_set()
        elif not altura_sujeto.replace('.', '', 1).isdigit() or not peso_sujeto.replace('.', '', 1).isdigit():
            messagebox.showwarning("ALERTA", "¡Recuerde ingresar solo numeros!")
            self.txb_altura.focus_set()
            self.txb_peso.focus_set()
        else:
            messagebox.showwarning("ALERTA", "¡Recuerde ingresar los decimales correctamente!")
            self.txb_altura.focus_set()
            self.txb_peso.focus_set()

    #Funcion para convertir la medida del peso a unidades del sistema internacional de medidas
    def convertir_altura(self, altura_sujeto:float):
        if(self.cb_altura.get()=='Pies'):
            conversion_altura = round((altura_sujeto)/3.281, 2)
            return conversion_altura
        else: return altura_sujeto
    
    #Funcion para convertir la medidad de la altura a unidades del sistema internacional de medidas
    def convertir_peso(self, peso_sujeto:float):
        if(self.cb_peso.get()=='Lb'):
            conversion_peso = round((peso_sujeto)/2.205, 2)
            return conversion_peso
        else: return peso_sujeto

    # Funcion para habilitar los botones luego de haber ingresado peso y altura           
    def habilitar_botones(self):
        self.btn_limpiar_textos_en_pantalla.config(state = 'normal')
        self.btn_saturacion_oxigeno.config(state = 'normal')
        self.btn_presion_arterial.config(state = 'normal')
        self.btn_frecuencia_cardiaca.config(state = 'normal')
        self.btn_temperatura.config(state = 'normal')
        self.txb_altura.config(state = "readonly")
        self.txb_peso.config(state = "readonly")
        self.cb_altura.config(state = "disabled")
        self.cb_peso.config(state = "disabled")
        self.btn_comenzar.config(state = "disabled")
        self.btn_generar_reporte.config(state = "normal")
        self.limpiar_textos_en_pantalla()
    
    # Esta funcion se encarga de validar si ya se ha tomado una medicion
    def validar(self, caso):
        def case_a(): #Caso a es para las instrucciones de temperatura 
            if self.confirmar_existencia_medicion('Temperatura'):
                if(messagebox.askokcancel("Comenzar medicion","¿Desea comenzar una medicion de temperatura?")== True):
                    self.tomar_medicion('Temperatura') 

                    if(messagebox.askokcancel("Confirmar medicion", f"¿Desea guardar la medición? Temperatura medida: {str(self.medida)} °C")== True):
                        self.almacenar_medicion('Temperatura')
                        self.habilitar_botones()
                    else:
                        self.habilitar_botones()
                else:
                   self.habilitar_botones()

        def case_b(): #Caso b es para las instrucciones de la  saturacion de oxigeno
            if self.confirmar_existencia_medicion("Saturacion de Oxigeno"):
                if(messagebox.askokcancel("Comenzar medicion","¿Desea comenzar una medicion de saturacion de oxigeno?")== True):
                    self.tomar_medicion('Saturacion de Oxigeno') 

                    if(messagebox.askokcancel("Confirmar medicion", f"¿Desea guardar la medición? saturacion de oxigeno medida: {str(self.medida)} %")== True):
                        self.almacenar_medicion('Saturacion de Oxigeno')
                        self.habilitar_botones()
                    else:
                        self.habilitar_botones()
                else:
                   self.habilitar_botones()
        
        def case_c(): #Caso c es para las instrucciones de la saturacion de presion arterial
            if self.confirmar_existencia_medicion("Presion Arterial"):
                if(messagebox.askokcancel("Comenzar medicion","¿Desea comenzar una medicion de presion?")== True):
                    self.tomar_medicion('Presion Arterial') 

                    if(messagebox.askokcancel("Confirmar medicion", f"¿Desea guardar la medición? Presion Arterial medida: {str(self.medida[0])}/{str(self.medida[1])} mmHg")== True):
                        self.almacenar_medicion('Presion Arterial')
                        self.habilitar_botones()
                    else:
                        self.habilitar_botones()
                else:
                   self.habilitar_botones()
        
        def case_d(): #Caso e es para las instrucciones de la frecuencia cardiaca 
            if self.confirmar_existencia_medicion("Frecuencia Cardiaca"):
                if(messagebox.askokcancel("Comenzar medicion","¿Desea comenzar una medicion de Frecuencia Cardiaca?")== True):
                    self.tomar_medicion('Frecuencia Cardiaca') 

                    if(messagebox.askokcancel("Confirmar medicion", f"¿Desea guardar la medición? Frecuencia Cardiaca medida: {str(self.medida)} BPM")== True):
                        self.almacenar_medicion('Frecuencia Cardiaca')
                        self.habilitar_botones()
                    else:
                        self.habilitar_botones()
                else:
                   self.habilitar_botones()
        
        def case_default():
             self.comprobar_altura_peso(self.txb_altura.get(), self.txb_peso.get())

        switch_case = {
            "a": case_a,
            "b": case_b,
            "c": case_c,
            "d": case_d
        }
        switch_case.get(caso, case_default)()


    # Funcion para impedir dos mediciones del mismo parametro fisiologico en una unica medicion_sujeto
    def confirmar_existencia_medicion(self, medicion:str):
        if self.controller.medicion.parametros_medidos:
                for una_medicion in self.controller.medicion.parametros_medidos:
                    if ("Presion Arterial" in medicion) and ("Presion Arterial" in una_medicion.parametro.descripcion):
                        if(messagebox.askokcancel("Sustituir medicion","¿Desea tomar nuevamente la medición y sustituirla la anterior?")== True):
                            self.habilitar_botones()
                            indice = self.controller.medicion.parametros_medidos.index(una_medicion)
                            self.controller.medicion.parametros_medidos.pop(indice)
                            self.controller.medicion.parametros_medidos.pop(indice)
                            return True
                    elif una_medicion.parametro.descripcion == medicion:
                        if(messagebox.askokcancel("Sustituir medicion","¿Desea tomar nuevamente la medición y sustituirla la anterior?")== True):
                            self.habilitar_botones()
                            self.controller.medicion.parametros_medidos.remove(una_medicion)
                            return True
                        else: return False
        return True

    # Funcion para tomar la medicion del parametro seleccionado y traer la medida que resulte
    def tomar_medicion(self, medicion:str):
        self.medida = self.parametros_fisiologicos.realizar_medicion_parametro()
        if(medicion == "Presion Arterial"):
            self.texto_parametro.set(str(self.medida[0]) + "/" +str(self.medida[1]))
            self.texto_parametro_medido.set(medicion + " Sistolica/Diastolica: ")
            self.medida_presion_arterial = self.medida
        else:
            self.texto_parametro.set(self.medida)
            self.texto_parametro_medido.set(self.parametros_fisiologicos.descripcion + ": ")    
    
    

    # Funcion para cargar los datos del parametro fisiologico segun se seleccione el parametro a medir
    def elegir_parametro(self,parametro:str,caso:str):
        
        if self.confirmar_existencia_medicion(parametro):
            self.validar_caso = caso # Se le asigna un valor a la variable validar caso para determinar cual es el caso activo al presionaro un  boton
            self.parametros_fisiologicos = ParametrosFisiologicos()
            self.instrucciones = " "
            self.deshabilitar_botones(parametro,self.instrucciones)
            
            if(parametro == "Presion Arterial"):
                self.parametros_fisiologicos.cargar_datos_parametro(parametro + " Sistolica")
                self.presion_arterial_sistolica = self.parametros_fisiologicos
                self.parametros_fisiologicos = ParametrosFisiologicos()
                self.parametros_fisiologicos.cargar_datos_parametro(parametro + " Diastolica")
                self.presion_arterial_diastolica = self.parametros_fisiologicos
                self.instrucciones = self.presion_arterial_diastolica.instrucciones
                self.mostrar_instrucciones(caso,self.instrucciones) #Se toman las instrucciones de la diastolica porque son las mismas que la sistolica
                self.deshabilitar_botones(parametro,self.instrucciones)
                
                
            else:
                self.parametros_fisiologicos.cargar_datos_parametro(parametro)
                self.instrucciones = self.parametros_fisiologicos.instrucciones
                self.mostrar_instrucciones(caso,self.instrucciones) #Se toman las instrucciones de la diastolica porque son las mismas que la sistolica
                

    # Funcion para limpiar los textos en pantalla
    def limpiar_textos_en_pantalla(self): 
        self.texto_parametro.set("") #Se eliminan los textos de las medidas de los parametros 
        self.texto_pantalla.set("") #Se eliminan las instrucciones de la pantalla
        self.texto_parametro_medido.set("Parametro medido: ") #Se coloca texto por defecto en el label que muestra los parametros
      
    # Funcion para guardar la medicion en la lista de mediciones por parametro
    def almacenar_medicion(self, medicion:str):

        if(medicion == "Presion Arterial"):
            medicion_presion_sistolica = MedicionParametro(self.presion_arterial_sistolica, self.medida_presion_arterial[0])
            medicion_presion_diastolica = MedicionParametro(self.presion_arterial_diastolica, self.medida_presion_arterial[1])
            self.controller.medicion.parametros_medidos.append(medicion_presion_sistolica)
            self.controller.medicion.parametros_medidos.append(medicion_presion_diastolica)

        else:
            medicion_parametro = MedicionParametro(self.parametros_fisiologicos, self.medida)
            self.controller.medicion.parametros_medidos.append(medicion_parametro)


    # Funcion para validar si hay mediciones desde que se cargue la pantalla, para colocar lo valores por defecto del peso y la altura de la medicion que haya y desabilitar esos campos
    def validar_medicion(self):
        if self.controller.medicion.id_medicion != 0:
            self.txb_altura.insert(0, str(self.controller.medicion.altura_sujeto))   
            self.txb_peso.insert(0, str(self.controller.medicion.peso_sujeto)) 
            self.txb_altura.config(state = 'readonly')
            self.txb_peso.config(state = "readonly")
            self.cb_altura.config(state = "disabled")
            self.cb_peso.config(state = "disabled")



        


    
   