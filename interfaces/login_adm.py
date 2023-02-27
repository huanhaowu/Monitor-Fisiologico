from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/login_adm")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1260x725")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 725,
    width = 1260,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    9.0,
    639.0,
    1278.0,
    730.0,
    fill="#39A9E9",
    outline="")

canvas.create_text(
    453.0,
    255.0,
    anchor="nw",
    text="Digite su nombre de usuario",
    fill="#000000",
    font=("RobotoRoman Regular", 25 * -1)
)

canvas.create_text(
    421.0,
    376.0,
    anchor="nw",
    text="Digite su contraseña",
    fill="#000000",
    font=("RobotoRoman Regular", 25 * -1)
)

canvas.create_text(
    255.0,
    662.0,
    anchor="nw",
    text="TODOS LOS DERECHOS RESERVADOS | COPYRIGHT (C)",
    fill="#FFFFFF",
    font=("Inter", 25 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=376.0,
    y=517.0,
    width=493.0,
    height=59.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    656.0,
    113.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    623.0,
    325.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=421.0,
    y=298.0,
    width=404.0,
    height=52.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    622.0,
    443.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=420.0,
    y=416.0,
    width=404.0,
    height=52.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))

button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)

button_2.place(
    x=21.0,
    y=18.0,
    width=61.0,
    height=59.0
)

window.resizable(False, False)
window.mainloop()

