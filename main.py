import numpy as np
import pandas as pd
import PySimpleGUI as sg
import pyperclip


sg.theme('DarkTeal4')

col1 = [[sg.Text('Compound Name: ')],
        [sg.Text('Compound Structure: ')],
        [sg.Text('CAS Number: ')]]

col2 = [[sg.InputText(key='-NAME-')],
        [sg.InputText(key='-STRUCTURE-')],
        [sg.InputText(key='-CAS-')]]

layout = [
    [
        sg.Frame('Search', [[sg.Column(col1), sg.Column(col2)]])
    ],
    [
        sg.Listbox([], key='-MANAGER-', size=(67, 15))
    ],
    [
        sg.Checkbox('Sort alphabetically', key='-SORT-'),
        sg.Checkbox('Format disposal information', key='-DISPOSAL-', default=True),
        sg.Checkbox('Pictograms', key='-PICTOGRAM-', default=True)
    ],
    [
        sg.Button('Remove compound', key='-REMOVE-'),
        sg.Button('Copy to clipboard', key='-WORDCOPY-'),
        sg.Button('Copy for LaTex', key='-LATEXCOPY-'),
        sg.Text(''.ljust(21)),
        sg.Button('Clear', key='-CLEAR-')
    ]
]

window = sg.Window("H/P phrases generator", layout, finalize=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()
