import win32print
import win32ui

x = 0
y = 50

fd = open("file.txt", "r", encoding = "utf-8")
input_string = fd.read()
multi_line_string = input_string.splitlines()

hDC = win32ui.CreateDC()
hDC.CreatePrinterDC("EPSON L382 Series (копия 1)")
hDC.StartDoc("Printing...")
hDC.StartPage()
for line in multi_line_string:
    hDC.TextOut(x, y, line)
    y+=50
hDC.EndPage()
hDC.EndDoc()

hDC = win32ui.CreateDC()
hDC.CreatePrinterDC("BIXOLON SRP-350plus (копия 1)")
hDC.StartDoc("Printing...")
hDC.StartPage()
for line in multi_line_string:
    hDC.TextOut(x, y, line)
    y+=50
hDC.EndPage()
hDC.EndDoc()
fd.close()
