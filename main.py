import PySimpleGUI as sg
import pyperclip
from HP_format import *
import time
import os
import sys


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
        sg.Text(''.ljust(23)),
        sg.Button('Clear', key='-CLEAR-')
    ],
    [
        sg.ProgressBar(max_value=1000, size=(51, 5), key='-PROGRESSBAR-')
    ]
]

window = sg.Window("H/P phrases generator", layout, finalize=True)
window['-NAME-'].bind('<Return>', '-ENTER-')
window['-CAS-'].bind('<Return>', '-ENTER-')
window['-STRUCTURE-'].bind('<Return>', '-ENTER-')

input_summary = []

root_path = sys._MEIPASS
# this is for pyinstaller to find the path of the h and p dictionaries
# when in IDE, use 'root_path = os.getcwd()'

hazards_dict = pd.read_excel(os.path.join(root_path, 'hazards_dict.xlsx'), index_col=0)
precautions_dict = pd.read_excel(os.path.join(root_path, 'precautions_dict.xlsx'), index_col=0)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == '-NAME-' + '-ENTER-' and len(values['-NAME-']) > 0:

        input_summary.append(values['-NAME-'])
        window['-MANAGER-'].update(input_summary)
        window['-NAME-'].update('')

    elif event == '-CAS-' + '-ENTER-' and len(values['-CAS-']) > 0:

        input_summary.append(values['-CAS-'])
        window['-MANAGER-'].update(input_summary)
        window['-CAS-'].update('')

    elif event == '-STRUCTURE-' + '-ENTER-' and len(values['-STRUCTURE-']) > 0:

        input_summary.append(values['-STRUCTURE-'])
        window['-MANAGER-'].update(input_summary)
        window['-STRUCTURE-'].update('')

    elif event == '-REMOVE-':

        for compound in values['-MANAGER-']:
            input_summary.remove(compound)

        window['-MANAGER-'].update(input_summary)

    elif event == '-CLEAR-':

        input_summary = []
        window['-MANAGER-'].update(input_summary)

    elif event == '-WORDCOPY-':

        word_copy = []

        for i, name in enumerate(input_summary):
            word_copy.append(format_for_word(get_cid_from_name(name), name, values['-SORT-'],
                                             hazards_dict, precautions_dict))
            window['-PROGRESSBAR-'].UpdateBar(int(1000/len(input_summary)*(i+1)))

        pyperclip.copy('\n'.join(flatten(word_copy)))

        for i in range(3):
            window['-PROGRESSBAR-'].UpdateBar(1000)
            time.sleep(0.2)
            window['-PROGRESSBAR-'].UpdateBar(0)
            time.sleep(0.2)

    elif event == '-LATEXCOPY-':

        latex_copy = []

        for name in input_summary:
            latex_copy.append(format_for_latex(get_cid_from_name(name), name, values['-PICTOGRAM-'], values['-SORT-'],
                                               hazards_dict, precautions_dict))

        pyperclip.copy('\n'.join(flatten(latex_copy)))

window.close()
