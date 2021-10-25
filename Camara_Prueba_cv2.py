import PySimpleGUI as sg
from datetime import date
import cv2

def main():

    camara = cv2.VideoCapture(1)

    sg.theme('DarkTeal11')

    layout = [[sg.Image(filename='', key='-image-')],
              [sg.Button('Tomar Foto'),sg.Button('Salir')]]

    window = sg.Window('Camara Prueba',
                       layout,
                       no_titlebar=False,
                       location=(0, 0))

    image_elem = window['-image-']

    numero = 0

    while camara.isOpened():
        event, values = window.read(timeout=0)
        ret, frame = camara.read()

        if event in ('Salir',None):
            break

        elif event == 'Tomar Foto':
            ruta = sg.popup_get_folder(title='Guardar', message="Carpeta")
            cv2.imwrite(ruta + "/" + str(date.today()) + str(numero) + ".png", frame)

        if not ret:
            break

        imgbytes = cv2.imencode('.png', frame)[1].tobytes()
        image_elem.update(data=imgbytes)
        numero = numero + 1
main()
