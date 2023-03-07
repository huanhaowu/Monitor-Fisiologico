from pathlib import Path
from tkinter import Tk, ttk, Canvas, Entry, Text, Button, PhotoImage, StringVar
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
        #Canvas
        self.canvas = Canvas(
            self.window,
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
            639.0,
            1278.0,
            730.0,
            fill="#39A9E9",
            outline=""
        )

        self.canvas.create_text(
            453.0,
            255.0,
            anchor="nw",
            text="¿Tiene cédula o pasaporte?",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )

        self.canvas.create_text(
            421.0,
            376.0,
            anchor="nw",
            text="Digite el código de su documento",
            fill="#000000",
            font=("RobotoRoman Regular", 25 * -1)
        )

        self.canvas.create_text(
            255.0,
            662.0,
            anchor="nw",
            text="TODOS LOS DERECHOS RESERVADOS | COPYRIGHT (C)",
            fill="#FFFFFF",
            font=("Inter", 25 * -1)
        )

        #Imagen Boton Acceder
        self.imagen_btn_acceder = PhotoImage(file=relative_to_assets("button_1.png"))
        #Prppieades del boton acceder
        self.btn_acceder = Button(
            image=self.imagen_btn_acceder,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.abrir_registro(self.cb_tipo_doc.get(), self.txb_codigo_doc.get()),
            relief="flat",
            bg = "white"
        )
        #Localización del boton acceder
        self.btn_acceder.place(
                x=376.0,
                y=517.0,
                width=493.0,
                height=59.0
            )
        #Imagen Logo de la Aplicación
        self.imagen_logo_app = PhotoImage(file=relative_to_assets("image_1.png"))
        #Localización del logo de la aplicación
        self.logo_app = self.canvas.create_image(
            656.0,
            113.0,
            image=self.imagen_logo_app
        )

        #Inicializando variable para obtener lista de tipo_documento permitidos
        tipo_documento = td()
        lista_tipo_documento = tipo_documento.obtener_lista_tipo_documento()

        #Aqui va el ComboBox para el tipo de documento
        self.cb_tipo_doc = ttk.Combobox(
            state = "readonly",
            value = lista_tipo_documento,
            font = ("RobotoRoman Regular", 25 * -1)
        )

        #Provocando que el documento inicial sea la cedula
        self.cb_tipo_doc.current(0)

        #Locación del ComboBox para el tipo de documento
        self.cb_tipo_doc.place(
            x=421.0,
            y=298.0,
            width=404.0,
            height=52.0
        )
        
        #Aqui va el textbox para el codigo de documetno
        self.txb_codigo_doc = Entry(
            bd=1,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font = ("RobotoRoman Regular", 25 * -1)
        )
        
        #Localización del textbox para el codigo de documento
        self.txb_codigo_doc.place(
            x=420.0,
            y=416.0,
            width=404.0,
            height=52.0
        )

        self.window.resizable(False, False)
        self.window.mainloop()

    
    def abrir_registro(self, id_tipo_documento = 0, descripcion = ""):
        from interfaces.registro_suj import RegistroSujeto as rs
        self.window.destroy()
        rs(id_tipo_documento,descripcion)
        
    
        