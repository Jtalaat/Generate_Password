# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
import tkinter as t

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
entry_1 = t.Entry(width=35)
entry_1.focus()
entry_1.grid(column=1,row=1,columnspan=2)
entry_2 = t.Entry(width=35)
entry_2.grid(column=1,row=2,columnspan=2)
entry_3 = t.Entry(width=21)
entry_3.grid(column=1,row=3)

#Button
button_gen = t.Button(text="Generate",command="")
button_gen.grid(row=3,column=2,)
button_add = t.Button(text="Supmit",width=30,command="")
button_add.grid(row=4,column=1,columnspan=2)




window.mainloop()