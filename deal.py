from tkinter import *
from PIL import ImageFont, Image, ImageDraw

win = Tk()
win.title("Moses -- add text to your images")
win.geometry("600x650")

def add():
    img = Image.open("images/edited.png")
    text_font = ImageFont.truetype("arial.ttf", 46)
    text_added = my_entry.get()
    edit_img = ImageDraw.Draw(img)
    edit_img.text((100, 90), text_added, ("blue"), font=text_font)
    img.save("images/img_added.png")
    my_label.after(2000, view_pic)

    my_entry.delete(0, END)
    my_entry.insert(0, "saving.....")


def view_pic():
    global img_added
    img_added = PhotoImage(file="images/img_added.png")
    my_label.config(image=img_added)
    my_entry.delete(0, END)


img = PhotoImage(file="images/edited.png")

my_label = Label(win, image=img)
my_label.pack(pady=20)

my_entry = Entry(win, font=("Helvetica", 24))
my_entry.pack(pady=20)

my_button = Button(win, text="add text", font=("Helvetica", 24), command=add)
my_button.pack(pady=20)

win.mainloop()