import PySimpleGUI as sg
import pandas as pd
from pathlib import Path


def is_valid_path(file_path):
    """
    This function checks if the paths exist.
    :param file_path: str
    :return: boolean
    """
    if file_path and Path(file_path).exists():
        return True
    sg.popup_error('Filepath not correct!')
    return False


def display(excel_file_path, sheet_name):
    """
    This function shown quick preview of Excel file
    :param excel_file_path: str
    :param sheet_name: str
    """
    df = pd.read_excel(excel_file_path, sheet_name)
    file_name = Path(excel_file_path).name
    sg.popup_scrolled(df.dtypes, '=' * 50, df, title=file_name)


def convert(excel_file_path, output_folder, sheet_name, separator, decimal):
    """
    This function converts Excel file to csv file and saved new file in Output folder.
    :param excel_file_path: str
    :param output_folder: str
    :param sheet_name: str
    :param separator: str
    :param decimal: str
    """
    df = pd.read_excel(excel_file_path, sheet_name)
    file_name = Path(excel_file_path).stem
    output_file = Path(output_folder) / f'{file_name}.csv'
    df.to_csv(output_file, sep=separator, decimal=decimal, index=False)
    sg.popup_no_titlebar('Ready!')


def settings_window(settings):
    """
    Creates new window with settings from where can be changed separator, decimal and sheet name.
    After click 'Save settings' button all setting are saved in config.ini file.
    :param settings: str
    """
    # Settings window definition
    layout = [[sg.Text('Settings')],
              [sg.Text('Separator'), sg.Input(settings['CSV']['separator'], s=1, key='-SEP-'),
               sg.Text('Decimal'), sg.Combo(settings['CSV']['decimal'].split('|'),
                                            default_value=settings['CSV']['decimal_default'],
                                            s=1, key='-DECI-'),
               sg.Text('Sheet name:'), sg.Input(settings['EXCEL']['sheet_name'], s=20, key='-SHEET_NAME-')],
              [sg.Button('Save settings', s=20)]]

    window = sg.Window('Settings', layout, modal=True, use_custom_titlebar=True)
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
    """
    This function creates main application window and handle actions for all buttons.
    """

    # Menu definition
    menu = [['Help', ['Settings', 'About']]]

    # Main GUI definition
    layout = [
        [sg.MenubarCustom(menu, tearoff=False)],
        [sg.Text('Input file:', s=11, justification='r'), sg.Input(key="-IN-"),
         sg.FileBrowse(file_types=(('Excel Files', '*.xls*'),))],
        [sg.Text('Output folder:', s=11, justification='r'), sg.Input(key="-OUT-"), sg.FolderBrowse()],
        [sg.Button('Convert to CSV', s=15), sg.Button('Display Excel file', s=15),
         sg.Button('Settings', s=15), sg.Exit(s=15, button_color='tomato')],
    ]

    window_title = settings['GUI']['title']
    window = sg.Window(window_title, layout, use_custom_titlebar=True)

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

        if event == 'About':
            sg.popup(window_title, 'version 0.1', 'Convert Excel file to CSV')

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
