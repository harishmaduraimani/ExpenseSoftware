from tkinter import*
from tkinter import messagebox

          
def income():
    screen1=Toplevel(screen)
    screen1.geometry("925x500+300+200")
    screen1.title("Income")
    img15=PhotoImage(file=r'.\project photo\images.png')
    screen1.iconphoto(False,img15)
    labell1=Label(screen1)
    labell1.place(relx=0, rely=0, width=925, height=500)
    img8 = PhotoImage(file=r'.\project photo\Picsart_22-11-24_06-00-59-263 - Copy.png')
    labell1.configure(image=img8)
    mainloop()
def expanse():
    screen2=Toplevel(screen)
    screen2.geometry("925x500+300+200")
    screen2.title("Expanse")
    img14=PhotoImage(file=r'.\project photo\download (1).png')
    screen2.iconphoto(False,img14)
    labell2=Label(screen2)
    labell2.place(relx=0, rely=0, width=925, height=500)
    img9 = PhotoImage(file=r'.\project photo\Picsart_22-11-24_06-00-59-263 - Copy.png')
    labell2.configure(image=img9)
    mainloop()
def data():
    screen3=Toplevel(screen)
    screen3.geometry("925x500+300+200")
    screen3.title("Data")
    labell3=Label(screen3)
    labell3.place(relx=0, rely=0, width=925, height=500)
    img13=PhotoImage(file=r'.\project photo\tttttttttttttttttt.png')
    screen3.iconphoto(False,img13)
    img10 = PhotoImage(file=r'.\project photo\Picsart_22-11-24_06-00-59-263 - Copy.png')
    labell3.configure(image=img10)
    mainloop()
def aboutus():
    screen4=Toplevel(screen)
    screen4.geometry("925x500+300+200")
    screen4.title("About Us")
    img12=PhotoImage(file=r'.\project photo\istockphoto-1284520409-612x612.png')
    screen4.iconphoto(False,img12)
    labell4=Label(screen4)
    labell4.place(relx=0, rely=0, width=925, height=500)
    img11 = PhotoImage(file=r'.\project photo\Picsart_22-11-24_06-00-59-263 - Copy.png')
    labell4.configure(image=img11)
    mainloop()
    
def login():
    global screen
    user=username.get()
    code=password.get()
    if user=="harish" and code=="1234":
        screen=Toplevel(root)
        screen.geometry('925x500+300+200')
        screen.title("Home Management(Main)")
        label1 = Label(screen)
        label1.place(relx=0, rely=0, width=925, height=500)
        img = PhotoImage(file=r'.\project photo\Picsart_22-11-24_06-01-35-065.png')
        label1.configure(image=img)
 
        img2 = PhotoImage(file=r'.\project photo\download.png')
        screen.iconphoto(False,img2)
        screen.resizable(False,False)
        img3 = PhotoImage(file=r'.\project photo\Picsart_22-11-23_19-28-09-892 (2) (1).png')
        img4 = PhotoImage(file=r'.\project photo\Picsart_22-11-23_19-33-44-411 (1).png')
        img5 = PhotoImage(file=r'.\project photo\Picsart_22-11-23_19-37-57-868.png')
        img6 = PhotoImage(file=r'.\project photo\Picsart_22-11-23_19-38-32-694 (1).png')



        Button(screen,image=img3,border=2,command=income).place(x=100,y=200)
        Button(screen,image=img4,border=2,command=expanse).place(x=300,y=200)
        Button(screen,image=img5,border=2,command=data).place(x=500,y=200)
        Button(screen,image=img6,border=2,command=aboutus).place(x=700,y=200)
    
        mainloop()
        
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
img = PhotoImage(file=r'.\project photo\download (2).png')
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
main_screen()
 


