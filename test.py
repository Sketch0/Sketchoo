import pyttsx3

engine = pyttsx3.init()

voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)

engine.say("I am activated")
engine.runAndWait()
from tkinter import *
from nltk.tokenize import word_tokenize
from nltk.tokenize import blankline_tokenize
from nltk.stem import PorterStemmer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import wikipedia

root = Tk()
'''img = Image.open("C:\\Users\\BEDAPRAKASH\\Downloads\\D.Tech_Logo.png")
resize_img = img.resize((1400,1050))
photo = ImageTk.PhotoImage(resize_img)'''
photo = PhotoImage(file=r"C:\\Users\\BEDAPRAKASH\\Downloads\\D.Tech_Logo.png")
root.config(bg='navy')
root.title("Darshan-Technologies")
#root.maxsize(542 , 700)
label = Label(
    root,
    image=photo
)
label.place(x=0, y=0)
'''Label(text="Wecome",font=('Stencil',30)).grid(row=0,column=0)
Label(text="To",font=('Stencil',25)).grid(row=1,column=0)'''
Label(text="Darshan's Technologies",font=('Stencil',30)).grid(row=2,column=0)
Label(text="Enter data here",font=('Stencil')).grid(row=3,column=0)
usr = StringVar()
l1 = Label(text="",font=('Stencil',10),bg='yellow')
l1.grid(row=7,column=0)
entry = Entry(textvariable=usr,width='85',bg='green')
entry.grid(row=4,column=0)
def usrentry():
    print(f"{usr.get()}")
    engine.say("You searched for " + f"{usr.get()}")
    engine.runAndWait()
    engine.say("here is the searching result")
    engine.runAndWait()
    result=wikipedia.summary({usr.get()},2)
    print(result)
    l1.configure(text=result)
    engine.say(result)
    engine.runAndWait()
button = Button(text="search",bd='10',command=usrentry,bg='green').grid(row=5,column=0)
button = Button(text="terminate",bd='10',command=root.destroy,bg='red').grid(row=6,column=0)
root.mainloop()