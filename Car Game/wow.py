
from tkinter import *
from PIL import Image
root = Tk()
root.title('Car Game')
bg = PhotoImage(file = "f122p.png")
root.geometry('660x360')
pic=Label( root, image = bg)
pic.place(x = 0, y = 0)
next=Button(root, text='GAME?', command=root.destroy, font =('calibri', 25, 'bold'),borderwidth = '1', relief='flat')
next.config( bg='red', fg='white')
next.place(x=300, y=220)

root.mainloop()

from utils import *
from main import *
