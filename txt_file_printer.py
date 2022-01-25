import win32print
import win32ui

x = 0
y = 50
printer_name = "EPSON L382 Series (копия 1)"
# if your printer is standard, replace the printer_name:
# win32print.GetDefaultPrinter()

fd = open("file.txt", "r", encoding = "utf-8")
input_string = fd.read()
multi_line_string = input_string.splitlines()

hDC = win32ui.CreateDC()
hDC.CreatePrinterDC()
hDC.StartDoc("Printing...")
hDC.StartPage()
for line in multi_line_string:
hDC.TextOut(x, y, line)
y+=50
hDC.EndPage()
hDC.EndDoc()
fd.close()
