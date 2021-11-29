# TODO: Run the program as super user
# TODO: Make an installation 'setup.py' for the program
# TODO: User choose the interface [DONE]
# TODO: Remove duplication [DONE]
# TODO: Alert/Notification
# TODO: System Tray Icon
# 	Program needs to be in multiple mode: {Unsecure, Secure, Ultimate Secure}, each mode represent by different icon
# TODO: Stop bad wifi using Scapy
# TODO: Kill Switch [DONE]
# TODO: VPN Connection
# TODO: Enable monitor mode [Optional I think only for Linux]
# TODO: Inherit. from network_profile and add some other features like taking BSSID for trusted and untrusted list
# TODO: Make the program running on the background
# TODO: Make the scan runs every X minutes
# TODO: Discover function will discover the attack if any of the following occurs:
#       - If the wifi disconnect , findCounter+=1
#       - If the computer connect to an open wifi, findCounter+=1
#       - If the computer connect to wifi with same SSID but different BSSID, findCounter+=1
#           If the findCounter > 2 then call alert function
######################################################################################################################
# Articles:  
#   -   https://github.com/awkman/pywifi/blob/master/DOC.md
#   -   https://programmerall.com/article/5941589508/
#   -   https://chowdera.com/2021/04/20210405093620137c.html
#    -   https://scapy.readthedocs.io/en/latest/
# Tools:
#   -   https://pypi.org/project/pywifi/
#   -   https://manytools.org/hacker-tools/ascii-banner/
#       Make the program runs
######################################################################################################################
import pywifi   
import time   
import sys
import pystray  
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import simpledialog
from pywifi import const
from PIL import Image
from pystray import Icon as icon, Menu as menu, MenuItem as item



# Function scan wifi
def scan():
    # interfaces = wifi.interfaces()[interfaceOption]
    # Calling a function that will start the scan
    interface.scan()
    # According to the documentation it is safer to call scan_results() 2 ~ 8 seconds later after calling scan().
    time.sleep(2)
    # Get the results of the previous scan. 
    result = interface.scan_results()
    # Print APs
    print('''
    
    .d88b.                       db    888b.      
    YPwww. .d8b .d88 8d8b.      dPYb   8  .8 d88b 
        d8 8    8  8 8P Y8     dPwwYb  8wwP' `Yb. 
    `Y88P' `Y8P `Y88 8   8    dP    Yb 8     Y88P 
    
    ''')
    print('-'*160)
    print(f'BSSID					SSID				        FREQ		        AUTH			AKM			SIGNAL')
    print('-'*160)
    for i in result:
    	# we need ssid and bssid
    	print(f'{i.bssid}			{i.ssid}			{i.freq}			{i.auth}			{i.akm}			{i.signal}')
    return result

# Function will keep the profile of the trusted profile
def trustedAPs():
    #Create a pop window with trusted list title
    ws = tk.Tk()
    ws.title("Trusted List")
    ws.geometry('400x200')
    # define columns
    columns = ('ssid', 'bssid')
    # attach columns to the tkinter window
    tree = ttk.Treeview(ws, columns=columns, show='headings')
    # define headings
    tree.heading('ssid', text='SSID')
    tree.heading('bssid', text='BSSID')
    ssid = simpledialog.askstring("SSID", "Please enter the SSID (wifi name):",
                                    parent=ws)
    if ssid is None:
        ws.destroy()
    bssid = simpledialog.askstring("BSSID", "Please enter the BSSID (Mac Address):",
                                    parent=ws,)
    if bssid is None:
        ws.destroy()

    # push informations into a tuple
    trusted.append({
        "ssid": ssid, "bssid" : bssid
    })
#    contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

    for ap in trusted:
        tree.insert('', tk.END, values=ap)
    tree.grid(row=0, column=0, sticky='nsew')

    # add a scrollbar
    scrollbar = ttk.Scrollbar(ws, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    # run the app
    ws.mainloop()
    
    
    print('''

      88888 888b. 8    8 .d88b. 88888 8888 888b.    8    888 .d88b. 88888 
        8   8  .8 8    8 YPwww.   8   8www 8   8    8     8  YPwww.   8   
        8   8wwK' 8b..d8     d8   8   8    8   8    8     8      d8   8   
        8   8  Yb `Y88P' `Y88P'   8   8888 888P'    8888 888 `Y88P'   8   

      ''')
    print('-'*50)
    print(f'BSSID					SSID')
    print('-'*50)
    # double check that my secure aps are stored into the dicts
    for i in trusted:
        print(f'{i["ssid"]}\t{i["bssid"]}')
    print(len(trusted))
    print(type(trusted))
    return trusted

# Function will check if my wifi got disconnected if yes then alert and enable the killswitch
def stayConnected():
    if interface.status() == const.IFACE_CONNECTED:
        return True
    elif interface.satus() == const.IFACE_DISCONNECTED:
        return False

# Function is kill switch will basically disconnect you from your connection entirly  if it found you risky situiation
def killSwitch():
    on_activate(icon)
    wifi = pywifi.PyWiFi() # make an object for the pywifi to start scanning
    icon.notify("Your safe you got disconnected from the internet!")
    interface = wifi.interfaces()[0] # use index 0 to obtain the Wi-Fi interface, according to the documentation
    interface.disconnect()


def on_activate(icon):
    clicks.append(icon)
    if len(clicks) == 5:
        icon.stop()
    else:
        icon.icon = images[len(clicks) % len(images)]

def enableMode():    
    on_activate(icon) # switch icon
    while True:
        # run the scan every 300 seconds (5 minute)

        print('\n')
        for i in scan():
            Scan_ssid = i.ssid
            Scan_bssid = i.bssid
            for x in trusted:
                if str(Scan_ssid) ==str( x["ssid"]):
                    print(Scan_bssid)
                    print(x["ssid"])
                    print("possible attack!")
                    icon.notify("My man in danger! you better run kill switch or connect to a badass VPN!")
            # print(f'{ssid}\t{bssid}')
        time.sleep(300)
        # for x in trusted:
        #     print(len(trusted))

# Exit function
def exit():
    sys.exit()

# According to the documentation we have to make the icon visiable in order for our icons to works in all platforms 
def setup(icon):
    icon.visible = True

# Our main program
wifi = pywifi.PyWiFi() # make an object for the pywifi to start scanning
interface = wifi.interfaces()[0] # use index 0 to obtain the Wi-Fi interface, according to the documentation
trusted = [] # save my trusted aps into a dict 
clicks = []
# Running icon
image1 = Image.open("c:/Users/Paxton/Python/InClassAssignments/Secure_Connection/disconnect.png")
image2 = Image.open("c:/Users/Paxton/Python/InClassAssignments/Secure_Connection/connected.png")
images = (image1, image2)
menu = (
    item('Enable security', enableMode),
    item('Kill Switch',  killSwitch),
    item('Trusted list', trustedAPs),
    item('Quit',exit)
    )
icon = pystray.Icon("Secure Connection", images[0], "Secure Connection", menu)
icon.run(setup)
