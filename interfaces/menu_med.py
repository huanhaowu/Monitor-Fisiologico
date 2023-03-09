from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, Label, StringVar, messagebox
from modelos.parametros_fisiologicos import ParametrosFisiologicos as pf

#Libreria para utilizar funciones del sistema
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/menu_med")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class MenuMed():
    def __init__(self, sujeto, mediciones = {}):
        self.sujeto = sujeto
        self.mediciones = mediciones
        self.window = Tk()
        self.window.geometry("1260x725+{}+{}".format(self.window.winfo_screenwidth() // 2 - 1260 // 2, self.window.winfo_screenheight() // 2 - 725 // 2))
        self.window.configure(bg = "#FFFFFF")
        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 725,
            width = 1260,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )


        #Aqui va el boton para volver al frame anterior
        self.canvas.place(x = 0, y = 0)
        bt_imagen_volver = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.bt_volver = Button(
            image=bt_imagen_volver,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.abrir_registro(),
            relief="flat",
            bg = "White"
        )
        self.bt_volver.place(
            x=21.0,
            y=26.0,
            width=61.0,
            height=60.0
        )

        self.texto_pantalla = StringVar()
        self.texto_pantalla.set("")

        self.txt_pantalla = Label(
            borderwidth=2, 
            relief="groove", 
            bg = "white",
            textvariable = self.texto_pantalla, 
            anchor="nw", #se coloca el texto hacia arriba y hacia la izquierda
            justify="left", #justificar el texto a la izquierda
            font = ("Arial", 12)
            )
        
        self.txt_pantalla.place(
            x = 561.0,
            y = 280.0,
            width = 630.0,
            height = 200.0  
            )
        
        #Aqui va el texbox para la estatura
        self.canvas.create_text(
            720.0,
            177.0,
            anchor="nw",
            text="Estatura",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.txb_estatura = Entry(
            bd=1,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.txb_estatura.place(
            x=640.0,
            y=233.0,
            width=165.0,
            height=35.0
        )

        #Aqui va el combobox para especificar si la estatura esta dado en Metros o Pies
        self.cb_estatura = ttk.Combobox(
        state = "readonly",
        values = ["Metros","Pies"]
        )
        self.cb_estatura.place(
            x=820.0,
            y=234.0,
            width=59.0,
            height=35.0
        )
        self.canvas.create_text(
            990.0,
            177.0,
            anchor="nw",
            text="Peso",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )

        #Aqui va el Texbox para el peso
        self.txb_peso = Entry(
            bd=1,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.txb_peso.place(
            x=900.0,
            y=234.0,
            width=178.0,
            height=34.0
        )

        #Aqui va el combobox para especificar si el peso esta dado en lb o kg
        self.cb_peso = ttk.Combobox(
        state = "readonly",
        values = ["Kg","Lb"]
        )
        self.cb_peso.place(
            x=1090.0,
            y=234.0,
            width=59.0,
            height=35.0
        )

        #Aqui va el label para el parametro medido
        self.texto_parametro = StringVar()
        self.texto_parametro.set("")

        self.txt_parametro = Label(
            borderwidth=2, 
            relief="groove", 
            bg = "white",
            textvariable= self.texto_parametro, 
            anchor="center", #se coloca el texto hacia arriba y hacia la izquierda
            font = ("Arial", 18)
        )
        self.txt_parametro.place(
            x=561.0,
            y=554.0,
            width=289.0,
            height=55.0 
        )
        self.texto_parametro_medido = StringVar()
        self.texto_parametro_medido.set("Parametro medido:")

        self.txt_parametro_medido = Label(
            borderwidth=0,
            relief="groove", 
            bg = "white",
            textvariable= self.texto_parametro_medido, 
            anchor="center", #se coloca el texto hacia arriba y hacia la izquierda
            font = ("Arial", 18)
        )
        self.txt_parametro_medido.place(
            x = 570.0,
            y = 510.0
        )

        #Aqui va el boton para comenzar una medicion
        self.bt_imagen_comenzar = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.bt_comenzar = Button(
            image=self.bt_imagen_comenzar,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.validar(),
            relief="flat",
            bg = "White"
        )
        self.bt_comenzar.place(
            x=1060.0,
            y=488.0,
            width=61.65789794921875,
            height=66.0
        )


        #Aqui va el boton para limpiar y elegir otra medicion
        self.bt_imagen_limpiar = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.bt_limpiar = Button(
            image=self.bt_imagen_limpiar,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.habilitar_botones(),
            relief="flat",
            bg = "White",  
        )
        self.bt_limpiar.place(
            x=1122.0,
            y=491.0,
            width=67.0,
            height=71.71826171875
        )


        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            640.0,
            61.0,
            image=self.image_image_1
        )

        #Aqui va el boton para iniciar medicion de saturacion de oxigeno 
        self.bt_imagen_saturacion_oxigeno = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.bt_saturacion_oxigeno = Button(
            image=self.bt_imagen_saturacion_oxigeno,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.tomar_medicion("Saturacion de Oxigeno","b"),
            relief="flat",
            bg = "White", 
        )
        self.bt_saturacion_oxigeno.place(
            x=-10.0,
            y=289.0,
            width=483.0,
            height=90.0
        )

        #Aqui va el boton para iniciar medicion de presion arterial 
        self.bt_imagen_presion_arterial = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.bt_presion_arterial = Button(
            image=self.bt_imagen_presion_arterial,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.tomar_medicion("Presion Arterial","c"),
            relief="flat",
            bg = "White",
        )
        self.bt_presion_arterial.place(
            x=-10.0,
            y=405.0,
            width=484.0,
            height=97.0
        )
        
        #Aqui va el boton para la medicion de frecuencia cardiaca
        self.bt_imagen_frecuencia_cardiaca = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.bt_frecuencia_cardiaca = Button(
            image=self.bt_imagen_frecuencia_cardiaca,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.tomar_medicion("Frecuencia Cardiaca","d"),
            relief="flat",
            bg = "White", 
        )
        self.bt_frecuencia_cardiaca.place(
            x=-10.0,
            y=522.0,
            width=471.0,
            height=92.0
        )

        #Aqui va el boton para la medicion de la temperatura
        self.bt_imagen_temperatura = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.bt_temperatura = Button(
            image=self.bt_imagen_temperatura,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.tomar_medicion("Temperatura","a"),
            relief="flat",
            bg = "White", 
        )
        self.bt_temperatura.place(
            x=-25.0,
            y=180.0,
            width=518.0,
            height=93.0
        )


        #Aqui va el boton
        self.bt_imagen_generar_informe = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.bt_generar_informe = Button(
            image=self.bt_imagen_generar_informe,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.abrir_reporte(),
            relief="flat",
            bg = "White", 
        )
        self.bt_generar_informe.place(
            x=838.0,
            y=646.0,
            width=424.0,
            height=91.0
        )
        self.deshabilitar_botones("")
        self.mensaje_pantalla("") #Colocar el texto por defecto al iniciar la interfaz en la pantalla
        self.window.resizable(False, False)
        self.window.mainloop()



#Funcion para abrir otro formulario
    
    def abrir_registro(self):
        from interfaces.registro_suj import RegistroSujeto
        self.window.destroy()
        registro = RegistroSujeto(self.sujeto.tipo_documento, self.sujeto.codigo_documento)

    def abrir_reporte(self):
        from interfaces.reporte_med import ReporteMed
        self.window.destroy()
        reporte = ReporteMed(self.sujeto, self.mediciones)
        

#Funciones para deshabilitar y habilitar las interfaces
    def deshabilitar_botones(self, boton):

        def case_a(): #Caso a es para la temperatura
            self.bt_limpiar.config(state = 'normal')
            self.bt_saturacion_oxigeno.config(state = 'disabled')
            self.bt_presion_arterial.config(state = 'disabled')
            self.bt_frecuencia_cardiaca.config(state = 'disabled')
            self.bt_temperatura.config(state = 'normal')
            self.bt_generar_informe.config(state = 'normal')
            self.bt_comenzar.config(state = "disabled")
            self.bt_limpiar.config(state = "normal")
            self.mensaje_pantalla("a")


        def case_b(): #Caso b es para la saturacion de oxigeno  
            self.bt_limpiar.config(state = 'normal')
            self.bt_saturacion_oxigeno.config(state = 'normal')
            self.bt_presion_arterial.config(state = 'disabled')
            self.bt_frecuencia_cardiaca.config(state = 'disabled')
            self.bt_temperatura.config(state = 'disabled')
            self.bt_generar_informe.config(state = 'normal')
            self.bt_comenzar.config(state = "disabled")
            self.bt_limpiar.config(state = "normal")
            self.mensaje_pantalla("b")


        def case_c(): #Caso c es para la presion arterial 
            self.bt_limpiar.config(state = 'normal')
            self.bt_saturacion_oxigeno.config(state = 'disabled')
            self.bt_presion_arterial.config(state = 'normal')
            self.bt_frecuencia_cardiaca.config(state = 'disabled')
            self.bt_temperatura.config(state = 'disabled')
            self.bt_generar_informe.config(state = 'normal')
            self.bt_limpiar.config(state = "normal")
            self.mensaje_pantalla("c")


        def case_d(): #Caso e es para la frecuencia cardiaca 
            self.bt_limpiar.config(state = 'normal')
            self.bt_saturacion_oxigeno.config(state = 'disabled')
            self.bt_presion_arterial.config(state = 'disabled')
            self.bt_frecuencia_cardiaca.config(state = 'normal')
            self.bt_temperatura.config(state = 'disabled')
            self.bt_generar_informe.config(state = 'normal')
            self.bt_comenzar.config(state = "disabled")
            self.bt_limpiar.config(state = "normal")
            self.mensaje_pantalla("d")

      
        def case_default():
            self.bt_limpiar.config(state = 'disabled')
            self.bt_saturacion_oxigeno.config(state = 'disabled')
            self.bt_presion_arterial.config(state = 'disabled')
            self.bt_frecuencia_cardiaca.config(state = 'disabled')
            self.bt_temperatura.config(state = 'disabled')
            self.bt_generar_informe.config(state = 'disabled')
            self.mensaje_pantalla("")

        switch_case = {
            "Temperatura": case_a,
            "Saturacion de Oxigeno": case_b,
            "Presion Arterial": case_c,
            "Frecuencia Cardiaca": case_d,            
        }
        switch_case.get(boton, case_default)()
              
    def mensaje_pantalla(self,caso):
        def case_a(): #Caso a es para las instrucciones de temperatura 
            self.texto_pantalla.set("\n\t\t\t INSTRUCCIONES: \n 1) Paso 1 \n 2) Paso 2 \n 3) Paso 3") 
        def case_b(): #Caso b es para las instrucciones de la  saturacion de oxigeno
            self.texto_pantalla.set("\n\t\t\t INSTRUCCIONES: \n 1) Paso 1 \n 2) Paso 2 \n 3) Paso 3") 
        def case_c(): #Caso c es para las instrucciones de la saturacion de presion arterial 
            self.texto_pantalla.set("\n\t\t\t INSTRUCCIONES: \n 1) Paso 1 \n 2) Paso 2 \n 3) Paso 3") 
        def case_d(): #Caso e es para las instrucciones de la frecuencia cardiaca 
            self.texto_pantalla.set("\n\t\t\t INSTRUCCIONES: \n 1) Paso 1 \n 2) Paso 2 \n 3) Paso 3") 
        def case_default():
            self.texto_pantalla.set("\n\t\t\t INSTRUCCIONES: \n 1) Digite su peso y estatura. \n\n 2) Haga click en el boton verde para validar sus datos") 


        switch_case = {
            "a": case_a,
            "b": case_b,
            "c": case_c,
            "d": case_d,            
        }
        switch_case.get(caso, case_default)()
    def alerta_texto_vacio(self):
        if (self.txb_estatura.get() == "" or self.txb_peso.get() == "" or self.cb_peso.get()=="" or self.cb_estatura.get()==""): #este if valida si el texto esta vacio
            messagebox.showwarning("ALERTA", "¡Recuerde ingresar su peso y estatura antes de comenzar!")
            self.txb_estatura.focus_set()
            self.txb_peso.focus_set()
        else:
            if(messagebox.askokcancel("Confirmación de información","¿Ha confirmado por completo sus datos?") == True):
                self.habilitar_botones()
                
    def habilitar_botones(self):
        self.bt_limpiar.config(state = 'normal')
        self.bt_saturacion_oxigeno.config(state = 'normal')
        self.bt_presion_arterial.config(state = 'normal')
        self.bt_frecuencia_cardiaca.config(state = 'normal')
        self.bt_temperatura.config(state = 'normal')
        self.txb_estatura.config(state = "readonly")
        self.txb_peso.config(state = "readonly")
        self.cb_estatura.config(state = "disabled")
        self.cb_peso.config(state = "disabled")
        self.limpiar()

    def validar(self):
        self.alerta_texto_vacio()

    def tomar_medicion(self,medicion,caso):
        self.mensaje_pantalla(caso)
        self.deshabilitar_botones(medicion)
        self.parametros_fisiologicos = pf()
        if(medicion == "Presion Arterial"):
            self.parametros_fisiologicos.cargar_datos_parametro(medicion + " Sistolica")
            self.presion_arterial_sistolica = self.parametros_fisiologicos.realizar_medicion_parametro()
            self.parametros_fisiologicos.cargar_datos_parametro(medicion + " Diastolica")
            self.presion_arterial_diastolica = self.parametros_fisiologicos.realizar_medicion_parametro()

            self.texto_parametro.set(str(self.presion_arterial_sistolica) + "/" +str(self.presion_arterial_diastolica))
            self.texto_parametro_medido.set(medicion + " Sistolica/Diastolica: ")

        else:
            self.parametros_fisiologicos.cargar_datos_parametro(medicion)
            self.texto_parametro.set(self.parametros_fisiologicos.realizar_medicion_parametro())
            self.texto_parametro_medido.set(self.parametros_fisiologicos.descripcion + ": ")
            
    def limpiar(self):
        self.texto_parametro.set("")
        self.texto_pantalla.set("")
        self.texto_parametro_medido.set("Parametro medido: ")
        



        



    
        





        
