from pathlib import Path
import tkinter as tk
from tkinter import Tk, ttk, Canvas, Entry, Button, PhotoImage, messagebox, StringVar
from tkinter.font import Font
from modelos.tipo_documento import TipoDocumento

class LoginSujEstudio(tk.Frame):
    
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#FFFFFF')
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"assets/login_suj")
        
        self.controller = controller
    

    def crear_elementos_formulario(self):
        
        self.controller.title("Login Sujetos de Estudio")

        # Canvas principal de la ventana
        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 725,
            width = 1260,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        #Imagen Logo de la Aplicación
        self.imagen_logo_app = PhotoImage(file=self.relative_to_assets("logo.png"))

        self.logo_app = self.canvas.create_image(
            656.0,
            113.0,
            image=self.imagen_logo_app
        )

        # Rectangulo del pie de la interfaz
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            639.0,
            1278.0,
            730.0,
            fill="#39A9E9",
            outline=""
        )

        self.canvas.create_text(
            255.0,
            662.0,
            anchor="nw",
            text="TODOS LOS DERECHOS RESERVADOS | COPYRIGHT (C)",
            fill="#FFFFFF",
            font=("Inter", 25 * -1)
        )
        
        #Boton Acceder

        self.imagen_btn_acceder = PhotoImage(file=self.relative_to_assets("btn_acceder.png"))

        self.btn_acceder = Button(
            self,
            image=self.imagen_btn_acceder,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.abrir_registro(self.cb_tipo_doc.get(), self.txb_codigo_doc.get()),
            relief="flat",
            bg = "white"
        )

        self.btn_acceder.place(
            x=376.0,
            y=517.0,
            width=493.0,
            height=59.0
        )
        
        # Label para el combobox
        
        self.canvas.create_text(
            453.0,
            255.0,
            anchor="nw",
            text="¿Tiene cédula o pasaporte?",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )

        # Combobox para el tipo de documento
        
        tipo_documento = TipoDocumento()
        lista_tipo_documento = tipo_documento.obtener_lista_tipo_documento()
        
        self.cb_tipo_doc = ttk.Combobox(
            self,
            state = "readonly",
            value = lista_tipo_documento,
            font = ("RobotoRoman Regular", 25 * -1)  
        )

        cb_tipo_doc_fs = Font(family = "RobotoRoman Regular", size = 30) #Variable para aumentar el tamaño de las opciones en el combobox
        self.cb_tipo_doc.option_add("*TCombobox*Listbox*Font", cb_tipo_doc_fs) #Agregando una opcion para aumentar el tamaño de un listbox dentro del combobox
    
        self.cb_tipo_doc.place(
            x=421.0,
            y=298.0,
            width=404.0,
            height=52.0
        )
        
        self.cb_tipo_doc.current(0)

        # Label para el texto

        self.canvas.create_text(
            421.0,
            376.0,
            anchor="nw",
            text="Digite el código de su documento",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )

        # Textbox para el codigo de documento
        self.txb_codigo_doc = Entry(
            self,
            bd=1,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font = ("RobotoRoman Regular", 25 * -1)
        )

        self.txb_codigo_doc.bind('<Key>', self.evitar_espacio) # enlaza la función evitar_espacio a la txb_codigo_doc cada vez que se presiona una tecla en la entrada.
        
        self.txb_codigo_doc.place(
            x=420.0,
            y=416.0,
            width=404.0,
            height=52.0
        )

    # Función para comprobar que se pase un codigo de documento antes de cambiar de pantalla
    def comprobar_cod_documento(self, codigo_documento:str):
        if codigo_documento.isalnum() and len(codigo_documento) >= 9 and codigo_documento.find("ñ") == -1 and codigo_documento.find("Ñ") == -1:
            return True
        else:
            error = ""
            if not codigo_documento.isalnum():
                error += " El código del documento debe contener únicamente letras y números."
            if len(codigo_documento) < 9:
                error += " El código del documento debe tener al menos 9 caracteres."
            if codigo_documento.find("ñ") != -1 or codigo_documento.find("Ñ") != -1:
                error += " El código del documento no puede contener la letra 'ñ' o 'Ñ'."
            return False, error # Devuelve una tupla el False indicando error tiene indice [0], y el mensaje de error tiene indice [1]

    # Funcion para evitar espacios dentro del txtbox
    def evitar_espacio(self, event):
        if event.keysym == 'space':
            return 'break'    

    def abrir_registro(self, tipo_documento:str, codigo_documento:str):
        codigo_aceptado = self.comprobar_cod_documento(codigo_documento)

        if codigo_aceptado == True:
            self.controller.codigo_documento = codigo_documento.upper()
            self.controller.tipo_documento = tipo_documento
            self.controller.show_frame("RegistroSujeto")
        else:
            # Canvas cuando el codigo de documento esté vacío
            self.txt_codigo_doc = Canvas(
                self,
                bg = "#FFFFFF",
                height = 25,
                width = 20,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )
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
            messagebox.showwarning("Rellene el formulario", codigo_aceptado[1])  
        