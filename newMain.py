import tkinter as t
import pandas as pd
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    with open('data.csv','a') as f:
        f.write(f"{entry_website.get()},{entry_Email.get()},{entry_Pass.get()}\n")
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
button_gen = t.Button(text="Generate",command="")
button_gen.grid(row=3,column=2,)
button_add = t.Button(text="Supmit",width=30,command=save)
button_add.grid(row=4,column=1,columnspan=2)




window.mainloop()