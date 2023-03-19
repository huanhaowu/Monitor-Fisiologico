from fpdf import FPDF
#Arreglo - Documentar el funcionamiento

class ReportePdf(FPDF):
    def __init__(self, reporte_med):
        FPDF.__init__(self)
        self.reporte_med = reporte_med

        self.add_page()
        self.header()
        self.footer()
        self.set_margins(20, 0, 20)
        self.set_font("helvetica", '', size=13)
        self.text(162, 42, reporte_med.fecha_actual_str)

        self.set_font("helvetica", 'B', size=13)
        self.text(20, 52, "REPORTE DE MEDICIONES")

        self.set_font("helvetica", '', size=13)
        self.text(20, 58,
                 "-------------------------------------------------------------------------------------------------------------")

        self.set_font("helvetica", 'B', size=13)
        self.text(20, 66, reporte_med.sujeto.nombres + " " + reporte_med.sujeto.apellidos)

        self.set_font("helvetica", '', size=11)
        self.text(20, 72, reporte_med.sujeto.tipo_documento.descripcion + ": " + reporte_med.sujeto.codigo_documento)

        self.set_font("helvetica", '', size=11)
        self.text(20, 78, f"Edad: {reporte_med.edad}")

        self.set_font("helvetica", '', size=11)
        self.text(20, 84, f"Sexo: {reporte_med.sujeto.sexo.descripcion}")

        self.set_font("helvetica", '', size=11)
        self.text(20, 90, f"Peso: {reporte_med.mediciones.peso_sujeto}")

        self.set_font("helvetica", '', size=11)
        self.text(20, 96, f"Estatura: {reporte_med.mediciones.altura_sujeto}")

        self.set_font("helvetica", '', size=11)
        self.text(20, 102,
                 "---------------------------------------------------------------------------------------------------------------------------------")

        self.set_font("helvetica", 'B', size=11)
        self.text(30, 108, "PARAMETRO")
        self.text(80, 108, "VALOR")
        self.text(120, 108, "UNIDAD")
        self.text(160, 108, "ESCALA")

        self.set_font("helvetica", '', size=11)
        self.text(20, 114,
                 "---------------------------------------------------------------------------------------------------------------------------------")
        self.text(20, 122, "Temperatura")
        self.text(20, 140, "Presión Arterial")
        self.text(20, 158, "Saturación de Oxígeno")
        self.text(20, 176, "Frecuencia Cardíaca")
        # VALORES
        self.text(85, 122, f"{reporte_med.lista_temperatura[2]}")
        self.text(85, 140, f"{reporte_med.lista_presion[2]}")
        self.text(85, 158, f"{reporte_med.lista_oxigeno[2]}")
        self.text(85, 176, f"{reporte_med.lista_frecuencia[2]}")
        # UNIDADES
        self.text(127, 122, "C")
        self.text(123, 140, "mmHg")
        self.text(127, 158, "%")
        self.text(125, 176, "lpm")
        # ESCALAS
        self.text(160, 122, f"{self.escala_en_texto(reporte_med.lista_temperatura)} {reporte_med.lista_temperatura[1]}")
        self.text(160, 140, f"{self.escala_en_texto(reporte_med.lista_presion)} {reporte_med.lista_presion[1]}")
        self.text(160, 158, f"{self.escala_en_texto(reporte_med.lista_oxigeno)} {reporte_med.lista_oxigeno[1]}")
        self.text(160, 176, f"{self.escala_en_texto(reporte_med.lista_frecuencia)} {reporte_med.lista_frecuencia[1]}")

        self.text(20, 183,
                 "---------------------------------------------------------------------------------------------------------------------------------")
        #region NOTA ACLARATORIA
        self.set_font("helvetica", 'B', size=11)
        self.text(20, 189, "NOTA ACLARATORIA")

        # Define the maximum width of the page
        max_width = 210

        # Define the margin
        margin = 20

        # Define the line height
        line_height = 7

        # Define the starting position for the text
        x_pos = margin
        y_pos = 193
        self.set_font("helvetica", '', size=9)

        # Loop through each character in the text
        for char in self.reporte_med.nota_aclaratoria:

            # If the character goes beyond the maximum width of the page, add a line break
            if x_pos + self.get_string_width(char) > max_width - margin or char == "-":
                y_pos += line_height
                x_pos = margin

            # If the text reaches the bottom of the page, add a new page
            if y_pos + line_height > self.h - margin:
                self.add_page()
                y_pos = 52

            # Add the character to the PDF and update the position
            self.text(x_pos, y_pos, char)
            x_pos += self.get_string_width(char)
        #endregion


        # save the pdf with name .pdf
        self.output(self.reporte_med.ruta_pdf)
    def header(self):
        self.image(self.reporte_med.ruta_logo, 115, 25, 73)

    def footer(self):
        self.set_font('helvetica', 'I', 9)
        self.text(20, 280,
                 "Leyenda: símbolo (+) representa por encima del estándar, símbolo (-) representa por debajo del estándar")
        self.text(20, 284,
                 "Alerta: un poco alejado del estándar | Crítico: bastante alejado del estándar | N/A: valor no medido")
        self.text(20, 288, "")
        self.text(20, 292, "")
    
    def escala_en_texto(self, lista=[]):
        if lista[0] == "rojo":
            return "Crítico"
        elif lista[0] == "verde":
            return "Estándar"
        elif lista[0] == "amarillo":
            return "Alerta"
        else:
            return "N/A"

