import pystray
from PIL import Image
from pystray import Icon as icon, Menu as menu, MenuItem as item

def print():
    pass
image = Image.open("c:/Users/Paxton/Python/InClassAssignments/Secure_Connection/Suit.png")
menu = (
    item('Enable security', print),
    item('Trusted list', print),
    item('Untrusted list', print),
    item('Quit',print)
    )
icon = pystray.Icon("name", image, "title", menu)


icon.visible = True
icon.run()