from pathlib import Path
from modelos.tipo_documento import TipoDocumento
from modelos.nacionalidad import Nacionalidad
from modelos.genero import Genero
from modelos.sexo import Sexo
from modelos.provincia import Provincia
from modelos.orientacion_sexual import OrientacionSexual
from modelos.condiciones_medicas import CondicionesMedicas 

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
from tkcalendar import DateEntry
import os
import datetime

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/registro_suj")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class RegistroSujeto():
    def _init_(self, tipo_documento, codigo_documento):
        self.tipo_documento = tipo_documento
        self.codigo_documento = codigo_documento

        
        self.window = Tk()
        self.window.geometry("1260x725+{}+{}".format(self.window.winfo_screenwidth() // 2 - 1260 // 2, self.window.winfo_screenheight() // 2 - 725 // 2))
        self.window.configure(bg = "#FFFFFF")
        self.window.title("Registro de Sujeto")

        #-------------------- Ventana Principal -------------------
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
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1335.0,
            91.0,
            fill="#39A9E9",
            outline="")
        #Titulo de la canva principal
        self.canvas.create_text(
            350.0,
            25.0,
            anchor="nw",
            text="FORMULARIO DE INFORMACIÓN PERSONAL",
            fill="#FFFFFF",
            font=("RobotoRoman Bold", 30 * -1),
            justify = 'center'
        )

        #Background de la seccion de datos personales
        self.canvas.create_rectangle(
            781.0,
            118.0,
            783.0,
            694.0,
            fill="#000000",
            outline="")

        #-------------------- Botón Regresar -------------------
        #Imagen del botón regresar
        self.btn_img_regresar = PhotoImage(
            file=relative_to_assets("button_1.png"))
        #Propiedades del botón regresar
        self.btn_regresar = Button(
            image=self.btn_img_regresar,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.abrir_login(),
            relief="flat",
            bg = "#39A9E9"
        )
        #Localización del botón regresar
        self.btn_regresar.place(
            x=30.0,
            y=22.0,
            width=48.0,
            height=47.0
        )

        #-------------------- Botón Siguiente -------------------
        #imagen del botón siguiente
        self.btn_imagen_siguiente = PhotoImage(
            file=relative_to_assets("button_2.png"))
        #Propiedades del botón siguiente
        self.btn_siguiente = Button(
            image=self.btn_imagen_siguiente,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.abrir_menu(),
            relief="flat"
        )
        #Localización del botón siguiente
        self.btn_siguiente.place(
            x=857.0,
            y=656.0,
            width=411.851318359375,
            height=68.0
        )

        """
        ------------------ LABELS Y CAMPOS ------------------
        """

        #-------------------- COD DOCUMENTO -------------------
        #Label del Codigo de Documento
        self.canvas.create_text(
            25.0,
            171.0,
            anchor="nw",
            text="Código de\n Documento",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'center'
        )
        #Textbox del Codigo de Documento
        self.txb_codigo_doc = Entry(
            bd=1,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        #Loacalización del textbox del codigo de documento
        self.txb_codigo_doc.place(
            x=204.0,
            y=184.0,
            width=165.0,
            height=34.0
        )

        #-------------------- TIPO DOCUMENTO -------------------
        #Label del Tipo de Documento
        self.canvas.create_text(
            400.0,
            169.0,
            anchor="nw",
            text="Tipo de\n Documento",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'center'
        )
        #Combobox del Tipo de Documento
        td = TipoDocumento()
        self.cb_tipo_doc = ttk.Combobox(
            state = "readonly",
            values = td.obtener_lista_tipo_documento()
        )
        #Localización del combobox del tipo de documento
        self.cb_tipo_doc.place(
            x=561.0,
            y=184.0,
            width=178.0,
            height=34.0
        )
        #-------------------- NOMBRE -------------------
        #Label del Nombre
        self.canvas.create_text(
            25.0,
            276.0,
            anchor="nw",
            text="Nombre",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'center'
        )

        #Texbox del nombre
        self.txb_nombre = Entry(
            bd=1,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        #Localización del textbox del nombre
        self.txb_nombre.place(
            x=204.0,
            y=274.0,
            width=165.0,
            height=34.0
        )

        #-------------------- APELLIDO -------------------
        #Label del Apellido
        self.canvas.create_text(
            420.0,
            276.0,
            anchor="nw",
            text="Apellido",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'center'
        )

        #Textbox del Apellido
        self.txb_apellido = Entry(
            bd=1,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        #Localización del textbox del apellido
        self.txb_apellido.place(
            x=561.0,
            y=276.0,
            width=178.0,
            height=34.0
        )
        #-------------------- FECHA NACIMIENTO -------------------
        #Label de la Fecha de Nacimiento
        self.canvas.create_text(
            25.0,
            358.0,
            anchor="nw",
            text="Fecha de\n Nacimiento",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'center'
        )
        
        #Definir el día máximo de selección en el DT
        maxdate = datetime.date.today()

        #Datetimepicker de la Fecha de Nacimiento  
        self.dt_fecha_nac = DateEntry() ## TO DO : CAMBIAR A DATETIMEPICKER
            #state = "readonly",
            #values = ["1","2"]
        #)
        #localización del datetimepicker de la fecha de nacimiento
        self.dt_fecha_nac.config(maxdate = maxdate,firstweekday = 'sunday')
        self.dt_fecha_nac.place(
            x=204.0,
            y=374.0,
            width=165.0,
            height=34.0
        )
        #-------------------- SEXO -------------------
        #Label del Sexo
        self.canvas.create_text(
            430.0,
            374.0,
            anchor="nw",
            text="Sexo",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'center'
        )
        sexo = Sexo()
        #Combobox de Sexo 
        self.cb_sexo = ttk.Combobox(
            state = "readonly",
            value = sexo.obtener_lista_sexos()
        )
        #Localización del combobox de sexo
        self.cb_sexo.place(
            x=561.0,
            y=374.0,
            width=178.0,
            height=34.0
        )

        #-------------------- NACIONALIDAD -------------------
        #Label de la Nacionalidad
        self.canvas.create_text(
            25.0,
            489.0,
            anchor="nw",
            text="Nacionalidad",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'center'
        )
        nacionalidad = Nacionalidad()
        #ComboBox de nacionalidad
        self.txb_nacionalidad = ttk.Combobox(
            state = "readonly",
            values = nacionalidad.obtener_lista_nacionalidades()
        )
        #Localización del combobox de nacionalidad
        self.txb_nacionalidad.place(
            x=204.0,
            y=485.0,
            width=165.0,
            height=35.0
        )

        #-------------------- PROVINCIA -------------------
        #Label de la Provincia
        self.canvas.create_text(
            410.0,
            488.0,
            anchor="nw",
            text="Provincia",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )
        provincia = Provincia()
        #ComboBox para las provincias
        self.cb_provincia = ttk.Combobox(
            state = "readonly",
            values = provincia.obtener_lista_provincias()
        )
        #Localización del combobox de provincia
        self.cb_provincia.place(
            x=561.0,
            y=481.0,
            width=178.0,
            height=35.0
        )

        #-------------------- GENERO -------------------
        #Label del Genero
        self.canvas.create_text(
            30.0,
            582.0,
            anchor="nw",
            text="Genero",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1) ,
            justify = 'center'
        )
        genero = Genero()
        #ComboBox de genero
        self.cb_genero = ttk.Combobox(
            state = "readonly",
            values = genero.obtener_lista_generos()
        )
        #Localización del combobox de genero
        self.cb_genero.place(
            x=204.0,
            y=582.0,
            width=165.0,
            height=35.0
        )

        #-------------------- ORIENTACION SEXUAL -------------------
        #Label de la Orientacion Sexual
        self.canvas.create_text(
            400.0,
            573.0,
            anchor="nw",
            text="Orientacion\n Sexual",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'center'
        )
        orientacion = OrientacionSexual()
        #ComboBox de Orientacion Sexual
        self.cb_orientacion_sexual = ttk.Combobox(
        state = "readonly",
        values = orientacion.obtener_lista_orientaciones()
        )
        #Localización del combobox de orientacion sexual
        self.cb_orientacion_sexual.place(
            x=561.0,
            y=583.0,
            width=178.0,
            height=34.0
        )
        
        """
        #-------------------- ESTADOS DE SALUD -------------------
        """
        #Label principal de la sección de Estado de Salud
        self.canvas.create_text(
            910.0,
            126.0,
            anchor="nw",
            text="ESTADO DE SALUD",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'center'
        )

        #Label de las opciones de los habitos de consumo
        self.canvas.create_text(
            850.0,
            168.0,
            anchor="nw",
            text="Seleccione las opciones que se adecuen \na sus hábitos de consumo:",
            fill="#000000",
            font=("RobotoRoman Regular", 20 * -1),
            justify = 'center'
        )

        #-------------------- ALCOHOL -------------------
        #Label de Alcohol
        self.canvas.create_text(
            830.0,
            230.0,
            anchor="nw",
            text="Ingerir\n alcohol",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'center'
        )

        #CheckBox de Alcohol
        self.ck_alcohol = ttk.Combobox(
        state = "readonly",
        values = ["Si","No"]
        )
        #Localización del checkbox de alcohol
        self.ck_alcohol.place(
            x=940.0,
            y=247.0,
            width=59.0,
            height=35.0
        )

        #-------------------- FUMA -------------------
        #Label de Fumar
        self.canvas.create_text(
            1020.0,
            247.0,
            anchor="nw",
            text="Fumar",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'center'
        )

        #checkbox de Fumar
        self.ck_fumar = ttk.Combobox(
        state = "readonly",
        values = ["Si","No"]
        )
        #Localización del checkbox de fumar
        self.ck_fumar.place(
            x= 1110.0,
            y= 244.0,
            width= 59.0,
            height=35.0
        )

        #-------------------- Condiciones DE SALUD -------------------
        #Label de Condiciones de Salud
        self.canvas.create_text(
            850.0,
            311.0,
            anchor="nw",
            text="¿Posee alguna condición de salud?",
            fill="#000000",
            font=("RobotoRoman Regular", 20 * -1),
            justify = 'center'
        )
        #Label de los ejemplos de condiciones de salud
        self.canvas.create_text(
            860.0,
            350.0,
            anchor="nw",
            text="Algunos ejemplos son:  \nDiabetes, asma, hipertensión, anemia, etc...",
            fill="#000000",
            font=("RobotoRoman Regular", 16 * -1),
            justify = 'center'
        )

        #Rectangulo de llenado para las condiciones de salud que tenga el usuario
        self.canvas.create_rectangle(
            850.0,
            400.0,
            1200.0,
            630.0,
            fill="#EEF8FF",
            outline=""
        )
        estados_salud = CondicionesMedicas()
        lista_condiciones = estados_salud.obtener_lista_condiciones_medicas()
        self.lista_condiciones_checkbox = []
        for i in range(len(lista_condiciones)):
            self.checkbox = ttk.Checkbutton(text=lista_condiciones[i])
            if i < 7:
                self.checkbox.place(x=860,y=410+(i*30),width=120,height=30)
            else :
                self.checkbox.place(x=1020,y=410+((i-7)*30),width=180,height=30)
            self.lista_condiciones_checkbox.append(self.checkbox)


        self.window.resizable(False, False)
        self.window.mainloop()

#Funcion para abrir otro formulario
    def condiciones_usuario(lista_condiciones_checkbox):
        lista_condiciones = []
        for i in range(len(lista_condiciones_checkbox)):
            if lista_condiciones_checkbox[i].instate(['selected']):
                lista_condiciones.append(lista_condiciones_checkbox[i].cget("text"))
        return lista_condiciones
    
    def abrir_menu(self):  
        from interfaces.menu_med import MenuMed
        self.window.destroy()
        from modelos.sujetos_estudio import SujetosEstudio
        sujeto = SujetosEstudio(
            self.tipo_documento, 
            self.codigo_documento,
            self.txb_nombre.get(),
            self.txb_apellido.get(),
            self.dt_fecha_nac.get_date(),
            self.cb_sexo.get(),
            self.cb_genero.get(),
            self.cb_orientacion_sexual.get(),
            self.txb_nacionalidad.get(),
            self.cb_provincia.get(),
            fecha_creacion= datetime.datetime.now(),
            condiciones_medicas= self.condiciones_usuario(self.lista_condiciones_checkbox)
            )
        menu = MenuMed(sujeto)

    
    def abrir_login(self):  
        from interfaces.login_suj import LoginSujEstudio
        self.window.destroy()
        menu = LoginSujEstudio()


#if _name_ == '_main_':
#    registro = RegistroSujeto(1,1)