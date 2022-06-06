from tkinter import *

root = Tk()
icon = PhotoImage(file='manager icon.png')
root.iconphoto(False, icon)
root.title(' my_manager')
root.geometry('300x500')
root.minsize(300,400)
root.resizable(True, True)


savat           =''
def yana():
	Kurs        =name.get()
	Davomiyligi =name2.get()
	Narx        =name3.get()
	Vaqti       =name4.get()

	global savat

	savat +=f" \nKurs nomi: {Kurs}."
	savat +=f" \nKurs davomiyligi: {Davomiyligi}."
	savat +=f" \nKurs narxi: {Narx}."
	savat +=f" \nKurs vaqti: {Vaqti}.\n "

	name.delete(0,END)
	name2.delete(0,END)
	name3.delete(0,END)
	name4.delete(0,END)

def ochir():
	name. delete(0,END)
	name2.delete(0,END)
	name3.delete(0,END)
	name4.delete(0,END)
	
	global savat
	global final
	
	final.destroy()
	savat =''

def satr():
	name. delete(0,END)
	name2.delete(0,END)
	name3.delete(0,END)
	name4.delete(0,END)

def res():
	Kurs        =name. get()
	Davomiyligi =name2.get()
	Narx        =name3.get()
	Vaqti       =name4.get()

	global savat
	global final

	savat +=f" \nKurs nomi: {Kurs}."
	savat +=f" \nKurs davomiyligi: {Davomiyligi}."
	savat +=f" \nKurs narxi: {Narx}."
	savat +=f" \nKurs vaqti: {Vaqti}.\n "
	
	final  =Label(text=f"Bizda mavjud kurslar ro'yhati \n{savat}", bg='#103DA4', fg='white')
	final.grid(row='9', column='1')
	
	name. delete(0,END)
	name2.delete(0,END)
	name3.delete(0,END)
	name4.delete(0,END)


name   =Entry(root)
name2  =Entry(root)
name3  =Entry(root)
name4  =Entry(root)
namee  =Label(font='Arial 9 bold', text="Kurs")
namee2 =Label(font='Arial 9 bold', text='Davomiyligi ')
namee3 =Label(font='Arial 9 bold', text='Narx ')
namee4 =Label(font='Arial 9 bold', text='Vaqti ')


name.  grid (row='0', column='1')
namee. grid (row='0', column='0')
name2. grid (row='1', column='1')
namee2.grid (row='1', column='0')
name3. grid (row='2', column='1')
namee3.grid (row='2', column='0')
name4. grid (row='3', column='1')
namee4.grid (row='3', column='0')


satr   =Button(bg='white',   fg='black',   font='Arial 9 bold',  command=satr,  text="Satrlarni tozalash")
ochir  =Button(bg='red',     fg='white',   font='Arial 11 bold', command=ochir, text="Tozalash" )
qayta  =Button(bg='#4a8abd', fg='white',   font='Arial 11 bold', command=yana,  text='Yangi kurs joylash',)
result =Button(bg='#72D538', fg='#1919ff', font='Arial 11 bold', command=res,   text='Tugatish')

satr.grid  (row='5',column='1', stick='we')
ochir.grid (row='6',column='1', stick='we')
result.grid(row='8',column='1', stick='we')
qayta.grid (row='7',column='1', stick='we')


root.mainloop()