
from datetime import date
from email import encoders
from email.mime.base import MIMEBase
from pathlib import Path
import re
from tkinter import Tk, messagebox, simpledialog, ttk, Canvas, Button, PhotoImage, HORIZONTAL, Label, Text, Scrollbar, \
    RIGHT, Y, \
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

        # Objetos sujeto y mediciones a partir de los que se genera el reporte
        self.sujeto = sujeto
        self.mediciones = mediciones

        #Rellenamos los valores de las mediciones realizadas con la funcion buscar_parametro
        self.lista_temperatura = self.buscar_parametro("Temperatura")
        lista_presion_sistolica = self.buscar_parametro("Presion Arterial Sistolica")
        lista_presion_diastolica = self.buscar_parametro("Presion Arterial Diastolica")
        self.lista_presion = ["", "", str(lista_presion_diastolica[2]) + '/' + str(lista_presion_sistolica[2])]
        
        if(lista_presion_sistolica[0] != "verde" and lista_presion_diastolica[0] != "verde"):
            if(lista_presion_sistolica[0] == "rojo"):
                self.lista_presion[0] = lista_presion_sistolica[0]
                self.lista_presion[1] = lista_presion_sistolica[1]
            elif((lista_presion_sistolica[0] == "amarillo")):
                self.lista_presion[0] = lista_presion_sistolica[0]
                self.lista_presion[1] = lista_presion_sistolica[1]
            

            if((lista_presion_diastolica[0] == "rojo")):
                self.lista_presion[0] = lista_presion_diastolica[0]
                self.lista_presion[1] = lista_presion_diastolica[1]
            elif((lista_presion_diastolica[0] == "amarillo")):
                self.lista_presion[0] = lista_presion_diastolica[0]
                self.lista_presion[1] = lista_presion_diastolica[1]
        else:
            self.lista_presion[0] = "verde"
            self.lista_presion[1] = " "

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
        self.window.title("Reporte de mediciones")


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

        #region CREACION PANTALLA

        

        #Creacion del canvas principal de la pantalla
        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=725,
            width=1260,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        #Posicionamiento del canvas
        self.canvas.place(x=0, y=0)

        #region LINEAS DIVISORAS (CANVAS.CREATE_RECTANGLE)

        # Linea divisoria entre Logo y Titulo Informe
        self.canvas.create_rectangle(
            49.0,
            95.93429565429688,
            1196.0,
            97.0,
            fill="gray",
            outline="")

        # Linea divisoria entre los datos del sujeto y los datos de las mediciones
        self.canvas.create_rectangle(
            47.0,
            322.0,
            1196.0,
            325.0,
            fill="#000000",
            outline="")
        #endregion

        #endregion

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
            text="Nombre:",
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
            text="Sexo:",
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
            text="Edad:",
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
            text="Peso:",
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
            text="Estatura:",
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
        self.canvas.create_text(
            50.0,
            247.0,
            anchor="nw",
            text= (self.sujeto.tipo_documento.descripcion) + ":",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.lbl_cod_doc = Label(
            self.window,
            text= self.sujeto.codigo_documento,
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            font=("RobotoRoman Regular", 25 * -1)
        )
        self.lbl_cod_doc.place(
            x= 177.0,
            y=247.0,
            width=388.0,
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
            text="Temperatura (C°)",
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
        #indicador de temperatura
        self.canvas.create_text(
            755.0,
            415.0,
            anchor="nw",
            text=self.lista_temperatura[1],
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )

        # endregion

        # region SATURACION DE OXIGENO
        self.canvas.create_text(
            50.0,
            489.0,
            anchor="nw",
            text="Saturación de Oxígeno (%)",
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
        # indicador de oxigeno
        self.canvas.create_text(
            755.0,
            478.0,
            anchor="nw",
            text=self.lista_oxigeno[1],
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )
        # endregion

        # region PRESION ARTERIAL
        self.canvas.create_text(
            90.0,
            549.0,
            anchor="nw",
            text="Presión Arterial (mmHg) ",
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
        # indicador de presion arterial
        self.canvas.create_text(
            755.0,
            538.0,
            anchor="nw",
            text=self.lista_presion[1],
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )
        # endregion

        # region FRECUENCIA CARDIACA
        self.canvas.create_text(
            60.0,
            608.0,
            anchor="nw",
            text="Frecuencia Cardiaca (lpm)",
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
        # indicador de frecuencia cardiaca
        self.canvas.create_text(
            755.0,
            597.0,
            anchor="nw",
            text=self.lista_frecuencia[1],
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
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
        f.config(height=14, width=140)
        f.place(x=800.0, y=417.0)
        scrollbar_nota = Scrollbar(f)
        self.txt_nota = Text(
            f,
            width=50,
            height=13,
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            font=("RobotoRoman Regular", 11),
            yscrollcommand = scrollbar_nota.set,
            wrap = 'word'
        )
        self.txt_nota.insert("1.0",self.nota_aclaratoria)
        scrollbar_nota.config(command=self.txt_nota.yview)
        scrollbar_nota.pack(side=RIGHT, fill=Y)
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
            command=lambda: self.confirmar_correo(),
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
    #esta funcion retorna un string que contiene la nota aclaratoria que se muestra en el reporte
    #se calcula en base a todas las condiciones medicas que posee el sujeto y todas las mediciones que esa condicion puede afectar
        mensaje = ""
        if self.sujeto.condiciones_medicas != []: #si el sujeto tiene alguna condicion
            for x in self.sujeto.condiciones_medicas: #para cada condicion que el sujeto tenga
                if mensaje == "": #si el mensaje esta vacio no se imprime salto de linea
                    mensaje += f"- La condición ({x.descripcion}) puede afectar: "
                else:  #si el mensaje ya tiene alguna condicion, imprime un salto de linea antes de colocar la sig
                    mensaje += f"\n\n- La condición ({x.descripcion}) puede afectar: "
                parametros = ", ".join([y.descripcion for y in x.parametros]) #separando por comas, ve concatenando cada parametro (y) que se ve afectado por esa condicion (x)
                mensaje += parametros
        return mensaje

    def calcular_edad(self): #retorna la edad en años del sujeto
        fecha_actual_date = date.today()
        edad = (fecha_actual_date - self.sujeto.fecha_nacimiento) #le resto a la fecha actual la fecha de nacimiento
        edad = (edad.days) // 365 #divido (con division entera) la cantidad de dias entre 365 para conseguir la cantidad de años
        return edad

    def buscar_parametro(self, parametro_fis): #le paso el parametro que quiero revisar, retorna una lista de tres elementos, se ejecuta una vez por cada parametro
    #el elemento en posicion [0] me dice el color para el progress bar del parametro
    #el elemento en posicion [1] me dice si el valor esta por encima (+), por debajo(-) o dentro del estandar( )
    #el elemento en posicion [2] me dice el valor medido

        for x in self.mediciones.parametros_medidos: #para cada medicion dentro de la lista de parametros medidos
            if parametro_fis in x.parametro.descripcion: #si encuentra el parametro llama al metodo asignar_color
                return x.asignar_color()

        return ["gris", " ", "N/A"] #si el parametro no se midio por defecto se asigna el color gris, el indicador " " y el valor "N/A"

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


    def enviar_pdf(self, correo_envio):
        from gmail.Google import Create_Service
        import base64
        from email.mime.multipart import MIMEMultipart

        self.crear_pdf()
        destinatario = correo_envio
        nombre_pdf = 'Reporte_HeartBeat.pdf'
        ruta_pdf = relative_to_assets(nombre_pdf)
        CLIENT_SECRET_FILE = 'gmail/credentials.json'
        API_NAME = 'gmail'
        API_VERSION = 'v1'
        SCOPES = ['https://mail.google.com/']

        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

        correo = MIMEMultipart()
        correo['to'] = destinatario
        correo['subject'] = f'Reporte {self.fecha_actual_str}'

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
    
    def verificar_correo_electronico(self, correo): 
        if(correo !="" or correo.isspace() == False):
               patron =  r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
               resultado = re.match(patron, correo)
               if(resultado):
                    return True
               else:
                    messagebox.showwarning("ALERTA", "El correo electronico no es valido. \n\nPor favor ingrese un correo electronico valido.")
                    return False
        return True
    

    def confirmar_correo(self):
        correo_envio = None
        while correo_envio == None:
            if(messagebox.askyesno("Confirmar envio","¿Desea recibir el reporte a su correo?")== True):
                correo_envio = simpledialog.askstring(title="Confirmar correo",
                prompt="Correo a enviar:",
                initialvalue= self.sujeto.correo)
                if(correo_envio != None):
                    while(self.verificar_correo_electronico(correo_envio) == False):
                        correo_envio = simpledialog.askstring(title="Confirmar correo",
                        prompt="Correo a enviar:",
                        initialvalue= self.sujeto.correo)
                    self.enviar_pdf(correo_envio)
                    messagebox.showinfo("Envio exitoso", "El reporte ha sido enviado a su correo")
            else:
                break

        from interfaces.login_suj import LoginSujEstudio
        self.window.destroy()
        menu = LoginSujEstudio()


    def abrir_menu(self):
        from interfaces.menu_med import MenuMed
        self.window.destroy()
        menu = MenuMed(self.sujeto, self.mediciones)
        