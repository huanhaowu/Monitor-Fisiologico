from pathlib import Path

# Librerias de Tkinter
import tkinter as tk
from tkinter import Canvas, Entry, Button, PhotoImage, ttk, BooleanVar, StringVar, Checkbutton, messagebox
from tkcalendar import DateEntry

import datetime # Libreria de fecha y hora
import re # Libreria de expresiones regulares

# Modelos de datos
from modelos.tipo_documento import TipoDocumento
from modelos.nacionalidad import Nacionalidad
from modelos.genero import Genero
from modelos.sexo import Sexo
from modelos.provincia import Provincia
from modelos.orientacion_sexual import OrientacionSexual
from modelos.condiciones_medicas import CondicionesMedicas 
from modelos.sujetos_estudio import SujetosEstudio

# Contantes de la interfaz
TAMANO_FUENTE = 16
FORMFECHA = str("%Y-%m-%d")
POS_X_LABELS = 45


class RegistroSujeto(tk.Frame):
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#FFFFFF')
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"assets/registro_suj")
        
        self.controller = controller
    
    def crear_elementos_formulario(self):
        self.controller.title("Registro de Sujeto")
    
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
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1335.0,
            91.0,
            fill="#39A9E9",
            outline="")
        
        #Titulo del formulario
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
    

        # region // Botón Regresar
        self.btn_img_regresar = PhotoImage(
            file=self.relative_to_assets("btn_regresar.png"))

        self.btn_regresar = Button(
            self,
            image=self.btn_img_regresar,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.abrir_login(),
            relief="flat",
            bg = "#39A9E9"
        )

        self.btn_regresar.place(
            x=30.0,
            y=22.0,
            width=48.0,
            height=47.0
        )
        # endregion

        #region // Botón Siguiente

        self.btn_imagen_siguiente = PhotoImage(
            file=self.relative_to_assets("btn_siguiente.png"))

        self.btn_siguiente = Button(
            self,
            image=self.btn_imagen_siguiente,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.abrir_menu(),
            relief="flat"
        )

        self.btn_siguiente.place(
            x=857.0,
            y=656.0,
            width=411.851318359375,
            height=68.0
        )
        #endregion
        

        # region // Textbox del Codigo de Documento

        # Label del Codigo de Documento
        self.canvas.create_text(
            POS_X_LABELS,
            171.0,
            anchor="nw",
            text="Código de\nDocumento",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'left'
        )
        
        var = StringVar(value=self.controller.codigo_documento)

        self.txb_codigo_doc = Entry(
            self,
            bd=1,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            state = "disabled",
            textvariable = var,
            font=("RobotoRoman Regular", TAMANO_FUENTE -1)
        )

        self.txb_codigo_doc.place(
            x=204.0,
            y=184.0,
            width=165.0,
            height=34.0
        )

        # endregion

        # region // Combobox del Tipo de Documento
        
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
        td = TipoDocumento()

        self.cb_tipo_doc = ttk.Combobox(
            self,
            state = "disabled",
            values = td.obtener_lista_tipo_documento(),
            font=("RobotoRoman Regular", TAMANO_FUENTE -1)
        )

        self.cb_tipo_doc.current(0)

        td.descripcion = self.controller.tipo_documento
        td.cargar_id_tipo_documento()
        
        self.cb_tipo_doc.current(td.id_tipo_documento-1)

        self.cb_tipo_doc.place(
            x=561.0,
            y=184.0,
            width=178.0,
            height=34.0
        )

        # endregion

        # region // Textbox del Nombre


        #Label del Nombre
        self.canvas.create_text(
            45.0,
            276.0,
            anchor="nw",
            text="Nombre",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'center'
        )

        self.txb_nombre = Entry(            
            self,
            bd=1,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("RobotoRoman Regular", TAMANO_FUENTE -1)
        )

        self.txb_nombre.place(
            x=204.0,
            y=274.0,
            width=165.0,
            height=34.0
        )

        # endregion

        # region // Textbox del Apellido
        # #Label del Apellido
        self.canvas.create_text(
            420.0,
            276.0,
            anchor="nw",
            text="Apellido",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'center'
        )

        self.txb_apellido = Entry(
            self,
            bd=1,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("RobotoRoman Regular", TAMANO_FUENTE -1)
        )
        self.txb_apellido.place(
            x=561.0,
            y=276.0,
            width=178.0,
            height=34.0
        )
        # endregion

        # region // DateTimePicker de la Fecha de Nacimiento

        #Label de la Fecha de Nacimiento
        self.canvas.create_text(
            POS_X_LABELS,
            358.0,
            anchor="nw",
            text="Fecha de\nNacimiento",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'left'
        )
        
        #Definir el día máximo de selección en el DT
        maxdate = datetime.date.today()

        #Datetimepicker de la Fecha de Nacimiento  
        self.dt_fecha_nac = DateEntry(self) 

        self.dt_fecha_nac.config(maxdate = maxdate,firstweekday = 'sunday',font=("RobotoRoman Regular", TAMANO_FUENTE -1))
        self.dt_fecha_nac.place(
            x=204.0,
            y=374.0,
            width=165.0,
            height=34.0
        )
        # endregion

        # region // Combobox del Sexo
        
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
        self.cb_sexo = ttk.Combobox(
            self,
            state = "readonly",
            value = [var[1] for var in sexo.obtener_lista_sexos()],
            font=("RobotoRoman Regular", TAMANO_FUENTE -1)
        )
        #Colocar el valor por defecto de sexo
        self.cb_sexo.current(0)

        self.cb_sexo.place(
            x=561.0,
            y=374.0,
            width=178.0,
            height=34.0
        )

        # endregion

        # region // Combobox de la Nacionalidad
        # Label de la Nacionalidad
        self.canvas.create_text(
            POS_X_LABELS,
            489.0,
            anchor="nw",
            text="Nacionalidad",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'center'
        )
        nacionalidad = Nacionalidad()

        self.cb_nacionalidad = ttk.Combobox(
            self,
            state = "readonly",
            values = [var[1] for var in nacionalidad.obtener_lista_nacionalidades()],
            font=("RobotoRoman Regular", TAMANO_FUENTE -1)
        )

        #Colocar el valor por defecto de nacionalidad
        self.cb_nacionalidad.current(0)

        self.cb_nacionalidad.place(
            x=204.0,
            y=485.0,
            width=165.0,
            height=35.0
        )

        # endregion

        # region // Combobox de la Provincia
        
        # Label de la Provincia
        self.canvas.create_text(
            410.0,
            488.0,
            anchor="nw",
            text="Provincia",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )
        provincia = Provincia()

        self.cb_provincia = ttk.Combobox(            
            self,
            state = "readonly",
            values = [var[1] for var in provincia.obtener_lista_provincias()],
            font=("RobotoRoman Regular", TAMANO_FUENTE -1)
        )

        #Colocar el valor por defecto de provincia
        self.cb_provincia.current(0)

        self.cb_provincia.place(
            x=561.0,
            y=481.0,
            width=178.0,
            height=35.0
        )

        # endregion

        # region // Combobox del Genero

        #Label del Genero
        self.canvas.create_text(
            POS_X_LABELS,
            582.0,
            anchor="nw",
            text="Género",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1) ,
            justify = 'center'
        )
        genero = Genero()
        #ComboBox de genero
        self.cb_genero = ttk.Combobox(
            self,
            state = "readonly",
            values = [var[1] for var in genero.obtener_lista_generos()],
            font=("RobotoRoman Regular", TAMANO_FUENTE -1)
        )

        #Colocar el valor por defecto de genero
        self.cb_genero.current(0)
        self.cb_genero.place(
            x=204.0,
            y=582.0,
            width=165.0,
            height=35.0
        )

        # endregion

        # region // Combobox de la Orientacion Sexual

        #Label de la Orientacion Sexual
        self.canvas.create_text(
            400.0,
            573.0,
            anchor="nw",
            text="Orientación\n Sexual",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'center'
        )
        orientacion = OrientacionSexual()

        self.cb_orientacion_sexual = ttk.Combobox(
        self,
        state = "readonly",
        values = [var[1] for var in orientacion.obtener_lista_orientaciones()],
        font=("RobotoRoman Regular", TAMANO_FUENTE -1)
        )
        
        self.cb_orientacion_sexual.place(
            x=561.0,
            y=583.0,
            width=178.0,
            height=34.0
        )

        #Colocar el valor por defecto de orientacion sexual
        self.cb_orientacion_sexual.current(0)
        # endregion

                
        # region // Textbox del correo electronico
        # Label del correo electronico
        self.canvas.create_text(
            910.0,
            126.0,
            anchor="nw",
            text="Correo Electrónico",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'center'
        )

        self.txb_correo = Entry(
            self,
            bd=1,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("RobotoRoman Regular", TAMANO_FUENTE -1)
        )
        self.txb_correo.place(
            x= 990.0,
            y= 235.0,
            width= 220.0,
            height=43.0
        )

        #Label de las opciones de los habitos de consumo
        self.canvas.create_text(
            850.0,
            168.0,
            anchor="nw",
            text="Ingrese el correo electrónico por defecto \nde su usuario:",
            fill="#000000",
            font=("RobotoRoman Regular", 20 * -1),
            justify = 'center'
        )

        #Label de correo electronico
        self.canvas.create_text(
            830.0,
            230.0,
            anchor="nw",
            text="Correo\n Electronico",
            fill="#000000",
            font=("RobotoRoman Regular", 22 * -1),
            justify = 'center'
        )

        
        #endregion

        self.option_add('*TCombobox*Listbox.font', '24') #Aumentar el tamaño de las listas de los drop down 
        self.option_add('*TCombobox*Listbox.height', '24')

        # region Sección de Condiciones de Salud
        # Label de Condiciones de Salud
        self.canvas.create_text(
            850.0,
            311.0,
            anchor="nw",
            text="¿Posee alguna condición de salud?",
            fill="#000000",
            font=("RobotoRoman Regular", 20 * -1),
            justify = 'center'
        )
        # Label de los ejemplos de condiciones de salud
        self.canvas.create_text(
            860.0,
            350.0,
            anchor="nw",
            text="Algunos ejemplos son:  \nDiabetes, asma, hipertensión, anemia, etc...",
            fill="#000000",
            font=("RobotoRoman Regular", 16 * -1),
            justify = 'center'
        )

        # Rectangulo de llenado para las condiciones de salud que tenga el usuario
        self.canvas.create_rectangle(
            850.0,
            400.0,
            1200.0,
            630.0,
            fill="#EEF8FF",
            outline=""
        )
        condiciones_salud = CondicionesMedicas()
        self.lista_condiciones = condiciones_salud.obtener_lista_condiciones_medicas()
        self.lista_condiciones_checkbox = []
        self.lista_valoresbool_checkbox = [BooleanVar() for i in range(len(self.lista_condiciones))]

        # endregion

        
        # Rellenado de los datos de un sujeto de estudio existente
        self.sujeto_existe = SujetosEstudio(self.controller.tipo_documento, self.controller.codigo_documento)
        
        if(self.sujeto_existe.ingresar() == True):
            self.buscar_sujeto_existente()
            
        numCond = len(self.lista_condiciones)
        for i in range(numCond):
            self.checkbox = Checkbutton(self, text=(self.lista_condiciones[i])[1], variable=self.lista_valoresbool_checkbox[i],bg="#EEF8FF",font=("RobotoRoman Regular", 13 * -1))
            if i < numCond/2:
                self.checkbox.place(x=860,y=410+(i*30),width=120,height=30)
            else :
                self.checkbox.place(x=1020,y=410+((i-round(numCond/2))*30),width=180,height=30)
            self.lista_condiciones_checkbox.append(self.checkbox)

    #Funcion asignar las condiciones medicas del usuario 1.0 
    def obtener_condiciones_sujeto(self):
        lista_obtener_condiciones_sujeto = []
        for i in range(len(self.lista_condiciones_checkbox)):
            if self.lista_valoresbool_checkbox[i].get() == True:
                lista_obtener_condiciones_sujeto.append(int(i+1))
        return lista_obtener_condiciones_sujeto

    # Funcion para rellenar los campos con los de un usuario existente
    def buscar_sujeto_existente(self):
        # Rellenando los datos de los sujetos de estudio
        self.txb_nombre.insert(0, self.sujeto_existe.nombres)
        self.txb_apellido.insert(0, self.sujeto_existe.apellidos)
        self.dt_fecha_nac.set_date(datetime.datetime.strptime(str(self.sujeto_existe.fecha_nacimiento),FORMFECHA))
        self.cb_sexo.current(int(self.sujeto_existe.sexo.id_sexo)-1)
        self.txb_correo.insert(0, self.sujeto_existe.correo)
        self.cb_genero.current(int(self.sujeto_existe.genero.id_genero)-1)
        self.cb_orientacion_sexual.current(int(self.sujeto_existe.orientacion_sexual.id_orientacion_sexual)-1),
        self.cb_nacionalidad.current(int(self.sujeto_existe.nacionalidad.id_nacionalidad)-1)
        self.cb_provincia.current(int(self.sujeto_existe.provincia.id_provincia)-1)
        j = 0
        # Marcando las condiciones de salud de ese usuario
        if(len(self.sujeto_existe.condiciones_medicas)>0):
            for i in range(len(self.lista_condiciones)):
                if(self.sujeto_existe.condiciones_medicas[j].id_condicion_medica == (i+1)):
                    self.lista_valoresbool_checkbox[i].set(True)
                    j+=1
                    if(j == len(self.sujeto_existe.condiciones_medicas)):
                        break

    # Funcion para indicar que existe un texto vacio
    def alertar_texto_vacio(self): 
        retornar = True
        if (self.txb_nombre.get().isspace() or self.txb_nombre.get() == "" ): # Este if valida si el texto esta vacio
            self.txt_codigo_doc = Canvas(
                self,
                bg = "#FFFFFF",
                height = 25,
                width = 20,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            self.txt_codigo_doc.place(x = 22, y = 278)
            self.txt_codigo_doc.create_rectangle(
                0.0,
                0.0,
                20.0,
                25.0,
                fill = "#FFFFFF",
                outline = ""
            )
            #Asterisco
            self.txt_codigo_doc.create_text(
                2.0,
                0.0,
                anchor = "nw",
                fill = "red",
                text = "*",
                font = ("RobotoRoman Bold", 35 * -1),
                justify= 'center',
            )
            retornar = False
        if (self.txb_apellido.get().isspace() or self.txb_apellido.get() == "" or self.txb_apellido.get().isspace() or self.txb_apellido.get() == ""): # Este if valida si el texto esta vacio
            self.txt_codigo_doc = Canvas(
                self,
                bg = "#FFFFFF",
                height = 25,
                width = 20,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )
            
            self.txt_codigo_doc.place(x = 400, y = 278)
            self.txt_codigo_doc.create_rectangle(
                0.0,
                0.0,
                20.0,
                25.0,
                fill = "#FFFFFF",
                outline = ""
            )
            #Asterisco
            self.txt_codigo_doc.create_text(
                2.0,
                0.0,
                anchor = "nw",
                fill = "red",
                text = "*",
                font = ("RobotoRoman Bold", 35 * -1),
                justify= 'center',
            )
            retornar = False
        
        if retornar == False:
            messagebox.showwarning("ALERTA", "Ha dejado campos vacios. Recuerde que tiene que llenar todos los campos. \n\nNOTA: Las condiciones medicas pueden quedar vacias. \n\nIngréselos para continuar.")
        return retornar

    def verificar_correo_electronico(self): 
        if(self.txb_correo.get() !="" and self.txb_correo.get().isspace() == False):
               patron =  r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
               resultado = re.match(patron, self.txb_correo.get())
               if(resultado):
                    return True
               else:
                    self.txt_codigo_doc = Canvas(
                        self,
                        bg = "#FFFFFF",
                        height = 25,
                        width = 20,
                        bd = 0,
                        highlightthickness = 0,
                        relief = "ridge"
                    )
                    #Posicionando el canva

                    self.txt_codigo_doc.place(x = 967, y = 245)
                    self.txt_codigo_doc.create_rectangle(
                        0.0,
                        0.0,
                        20.0,
                        25.0,
                        fill = "#FFFFFF",
                        outline = ""
                    )
                    #Asterisco
                    self.txt_codigo_doc.create_text(
                        2.0,
                        0.0,
                        anchor = "nw",
                        fill = "red",
                        text = "*",
                        font = ("RobotoRoman Bold", 35 * -1),
                        justify= 'center',
                    )
                    messagebox.showwarning("ALERTA", "El correo electronico no es valido. \n\nPor favor ingrese un correo electronico valido.")
                    return False
        return True
            
    # Funcion para abrir el Menu de Mediciones
    def abrir_menu(self):  
        if(self.alertar_texto_vacio() == True and self.verificar_correo_electronico() == True):
            self.controller.sujeto = SujetosEstudio(self.controller.tipo_documento, self.controller.codigo_documento)
            self.controller.sujeto.nombres = " ".join(self.txb_nombre.get().split())
            self.controller.sujeto.apellidos = " ".join(self.txb_apellido.get().split())
            self.controller.sujeto.fecha_nacimiento = self.dt_fecha_nac.get_date()
            self.controller.sujeto.sexo = self.cb_sexo.current() + 1
            self.controller.sujeto.genero = self.cb_genero.current() + 1
            self.controller.sujeto.orientacion_sexual = self.cb_orientacion_sexual.current() + 1
            self.controller.sujeto.nacionalidad = self.cb_nacionalidad.current() + 1
            self.controller.sujeto.provincia = self.cb_provincia.current() + 1
            self.controller.sujeto.correo = self.txb_correo.get()
            if(self.controller.sujeto.correo.isspace()):
                self.controller.sujeto.correo = ""
            self.controller.sujeto.registrar(
                self.controller.sujeto.nombres, 
                self.controller.sujeto.apellidos, 
                self.controller.sujeto.fecha_nacimiento, 
                self.controller.sujeto.sexo, 
                self.controller.sujeto.genero, 
                self.controller.sujeto.orientacion_sexual, 
                self.controller.sujeto.nacionalidad, 
                self.controller.sujeto.provincia, 
                self.controller.sujeto.correo, 
                self.obtener_condiciones_sujeto())
            
            #self.controller.show_frame("MenuMediciones")

    def abrir_login(self):  
        self.controller.tipo_documento = ""
        self.controller.codigo_documento = ""
        self.controller.show_frame("LoginSujEstudio")