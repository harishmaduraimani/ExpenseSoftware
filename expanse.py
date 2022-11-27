from tkinter import*
from tkinter import messagebox
from tkinter import Label
from tkinter import ttk
from datetime import datetime
from time import strftime
format = "%d-%m-%Y"
def checki():
    f=rdate.get()
    a=edate.get()
    try:
        datetime.strptime(a, format)
        datetime.strptime(f, format)
        c=int(amounti.get())
        
    except ValueError:
        messagebox.showerror("invalid","Check whether Amount in Number or date in DD-MM-YYY format")
        rDate.delete(0,END)
        eDate.delete(0,END)
        amoi.delete(0,END)
        ode.delete(0,END)
        sn.delete(0,END)
        bn.delete(0,END)
        tote.delete(0,END)
        catt.delete(0,END)
       



def save():
    checki()
    
    f=rdate.get()
    a=edate.get()
    b=income11.get()
    d=tote.get()
    f=Storename.get()
    g=billno.get()
    ci=amounti.get()
    e=otherdescription.get()
    if f=="" and a=="" and b=="" and ci=="" and d==""and g=="" and f=="":
        messagebox.showerror("invalid","No Save")

       
    else:
        messagebox.showerror("invalid","No data to Save")



def export():
    messagebox.showerror("invalid","invalid username and password (use this harish,1234)")
def Import():
    messagebox.showerror("invalid","invalid username and password (use this harish,1234)")
def add():
    rDate.delete(0,END)
    eDate.delete(0,END)
    amoi.delete(0,END)
    ode.delete(0,END)
    sn.delete(0,END)
    bn.delete(0,END)
    tote.delete(0,END)
    catt.delete(0,END)
    

def total():
    messagebox.showerror("invalid","invalid username and password (use this harish,1234)")
def search():
    messagebox.showerror("invalid","invalid username and password (use this harish,1234)")
def back():
    messagebox.showerror("invalid","invalid username and password (use this harish,1234)")
    
def screen():
    global screen2
    global rdate
    global smonth
    global edate
    global income11
    global otherdescription
    global Storename
    global amounti
    global billno
    global tote
    global catt
    global rDate
    global monthl
    global eDate
    global amoi
    global Normal
    global Monthly
    global sn
    global bn
    global ode
    
    
    
    
    
    
    
    
    
    
#---------------------------Creating TK Mamin screen--------------------------------#
screen2=Tk()
screen2.geometry("925x500+300+200")
screen2.title("Home Management(Expanse)")
screen2.resizable(False,False)
img21=PhotoImage(file=r'.\project photo\download (1).png')
screen2.iconphoto(False,img21)
lable11=Label(screen2)
lable11.place(relx=0, rely=0, width=925, height=500)
img22 = PhotoImage(file=r'.\project photo\Picsart_22-11-24_06-00-59-263 - Copy.png')
lable11.configure(image=img22)
#------------------------------------------------------------------------------------#


#------------------------------------frames in main screen----------------------------#
frame11=Frame(screen2,bg='white',width=875,height=450).place(x=25,y=25)
lable11=Label(frame11,text="Expanse",bg="white",fg="black",font=("times new roman",25,"bold")).place(x=400,y=50)

framelable11=LabelFrame(frame11,text="Details",bg="white",fg="black",font=("times new roman",10,"bold"))
framelable11.place(x="27",y="100",width='870',height='50')

framelable12=LabelFrame(frame11,text="Expanse",bg="white",fg="black",font=("times new roman",10,"bold"))
framelable12.place(x="27",y="150",width='400',height='320')

framelable13=LabelFrame(frame11,text="Gentrate",bg="white",fg="black",font=("times new roman",10,"bold"))
framelable13.place(x="450",y="150",width='110',height='320')
#--------------------------------------------------------------------------------------#

#-----------------------------------FRAMELABLE11---------------------------------------#
lable12=Label(frame11,text="Date:",bg="white",fg="black",font=("times new roman",10,"bold")).place(x=30,y=120)
lable13=Label(frame11,text="Month:",bg="white",fg="black",font=("times new roman",10,"bold")).place(x=250,y=120)
lable14=Label(frame11,text="Details:",bg="white",fg="black",font=("times new roman",10,"bold")).place(x=500,y=120)

frame12=Frame(frame11,bg="black",width=180,height=2).place(x=65,y=140)
frame13=Frame(frame11,bg="black",width=180,height=2).place(x=300,y=140)
frame14=Frame(frame11,bg="black",width=180,height=2).place(x=570,y=140)

img23 = PhotoImage(file=r'.\project photo\Picsart_22-11-26_05-49-32-004.png')
button1=Button(frame11,image=img23,border=0,command=search).place(x=750,y=115)

rdate=StringVar()
rmonth=StringVar()

def on_enter(e):
    rDate.delete(0,'end')
def on_leave(e):
    user=rDate.get()
    if user =='':
        rDate.insert(0,'Date')

rDate= Entry(frame11,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",9),textvariable=rdate)
rDate.place(x=65,y=120)
rDate.insert(0,'Date(DD-MM-YYY)')
rDate.bind('<FocusIn>',on_enter)
rDate.bind('<FocusOut>',on_leave)


rn=['Jan','Feb','mar','apr','may','june','july','Aug','Sep','Oct','Nov','Dec']
monthl = OptionMenu(screen2 , rmonth , *rn )
monthl.place(x="320",y="120",width="140",height="20")
rmonth.set("Jan")

rm=['Jan','Feb','mar','apr','may','june','july','Aug','Sep','Oct','Nov','Dec']
smonth = ttk.Combobox(screen2 ,values=rm ,width=20)
smonth.grid(padx=590,pady=120)
smonth.set("Jan")

#--------------------------------------------------------------------------------------#\


#----------------------------------clock and logout------------------------------------#
   
clock = Label(screen2,font=("times new roman",12),fg="black",bg="white")
clock.place(x=775, y=50, width=102, height=36)
def get_time():
        timeVar = strftime("%H:%M:%S %p")
        clock.config(text=timeVar)
        clock.after(1000, get_time)
get_time()
img29 = PhotoImage(file=r'.\project photo\Picsart_22-11-25_08-46-45-143.png')
button8=Button(frame11,image=img29,command=screen2.destroy,border=0).place(x=30,y=65)

img30 = PhotoImage(file=r'.\project photo\images (1) (1).png')
button9=Button(frame11,image=img30,border=0,command=back).place(x=30,y=35)
#-------------------------------------------------------------------------------------#

img24 = PhotoImage(file=r'.\project photo\Picsart_22-11-26_06-04-13-834.png')
img25 = PhotoImage(file=r'.\project photo\Picsart_22-11-26_05-48-48-470.png')
img26 = PhotoImage(file=r'.\project photo\Picsart_22-11-26_05-47-30-520.png')
img27 = PhotoImage(file=r'.\project photo\Picsart_22-11-26_05-47-03-224.png')
img28 = PhotoImage(file=r'.\project photo\Picsart_22-11-26_05-46-15-207.png')

button2=Button(frame11,image=img24,border=0,command=save).place(x=455,y=200)
button4=Button(frame11,image=img25,border=0,command=add).place(x=455,y=250)
button5=Button(frame11,image=img26,border=0,command=export).place(x=455,y=300)
button6=Button(frame11,image=img27,border=0,command=Import).place(x=455,y=350)
button7=Button(frame11,image=img28,border=0,command=total).place(x=455,y=400)




#------------------------------------------Expanse Details----------------------------#
#
expansedata1=Label(framelable12,text="Date:",font=("times new roman",10),bg="white",fg="black")
expansedata2=Label(framelable12,text="Catagory:",font=("times new roman",10),bg="white",fg="black")
expansedata3=Label(framelable12,text="Amount in INR:",font=("times new roman",10),bg="white",fg="black")
expansedata4=Label(framelable12,text="Type of Transation:",font=("times new roman",10),bg="white",fg="black")
expansedata5=Label(framelable12,text="Type of Expanse:",font=("times new roman",10),bg="white",fg="black")
expansedata6=Label(framelable12,text="Store Name:",font=("times new roman",10),bg="white",fg="black")
expansedata7=Label(framelable12,text="Bill:",font=("times new roman",10),bg="white",fg="black")
expansedata8=Label(framelable12,text="Other description:",font=("times new roman",10),bg="white",fg="black")

expansedata1.grid(row=1,column=0,padx=3,pady=5)
expansedata2.grid(row=2,column=0,padx=3,pady=6)
expansedata3.grid(row=3,column=0,padx=3,pady=7)
expansedata4.grid(row=4,column=0,padx=3,pady=8)
expansedata5.grid(row=5,column=0,padx=3,pady=9)
expansedata6.grid(row=6,column=0,padx=3,pady=10)
expansedata7.grid(row=7,column=0,padx=3,pady=11)
expansedata8.grid(row=8,column=0,padx=3,pady=12)

frame15=Frame(frame11,bg="black",width=180,height=2).place(x=150,y=190)
frame17=Frame(frame11,bg="black",width=180,height=2).place(x=150,y=220)
frame18=Frame(frame11,bg="black",width=180,height=2).place(x=150,y=260)
frame19=Frame(frame11,bg="black",width=180,height=2).place(x=150,y=300)
frame20=Frame(frame11,bg="black",width=180,height=2).place(x=150,y=380)
frame21=Frame(frame11,bg="black",width=180,height=2).place(x=150,y=420)
frame22=Frame(frame11,bg="black",width=180,height=2).place(x=150,y=460)
#
edate=StringVar()
income11=StringVar()
Storename=StringVar()
otherdescription=StringVar()
amounti=IntVar()
billno=StringVar()
def on_enter2(e):
    eDate.delete(0,'end')
def on_leave2(e):
    user=eDate.get()
    if user =='':
        eDate.insert(0,'Date')

eDate= Entry(frame11,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",9),textvariable=edate)
eDate.place(x=150,y=170)
eDate.insert(0,'Date(DD-MM-YYY)')
eDate.bind('<FocusIn>',on_enter2)
eDate.bind('<FocusOut>',on_leave2)

cat=['Veg','Fruit','groceries','Entertiment','stationary','home decor']
catt = ttk.Combobox(frame11 ,values=cat ,width=20)
catt.place(x=150,y=200)
catt.set("Veg")

def on_enter2(e):
    amoi.delete(0,'end')
def on_leave2(e):
    user=amoi.get()
    if user =='':
        amoi.insert(0,'Amount(INR)')
    

amoi= Entry(frame11,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",9),textvariable=amounti)
amoi.place(x=150,y=240)
amoi.insert(0,'Amount(INR)')
amoi.bind('<FocusIn>',on_enter2)
amoi.bind('<FocusOut>',on_leave2)

ttte=['Gpay','Bank','Loan','Card','Cash']
tote = ttk.Combobox(frame11 ,values=ttte ,width=20)
tote.place(x=150,y=280)
tote.set("Gpay")

Normal=Radiobutton(frame11,text='Normal',variable=income11,value="Normal")
Normal.place(x=150,y=315)
Monthly=Radiobutton(frame11,text='Monthly',variable=income11,value="Monthly Expanse")
Monthly.place(x=230,y=315)

def on_enter2(e):
    sn.delete(0,'end')
def on_leave2(e):
    user=sn.get()
    if user =='':
        sn.insert(0,'Store Name')

sn= Entry(frame11,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",9),textvariable=Storename)
sn.place(x=150,y=355)
sn.insert(0,'Store Name')
sn.bind('<FocusIn>',on_enter2)
sn.bind('<FocusOut>',on_leave2)

def on_enter2(e):
    bn.delete(0,'end')
def on_leave2(e):
    user=bn.get()
    if user =='':
        bn.insert(0,'Bill no ')

bn= Entry(frame11,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",9),textvariable=billno)
bn.place(x=150,y=400)
bn.insert(0,'Bill no')
bn.bind('<FocusIn>',on_enter2)
bn.bind('<FocusOut>',on_leave2)


def on_enter2(e):
    ode.delete(0,'end')
def on_leave2(e):
    user=ode.get()
    if user =='':
        ode.insert(0,'Other details')

ode= Entry(frame11,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",9),textvariable=otherdescription)
ode.place(x=150,y=440)
ode.insert(0,'Other details')
ode.bind('<FocusIn>',on_enter2)
ode.bind('<FocusOut>',on_leave2)
#--------------------------------------------------------------------------------------------------------------------------#

#------------------------------------generframe----------------------------------------------------------------------------#
def welcome():
    textarea.delete(1.0,END)
    textarea.insert(END,'''\t         Welcome to income office!
                                         see your income''')
    
    textarea.insert(END,f"\nMonth:\t{month.get()}")
    textarea.insert(END,f"\nDat.\t{date1.get()}")
    textarea.insert(END,f"\n\n============================================")
    textarea.insert(END,"\nDate\tAmount\t\tIncome\t\tmode")
    textarea.insert(END,f"\n============================================\n")
    textarea.configure(font='arial 10')



l=Frame(screen2,relief=GROOVE,bd=10)
l.place(x=600,y=150,width=300,height=300)

bill_title=Label(l,text='Home Management',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(l,orient='vertical')
scrol_x=Scrollbar(l,orient='horizontal')
textarea=Text(l,yscrollcommand=scrol_y.set,xscrollcommand=scrol_x.set)
scrol_y.pack(side=RIGHT,fill='y')
scrol_x.pack(side=BOTTOM,fill='x')
scrol_y.config(command=textarea.yview)
scrol_x.config(command=textarea.xview)
textarea.pack()
welcome()
#------------------------------------------------------------------------------------------------------------------------#








    

mainloop()
