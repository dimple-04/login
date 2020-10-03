from tkinter import*

#--------window--------
window=Tk()

window.title("selmon boi fan club")
window. configure(bg="Black")

#------labels---------
Label(window,text="Fname",bg="BLACK",fg="ORANGE",font='none 10 bold') .grid(row=0,column=0, sticky=W)

Label(window,text="",bg='black') .grid(row=1,column=0)

Label(window,text="Lname",bg="BLACK",fg="ORANGE",font='none 10 bold') .grid(row=2,column=0, sticky=W)

Label(window,text="",bg='black') .grid(row=3,column=0)

Label(window,text="Email-ID",bg="BLACK",fg="ORANGE",font='none 10 bold') .grid(row=4,column=0, sticky=W)

Label(window,text="",bg='black') .grid(row=5,column=0)

Label(window,text="Password  ",bg="BLACK",fg="ORANGE",font='none 10 bold') .grid(row=6,column=0, sticky=W)

Label(window,text="",bg='black') .grid(row=7,column=0)

#------entries-------
Efname=Entry(window,bd=9,font='none 10 bold')
Efname.grid(row=0,column=1)


Elname=Entry(window,bd=9,font='none 10 bold')
Elname.grid(row=2 ,column=1)


Euserid=Entry(window,bd=9,font='none 10 bold')
Euserid.grid(row=4,column=1)

Epass=Entry(window,bd=9,font='none 10 bold')
Epass.grid(row=6,column=1)

#------loginkey------
loginbutton=Button(window,text="SIGNIN",bg="grey",fg="black",bd=10,)
loginbutton.grid(row=15, column=1,sticky=W)

#------exit label-----
Label(window,text='\nClick here to Exit:',bg='black',fg='orange',font='none 10 bold') .grid(row=17,column=0)

#------exit Function-----
def close_window():
	window.destroy()
	exit()
	
#------exit button-------
exitbutton=Button(window,text="EXIT",bg='grey',fg='green',bd=10, command=close_window)
exitbutton.grid(row=18,column=0)

window.mainloop()