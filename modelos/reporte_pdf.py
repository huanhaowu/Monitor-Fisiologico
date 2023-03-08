from fpdf import FPDF

class ReportePdf(FPDF):
    def __init__(self, reporte_med):
        FPDF.__init__(self)
        self.reporte_med = reporte_med

        self.add_page()
        self.header()
        self.footer()
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
        lista_presion = reporte_med.buscar_parametro("Presion Arterial")
        self.text(20, 140, "Presión Arterial")
        self.text(20, 158, "Saturación de Oxígeno")
        self.text(20, 176, "Frecuencia Cardíaca")
        # UNIDADES
        self.text(127, 122, "C")
        self.text(123, 140, "mmHg")
        self.text(127, 158, "%")
        self.text(125, 176, "lpm")
        # ESCALAS
        self.text(20, 122, "")
        self.text(20, 140, "Presión Arterial")
        self.text(20, 158, "Saturación de Oxígeno")
        self.text(20, 176, "Frecuencia Cardíaca")

        self.text(20, 183,
                 "---------------------------------------------------------------------------------------------------------------------------------")

        self.set_font("helvetica", 'B', size=11)
        self.text(20, 189, "NOTA ACLARATORIA")

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