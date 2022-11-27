from tkinter import *
from tkinter import messagebox


def login():

    
    user=username.get()
    code=password.get()
    if user=="harish" and code=="1234":
        import home
        home.screen()
        
    elif user!="harish" and code!="1234":
        messagebox.showerror("invalid","invalid username and password (use this harish,1234)")
    elif user!="harish":
        messagebox.showerror("invalid","invalid username(use this harish,1234)")
    elif code!="1234":
        messagebox.showerror("invalid","invalid password (use this harish,1234)")

       
def reset():
        username.delete(0,END)
        password.delete(0,END)
def main_screen():
    global root
    global username
    global password

    
    root = Tk()
    root.geometry('925x500+300+200')
    root.title("Login Screen")
    root.configure(bg="#fff")
    img = PhotoImage(file='.\project photo\download (2).png')
    root.iconphoto(False,img)
    root.resizable(False,False)
    lab = Label(root,text="Welcome to Home management!",font=('Calibri(Body)',15),fg='blue',bg='white').pack(padx=30,pady=30)

    img1 = PhotoImage(file=r'.\project photo\download.png')
    Label(root,image=img1,bg="white").place(x=50,y=90)

    frm=Frame(root,width=350,height=350,bg="white")
    frm.place(x=480,y=70)

    heading = Label(frm,text="sign in",bg = 'white',font=("Microsoft YaHei UI Light",23,'bold'),fg='blue')
    heading.place(x=100,y=5)
    def on_enter(e):
        username.delete(0,'end')
    def on_leave(e):
        user=username.get()
        if user =='':
            username.insert(0,'username')
    username= Entry(frm,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
    username.place(x=30,y=80)
    username.insert(0,'username')
    username.bind('<FocusIn>',on_enter)
    username.bind('<FocusOut>',on_leave)


    Frame(frm,width=295,height=2,bg='black').place(x=30,y=100)
    def on_enter(e):
        password.delete(0,'end')
    def on_leave(e):
        passw=password.get()
        if passw =='':
            password.insert(0,'password')

    password = Entry(frm,width=25,bg='white',border=0,fg='black',font=("Microsoft YaHei UI Light",11),show="*")
    password.place(x=30,y=150)

    password.insert(0,'Password')
    password.bind('<FocusIn>',on_enter)
    password.bind('<FocusOut>',on_leave)
    Frame(frm,width=295,height=2,bg='black').place(x=30,y=170)

    Button(frm,width=35,height=1,bg='#57a1f8',text="Sign in",fg='white',font=("Microsoft YaHei UI Light",11),command=login).place(x=35,y=220)
    Button(frm,width=6,height=1,bg='white',text="Reset",fg='blue',border=0,font=("Microsoft YaHei UI Light",11),command=reset).place(x=35,y=270)
    Button(frm,width=6,height=1,bg='white',text="Clear",border=0,fg='blue',font=("Microsoft YaHei UI Light",11),command=root.destroy).place(x=35,y=300)
    mainloop()
main_screen()
 


