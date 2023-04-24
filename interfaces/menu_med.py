from pathlib import Path
from tkinter.font import Font
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, Label, StringVar, messagebox
from modelos.parametros_fisiologicos import ParametrosFisiologicos as pf
from modelos.medicion_parametro import MedicionParametro as mp
from modelos.mediciones_sujeto import MedicionesSujeto as ms
from modelos.sujetos_estudio import SujetosEstudio as se

#Libreria para utilizar funciones del sistema
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/menu_med")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class MenuMed():
    def __init__(self, sujeto:se, mediciones:ms):
        self.sujeto = sujeto
        self.mediciones = mediciones
        self.window = Tk()
        self.window.geometry("1260x725+{}+{}".format(self.window.winfo_screenwidth() // 2 - 1260 // 2, self.window.winfo_screenheight() // 2 - 725 // 2))
        self.window.configure(bg = "#FFFFFF")
        self.window.title("Menu de Mediciones")

        

    #region // Ventana Principal
        #Canvas de la ventana principal
        #Dimensiones del canva
        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 725,
            width = 1260,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        #Localización del canvas principal
        self.canvas.place(x = 0, y = 0)

        #Imagen del logo (HEARTBEAT)
        self.imagen_logo_app = PhotoImage(file=relative_to_assets("image_1.png"))
        #Localizacion del logo
        self.logo_app = self.canvas.create_image(
            640.0,
            61.0,
            image=self.imagen_logo_app
        )         

    #endregion 
       
    #region // Botón Regresar
        #-------------------- Botón Regresar -------------------
        #Imagen del botón regresar
        btn_imagen_regresar = PhotoImage(
            file=relative_to_assets("button_1.png"))
        #Propiedades del botón regresar
        self.btn_volver = Button(
            image=btn_imagen_regresar,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.confirmar_regreso(),
            relief="flat",
            bg = "White"
        )
        #Localización del botón regresar
        self.btn_volver.place(
            x=21.0,
            y=26.0,
            width=61.0,
            height=60.0
        )
    #endregion

    #region // Botón Comenzar (Comienza el proceso de una medicion)
        #-------------------- Botón Comenzar -------------------
        #Imagen del botón comenzar
        self.btn_imagen_comenzar = PhotoImage(
            file=relative_to_assets("button_2.png"))
        #Propiedades del botón comenzar
        self.btn_comenzar = Button(
            image=self.btn_imagen_comenzar,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.validar(self.validar_caso),
            relief="flat",
            bg = "White"
        )
        #Localización del botón comenzar
        self.btn_comenzar.place(
            x=1060.0,
            y=488.0,
            width=61.65789794921875,
            height=66.0
        )

    #endregion

    #region // Botón Limpiar Textos en Pantalla (Limpia los datos de la medición actual y sus respectivas instrucciones)
        #-------------------- Botón Limpiar Textos en Pantalla -------------------
        #Imagen del botón limpiar textos en pantalla
        self.btn_imagen_limpiar_textos_en_pantalla = PhotoImage(
            file=relative_to_assets("button_3.png"))
         #Propiedades del botón limpiar textos en pantalla
        self.btn_limpiar_textos_en_pantalla = Button(
            image=self.btn_imagen_limpiar_textos_en_pantalla,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.habilitar_botones(),
            relief="flat",
            bg = "White",  
        )
        #Localización del botón limpiar_textos_en_pantalla
        self.btn_limpiar_textos_en_pantalla.place(
            x=1122.0,
            y=491.0,
            width=67.0,
            height=71.71826171875
        )
    #endregion

    #region // Botón Temperatura (Boton para iniciar medición de temperatura)
        #-------------------- Botón Temperatura  -------------------
        #Imagen del botón temperatura
        self.btn_imagen_temperatura = PhotoImage(
            file=relative_to_assets("button_7.png"))
        #Propiedades del botón temperatura
        self.btn_temperatura = Button(
            image=self.btn_imagen_temperatura,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.elegir_parametro("Temperatura","a"),
            relief="flat",
            bg = "White", 
        )
        #Localización del botón temperatura
        self.btn_temperatura.place(
            x=-25.0,
            y=180.0,
            width=518.0,
            height=93.0
        )

    #endregion

      
    #region // Botón Saturación de Oxígeno (Boton para iniciar medición de saturación de oxígeno)
        #-------------------- Botón Saturación de Oxígeno -------------------
        #Imagen del botón saturación de oxígeno
        self.btn_imagen_saturacion_oxigeno = PhotoImage(
            file=relative_to_assets("button_4.png"))
        #Propiedades del botón saturación de oxígeno
        self.btn_saturacion_oxigeno = Button(
            image=self.btn_imagen_saturacion_oxigeno,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.elegir_parametro("Saturacion de Oxigeno","b"),
            relief="flat",
            bg = "White", 
        )
        #Localización del botón saturación de oxígeno
        self.btn_saturacion_oxigeno.place(
            x=-10.0,
            y=289.0,
            width=483.0,
            height=90.0
        )

    #endregion

    #region // Botón Presión Arterial (Boton para iniciar medición de presión arterial)
        #-------------------- Botón Presión Arterial -------------------
        #Imagen del botón presión arterial
        self.btn_imagen_presion_arterial = PhotoImage(
            file=relative_to_assets("button_5.png"))
        #Propiedades del botón presión arterial
        self.btn_presion_arterial = Button(
            image=self.btn_imagen_presion_arterial,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.elegir_parametro("Presion Arterial","c"),
            relief="flat",
            bg = "White",
        )
        #Localización del botón presión arterial
        self.btn_presion_arterial.place(
            x=-10.0,
            y=405.0,
            width=484.0,
            height=97.0
        )
    
    #endregion

    #region // Botón Frecuencia Cardíaca (Boton para iniciar medición de frecuencia cardíaca)
        #-------------------- Botón Frecuencia Cardíaca -------------------
        #Imagen del botón frecuencia cardíaca
        self.btn_imagen_frecuencia_cardiaca = PhotoImage(
            file=relative_to_assets("button_6.png"))
        #Propiedades del botón frecuencia cardíaca
        self.btn_frecuencia_cardiaca = Button(
            image=self.btn_imagen_frecuencia_cardiaca,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.elegir_parametro("Frecuencia Cardiaca","d"),
            relief="flat",
            bg = "White", 
        )
        #Localización del botón frecuencia cardíaca
        self.btn_frecuencia_cardiaca.place(
            x=-10.0,
            y=522.0,
            width=471.0,
            height=92.0
        )
    #endregion

    #region // Botón Generar Informe (Boton para pasar a la pantalla de generar informe)
        #-------------------- Botón Generar Informe -------------------
        #Imagen del botón generar informe
        self.btn_imagen_generar_informe = PhotoImage(
            file=relative_to_assets("button_8.png"))
        #Propiedades del botón generar informe
        self.btn_generar_informe = Button(
            image=self.btn_imagen_generar_informe,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.abrir_reporte(), 
            relief="flat",
            bg = "White", 
        )
        #Localización del botón generar informe
        self.btn_generar_informe.place(
            x=838.0,
            y=646.0,
            width=424.0,
            height=91.0
        )
        
    #endregion

    #region // Labels, campos y combobox sobre el peso, la altura y la medicion del parametro

        #LISTO Arreglo - Sigue la nomenclatura de los label, es lbl

        # -------------------- Instrucciones en Pantalla -------------------

        #Variable de texto para ir cambiando las instrucciones para las mediciones
        self.texto_pantalla = StringVar()
        #Inicializando la variable
        self.texto_pantalla.set("")

        #Label que muestra las instrucciones en pantalla (Propiedades)
        self.lbl_pantalla = Label(
            borderwidth=2, 
            relief="groove", 
            bg = "white",
            textvariable = self.texto_pantalla, 
            anchor="nw", #se coloca el texto hacia arriba y hacia la izquierda
            justify="left", #justificar el texto a la izquierda
            font = ("Arial", 12)
            )
        #Label que muestra las instrucciones en pantalla (Localización)
        self.lbl_pantalla.place(
            x = 561.0,
            y = 280.0,
            width = 630.0,
            height = 200.0  
            )
        
        
        #region // Altura
        #-------------------- Altura -------------------
        #Texto Altura
        self.canvas.create_text(
            720.0,
            177.0,
            anchor="nw",
            text="Altura",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )
        #Texbox de la altura
        self.txb_altura = Entry(
            bd=1,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0, 
            font=("Arial", 16)
        )

        #Enlaza la función evitar_espacio a la txb_altura cada vez que se presiona una tecla en la entrada.
        self.txb_altura.bind('<Key>', self.evitar_espacio)

        #Localización del texbox de la altura
        self.txb_altura.place(
            x=610.0,
            y=233.0,
            width=165.0,
            height=35.0
        )


        #Combobox unidad de medida de la altura (si esta dada en Metros o Pies)
        self.cb_altura = ttk.Combobox(
        state = "readonly",
        values = ["Metros","Pies"], 
        font=("Arial", 16)
        )
      
        #Localizacion del combobox de la altura
        self.cb_altura.place(
            x=790.0,
            y=234.0,
            width=90.0,
            height=35.0
        )

        self.cb_altura.config(font=("Arial", 16))

        #Estableciendo por defecto el primer elemento de la lista del combobox de la altura
        self.cb_altura.current(0)

        #endregion 
        
        #region // Peso
        #-------------------- Peso -------------------
        #Texto Peso
        self.canvas.create_text(
            990.0,
            177.0,
            anchor="nw",
            text="Peso",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )

        #Texbox del peso
        self.txb_peso = Entry(
            bd=1,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 16)
        )
        
        #Enlaza la función evitar_espacio a la txb_peso cada vez que se presiona una tecla en la entrada.
        self.txb_peso.bind('<Key>', self.evitar_espacio) 

        #Localizacion del texbox del peso
        self.txb_peso.place(
            x=900.0,
            y=234.0,
            width=178.0,
            height=34.0
        )

        #Combobox unidad de medida del peso (si esta dado en lb o kg)
        self.cb_peso = ttk.Combobox(
        state = "readonly",
        values = ["Kg","Lb"], 
        font=("Arial", 16)
        )
        #Localización del combobox del peso
        self.cb_peso.place(
            x=1090.0,
            y=234.0,
            width=59.0,
            height=35.0
        )

        #Estableciendo por defecto el primer elemento de la lista del combobox del peso
        self.cb_peso.current(0)
        #endregion 


        # -------------------- Medida Parametro Medido -------------------

        #Variable de texto para ir cambiando la medida de los parametro medidos
        self.texto_parametro = StringVar()
        #Inicializando la variable
        self.texto_parametro.set("")
        
        #Propiedades  del label que muestra la medida parametro medido 
        self.lbl_parametro = Label(
            borderwidth=2, 
            relief="groove", 
            bg = "white",
            textvariable= self.texto_parametro, 
            anchor="center", #se coloca el texto hacia arriba y hacia la izquierda
            font = ("Arial", 18)
        )
        #Localización que muestra la medida del parametro medido
        self.lbl_parametro.place(
            x=561.0,
            y=554.0,
            width=289.0,
            height=55.0 
        )

        # -------------------- Parametro Medido -------------------

        #Variable de texto para ir cambiando el label de los parametro medidos
        self.texto_parametro_medido = StringVar()
        #Inicializando la variable
        self.texto_parametro_medido.set("Parametro medido:")

        #Propiedades del label que muestra el parametro medido
        self.lbl_parametro_medido = Label(
            borderwidth=0,
            relief="groove", 
            bg = "white",
            textvariable= self.texto_parametro_medido, 
            anchor="center", #se coloca el texto hacia arriba y hacia la izquierda
            font = ("Arial", 18)
        )
        #Localizacion del label que muestra el parametro medido 
        self.lbl_parametro_medido.place(
            x = 570.0,
            y = 510.0
        )

    #endregion

        self.validar_medicion()
        self.window.option_add('*TCombobox*Listbox.font', '50') #Aumentar el tamaño de las listas de los drop down 
        self.window.option_add('*TCombobox*Listbox.height', '50')
        self.validar_caso = " " #variable que funciona para validar cual es el caso que se encuentra activo, esta inicializada en " " debido a que es el caso por defecto
        self.deshabilitar_botones("", "")
        #Arreglo - Las funciones deben comenzar por un verbo
        self.mostrar_instrucciones("", "") #Colocar el texto por defecto al iniciar la interfaz en la pantalla
        self.window.resizable(False, False)
        self.window.mainloop()
            


#region // Funcion para abrir otro formulario
    
    def abrir_registro(self):
        from interfaces.registro_suj import RegistroSujeto
        self.window.destroy()
        self.registro = RegistroSujeto(self.sujeto.tipo_documento.descripcion, self.sujeto.codigo_documento)

    def abrir_reporte(self):
        from interfaces.reporte_med import ReporteMed
        import datetime
        medicion_sujeto = ms()
        medicion_sujeto.guardar_medicion(self.sujeto, self.convertir_peso(float(self.txb_peso.get())), self.convertir_altura(float(self.txb_altura.get())), datetime.date.today(), self.mediciones.parametros_medidos, self.mediciones.id_medicion)        
        self.window.destroy()
        self.reporte = ReporteMed(self.sujeto, medicion_sujeto)

#endregion      


#region // Funcion para desabilitar botones segun el parametro seleccionado
    def deshabilitar_botones(self, boton:str, instruccion:str):

        def case_a(): #Caso a es para la temperatura
            self.btn_limpiar_textos_en_pantalla.config(state = 'normal')
            self.btn_saturacion_oxigeno.config(state = 'disabled')
            self.btn_presion_arterial.config(state = 'disabled')
            self.btn_frecuencia_cardiaca.config(state = 'disabled')
            self.btn_temperatura.config(state = 'normal')
            self.btn_generar_informe.config(state = 'normal')
            self.btn_limpiar_textos_en_pantalla.config(state = "normal")
            self.btn_comenzar.config(state = "normal")
            self.btn_generar_informe.config(state = "disabled")
            self.mostrar_instrucciones("a",instruccion)


        def case_b(): #Caso b es para la saturacion de oxigeno  
            self.btn_limpiar_textos_en_pantalla.config(state = 'normal')
            self.btn_saturacion_oxigeno.config(state = 'normal')
            self.btn_presion_arterial.config(state = 'disabled')
            self.btn_frecuencia_cardiaca.config(state = 'disabled')
            self.btn_temperatura.config(state = 'disabled')
            self.btn_generar_informe.config(state = 'normal')
            self.btn_limpiar_textos_en_pantalla.config(state = "normal")
            self.btn_comenzar.config(state = "normal")
            self.btn_generar_informe.config(state = "disabled")
            self.mostrar_instrucciones("b",instruccion)


        def case_c(): #Caso c es para la presion arterial 
            self.btn_limpiar_textos_en_pantalla.config(state = 'normal')
            self.btn_saturacion_oxigeno.config(state = 'disabled')
            self.btn_presion_arterial.config(state = 'normal')
            self.btn_frecuencia_cardiaca.config(state = 'disabled')
            self.btn_temperatura.config(state = 'disabled')
            self.btn_generar_informe.config(state = 'normal')
            self.btn_limpiar_textos_en_pantalla.config(state = "normal")
            self.btn_comenzar.config(state = "normal")
            self.btn_generar_informe.config(state = "disabled")
            self.mostrar_instrucciones("c",instruccion)


        def case_d(): #Caso e es para la frecuencia cardiaca 
            self.btn_limpiar_textos_en_pantalla.config(state = 'normal')
            self.btn_saturacion_oxigeno.config(state = 'disabled')
            self.btn_presion_arterial.config(state = 'disabled')
            self.btn_frecuencia_cardiaca.config(state = 'normal')
            self.btn_temperatura.config(state = 'disabled')
            self.btn_generar_informe.config(state = 'normal')
            self.btn_limpiar_textos_en_pantalla.config(state = "normal")
            self.btn_comenzar.config(state = "normal")
            self.btn_generar_informe.config(state = "disabled")
            self.mostrar_instrucciones("d",instruccion)

      
        def case_default():
            self.btn_limpiar_textos_en_pantalla.config(state = 'disabled')
            self.btn_saturacion_oxigeno.config(state = 'disabled')
            self.btn_presion_arterial.config(state = 'disabled')
            self.btn_frecuencia_cardiaca.config(state = 'disabled')
            self.btn_temperatura.config(state = 'disabled')
            self.btn_generar_informe.config(state = 'disabled')
            self.mostrar_instrucciones("", "")

        switch_case = {
            "Temperatura": case_a,
            "Saturacion de Oxigeno": case_b,
            "Presion Arterial": case_c,
            "Frecuencia Cardiaca": case_d,            
        }
        switch_case.get(boton, case_default)()
    
#endregion

#region // Funcion para ir cambiando las instrucciones en pantalla       
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

    #endregion


    #region // Funcion para evitar espacios dentro de los lblbox de altura y peso
    def evitar_espacio(self, event):
        if event.keysym == 'space':
            return 'break'      
    #endregion

    #region // Funcion para validar que el punto decimal dle peso o la altura no este ni al principio ni al final
    def validar_punto_decimal(self, altura_sujeto:float, peso_sujeto:float):
        if (altura_sujeto.find('.') !=0 and altura_sujeto.find('.') != len(altura_sujeto) - 1) and (peso_sujeto.find('.') !=0 and peso_sujeto.find('.') != len(peso_sujeto) - 1 ):
            return True
        else:
            return False
    #endregion

    #region // Funcion para validar navegacion hacia registro
    def confirmar_regreso(self):
        if(messagebox.askokcancel("Confirmación de navegación","¿Estás seguro de volver hacia atrás? \n\n No se conservarán las mediciones actuales.") == True):
            self.abrir_registro()

    #endregion


    #region // Funcion para validar que la altura y peso introducidos por el sujeto de estudio esten correctamente
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

    #endregion

    #region // Conversiones
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
    #endregion

    #region // Funcion para habilitar los botones luego de haber ingresado peso y altura           
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
        self.btn_generar_informe.config(state = "normal")
        self.limpiar_textos_en_pantalla()
    #endregion
    


    #region #Este switch se ejecuta al darle al boton de comentar medicion y evalua el caso de cada parametro
    #Arreglo - Documenta mejor para que sirve la funcion (Aqui estan los problemas Pazzis)
    def validar(self, caso): #Arreglo - se mas especifico con el nombre de la funcion
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

                    if(messagebox.askokcancel("Confirmar medicion", f"¿Desea guardar la medición? saturacion de oxigeno medida: {str(self.medida)} °C")== True):
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

                    if(messagebox.askokcancel("Confirmar medicion", f"¿Desea guardar la medición? Presion Arterial medida: {str(self.medida)} °C")== True):
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

                    if(messagebox.askokcancel("Confirmar medicion", f"¿Desea guardar la medición? Frecuencia Cardiaca medida: {str(self.medida)} °C")== True):
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
    #endregion



    #region // Funcion para impedir dos mediciones del mismo parametro fisiologico en una unica medicion_sujeto
    def confirmar_existencia_medicion(self, medicion:str):
        if self.mediciones.parametros_medidos:
                for una_medicion in self.mediciones.parametros_medidos:
                    if ("Presion Arterial" in medicion) and ("Presion Arterial" in una_medicion.parametro.descripcion):
                        if(messagebox.askokcancel("Sustituir medicion","¿Desea tomar nuevamente la medición y sustituirla la anterior?")== True):
                            self.habilitar_botones()
                            indice = self.mediciones.parametros_medidos.index(una_medicion)
                            self.mediciones.parametros_medidos.pop(indice)
                            self.mediciones.parametros_medidos.pop(indice)
                            return True
                    elif una_medicion.parametro.descripcion == medicion:
                        if(messagebox.askokcancel("Sustituir medicion","¿Desea tomar nuevamente la medición y sustituirla la anterior?")== True):
                            self.habilitar_botones()
                            self.mediciones.parametros_medidos.remove(una_medicion)
                            return True
                        else: return False
        return True
    #endregion

    #region // Funcion para tomar la medicion del parametro seleccionado y traer la medida que resulte
    def tomar_medicion(self, medicion:str):
        self.medida = self.parametros_fisiologicos.realizar_medicion_parametro()
        if(medicion == "Presion Arterial"):
            self.texto_parametro.set(str(self.medida[0]) + "/" +str(self.medida[1]))
            self.texto_parametro_medido.set(medicion + " Sistolica/Diastolica: ")
            self.medida_presion_arterial = self.medida
        else:
            self.texto_parametro.set(self.medida)
            self.texto_parametro_medido.set(self.parametros_fisiologicos.descripcion + ": ")
    #endregion
    
    
    

    #Arreglo - Documenta mejor el funcionamiento del metodo 
    #region // Funcion para cargar los datos del parametro fisiologico segun se seleccione el parametro a medir
    def elegir_parametro(self,parametro:str,caso:str):
        
        if self.confirmar_existencia_medicion(parametro):
            self.validar_caso = caso # se le asigna un valor a la variable validar caso para determinar cual es el caso activo al presionaro un  boton
            self.parametros_fisiologicos = pf()
            self.instrucciones = " "
            self.deshabilitar_botones(parametro,self.instrucciones)
            
            if(parametro == "Presion Arterial"):
                self.parametros_fisiologicos.cargar_datos_parametro(parametro + " Sistolica")
                self.presion_arterial_sistolica = self.parametros_fisiologicos
                self.parametros_fisiologicos = pf()
                self.parametros_fisiologicos.cargar_datos_parametro(parametro + " Diastolica")
                self.presion_arterial_diastolica = self.parametros_fisiologicos
                self.instrucciones = self.presion_arterial_diastolica.instrucciones
                self.mostrar_instrucciones(caso,self.instrucciones) #se toman las instrucciones de la diastolica porque son las mismas que la sistolica
                self.deshabilitar_botones(parametro,self.instrucciones)
                
                
            else:
                self.parametros_fisiologicos.cargar_datos_parametro(parametro)
                self.instrucciones = self.parametros_fisiologicos.instrucciones
                self.mostrar_instrucciones(caso,self.instrucciones) #se toman las instrucciones de la diastolica porque son las mismas que la sistolica
    #endregion           
                

    #region// Funcion para limpiar los textos en pantalla
    def limpiar_textos_en_pantalla(self): 
        self.texto_parametro.set("") #Se eliminan los textos de las medidas de los parametros 
        self.texto_pantalla.set("") #Se eliminan las instrucciones (Pazzis te hablo a ti, las instrucciones nunca se deben limpiar del todo, se deberian sustituir segun cada caso)
        self.texto_parametro_medido.set("Parametro medido: ") #Se coloca texto por defecto en el label que muestra los parametros
    #endregion
      
    #region //Funcion para guardar la medicion en la lista de mediciones por parametro
    def almacenar_medicion(self, medicion:str):

        if(medicion == "Presion Arterial"):
            medicion_presion_sistolica = mp(self.presion_arterial_sistolica, self.medida_presion_arterial[0])
            medicion_presion_diastolica = mp(self.presion_arterial_diastolica, self.medida_presion_arterial[1])
            self.mediciones.parametros_medidos.append(medicion_presion_sistolica)
            self.mediciones.parametros_medidos.append(medicion_presion_diastolica)

        else:
            medicion_parametro = mp(self.parametros_fisiologicos, self.medida)
            self.mediciones.parametros_medidos.append(medicion_parametro)

    #endregion

    #region// Funcion para validar si hay mediciones desde que se cargue la pantalla, para colocar lo valores por defecto del peso y la altura de la medicion que haya y desabilitar esos campos
    def validar_medicion(self):
        if self.mediciones.id_medicion != 0:
            self.txb_altura.insert(0, str(self.mediciones.altura_sujeto))   
            self.txb_peso.insert(0, str(self.mediciones.peso_sujeto)) 
            self.txb_altura.config(state = 'readonly')
            self.txb_peso.config(state = "readonly")
            self.cb_altura.config(state = "disabled")
            self.cb_peso.config(state = "disabled")
    #endregion




        


    
   