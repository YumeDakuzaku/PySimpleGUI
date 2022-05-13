from fileinput import filename

import PySimpleGUI as sg

layout = [
    [sg.Image(filename="Patins_Fotografia_YumeDakuzaku.PNG")],
    [sg.Button('Exit')]
]

window = sg.Window("Visualizador de Imagem", layout)

while True:
    event, values = window.read()
    if event =="Exit" or event == sg.WIN_CLOSED:
        break
window.close()