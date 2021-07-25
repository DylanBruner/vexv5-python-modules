from vex import *

#PLACEHOLDERS that way vexcode doesn't complain about errors
load_module = print
screenlib_screen_menu = print
screenlib_screen_button = print
screenlib_screen_text = print
#PLACEHOLDERS that way vexcode doesn't complain about errors

f = open('module_loader.py', 'r');  module_loader = f.read(); f.close()
exec(module_loader)
load_module('screenlib')


Menu1 = screenlib_screen_menu()#Create a new menu


Button1 = screenlib_screen_button(x=1,y=1,w=120,h=100,c=Color.GREEN,text="Hello",tc=1,tr=1)
Button2 = screenlib_screen_button(x=125,y=1,w=120,h=100,c=Color.GREEN,text="Hello!",tc=1,tr=14)

"""
x    | The X pos of the button
y    | The y pos of the button
w    | The width of the button
h    | The height of the button
c    | The color of the button
text | The text the button displays
tc   | The coloum to print the text in
tr   | The row to print the text in
"""

Menu1.buttons.append(Button1)
Menu1.buttons.append(Button2)


selectedButton = Menu1.mainloop() #Returns the text of whatever button was pressed

newMenu = screenlib_screen_menu()

if selectedButton == "Hello":
    newMenu.alert("Hello")

elif selectedButton == "Hello!":
    newMenu.alert("Hello!")


newMenu.mainloop()
