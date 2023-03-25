from pathlib import Path
from tkinter import Tk, ttk, Canvas, Entry, Button, PhotoImage, messagebox, StringVar
from tkinter.font import Font
from modelos.tipo_documento import TipoDocumento as td



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/login_suj")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class LoginSujEstudio():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1260x725+{}+{}".format(self.window.winfo_screenwidth() // 2 - 1260 // 2, self.window.winfo_screenheight() // 2 - 725 // 2))
        self.window.configure(bg = "#FFFFFF")
        self.window.title("Login Sujetos de Estudio")
        #Arreglo - Agrupa los controles del formulario en secciones por tipo, es decir, pon todos los botones en un solo lado, todos los textos en otro. Esto con el objetivo facilitar los arreglos
        #Arreglo - Usa los "region" para definir las secciones de los controles

        #INICIALIZACION DE VARIABLES
        #Inicializando canvas principal de la ventana
        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 725,
            width = 1260,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        #Imagen Boton Acceder
        self.imagen_btn_acceder = PhotoImage(file=relative_to_assets("button_1.png"))

        #Inicializando boton "Acceder"
        self.btn_acceder = Button(
            image=self.imagen_btn_acceder,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.abrir_registro(self.cb_tipo_doc.get(), self.txb_codigo_doc.get()),
            relief="flat",
            bg = "white"
        )

        #Imagen Logo de la Aplicación
        self.imagen_logo_app = PhotoImage(file=relative_to_assets("image_1.png"))

        #Inicializando variable para obtener lista de tipo_documento permitidos
        tipo_documento = td()
        lista_tipo_documento = tipo_documento.obtener_lista_tipo_documento()

        #Inicializacion Combobox para el tipo de documento
        self.cb_tipo_doc = ttk.Combobox(
            state = "readonly",
            value = lista_tipo_documento,
            font = ("RobotoRoman Regular", 25 * -1)  
        )

        cb_tipo_doc_fs = Font(family = "RobotoRoman Regular", size = 30) #Variable para aumentar el tamaño de las opciones en el combobox
        self.cb_tipo_doc.option_add("*TCombobox*Listbox*Font", cb_tipo_doc_fs) #Agregando una opcion para aumentar el tamaño de un listbox dentro del combobox
    

        #Inicializacion del textbox para el numero de documento
        self.txb_codigo_doc = Entry(
            bd=1,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font = ("RobotoRoman Regular", 25 * -1)
        )

        #UBICACIONES
        #Ubicacion del canvas principal
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            639.0,
            1278.0,
            730.0,
            fill="#39A9E9",
            outline=""
        )

        #Ubicacion del logo de la aplicación
        self.logo_app = self.canvas.create_image(
            656.0,
            113.0,
            image=self.imagen_logo_app
        )

        #Ubicacion del boton acceder
        self.btn_acceder.place(
            x=376.0,
            y=517.0,
            width=493.0,
            height=59.0
        )

         #Ubicacion del ComboBox para el tipo de documento
        self.cb_tipo_doc.place(
            x=421.0,
            y=298.0,
            width=404.0,
            height=52.0
        )
        
        #Ubicacion del textbox para el codigo de documento
        self.txb_codigo_doc.place(
            x=420.0,
            y=416.0,
            width=404.0,
            height=52.0
        )

        #TEXTOS
        #Pregunta acerca del tipo de documento
        self.canvas.create_text(
            453.0,
            255.0,
            anchor="nw",
            text="¿Tiene cédula o pasaporte?",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )

        #Solicitud para ingresar el numero de documento
        self.canvas.create_text(
            421.0,
            376.0,
            anchor="nw",
            text="Digite el código de su documento",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )

        #Texto extra
        self.canvas.create_text(
            255.0,
            662.0,
            anchor="nw",
            text="TODOS LOS DERECHOS RESERVADOS | COPYRIGHT (C)",
            fill="#FFFFFF",
            font=("Inter", 25 * -1)
        )
        
        #PROCESOS
        #Provocando que el documento inicial sea la cedula
        self.cb_tipo_doc.current(0)
        
        self.window.resizable(False, False)
        self.window.mainloop()
        
    def abrir_registro(self, id_tipo_documento:int, descripcion:str):
        from interfaces.registro_suj import RegistroSujeto as rs
        codigo_aceptado = self.comprobar_cod_documento(descripcion)
        if codigo_aceptado == True:
            self.window.destroy()
            descripcion = descripcion.upper()
            rs(id_tipo_documento,descripcion)
        else:
            #Creacion de canva cuando el codigo de documento esté vacío
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
            self.txt_codigo_doc.place(x = 400, y = 426)
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
            messagebox.showwarning("Rellene el formulario", "Ingrese el código de su documento")

    # Función para comprobar que se pase un codigo de documento antes de cambiar de pantalla
    def comprobar_cod_documento(self, codigo_documento:str):
        if codigo_documento.isalnum() == True and len(codigo_documento) >= 9 and codigo_documento.find("ñ") == -1 and codigo_documento.find("Ñ") == -1:
            return True
        else:
            return False
                
        