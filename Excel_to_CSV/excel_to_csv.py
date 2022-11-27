import PySimpleGUI as sg
import pandas as pd
from pathlib import Path


def is_valid_path(file_path):
    if file_path and Path(file_path).exists():
        return True
    sg.popup_error('Filepath not correct!')
    return False


def display(excel_file_path, sheet_name):
    df = pd.read_excel(excel_file_path, sheet_name)
    file_name = Path(excel_file_path).name
    sg.popup_scrolled(df.dtypes, '=' * 50, df, title=file_name)


def convert(excel_file_path, output_folder, sheet_name, separator, decimal):
    df = pd.read_excel(excel_file_path, sheet_name)
    file_name = Path(excel_file_path).stem
    output_file = Path(output_folder) / f'{file_name}.csv'
    df.to_csv(output_file, sep=separator, decimal=decimal, index=False)
    sg.popup_no_titlebar('Ready!')


def settings_window(settings):
    layout = [[sg.Text('Settings')],
              [sg.Text('Separator'), sg.Input(settings['CSV']['separator'], s=1, key='-SEP-'),
               sg.Text('Decimal'), sg.Combo(settings['CSV']['decimal'].split('|'),
                                            default_value=settings['CSV']['decimal_default'],
                                            s=1, key='-DECI-'),
               sg.Text('Sheet name:'), sg.Input(settings['EXCEL']['sheet_name'], s=20, key='-SHEET_NAME-')],
              [sg.Button('Save settings', s=20)]]

    window = sg.Window('Settings', layout, modal=True)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'Save settings':
            settings['CSV']['separator'] = values['-SEP-']
            settings['CSV']['decimal_default'] = values['-DECI-']
            settings['EXCEL']['sheet_name'] = values['-SHEET_NAME-']

            sg.popup_no_titlebar('Successfully saved!')
            break
    window.close()


def main():
    # GUI definition
    layout = [
        [sg.Text('Input file:'), sg.Input(key="-IN-"), sg.FileBrowse(file_types=(('Excel Files', '*.xls*'),))],
        [sg.Text('Output folder:'), sg.Input(key="-OUT-"), sg.FolderBrowse()],
        [sg.Exit(), sg.Button('Settings'), sg.Button('Display Excel file'), sg.Button('Convert to CSV')],
    ]

    window_title = settings['GUI']['title']
    window = sg.Window(window_title, layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break

        if event == 'Settings':
            settings_window(settings)

        if event == 'Display Excel file':
            if is_valid_path(values['-IN-']):
                display(values['-IN-'], settings['EXCEL']['sheet_name'])

        if event == 'Convert to CSV':
            if is_valid_path(values['-IN-']) and is_valid_path(values['-OUT-']):
                convert(
                    excel_file_path=values['-IN-'],
                    output_folder=values['-OUT-'],
                    sheet_name=settings['EXCEL']['sheet_name'],
                    separator=settings['CSV']['separator'],
                    decimal=settings['CSV']['decimal'],
                )

    window.close()


if __name__ == '__main__':
    SETTINGS_PATH = Path.cwd()
    settings = sg.UserSettings(
        path=SETTINGS_PATH, filename='config.ini', use_config_file=True, convert_bools_and_none=True
    )
    font_size = int(settings['GUI']['font_size'])
    font_family = settings['GUI']['font_family']
    theme = settings['GUI']['theme']
    sg.theme(theme)
    sg.set_options(font=(font_family, font_size))
    main()
