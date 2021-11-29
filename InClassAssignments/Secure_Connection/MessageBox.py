from tkinter import *
from tkinter import simpledialog

ws = Tk()
ws.title("Trusted List")

trusted = []
answer1 = simpledialog.askstring("SSID", "Please enter the SSID (wifi name):",
                                parent=ws)
if answer1 is not None:
    print("SSID :", answer1)
else:
    ws.destroy()

answer2 = simpledialog.askstring("BSSID", "Please enter the BSSID (Mac Address):",
                                parent=ws,)
if answer2 is not None:
    print("BSSID: ", answer2)
else:
    ws.destroy()

trusted.append({"ssid":answer1,
                "bssid":answer2})
opt_list = [answer1]
opt_list2 = [answer2]

for i in trusted:
    print(f'ssid is {i["ssid"]}, bssid is : {i["bssid"]}')

def cancel():
    ws.destroy()
E = Entry(ws)
C = Button(ws, text ="Cancel", command = cancel)
Lb1 = Listbox(ws, selectmode=MULTIPLE)
Lb2 = Listbox(ws, selectmode=MULTIPLE)


for i,j in enumerate(opt_list):
    Lb1.insert(i,j)

for i,j in enumerate(opt_list2):
    Lb2.insert(i,j)

Lb1.pack()
Lb2.pack()
C.pack()
E.pack()

ws.mainloop()