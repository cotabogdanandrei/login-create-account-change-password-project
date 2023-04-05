from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.destroy()
    usernameEntry.destroy()
    parolaEntry.destroy()
    confirmaparolaEntry.destroy()
    check.set(0)

def login_page():
    singup_window.destroy()
    import conectare

def connect_login():
    if emailEntry.get()=='' or usernameEntry.get()=='' or parolaEntry.get()=='' or confirmaparolaEntry.get()=='':
        messagebox.showerror('Eroare' , 'Toate cerintele nu sunt acceptate')
    elif parolaEntry.get() != confirmaparolaEntry.get():
        messagebox.showerror('Eroare', 'Parolele nu coincid')
    elif check.get()==0:
        messagebox.showerror('Eroare', 'Nu ai acceptat termeni si conditiile')
    else:
        try:
            conn = pymysql.connect(host='localhost' , user='root' , password='280802' , db='login')
            mycursor=conn.cursor()
        except:
            messagebox.showerror('Eroare' , 'Problema cu baza de date,Incearca mai tarziu')
            return
        try:
            query='create login'
            mycursor.execute(query)
            query='use login'
            mycursor.execute(query)
            query='CREATE TABLE data(id int NOT NULL AUTO_INCREMENT,email varchar(50),username varchar(100),parola varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use login')
        query=('SELECT * FROM data where username=%s')
        mycursor.execute(query , (usernameEntry.get()))

        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Eroare','Acest utilizator exista')
        else:
            query=('INSERT INTO data(email,username,parola) VALUES (%s,%s,%s)')
            mycursor.execute(query , (emailEntry.get() , usernameEntry.get() , parolaEntry.get()))

        conn.commit()
        conn.close()
        messagebox.showinfo('Succes','Inregistrare cu succes')
        clear()
        singup_window.destroy()
        import conectare


singup_window=Tk()

background=ImageTk.PhotoImage(file='nori.jpg')

bgLabel = Label(singup_window,image=background)
bgLabel.grid()

singup_window.title('Creare cont')

frame=Frame(singup_window)
frame.place(x=80,y=50)

heading=Label(singup_window,text='Creaza un cont' , font=('Microsoft Yahei UI Light' , 21 , 'bold') , fg='black' , bg='white')
heading.place(x=80 , y=50)

emailLabel=Label(frame , text='Email' , font=('Microsoft Yahei UI Light',10,'bold'),bg='white')

emailLabel.grid(row=1 , column=0 , sticky='w' , padx=25 , pady=(10 , 0))

frame.place(x=80,y=100)

emailEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),bg='white')

emailEntry.grid(row=2,column=0,sticky='w',padx=25)


usernameLabel=Label(frame,text='Utilizator',font=('Microsoft Yahei UI Light',10,'bold'),bg='white')

usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

usernameEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),bg='white')

usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

frame.place(x=80,y=100)

parolaLabel=Label(frame,text='Parola',font=('Microsoft Yahei UI Light',10,'bold'),bg='white')

parolaLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

parolaEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),bg='white')

parolaEntry.grid(row=6,column=0,sticky='w',padx=25)


confirmaparolaLabel=Label(frame,text='Confirma Parola',font=('Microsoft Yahei UI Light',10,'bold'),bg='white')

confirmaparolaLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmaparolaEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),bg='white')

confirmaparolaEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()
termeni=Checkbutton(frame,text='Accept termeni si conditiile',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',variable=check)
termeni.grid(row=9,column=0,pady=10,padx=15)


singupButton=Button(frame,text='Singup',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',bd=0,fg='black',width=20,command=connect_login)
singupButton.grid(row=10,column=0,pady=10)

aidejacont=Label(frame,text='Ai deja un cont?',font=('Open Sans',9,'bold'),bg='white')
aidejacont.grid(row=11,column=0,sticky='w,',padx=25,pady=10)

loginButton=Button(frame,text='Conecteaza-te',font=('Open Sans',9,'bold underline'),bg='white',bd=0,cursor='hand2',activebackground='red',command=login_page)
loginButton.place(x=120,y=340)



singup_window.mainloop()
