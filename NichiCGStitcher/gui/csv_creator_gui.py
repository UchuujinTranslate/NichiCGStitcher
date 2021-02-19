# A (currently standalone) tool to create csv files for the rest of this tool
# to interpret from the coordinates output by the PPSSPP GE debugger.


import PySimpleGUI as sg
import pandas as pd
import io


def test_gui():
    main_df = pd.DataFrame(columns=[
                           'X', 'Y', 'Z', 'U', 'V', 'Color', 'NX', 'NY', 'NZ'])

    layout = [
        [sg.Text("Please paste in from PPSSPP GE debugger.")],
        [sg.Multiline(size=(100, 10), key="main_input", autoscroll=True,
                      focus=True, font=["Lucida Sans Typewriter", 10],
                      do_not_clear=False)],
        [sg.Submit(),
            sg.Button(button_text="Export", key="export")],
        ]

    window = sg.Window("GE Coords",
                       layout,
                       default_element_size=(12, 1),
                       default_button_element_size=(12, 1))

    while True:
        event, values = window.read()
        if event is None or event == 'Exit':
            return
        if event == "Submit":
            geCoords = values["main_input"]
            geCoordsFile = io.StringIO(geCoords)

            in_df = pd.read_table(geCoordsFile)
            print("In Dataframe")
            print(in_df)
            print('')

            for index, row in in_df.iterrows():
                main_df = main_df.append(row, ignore_index=True)
                main_df = main_df[
                    ['X', 'Y', 'Z', 'U', 'V', 'Color', 'NX', 'NY', 'NZ']]
            print("Main Dataframe")
            print(main_df)

            # sg.popup(d, title="Input Result", line_width=75, font=[
            #     "Lucida Sans Typewriter", 10])
            print("Submitted!")

        if event == "export":
            main_df.to_csv("guioutput.csv", index=False)
            sg.popup("Exported to guioutput.csv")


test_gui()

# pyinstaller tests/csv_creator_gui.py -F -c
