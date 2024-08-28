import tkinter
from tkinter import *
from  random import randint
root=Tk()
root.title("Strong Password Generator")
#root.iconbitmap("")
root.geometry("500x300")

#generate random ascii
#my_password=chr(randint(33,126))
# this two has the code that implements the both buttons
def new_rand():
    #clearing  our entry box
    pw_entry.delete(0,END)
    #get pw length  and convert to integer"
    pw_length=int(my_entry.get())
    #create a variable to hold our password
    my_password=''
    #loop through the pw length
    for x in range(pw_length):
        my_password +=chr(randint(33,126))
    #output ouur password
    pw_entry.insert(0,my_password)
    
def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
    
  

#label frame
lf=LabelFrame(root,text="How many Character?")
lf.pack(pady=20)

#create entry box to designate number of character
my_entry=Entry(lf,font=("Helvetica",24),)#bd=0,bg="systembuttonface")
my_entry.pack(pady=20,padx=20)

#create entry box fro our returned password
pw_entry=Entry(root,text='',font=("Helvetica",24))
pw_entry.pack(pady=20)

#create a frame for our buttons
my_frame=Frame(root)
my_frame.pack(pady=20)

#create buttons
my_button=Button(my_frame,text="Generate Strong Password",command=new_rand)
my_button.grid(row=0,column=0,padx=10)

clip_button=Button(my_frame,text="Copy to Clipboard",command=clipper)
clip_button.grid(row=0,column=1,padx=10)





root.mainloop()