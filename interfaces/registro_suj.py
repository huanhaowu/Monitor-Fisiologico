from pathlib import Path
from modelos.tipo_documento import TipoDocumento
from modelos.nacionalidad import Nacionalidad
from modelos.genero import Genero
from modelos.sexo import Sexo
from modelos.provincia import Provincia
from modelos.orientacion_sexual import OrientacionSexual
from modelos.condiciones_medicas import CondicionesMedicas 
from modelos.sujetos_estudio import SujetosEstudio

from tkinter import Tk, Canvas, Entry, Button, PhotoImage, ttk,BooleanVar,StringVar,Checkbutton,messagebox
from tkcalendar import DateEntry
import os
import datetime
import re

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/registro_suj")
TAMANO_FUENTE = 16 # (ARREGLADO)Arreglo - esta variable debe declararse como constante y escribirse en mayusculas
FORMFECHA = str("%Y-%m-%d")
POS_X_LABELS = 45
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class RegistroSujeto():
    def __init__(self, tipo_documento, codigo_documento):
        self.tipo_documento = tipo_documento
        self.codigo_documento = codigo_documento
        
        self.window = Tk()
        self.window.geometry("1260x725+{}+{}".format(self.window.winfo_screenwidth() // 2 - 1260 // 2, self.window.winfo_screenheight() // 2 - 725 // 2))
        self.window.configure(bg = "#FFFFFF")
        self.window.title("Registro de Sujeto")
    
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
    #endregion    

        #(Arreglado)Arreglo - Usa los "region" para agrupar las secciones que defines
    #region // Botón Regresar
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
    #endregion

    #region // Botón Siguiente

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
    #endregion
        
    #region // Labels y Campos de la sección principal de registro de datos
        """
        ------------------ LABELS Y CAMPOS ------------------
        """

        #-------------------- COD DOCUMENTO -------------------
        #Label del Codigo de Documento
        self.canvas.create_text(
            POS_X_LABELS,
            171.0,
            anchor="nw",
            text="Código de\nDocumento",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'left'
        )
        #Textbox del Codigo de Documento
        var = StringVar(value=self.codigo_documento)
        #(Arreglado)Arreglo - Todo el codigo que no estes utilizando borralo
        self.txb_codigo_doc = Entry(
            bd=1,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            state = "disabled",
            textvariable = var,
            font=("RobotoRoman Regular", TAMANO_FUENTE -1)
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
        td = TipoDocumento()
        #Combobox del Tipo de Documento
        self.cb_tipo_doc = ttk.Combobox(
            state = "disabled",
            values = td.obtener_lista_tipo_documento(),
            font=("RobotoRoman Regular", TAMANO_FUENTE -1)
        )

        #Colocar el valor por defecto de tipo documento
        self.cb_tipo_doc.current(0)

        td.descripcion = self.tipo_documento
        td.cargar_id_tipo_documento()
        self.cb_tipo_doc.current(td.id_tipo_documento-1)
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
            45.0,
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
            highlightthickness=0,
            font=("RobotoRoman Regular", TAMANO_FUENTE -1)
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
            highlightthickness=0,
            font=("RobotoRoman Regular", TAMANO_FUENTE -1)
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
        self.dt_fecha_nac = DateEntry() 

        #localización del datetimepicker de la fecha de nacimiento
        self.dt_fecha_nac.config(maxdate = maxdate,firstweekday = 'sunday',font=("RobotoRoman Regular", TAMANO_FUENTE -1))
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
            value = [var[1] for var in sexo.obtener_lista_sexos()],
            font=("RobotoRoman Regular", TAMANO_FUENTE -1)
        )
        #Colocar el valor por defecto de sexo
        self.cb_sexo.current(0)

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
            POS_X_LABELS,
            489.0,
            anchor="nw",
            text="Nacionalidad",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'center'
        )
        nacionalidad = Nacionalidad()
        #ComboBox de nacionalidad
        self.cb_nacionalidad = ttk.Combobox(
            state = "readonly",
            values = [var[1] for var in nacionalidad.obtener_lista_nacionalidades()],
            font=("RobotoRoman Regular", TAMANO_FUENTE -1)
        )

        #Colocar el valor por defecto de nacionalidad
        self.cb_nacionalidad.current(0)

        #Localización del combobox de nacionalidad
        self.cb_nacionalidad.place(
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
            values = [var[1] for var in provincia.obtener_lista_provincias()],
            font=("RobotoRoman Regular", TAMANO_FUENTE -1)
        )

        #Colocar el valor por defecto de provincia
        self.cb_provincia.current(0)

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
            state = "readonly",
            values = [var[1] for var in genero.obtener_lista_generos()],
            font=("RobotoRoman Regular", TAMANO_FUENTE -1)
        )

        #Colocar el valor por defecto de genero
        self.cb_genero.current(0)
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
            text="Orientación\n Sexual",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'center'
        )
        orientacion = OrientacionSexual()
        #ComboBox de Orientacion Sexual
        self.cb_orientacion_sexual = ttk.Combobox(
        state = "readonly",
        values = [var[1] for var in orientacion.obtener_lista_orientaciones()],
        font=("RobotoRoman Regular", TAMANO_FUENTE -1)
        )
        
        #Localización del combobox de orientacion sexual
        self.cb_orientacion_sexual.place(
            x=561.0,
            y=583.0,
            width=178.0,
            height=34.0
        )

        #Colocar el valor por defecto de orientacion sexual
        self.cb_orientacion_sexual.current(0)
        
        """
        #-------------------- Correo Electronico -------------------
        """
        #Label principal de la sección de Correo Electronico
        self.canvas.create_text(
            910.0,
            126.0,
            anchor="nw",
            text="Correo Electrónico",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1),
            justify = 'center'
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

        #-------------------- CORREO ELECTRONICO -------------------
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

        #CheckBox de correo electronico
        self.txb_correo = Entry(
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
    #endregion

        self.window.option_add('*TCombobox*Listbox.font', '24') #Aumentar el tamaño de las listas de los drop down 
        self.window.option_add('*TCombobox*Listbox.height', '24')

    #region // Labels y Campos de la sección de Condiciones de Salud
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
        self.lista_condiciones = estados_salud.obtener_lista_condiciones_medicas()
        self.lista_condiciones_checkbox = []
        self.lista_valoresbool_checkbox = [BooleanVar() for i in range(len(self.lista_condiciones))]
        self.sujeto_existe = SujetosEstudio(tipo_documento, codigo_documento) #(ARREGLADO)Arreglo - Colocar underscore para separar las dos palabras sujeto_existe
        if(self.sujeto_existe.ingresar() == True):
            self.buscar_usuario_existente() #(Arreglado)Arreglo - Las funciones deben comenzar por un verbo
            
        numCond = len(self.lista_condiciones)
        for i in range(numCond):
            self.checkbox = Checkbutton(text=(self.lista_condiciones[i])[1], variable=self.lista_valoresbool_checkbox[i],bg="#EEF8FF",font=("RobotoRoman Regular", 13 * -1))
            if i < numCond/2:
                self.checkbox.place(x=860,y=410+(i*30),width=120,height=30)
            else :
                self.checkbox.place(x=1020,y=410+((i-round(numCond/2))*30),width=180,height=30)
            self.lista_condiciones_checkbox.append(self.checkbox)

        self.window.resizable(False, False)
        self.window.mainloop()
    #endregion


#Funcion asignar las condiciones medicas del usuario 1.0 
    def obtener_condiciones_usuario(self): #(Arreglado)Arreglo - Las funciones deben comenzar con un verbo en infinitivo
        lista_obtener_condiciones_usuario = []
        for i in range(len(self.lista_condiciones_checkbox)):
            if self.lista_valoresbool_checkbox[i].get() == True:
                lista_obtener_condiciones_usuario.append(int(i+1))
        return lista_obtener_condiciones_usuario

#region // Funcion para rellenar los campos con los de un usuario existente
    def buscar_usuario_existente(self): #(Arreglado)Arreglo - Las funciones deben comenzar con un verbo en infinitivo
         self.txb_nombre.insert(0, self.sujeto_existe.nombres)
         self.txb_apellido.insert(0, self.sujeto_existe.apellidos)
         self.dt_fecha_nac.set_date(datetime.datetime.strptime(str(self.sujeto_existe.fecha_nacimiento),FORMFECHA))
         self.cb_sexo.current(int(self.sujeto_existe.sexo.id_sexo)-1)
         self.txb_correo.insert(0, self.sujeto_existe.correo)
         self.cb_genero.current(int(self.sujeto_existe.genero.id_genero)-1)
         self.cb_orientacion_sexual.current(int(self.sujeto_existe.orientacion_sexual.id_orientacion_sexual)-1),
         self.cb_nacionalidad.current(int(self.sujeto_existe.nacionalidad.id_nacionalidad)-1)
         self.cb_provincia.current(int(self.sujeto_existe.provincia.id_provincia)-1)
         #Arreglo - Documenta mejor esta parte del codigo
         j = 0
         if(len(self.sujeto_existe.condiciones_medicas)>0):
            for i in range(len(self.lista_condiciones)):
                if(self.sujeto_existe.condiciones_medicas[j].id_condicion_medica == (i+1)):
                    self.lista_valoresbool_checkbox[i].set(True)
                    j+=1
                    if(j == len(self.sujeto_existe.condiciones_medicas)):
                        break

    def alertar_texto_vacio(self): #(Arreglado)Arreglo - Las funciones deben comenzar por un verbo
        retornar = True
        if (self.txb_nombre.get().isspace() or self.txb_nombre.get() == "" ): #este if valida si el texto esta vacio
            self.txt_codigo_doc = Canvas(
                self.window,
                bg = "#FFFFFF",
                height = 25,
                width = 20,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )
            #Posicionando el canva
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
        if (self.txb_apellido.get().isspace() or self.txb_apellido.get() == "" or self.txb_apellido.get().isspace() or self.txb_apellido.get() == ""): #este if valida si el texto esta vacio
            self.txt_codigo_doc = Canvas(
                self.window,
                bg = "#FFFFFF",
                height = 25,
                width = 20,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )
            #Posicionando el canva
            
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

#endregion

    def verificar_correo_electronico(self): 
        if(self.txb_correo.get() !="" and self.txb_correo.get().isspace() == False):
               patron =  r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
               resultado = re.match(patron, self.txb_correo.get())
               if(resultado):
                    return True
               else:
                    self.txt_codigo_doc = Canvas(
                        self.window,
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
            
#region // Funcion para abrir otro formulario
    def abrir_menu(self):  
        if(self.alertar_texto_vacio() == True and self.verificar_correo_electronico() == True):
            #self.window.destroy()
            from interfaces.menu_med import MenuMed
            sujeto = SujetosEstudio(self.tipo_documento, self.codigo_documento)
            sujeto.nombres = " ".join(self.txb_nombre.get().split())
            sujeto.apellidos = " ".join(self.txb_apellido.get().split())
            sujeto.fecha_nacimiento = self.dt_fecha_nac.get_date()
            sujeto.sexo = self.cb_sexo.current() + 1
            sujeto.genero = self.cb_genero.current() + 1
            sujeto.orientacion_sexual = self.cb_orientacion_sexual.current() + 1
            sujeto.nacionalidad = self.cb_nacionalidad.current() + 1
            sujeto.provincia = self.cb_provincia.current() + 1
            sujeto.correo = self.txb_correo.get()
            if(sujeto.correo.isspace()):
                sujeto.correo = ""
            sujeto.registrar(sujeto.nombres, sujeto.apellidos, sujeto.fecha_nacimiento, sujeto.sexo, sujeto.genero, sujeto.orientacion_sexual, sujeto.nacionalidad, sujeto.provincia, sujeto.correo, self.obtener_condiciones_usuario())
            self.window.destroy()
            menu = MenuMed(sujeto)
#endregion

    def abrir_login(self):  
        from interfaces.login_suj import LoginSujEstudio
        self.window.destroy()
        menu = LoginSujEstudio()