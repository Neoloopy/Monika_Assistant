from tkinter import *
from PIL import ImageTk, Image
from playsound import playsound
root = Tk()
root.title("Monika Assistant")
#root.geometry("1920x1080")
root.geometry("1280x720")

global monika_num

monika_num = [
	PhotoImage(file = "Moni_og.png"),
	PhotoImage(file = "Moni_blush.png"),
]

#nut definition
def nut():
	my_canvas.create_image(0,0, image = monika_num[1], anchor = "nw")
	playsound ("Nut_Button_Audio.mp3")
	my_button1.after(2000, moni_set)


#moni_set definition
def moni_set():
	my_canvas.create_image(0,0, image = monika_num[0], anchor = "nw")

#canvas defined
my_canvas = Canvas(root, width = 1280, height = 720, bd = 0, highlightthickness = 0)
my_canvas.pack(fill = "both", expand = True)

#monika's dayroom background image
monika_bg = ImageTk.PhotoImage(Image.open("monika_day_room.png"))

#places the monika background
my_canvas.create_image(0,0, image = monika_bg, anchor = "nw")
my_canvas.create_image(0,0, image = monika_num[0], anchor = "nw")

#button entry
my_button1 = Button(root, text = " N U T ", width = 15, command=nut)
window_button1 = my_canvas.create_window(200,800, anchor = "nw", window = my_button1)


root.mainloop()
