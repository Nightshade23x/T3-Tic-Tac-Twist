from tkinter import *
count=0
def click():
    global count
    count+=1
    print(f"Hello!{count}")
window=Tk()#initialize the window
window.geometry("420x420")#set its size
window.title("Prac for GUI")#put a title for the window
window.config(background="black")#bg for the window
label=Label(window,text="Hey,this is prac",relief=RAISED,bd=15,padx=20,pady=40)#add some text to the window
label.place(x=0,y=50)#where i wanna place the text
button=Button(window,text="Click me")
button.config(command=click)#add a func to the button and it displays the text when called
button.pack()
window.mainloop()#makes everything work,kinda like if main in normal python coding