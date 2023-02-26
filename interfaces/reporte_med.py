import datetime

from pathlib import Path

from tkinter import Tk, ttk, Canvas, Button, PhotoImage, HORIZONTAL, Label

# Bloque de codigo para trabajar con el path de los archivos
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\reporte_med")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Clase del formulario
class ReporteMed():
     def __init__(self, sujeto, mediciones):
        # Datos a mostrar dentro del formulario
        self.sujeto = sujeto
        self.mediciones = mediciones
        
        # Iniciacion de la pantalla
        self.window = Tk()
        self.window.geometry("1260x725")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=725,
            width=1260,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)

        self.img_regresar = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.btn_regresar = Button(
            image=self.img_regresar,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat",
            bg="white"
        )
        self.btn_regresar.place(
            x=50.0,
            y=16.0,
            width=61.0,
            height=60.0
        )
        # LINEA DIVISORIA ENTRE LOGO Y TITULO INFORME
        self.canvas.create_rectangle(
            49.0,
            95.93429565429688,
            1196.0,
            97.0,
            fill="gray",
            outline="")
        # LINEA DIVISORIA ENTRE DATOS SUJETO Y MEDIDAS PARAMETROS
        self.canvas.create_rectangle(
            47.0,
            322.0,
            1196.0,
            325.0,
            fill="#000000",
            outline="")

        self.img_logo = PhotoImage(
            file=relative_to_assets("logo1.png"))
        self.logo1 = self.canvas.create_image(
            1070.0,
            70.0,
            image=self.img_logo
        )

        self.canvas.create_text(
            50.0,
            120.0,
            anchor="nw",
            text="INFORME DE MEDICIÓN",
            fill="#000000",
            font=("RobotoRoman Regular", 30 * -1)
        )

        # -- CAMPOS DEL SUJETO --
        # Ordenados por label (Nombres:) y luego textbox (Ricardo Jose).

        # NOMBRES
        self.canvas.create_text(
            50.0,
            195.0,
            anchor="nw",
            text="Nombre : ",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.lbl_nombre = Label(
            self.window,
            text=sujeto.nombres + " " + sujeto.apellidos,
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.lbl_nombre.place(
            x=177.0,
            y=198.0,
            width=388.0,
            height=34.0
        )

        # SEXO
        self.canvas.create_text(
            900.0,
            198.0,
            anchor="nw",
            text="Sexo :",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.lbl_sexo = Label(
            self.window,
            text=sujeto.sexo,
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.lbl_sexo.place(
            x=985.0,
            y=198.0,
            width=108.0,
            height=34.0
        )

        # EDAD
        self.canvas.create_text(
            600,
            195.0,
            anchor="nw",
            text="Edad : ",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )

        self.lbl_edad = Label(
            self.window,
            text=sujeto.fecha_nacimiento,
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.lbl_edad.place(
            x=707.6485595703125,
            y=198.0,
            width=108.0,
            height=34.0
        )

        # PESO
        self.canvas.create_text(
            600,
            242.60400390625,
            anchor="nw",
            text="Peso :",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.lbl_peso = Label(
            self.window,
            text="",
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.lbl_peso.place(
            x=707.6485595703125,
            y=247.0,
            width=108.0,
            height=34.0
        )

        # ESTATURA
        self.canvas.create_text(
            862.0,
            247.0,
            anchor="nw",
            text="Estatura :",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )

        self.lbl_estatura = Label(
            self.window,
            text="",
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.lbl_estatura.place(
            x=985.0,
            y=247.0,
            width=108.0,
            height=34.0
        )

        # FECHA DE EMISION
        self.canvas.create_text(
            685.0,
            122.0,
            anchor="nw",
            text="Fecha de emisión :",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.lbl_fecha = Label(
            self.window,
            text='datetime.date.today()',
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.lbl_fecha.place(
            x=946.0,
            y=122.0,
            width=250.0,
            height=34.0
        )

        # CODIGO DOCUMENTO
        self.lbl_cod_doc = Label(
            self.window,
            text=sujeto.tipo_documento + " " + sujeto.codigo_documento,
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.lbl_cod_doc.place(
            x=50.0,
            y=247.0,
            width=515.0,
            height=34.0
        )
        # -- PARAMETROS FISIOLOGICOS --
        def fill_progress(self):
            return 50
        # region TITULOS COLUMNAS
        self.canvas.create_text(
            50.0,
            359.0,
            anchor="nw",
            text="Parámetro Fisiológico",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.canvas.create_text(
            400.0,
            359.0,
            anchor="nw",
            text="Valor",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.canvas.create_text(
            600.0,
            361.0,
            anchor="nw",
            text="Escala",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )
        # endregion

        # region TEMPERATURA
        self.canvas.create_text(
            162.0,
            424.0,
            anchor="nw",
            text="Temperatura",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )
        # aqui se colocara el textbox con el valor de la temperatura
        self.lbl_temperatura = Label(
            self.window,
            text="",
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.lbl_temperatura.place(
            x=379.0,
            y=417.0,
            width=96.0,
            height=34.0
        )
        # Aqui se colora el progress bar para la escala de la temperatura
        TROUGH_COLOR = '#F5F5F5'
        BAR_COLOR = 'red'
        sty_temp = ttk.Style()
        sty_temp.theme_use('clam')
        sty_temp.configure("bar.Horizontal.TProgressbar", troughcolor=TROUGH_COLOR,
                      bordercolor=TROUGH_COLOR, background=BAR_COLOR, lightcolor=BAR_COLOR,
                      darkcolor=BAR_COLOR)

        self.pb_temperatura = ttk.Progressbar(self.window, orient=HORIZONTAL, mode='determinate',
                                         style="bar.Horizontal.TProgressbar")
        self.pb_temperatura.place(
            x=527.0,
            y=415.0,
            width=224.0,
            height=34.0
        )



        self.pb_temperatura['value'] = fill_progress(self)

        # endregion

        # region SATURACION DE OXIGENO
        self.canvas.create_text(
            56.0,
            489.0,
            anchor="nw",
            text="Saturación de Oxígeno",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )
        # aqui se colocara el textbox que contiene el valor de la saturacion de oxigeno
        self.lbl_saturacion_oxigeno = Label(
            self.window,
            text="",
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.lbl_saturacion_oxigeno.place(
            x=379.0,
            y=480.0,
            width=96.0,
            height=34.0
        )
        # Aqui se colocara el progress bar para la escala de saturacion de oxigeno
        TROUGH_COLOR = '#F5F5F5'
        BAR_COLOR = 'red'
        sty = ttk.Style()
        sty.theme_use('clam')
        sty.configure("bar.Horizontal.TProgressbar", troughcolor=TROUGH_COLOR,
                      bordercolor=TROUGH_COLOR, background=BAR_COLOR, lightcolor=BAR_COLOR,
                      darkcolor=BAR_COLOR)

        self.pb_saturacion_oxigeno = ttk.Progressbar(self.window, orient=HORIZONTAL, mode='determinate',
                                                style="bar.Horizontal.TProgressbar")
        self.pb_saturacion_oxigeno.place(
            x=527.0,
            y=478.0,
            width=224.0,
            height=34.0
        )


        self.pb_saturacion_oxigeno['value'] = fill_progress(self)

        # endregion

        # region PRESION ARTERIAL
        self.canvas.create_text(
            137.0,
            549.0,
            anchor="nw",
            text="Presión Arterial ",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )
        #endregion
        
        # aqui va el textbox del valor correspondiente a la presion arterial
        self.lbl_presion_arterial = Label(
            self.window,
            text="",
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            font=("RobotoRoman Regular", 25 * -1)
        )

        self.lbl_presion_arterial.place(
            x=379.0,
            y=540.0,
            width=96.0,
            height=34.0
        )

        # aqui va el progress bar de la presion arterial

        self.lbl_saturacion_oxigeno = Label(
            self.window,
            text="",
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.lbl_saturacion_oxigeno.place(
            x=379.0,
            y=480.0,
            width=96.0,
            height=34.0
        )

        TROUGH_COLOR = '#F5F5F5'
        BAR_COLOR = 'red'
        sty = ttk.Style()
        sty.theme_use('clam')
        sty.configure("bar.Horizontal.TProgressbar", troughcolor=TROUGH_COLOR,
                      bordercolor=TROUGH_COLOR, background=BAR_COLOR, lightcolor=BAR_COLOR,
                      darkcolor=BAR_COLOR)

        self.pb_presion_arterial = ttk.Progressbar(self.window, orient=HORIZONTAL, mode='determinate',
                                              style="bar.Horizontal.TProgressbar")
        self.pb_presion_arterial.place(
            x=527.0,
            y=538.0,
            width=224.0,
            height=34.0
        )


        self.pb_presion_arterial['value'] = fill_progress(self)
        #####################

        # region FRECUENCIA CARDIACA
        self.canvas.create_text(
            70.0,
            608.0,
            anchor="nw",
            text="Frecuencia Cardiaca ",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )

        # aqui va el valor correspondiente a la medicion de la frecuencia cardiaca
        self.lbl_frecuencia_cardiaca = Label(
            self.window,
            text="",
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.lbl_frecuencia_cardiaca.place(
            x=379.0,
            y=597.0,
            width=96.0,
            height=34.0
        )
        # aqui debe ir el progress bar para colocar la frecuencia cardiaca
        TROUGH_COLOR = '#F5F5F5'
        BAR_COLOR = 'red'
        sty = ttk.Style()
        sty.theme_use('clam')
        sty.configure("bar.Horizontal.TProgressbar", troughcolor=TROUGH_COLOR,
                      bordercolor=TROUGH_COLOR, background=BAR_COLOR, lightcolor=BAR_COLOR,
                      darkcolor=BAR_COLOR)

        self.pb_frecuencia_cardiaca = ttk.Progressbar(self.window, orient=HORIZONTAL, mode='determinate',
                                                   style="bar.Horizontal.TProgressbar")
        self.pb_frecuencia_cardiaca.place(
            x=527.0,
            y=597.0,
            width=224.0,
            height=34.0,
        )
        self.pb_frecuencia_cardiaca['value']=fill_progress(self)

        # endregion

        # region NOTA ACLARATORIA
        self.canvas.create_text(
            837.0,
            359.0,
            anchor="nw",
            text="Nota aclaratoria : ",
            fill="#000000",
            font=("RobotoRoman Regular", 30 * -1)
        )
        # Aqui debe ir el textbox con el valor de la nota aclaratoria
        self.lbl_nota = Label(
            self.window,
            text="",
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.lbl_nota.place(
            x=840.0,
            y=417.0,
            width=356.0,
            height=214.0
        )
        # endregion

        # region BOTON GUARDAR
        self.img_guardar = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.btn_guardar = Button(
            image=self.img_guardar,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.btn_guardar.place(
            x=840.0,
            y=657.0,
            width=431.851318359375,
            height=68.0
        )
        # endregion
        self.window.resizable(False, False)
        self.window.mainloop()


