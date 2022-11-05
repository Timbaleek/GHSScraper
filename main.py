import numpy as np
import pandas as pd
import PySimpleGUI as sg
import pyperclip


sg.theme('DarkTeal4')

input_column = [
    [
        sg.Frame('search', [[sg.Text('Name: '), sg.InputText(key='-NAME-')],
                            [sg.Text('CAS registry: '), sg.InputText(key='-CAS-')],
                            [sg.Text('Formula: '), sg.InputText(key='-FORMULA-')],
                            [sg.Listbox([], key='-AUTOCOMPLETE-', size=(30, 6))]])
    ],
    [
        sg.Listbox([], key='-MANAGER-', size=(40, 10))
    ]
]

output_column = [
    [
        sg.Text(key='-PREVIEW-')
    ],
    [
        sg.Button('Copy to Clipboard', key='-WORDCOPY-'),
        sg.Button('Copy to Clipboard formatted for LaTex', key='-LATEXCOPY-')
    ]
]

layout = [
    [
        sg.Column(input_column),
        sg.VSeparator(),
        sg.Column(output_column)
    ]
]

window = sg.Window("H/P phrases generator", layout, finalize=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()
