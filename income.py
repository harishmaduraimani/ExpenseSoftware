from tkinter import*
from tkinter import messagebox
from tkinter import Label
from tkinter import ttk
from datetime import datetime
from time import strftime

format = "%d-%m-%Y"
def check():
    f=date1.get()
    a=Date1.get()
    b=income1.get()
    d=tot.get()
    e=otherdescription.get()
    
        
    try:
        datetime.strptime(a, format)
        datetime.strptime(f, format)
        c=int(amount.get()) 
    except ValueError:
        messagebox.showerror("invalid","Check whether Amount in Number or date in DD-MM-YYY format")
        drop.delete(0,END)
        Date.delete(0,END)
        Date1.delete(0,END)
        amo.delete(0,END)
        tot.delete(0,END)
        od.delete(0,END)
        income1.delete(0,END)
#search button
def search():
    monthname=drop.get()
    if monthname=="January":
        messagebox.showerror("invalid","invalid username and password (use this harish,1234)")

#searchbutton
def add():
        
        drop.delete(0,END)
        Date.delete(0,END)
        Date1.delete(0,END)
        amo.delete(0,END)
        tot.delete(0,END)
        od.delete(0,END)


        
#
def save():
    check()
    
    f=date1.get()
    a=Date1.get()
    b=income1.get()
    d=tot.get()
    c=amount.get()
    l.append(c)
    e=otherdescription.get()
    if f!="" and a!="" and b!="" and c!="" and d!="":
        textarea.insert((10.0+float(len(l)-1)), f"{a}\t{b}\t{d}\t{c}\n")
       
    else:
        messagebox.showerror("invalid","No data to Save")
        
        

def Import():
    messagebox.showerror("invalid","invalid username and password (use this harish,1234)")
def total():
    j=sum(l)
    if date1.get() == "" or month.get() == "":
        messagebox.showerror("Error", "Customer detail are must")
    else:
        textAreaText = textarea.get(10.0,(10.0+float(len(l))))
        welcome()
        textarea.insert(END, textAreaText)
        textarea.insert(END, f"\n======================================")
        textarea.insert(END, f"\nTotal income  :\t\t{j}")
        textarea.insert(END, f"\n\n======================================")
        
def export():
    op=messagebox.askyesno("Save bill","Do you want t o save the Bill?")
    if op>0:
        incomedetails=textarea.get('1.0',END)
        f1=open('.\home'+ str(month.get())+'.txt','w')
        f1.write(incomedetails)
        f1.close()
        messagebox.showinfo("Saved",f"month, :{month.get()} Saved Successfully")
    else:
        return

#
def screen():
    global l

    global date1
    global month
    global drop
    global screen1
    global Salary
    global Date1
    global Date
    global amo
    global tot
    global od
    global drop1
    global amount
    

screen1=Tk()
screen1.geometry("925x500+300+200")
screen1.title("Income")
screen1.resizable(False,False)
img15=PhotoImage(file=r'.\project photo\images.png')
screen1.iconphoto(False,img15)
labell1=Label(screen1)
labell1.place(relx=0, rely=0, width=925, height=500)
img8 = PhotoImage(file=r'.\project photo\Picsart_22-11-24_06-00-59-263 - Copy.png')
labell1.configure(image=img8)
#
l=[]


#bases
frame1=Frame(screen1,bg='white',width=875,height=450).place(x=25,y=25)
label=Label(frame1,text="Income",bg="white",fg="black",font=("times new roman",25,"bold")).place(x=400,y=50)

label2=LabelFrame(frame1,text="Details",bg="white",fg="black",font=("times new roman",10,"bold"))
label2.place(x="27",y="100",width='870',height='50')

label3=LabelFrame(frame1,text="Income",bg="white",fg="black",font=("times new roman",10,"bold"))
label3.place(x="27",y="150",width='400',height='250')


label5=LabelFrame(frame1,text="Gentrate",bg="white",fg="black",font=("times new roman",10,"bold"))
label5.place(x="27",y="400",width='400',height='50')
#base

#first frame
lable2=Label(frame1,text="Date:",bg="white",fg="black",font=("times new roman",10,"bold")).place(x=30,y=120)
lable3=Label(frame1,text="Month:",bg="white",fg="black",font=("times new roman",10,"bold")).place(x=250,y=120)
lable4=Label(frame1,text="Month Name:",bg="white",fg="black",font=("times new roman",10,"bold")).place(x=500,y=120)
frame2=Frame(frame1,bg="black",width=180,height=2).place(x=65,y=140)
frame3=Frame(frame1,bg="black",width=180,height=2).place(x=300,y=140)
frame4=Frame(frame1,bg="black",width=180,height=2).place(x=570,y=140)
#
img21 = PhotoImage(file=r'.\project photo\Picsart_22-11-25_08-42-15-804.png')
img22 = PhotoImage(file=r'.\project photo\Picsart_22-11-25_08-39-09-391.png')
img24 = PhotoImage(file=r'.\project photo\Picsart_22-11-25_08-41-30-210.png')
img25 = PhotoImage(file=r'.\project photo\Picsart_22-11-25_08-43-29-154.png')
img26 = PhotoImage(file=r'.\project photo\Picsart_22-11-25_08-43-57-164.png')
img27 = PhotoImage(file=r'.\project photo\Picsart_22-11-25_08-44-58-406.png')
img28 = PhotoImage(file=r'.\project photo\Picsart_22-11-25_08-46-45-143.png')
button1=Button(frame1,image=img21,command=search,border=0).place(x=740,y=110)
button2=Button(frame1,image=img22,command=save,border=0).place(x=50,y=360)
button4=Button(frame1,image=img24,command=add,border=0).place(x=250,y=360)
button5=Button(frame1,image=img25,command=export,border=0).place(x=50,y=415)
button6=Button(frame1,image=img26,command=Import,border=0).place(x=150,y=415)
button7=Button(frame1,image=img27,command=total,border=0).place(x=250,y=415)
button8=Button(frame1,image=img28,command=screen1.destroy,border=0).place(x=30,y=50)
#
#first base
#clock        
clock = Label(screen1,font=("times new roman",12),fg="black",bg="white")
clock.place(x=775, y=50, width=102, height=36)
def get_time():
        timeVar = strftime("%H:%M:%S %p")
        clock.config(text=timeVar)
        clock.after(1000, get_time)
get_time()
#clock
#entry

date1=StringVar()
month=StringVar()
def on_enter(e):
    Date.delete(0,'end')
def on_leave(e):
    user=Date.get()
    if user =='':
        Date.insert(0,'Date')

Date= Entry(frame1,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",9),textvariable=date1)
Date.place(x=65,y=120)
Date.insert(0,'Date(DD-MM-YYY)')
Date.bind('<FocusIn>',on_enter)
Date.bind('<FocusOut>',on_leave)


n=['January','Febuary','march','april','may','june','july','Aug','Sep','Oct','Novem','Dec']
drop1 = OptionMenu(screen1 , month , *n )
drop1.place(x="320",y="120",width="140",height="20")
month.set("January")

m=['January','Febuary','march','april','may','june','july','Aug','Sep','Oct','Novem','Dec']
drop = ttk.Combobox(screen1 ,values=m ,width=20)
drop.grid(padx=590,pady=120)
drop.set("January")


#firt entry

#income
date=StringVar()
income1=StringVar()
amount=IntVar()
typeoftransation=StringVar()
otherdescription=StringVar()

                
                
                
#
incomedata1=Label(label3,text="Date:",font=("times new roman",10),bg="white",fg="black")
incomedata2=Label(label3,text="Income:",font=("times new roman",10),bg="white",fg="black")
incomedata3=Label(label3,text="Amount in INR:",font=("times new roman",10),bg="white",fg="black")
incomedata4=Label(label3,text="Type of Transation:",font=("times new roman",10),bg="white",fg="black")
incomedata5=Label(label3,text="Other description:",font=("times new roman",10),bg="white",fg="black")
incomedata1.grid(row=1,column=0,padx=3,pady=5)
incomedata2.grid(row=3,column=0,padx=3,pady=7)
incomedata3.grid(row=5,column=0,padx=3,pady=9)
incomedata4.grid(row=7,column=0,padx=3,pady=11)
incomedata5.grid(row=9,column=0,padx=3,pady=13)
frame5=Frame(frame1,bg="black",width=180,height=2).place(x=150,y=190)

frame7=Frame(frame1,bg="black",width=180,height=2).place(x=150,y=270)
frame8=Frame(frame1,bg="black",width=180,height=2).place(x=150,y=310)
frame9=Frame(frame1,bg="black",width=180,height=2).place(x=150,y=355)
#

    
def on_enter(e):
    Date1.delete(0,'end')
def on_leave(e):
    user=Date1.get()
    if user =='':
        Date1.insert(0,'Date')

Date1= Entry(frame1,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",9),textvariable=date)
Date1.place(x=150,y=170)
Date1.insert(0,'Date(DD-MM-YYY)')
Date1.bind('<FocusIn>',on_enter)
Date1.bind('<FocusOut>',on_leave)


Salary=Radiobutton(frame1,text='Salary',variable=income1,value="Salary")
Salary.place(x=150,y=205)
Otherincome=Radiobutton(frame1,text='Other Income',variable=income1,value="Other income")
Otherincome.place(x=230,y=205)

def on_enter(e):
    amo.delete(0,'end')
def on_leave(e):
    user=amo.get()
    if user =='':
        amo.insert(0,'Amount(INR)')

amo= Entry(frame1,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",9),textvariable=amount)
amo.place(x=150,y=250)
amo.insert(0,'Amount(INR)')
amo.bind('<FocusIn>',on_enter)
amo.bind('<FocusOut>',on_leave)



ttt=['Gpay','Bank','Loan','Card','Cash']
tot = ttk.Combobox(frame1 ,values=ttt ,width=20)
tot.place(x=150,y=290)
tot.set("Gpay")


def on_enter(e):
    od.delete(0,'end')
def on_leave(e):
    user=od.get()
    if user =='':
        od.insert(0,'Other details')

od= Entry(frame1,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",9),textvariable=otherdescription)
od.place(x=150,y=335)
od.insert(0,'Other details')
od.bind('<FocusIn>',on_enter)
od.bind('<FocusOut>',on_leave)


#
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
#


label4=Frame(frame1,relief=GROOVE,bd=10)
label4.place(x=495,y=150,width=400,height=300)

bill_title=Label(label4,text='Home Management',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(label4,orient=VERTICAL)
textarea=Text(label4,yscrollcommand=scrol_y)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack()
welcome()
#





screen()
