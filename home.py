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
def main_screen():
    global screen
screen= Tk()
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


main_screen()
