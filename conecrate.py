from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def conectare2_page():
    login_window.destroy()
    import conectare2


def forget_pass():
    def change_parola():
        if user_entry.get()=='' or parolanew_entry.get()=='' or confirmaparola_entry.get()=='':
            messagebox.showerror('Eroare','Toate spatiile sunt necesare',parent=window)
        elif parolanew_entry.get() !=confirmaparola_entry.get():
            messagebox.showerror('Eroare','Parola si confirma parola nu coincid',parent=window)
        else:
            conn = pymysql.connect(host='localhost', user='root', password='280802',database='login')
            mycursor = conn.cursor()
            query ='SELECT * FROM data where username=%s'
            mycursor.execute(query,(user_entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Eroare','Username incorect',parent=window)
            else:
                query='update data set parola=%s where username=%s'
                mycursor.execute(query,(parolanew_entry.get(),user_entry.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo('Succes','Parola este schimbata, acum te poti loga',parent=window)
                window.destroy()
    window = Toplevel()
    window.title('Schimba Parola')

    bgPic = ImageTk.PhotoImage(file='parola.jpg')
    bgLabel = Label(window, image=bgPic)
    bgLabel.grid()

    heading_label = Label(window, text='RESETEAZA PAROLA', font=('arial','19','bold',),bg='deep sky blue', fg='black')
    heading_label.place(x=100, y=150)

    userLabel = Label(window, text='Username', font=('arial',13, 'bold'),bg='deep sky blue',fg='black')
    userLabel.place(x=100, y=210)

    user_entry = Entry(window, width=26, fg='black', font=('arial',11,'bold'),bd=0)
    user_entry.place(x=100, y=240)

    Frame(window, width=210, height=2, bg='deep sky blue').place(x=100, y=260)

    parolanewlabel = Label(window, text='Parola noua', font=('arial',13,'bold'),bg='deep sky blue',fg='black')
    parolanewlabel.place(x=100, y=270)

    parolanew_entry = Entry(window, width=26, fg='black', font=('arial',11,'bold'),bd=0)
    parolanew_entry.place(x=100, y=295)

    Frame(window, width=210, height=2, bg='deep sky blue').place(x=100, y=315)

    confirmaparolalabel = Label(window, text='Confirma parola', font=('arial',13,'bold'),bg='deep sky blue',fg='black')
    confirmaparolalabel.place(x=100, y=325)

    confirmaparola_entry = Entry(window, width=26, fg='black', font=('arial',11,'bold'),bd=0)
    confirmaparola_entry.place(x=100, y=346)

    Frame(window, width=210, height=2, bg='deep sky blue').place(x=100, y=365)

    confirmaButton = Button(window, text='Confirma',bd=0, bg='deep sky blue', fg='black', font=('Open Sans','16','bold'),width=25, cursor='hand2', activebackground='deep sky blue', activeforeground='white',command=change_parola)

    confirmaButton.place(x=100, y=400)


    window.mainloop()



def login_user():
    if usernameEntry.get()=='' or parolaEntry.get()=='':
        messagebox.showerror('Eroare','Completati toate campurile')
    else:
        try:
            conn = pymysql.connect(host='localhost', user='root', password='280802',db='login')
            mycursor=conn.cursor()
        except:
            messagebox.showerror('Eroare','Baza de date este offline')
            return
        query = 'use login'
        mycursor.execute(query)
        query='select * from data where username=%s and parola=%s'
        mycursor.execute(query, (usernameEntry.get(), parolaEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Eroare','Nume sau parola incorecta')
        else:
            messagebox.showinfo('Succes','Te-ai conectat cu succes')

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
def parola_enter(event):
    if parolaEntry.get()=='Password':
        parolaEntry.delete(0,END)


login_window=Tk()

background=ImageTk.PhotoImage(file='poza6.png')

bgLabel=Label(login_window,image=background)
bgLabel.grid(row=100,column=100)

login_window.resizable(10,10)
login_window.title('Pagina de autentificare')


heading=Label(login_window,text='Autentificare operator',font=('Microsoft Yahei UI Light',23,'bold'),fg='black',bg='purple2')

heading.place(x=200,y=120)

usernameEntry=Entry(login_window,width=35,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg="black",bg='purple2')
usernameEntry.place(x=200,y=210)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login_window,width=320,height=2,bg='black').place(x=200,y=230)

parolaEntry=Entry(login_window,width=35,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg="black",bg='purple2')
parolaEntry.place(x=200,y=260)
parolaEntry.insert(0,'Parola')

parolaEntry.bind('<FocusIn>',parola_enter)

frame2=Frame(login_window,width=320,height=2,bg='black').place(x=200,y=280)


forgetButton=Button(login_window,text='Ai uitat parola?',bd=0,bg='purple2',activebackground='white',cursor='hand2',font=('Microsoft Yahei UI Light',9,'bold'),fg="black",command=forget_pass)
forgetButton.place(x=400,y=290)

loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='purple2',activeforeground='white',cursor='hand2',bd=0,width=19,command=login_user)
loginButton.place(x=200,y=330)

singupLabel=Label(login_window,text='Nu ai cont?',font=('Open Sans',9,'bold'),fg='white',bg='purple2')
singupLabel.place(x=200, y=290)

newaccountButton=Button(login_window, text='Creaza un cont',font=('Open Sans',9,'bold underline'),fg='white',bg='purple2',activeforeground='white',activebackground='purple2',cursor='hand2',bd=0,command=conectare2_page)
newaccountButton.place(x=269 , y=290)


login_window.mainloop()
