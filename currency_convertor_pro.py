import sys
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

root=Tk()   
root.title("currency converter")
root.geometry("670x240")

root.resizable(True ,True)
root.call("tk", "scaling", 2.0)

root.iconbitmap(r'C:\Users\riyansh agrawal\OneDrive\Desktop\curic.ico')



image = Image.open(r"C:\Users\riyansh agrawal\OneDrive\Desktop\reverse.png")
image = image.resize((60, 60),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.image = photo
label.grid(row=2, column=2)

root.configure(bg='yellow')
font = ("Courier", 12, "bold")
def clicked():

#==============================exception handling===================================
 try: 
# ==============================USD TO .......======================================
   if n.get()=="USD":
        if m.get()=="USD":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*1,3)))
        if m.get()=="AUSD":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*1.40,3)))
        if m.get()=="EURO":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*0.84,3)))
        if m.get()=="POUND":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*0.76,3)))
        if m.get()=="INR":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*73.63,3)))
 # ==============================AUSD TO .......======================================
   elif n.get()=="AUSD":
        if m.get()=="USD":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*0.71,3)))
        if m.get()=="AUSD":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*1,3)))
        if m.get()=="EURO":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*0.60,3)))
        if m.get()=="POUND":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*0.55,3)))
        if m.get()=="INR":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*52.59,3)))
  
# ==============================EURO TO .......======================================
   elif n.get()=="EURO":
        if m.get()=="USD":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*1.19,3)))
        if m.get()=="AUSD":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*1.66,3)))
        if m.get()=="EURO":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*1,3)))
        if m.get()=="POUND":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*0.91,3)))
        if m.get()=="INR":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*87.53,3)))
  
# ==============================POUND TO .......======================================
   elif n.get()=="POUND":
        if m.get()=="USD":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*1.30,3)))
        if m.get()=="AUSD":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*1.83,3)))
        if m.get()=="EURO":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*1.10,3)))
        if m.get()=="POUND":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*1,3)))
        if m.get()=="INR":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*96.19,3)))            

  
# ==============================INR TO .......======================================
   elif n.get()=="INR":
        if m.get()=="USD":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())/73.98)))
        if m.get()=="AUSD":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*0.019)))
        if m.get()=="EURO":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*0.011,3)))
        if m.get()=="POUND":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*0.010,3)))
        if m.get()=="INR":
            e2.delete(0,END)
            e2.insert(0,str(round(int(e1.get())*1,3)))
 except:
    messagebox.askretrycancel("Invalid Input", "Try again?")
     

#label
l1=Label(root,text="Currency Converter",bg='yellow',fg="black",font=("Times New Roman",10))
l1.grid(row=1,column=2,padx=10,pady=10)

l2=Label(root,text="WHAT I HAVE :",bg='yellow',fg="blue",font=("Times New Roman",7))
l2.grid(row=2,column=1,padx=10,pady=4)

l3=Label(root,text="WHAT I WANT :",bg="yellow",fg="blue",font=("Times New Roman",7))
l3.grid(row=2,column=3,padx=10,pady=4)



# Combobox creation 1
n = StringVar() 
curop1 = ttk.Combobox(root, width = 30, textvariable = n) 
curop1['values']=("USD","AUSD","EURO","POUND","INR")
curop1.grid(column = 1, row = 3,padx=20,pady=4) 
curop1.current(4)
# Combobox creation 2
m = StringVar() 
curop2 = ttk.Combobox(root, width = 30, textvariable = m) 
curop2['values']=("USD","AUSD","EURO","POUND","INR")
curop2.grid(column = 3, row = 3,padx=20,pady=4) 
curop2.current(0)

# entry box
e1=Entry(root,width=30,bd=3)
e1.grid(column=1,row=4,padx=10,pady=10)

e2=Entry(root,width=30,bd=3)
e2.grid(column=3,row=4)

b1=Button(root,text="convert",width=12,height=2,bg="black",fg="white",font = ("Courier", 6, "bold"),command=clicked)
b1.grid(column=2,row=7)
root.mainloop()