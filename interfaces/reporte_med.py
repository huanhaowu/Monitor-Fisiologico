

from datetime import date, datetime
from email import encoders
from email.mime.base import MIMEBase
from pathlib import Path
from tkinter import Tk, ttk, Canvas, Button, PhotoImage, HORIZONTAL, Label, Text, Scrollbar, RIGHT, Y, \
    DISABLED

# Bloque de codigo para trabajar con el path de los archivos
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/reporte_med")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Clase del formulario
class ReporteMed():
    def __init__(self, sujeto, mediciones):

        #Arreglo - Documenta esta parte para que sea mas facil encontrar los campos, puedes guiarte de la estructura que siguieron los de la interfaz registro_suj.py
        #Arreglo - Agrupa los controles del formulario en secciones por tipo, es decir, pon todos los botones en un solo lado, todos los textos en otro. Esto con el objetivo facilitar los arreglos
        #Arreglo - Continua usando los "region" para definir las secciones de los controles

        # Datos a mostrar dentro del formulario
        self.sujeto = sujeto
        self.mediciones = mediciones

        #Rellenamos los valores de las mediciones realizadas con la funcion buscar_parametro
        self.lista_temperatura = self.buscar_parametro("Temperatura")
        self.lista_presion = self.buscar_parametro("Presion Arterial")
        self.lista_oxigeno = self.buscar_parametro("Saturacion de Oxigeno")
        self.lista_frecuencia = self.buscar_parametro("Frecuencia Cardiaca")

        #Campos calculados en cada reporte
        self.fecha_actual_str = date.today().strftime("%Y/%m/%d")
        self.edad = self.calcular_edad()
        self.nota_aclaratoria = self.crear_nota_aclaratoria()
        self.ruta_logo = relative_to_assets("logo1.png")
        self.ruta_pdf = str(relative_to_assets("Reporte_HeartBeat.pdf"))

        # Iniciacion de la pantalla
        self.window = Tk()
        self.window.geometry("1260x725+{}+{}".format(self.window.winfo_screenwidth() // 2 - 1260 // 2,
                                                     self.window.winfo_screenheight() // 2 - 725 // 2))
        self.window.configure(bg="#FFFFFF")

        # region ESTILOS DE PROGRESS BAR
        TROUGH_COLOR = '#F5F5F5'
        BAR_COLOR = '#FF0211'
        sty_rojo = ttk.Style()
        sty_rojo.theme_use('clam')
        sty_rojo.configure("rojo.Horizontal.TProgressbar", troughcolor=TROUGH_COLOR,
                           bordercolor=TROUGH_COLOR, background=BAR_COLOR, lightcolor=BAR_COLOR,
                           darkcolor=BAR_COLOR)

        TROUGH_COLOR = '#F5F5F5'
        BAR_COLOR = '#FFBF00'
        sty_amarillo = ttk.Style()
        sty_amarillo.theme_use('clam')
        sty_amarillo.configure("amarillo.Horizontal.TProgressbar", troughcolor=TROUGH_COLOR,
                               bordercolor=TROUGH_COLOR, background=BAR_COLOR, lightcolor=BAR_COLOR,
                               darkcolor=BAR_COLOR)

        TROUGH_COLOR = '#F5F5F5'
        BAR_COLOR = '#00C040'
        sty_verde = ttk.Style()
        sty_verde.theme_use('clam')
        sty_verde.configure("verde.Horizontal.TProgressbar", troughcolor=TROUGH_COLOR,
                            bordercolor=TROUGH_COLOR, background=BAR_COLOR, lightcolor=BAR_COLOR,
                            darkcolor=BAR_COLOR)

        TROUGH_COLOR = '#F5F5F5'
        BAR_COLOR = '#F5F5F5'
        sty_gris = ttk.Style()
        sty_gris.theme_use('clam')
        sty_gris.configure("gris.Horizontal.TProgressbar", troughcolor=TROUGH_COLOR,
                            bordercolor=TROUGH_COLOR, background=BAR_COLOR, lightcolor=BAR_COLOR,
                            darkcolor=BAR_COLOR)

        # endregion
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
            command=lambda: self.abrir_menu(),
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
            text=self.sujeto.nombres + " " + self.sujeto.apellidos,
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
            text=self.sujeto.sexo.descripcion,
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.lbl_sexo.place(
            x=985.0,
            y=198.0,
            width=120.0,
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
            text=self.edad,
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
            text=self.mediciones.peso_sujeto,
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
            text=self.mediciones.altura_sujeto,
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
            text=self.fecha_actual_str,
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
            text=(self.sujeto.tipo_documento.descripcion) + " " + self.sujeto.codigo_documento,
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
            text=self.lista_temperatura[2],
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

        self.pb_temperatura = self.llenar_barras(self.lista_temperatura)
        self.pb_temperatura.place(
            x=527.0,
            y=415.0,
            width=224.0,
            height=34.0
        )
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
            text=self.lista_oxigeno[2],
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

        self.pb_saturacion_oxigeno = self.llenar_barras(self.lista_oxigeno)
        self.pb_saturacion_oxigeno.place(
            x=527.0,
            y=478.0,
            width=224.0,
            height=34.0
        )
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

        # aqui va el textbox del valor correspondiente a la presion arterial
        self.lbl_presion_arterial = Label(
            self.window,
            text=self.lista_presion[2],
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
        self.pb_presion_arterial = self.llenar_barras(self.lista_presion)
        self.pb_presion_arterial.place(
            x=527.0,
            y=538.0,
            width=224.0,
            height=34.0
        )
        # endregion

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
            text=self.lista_frecuencia[2],
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

        self.pb_frecuencia_cardiaca = self.llenar_barras(self.lista_frecuencia)
        self.pb_frecuencia_cardiaca.place(
            x=527.0,
            y=597.0,
            width=224.0,
            height=34.0,
        )
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
        f = ttk.Frame(self.window)
        f.config(height=14, width=50)
        f.place(x=840.0, y=417.0)
        scrollbar = Scrollbar(f)
        self.txt_nota = Text(
            f,
            width=50,
            height=13,
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            font=("RobotoRoman Regular", 11),
            yscrollcommand = scrollbar.set,
            wrap = 'word'
        )
        self.txt_nota.insert("1.0",self.nota_aclaratoria)
        scrollbar.config(command=self.txt_nota.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.txt_nota.pack(side="left")
        self.txt_nota.config(state=DISABLED)
        # endregion

        # region BOTON GUARDAR
        self.img_guardar = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.btn_guardar = Button(
            image=self.img_guardar,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.enviar_pdf(),
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

    #Arreglo - Documenta todas tus funciones
    def crear_nota_aclaratoria(self):
        mensaje = ""
        if self.sujeto.condiciones_medicas != []:
            for x in self.sujeto.condiciones_medicas:
                if mensaje == "":
                    mensaje += f"- La condición ({x.descripcion}) puede afectar: "
                else:
                    mensaje += f"\n\n- La condición ({x.descripcion}) puede afectar: "
                parametros = ", ".join([y.descripcion for y in x.parametros])
                mensaje += parametros
        return mensaje

    def calcular_edad(self):
        fecha_actual_date = date.today()
        edad = (fecha_actual_date - self.sujeto.fecha_nacimiento)
        edad = (edad.days) // 365
        return edad

    def buscar_parametro(self, parametro_fis):
        for x in self.mediciones.parametros_medidos:
            if x.parametro.descripcion == parametro_fis:
                return x.asignar_color()

        return ["gris", " ", "N/A"]

    def crear_pdf(self):
        from modelos.reporte_pdf import ReportePdf
        self.ruta_logo = relative_to_assets("logo1.png")
        self.ruta_pdf = str(relative_to_assets("Reporte_HeartBeat.pdf"))
        pdf = ReportePdf(self)


    def llenar_barras(self, lista=[]):
        if lista[0] == "rojo":
            pb=ttk.Progressbar(self.window, orient=HORIZONTAL, mode='determinate',
                                              style="rojo.Horizontal.TProgressbar")
            pb['value'] = 50
        elif lista[0] == "verde":
            pb = ttk.Progressbar(self.window, orient=HORIZONTAL, mode='determinate',
                                 style="verde.Horizontal.TProgressbar")
            pb['value'] = 100
        elif lista[0] == "amarillo":
            pb = ttk.Progressbar(self.window, orient=HORIZONTAL, mode='determinate',
                                 style="amarillo.Horizontal.TProgressbar")
            pb['value'] = 75
        else:
            pb = ttk.Progressbar(self.window, orient=HORIZONTAL, mode='determinate',
                                 style="gris.Horizontal.TProgressbar")
            pb['value'] = 0
        return pb


    def enviar_pdf(self):
        self.crear_pdf()
        destinatario = self.sujeto.correo
        from Google import Create_Service
        import base64
        from email.mime.multipart import MIMEMultipart

        nombre_pdf = 'Reporte_HeartBeat.pdf'
        ruta_pdf = relative_to_assets(nombre_pdf)
        CLIENT_SECRET_FILE = 'credentials.json'
        API_NAME = 'gmail'
        API_VERSION = 'v1'
        SCOPES = ['https://mail.google.com/']

        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

        correo = MIMEMultipart()
        correo['to'] = destinatario
        correo['subject'] = f'Reporte {self.fecha_actual_str}'
        # correo.attach(MIMEText(cuerpo_correo, 'plain'))


        # se abre el archivo pdf en binario
        binary_pdf = open(ruta_pdf, 'rb')

        payload = MIMEBase('application', 'octate-stream', Name=nombre_pdf)
        payload.set_payload((binary_pdf).read())

        # se codifica el binario a base64
        encoders.encode_base64(payload)

        # adjuntar el archivo o 'carga' al correo
        correo.attach(payload)

        #enviar correo
        cuerpo_crudo = base64.urlsafe_b64encode(correo.as_bytes()).decode()
        message = service.users().messages().send(userId='me', body={'raw': cuerpo_crudo}).execute()


    def abrir_menu(self):
        from interfaces.menu_med import MenuMed
        self.window.destroy()
        menu = MenuMed(self.sujeto, self.mediciones)
        