import tkinter as tk
from interfaces.login_suj import LoginSujEstudio
from interfaces.menu_med import MenuMed
from interfaces.registro_suj import RegistroSujeto
from interfaces.reporte_med import ReporteMed 
from modelos.sujetos_estudio import SujetosEstudio
from modelos.mediciones_sujeto import MedicionesSujeto

class Contenedor(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        # region // Variables compartidas entre formulario

        self.tipo_documento = ""
        self.codigo_documento = ""

        self.sujeto = None
        self.medicion = None

        # endregion
        
        self.geometry("1260x725+{}+{}".format(self.winfo_screenwidth() // 2 - 1260 // 2, self.winfo_screenheight() // 2 - 755 // 2))
        
        self.configure(bg = "#FFFFFF")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.state('zoomed') #Maximizar la ventana
        
        self.option_add('*TCombobox*Listbox.font', '50') #Aumentar el tamaño de las listas de los drop down 
        self.option_add('*TCombobox*Listbox.height', '50')

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginSujEstudio, RegistroSujeto, MenuMed, ReporteMed):
            page_name = F.__name__
            frame = F(parent = container, controller = self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            

        self.show_frame("LoginSujEstudio")

        self.resizable(False, False)
        self.mainloop()

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        frame.crear_elementos_formulario()