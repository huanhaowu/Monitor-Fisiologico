from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk

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

        self.canvas.create_rectangle(
            561.0,
            302.0,
            1189.0,
            480.0,
            fill="#EEF8FF",
            outline="")

        self.canvas.create_text(
            720.0,
            177.0,
            anchor="nw",
            text="Estatura",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )

        #Aqui va el texbox para la estatura
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

        #Aqui va el textbox para el parametro medido

        self.txb_parametro = Entry(
            bd=1,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.txb_parametro.place(
            x=561.0,
            y=554.0,
            width=289.0,
            height=55.0
        )

        self.canvas.create_text(
            570.0,
            510.0,
            anchor="nw",
            text="Parámetro medido:",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )

        #Aqui va el boton para comenzar una medicion
        self.bt_imagen_comenzar = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.bt_comenzar = Button(
            image=self.bt_imagen_comenzar,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
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
            command=lambda: print("button_3 clicked"),
            relief="flat",
            bg = "White"
        )
        self.bt_limpiar.place(
            x=1122.0,
            y=491.0,
            width=67.0,
            height=71.71826171875
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
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
            command=lambda: print("button_4 clicked"),
            relief="flat",
            bg = "White"
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
            command=lambda: print("button_5 clicked"),
            relief="flat",
            bg = "White"
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
            command=lambda: print("button_6 clicked"),
            relief="flat",
            bg = "White"
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
            command=lambda: print("button_7 clicked"),
            relief="flat",
            bg = "White"
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
            bg = "White"
        )
        self.bt_generar_informe.place(
            x=838.0,
            y=646.0,
            width=424.0,
            height=91.0
        )
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
