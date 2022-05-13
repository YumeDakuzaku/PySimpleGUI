from inspect import getargvalues
from turtle import update
import PySimpleGUI as sg
import io
import os
from PIL import Image

file_types = [("JPEG (*.jpg)","*.jpg"),
              ("All files (*.*)","*.*")]
layout = [
    [sg.Image(key="-IMAGE-")],
    [
        sg.Text("Diretório da Imagem"),
        sg.Input(size=(25,1),key="-FILE-"),
        sg.FileBrowse(file_types=file_types),
        sg.Button("Load Image"),
    ],
]
window = sg.Window("Carrega e Visualiza imagem", layout)

while True:
    event,values = window.read()
    if event =="Exit" or event ==sg.WIN_CLOSED:
        break
    if event =="Load Image":
        filename = values["-FILE-"]
        if os.path.exists(filename):
            image = Image.open(values["-FILE-"])
            image.thumbnail((400,400))
            bio = io.BytesIO()
            #Armazena a imagem na memória
            image.save(bio,format="PNG")
            #Usa a imagem
            window["-IMAGE-"].update(data=bio.getvalue())
window.close()        