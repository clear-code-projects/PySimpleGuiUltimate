import PySimpleGUI as sg

print(sg.Window('', [[sg.Input(),sg.Button('Ok'),sg.Button('Cancel')]]).read())