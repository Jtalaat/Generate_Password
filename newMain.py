
import email
import tkinter as t
from tkinter import messagebox
import pandas as pd
import json
from Password_engine import password1
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    entry_Pass.delete(0,t.END)
    entry_Pass.insert(0,password1)
    pyperclip.copy(password1)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = entry_website.get()
    mail = entry_Email.get()
    pas = entry_Pass.get()
    new_data = {web:{'email':mail,'password':pas}}

    if len(web)==0 or len(mail) ==0 or len(pas) == 0:
        messagebox.showinfo(title='oobs' ,message="Please check entired data")
    elif messagebox.askokcancel(title=web,message=f'we need to add this {mail}\n,and {pas}\n for mentioned web \nis it Ok'):     
        with open('data.json','r') as f:
            data =json.load(f)
            data.update(new_data)
        with open('data.json','w') as f:
            json.dump(data,f,indent=4)
        entry_website.delete(0,t.END)
        entry_Pass.delete(0,t.END)

# ---------------------------- UI SETUP ------------------------------- #

window = t.Tk()
window.title("Bassword Generate")
window.config(padx=50,pady=50)
canves = t.Canvas(height=200,width=200)
file =t.PhotoImage(file='logo.png')
canves.create_image(100,100,image=file)
canves.config(bg='white')
canves.grid(column= 1,row= 0)

#Label

label_web = t.Label(text='Website')
label_web.grid(column=0,row=1)
label_mail = t.Label(text='Email/UserName')
label_mail.grid(column=0,row=2)
label_pass = t.Label(text='Password')
label_pass.grid(column=0,row=3)

#Entry
entry_website = t.Entry(width=35)
entry_website.focus()
entry_website.grid(column=1,row=1,columnspan=2)
entry_Email = t.Entry(width=35)
entry_Email.insert(0,'john.abdelmasseh@gmail.com')
entry_Email.grid(column=1,row=2,columnspan=2)
entry_Pass = t.Entry(width=25)
entry_Pass.grid(column=1,row=3)

#Button
button_gen = t.Button(text="Generate",command=generate)
button_gen.grid(row=3,column=2,)
button_add = t.Button(text="Supmit",width=30,command=save)
button_add.grid(row=4,column=1,columnspan=2)




window.mainloop()