#Librerias para pruebas, aun no estan siendo utilizadas
#import smtplib
#import ssl
#from pdf_mail import sendpdf

from datetime import date, datetime
from pathlib import Path
from tkinter import Tk, ttk, Canvas, Button, PhotoImage, HORIZONTAL, Label, Text, Scrollbar, RIGHT, scrolledtext, Y, \
    DISABLED

import tk

# Bloque de codigo para trabajar con el path de los archivos
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/reporte_med")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Clase del formulario
class ReporteMed():
    def __init__(self, sujeto, mediciones):

        # Datos a mostrar dentro del formulario
        self.sujeto = sujeto
        self.mediciones = mediciones

        #Rellenamos los valores de las mediciones realizadas con la funcion buscar_parametro
        self.lista_temperatura = self.buscar_parametro("Temperatura")
        self.lista_presion = self.buscar_parametro("Presion Arterial")
        self.lista_oxigeno = self.buscar_parametro("Saturacion Oxigeno")
        self.lista_frecuencia = self.buscar_parametro("Frecuencia Cardiaca")

        #Definicion puerto, servidor, correo y contraseña de envio de reportes
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "heartbeatmonitorfisiologico@gmail.com"
        self.password = "!#MonitorHeartBeat2686"

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
            font=("RobotoRoman Regular", 9),
            yscrollcommand = scrollbar.set
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
        self.crear_pdf()
        self.window.resizable(False, False)
        self.window.mainloop()

    def crear_nota_aclaratoria(self):
        mensaje = ""
        for x in self.sujeto.condiciones_medicas:
            if mensaje == "":
                mensaje += f"-La condicion ({x.descripcion}) puede afectar: "
            else:
                mensaje +=f"\n-La condicion ({x.descripcion}) puede afectar: "
            for y in x.parametros:
                mensaje += f"({y.descripcion})  "
        return mensaje

    def calcular_edad(self):
        fecha_actual_date = datetime.strptime(self.fecha_actual_str, '%Y/%m/%d')
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
        elif lista[0] == "gris":
            pb = ttk.Progressbar(self.window, orient=HORIZONTAL, mode='determinate',
                                 style="gris.Horizontal.TProgressbar")
            pb['value'] = 0
        return pb

    # def enviar_pdf2(self):
    #     ssl_context = ssl.create_default_context()
    #     service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
    #     service.login(self.sender_mail, self.password)
    #     service.sendmail(self.sender_mail, "saldanaquezada@gmail.com", "Subject")
    #     service.quit()

    # def enviar_pdf(self):
    #     pdf_envio = sendpdf("heartbeatmonitorfisiologico@gmail.com",
    #                         self.sujeto.correo,
    #                         "!#MonitorHeartBeat2686",
    #                         "Reporte de Medicion ",
    #                         "Este es el reporte con las mediciones generadas en el sistema HeartBeat. Gracias por preferirnos!",
    #                         "Reporte_HeartBeat",
    #                         "C:/Users/Angel/Monitor-Fisiologico/interfaces")
    #     pdf_envio.email_send()

    def abrir_menu(self):
        from interfaces.menu_med import MenuMed
        self.window.destroy()
        menu = MenuMed(self.sujeto, self.mediciones)


if __name__ == "__main__":
    # region IMPORTS CLASES
    from datetime import date, datetime
    from modelos.sujetos_estudio import SujetosEstudio
    from modelos.mediciones_sujeto import MedicionesSujeto
    from modelos.medicion_parametro import MedicionParametro
    from modelos.parametros_fisiologicos import ParametrosFisiologicos
    from modelos.tipo_documento import TipoDocumento
    from modelos.sexo import Sexo
    from modelos.genero import Genero
    from modelos.orientacion_sexual import OrientacionSexual
    from modelos.nacionalidad import Nacionalidad
    from modelos.provincia import Provincia
    from modelos.condiciones_medicas import CondicionesMedicas

    # endregion
    sexo = Sexo(0, "Hombre")
    genero = Genero(0, "Masculino")
    orientacion = OrientacionSexual(0, "Heterosexual")
    provincia = Provincia(0, "Santo Domingo")
    nacionalidad = Nacionalidad(0, "Dominicano")
    parametro1 = ParametrosFisiologicos(1, "Temperatura", 36, 37, 40, 34, 46, 29.99, "Instruccion")
    parametro2 = ParametrosFisiologicos(2, "Presion Arterial", 36, 37, 40, 34, 46, 29.99, "Instruccion")
    lista_parametros = [parametro1, parametro2]
    condicion1 = CondicionesMedicas(0, "Asma", lista_parametros)
    condicion2 = CondicionesMedicas(1, "Diabetes", lista_parametros)
    lista_condiciones = [condicion1, condicion2]
    tipo_documento = TipoDocumento(0, "Cedula"
                                      "")
    fecha_nacimiento = datetime.strptime("1990/01/01", '%Y/%m/%d')

    sujeto1 = SujetosEstudio(tipo_documento.descripcion, "1234532", 1, "Juan", "Perez", fecha_nacimiento,
                             sexo, genero, orientacion, nacionalidad, provincia, "paolasaldanaquezada@gmail.com",
                             lista_condiciones)

    medicion_parametros1 = MedicionParametro(parametro1, 36)
    medicion_parametros2 = MedicionParametro(parametro2, 45)
    listaMediciones = [medicion_parametros1, medicion_parametros2]
    medicion1 = MedicionesSujeto(1, sujeto1, 70, 180, date.today(), listaMediciones)
    reporte = ReporteMed(sujeto1, medicion1)
    reporte.crear_pdf()





