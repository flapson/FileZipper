import PySimpleGUI

label1 = PySimpleGUI.Text("Enter feet:")
input1 = PySimpleGUI.Input()

label2 = PySimpleGUI.Text("Enter Inches:")
input2 = PySimpleGUI.Input()

button = PySimpleGUI.Button("Convert")

window = PySimpleGUI.Window("Convertor", layout=[[label1, input1],
                                                 [label2, input2],
                                                 [button]])

window.read()
window.close()