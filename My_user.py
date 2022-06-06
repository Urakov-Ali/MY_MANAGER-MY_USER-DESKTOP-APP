from tkinter import *

root = Tk()
#icon = PhotoImage(file='user.ico')
#root.iconphoto(False, icon)
root.title('   User_interface')
root.geometry('841x595')
root.minsize(400,300)
root.resizable(True, True)
root.config(bg='gray')

kurs =Label(root, bg='gray', fg='black',font='Arial 14 bold', text="O'quv markazda mavjud kurslar")
vaqt =Label(root, bg='gray', fg='black',font='Arial 14 bold', text="Dars vaqtlari")

kurs.grid(row='0', column='0', columnspan='13')
vaqt.grid(row='4', column='0', columnspan='13')

savat =''
narx  =''
vaqt  =''
def back():
	global savat
	global narx

	narx  =''
	savat =''
	savat +=f"\nKurs nomi: Back-end." 
	savat +=f"\nKurs davomiyligi: 5 oy."
	savat +=f"\nOylik to'lov: 600 000."
	narx  +=f"\nTo'liq kurs narxi: 3 000 000."
	
	front  ['state'] ='disabled'
	full   ['state'] ='disabled'
	flut   ['state'] ='disabled'
	smm    ['state'] ='disabled'
	pyt    ['state'] ='disabled'
	grdes  ['state'] ='disabled'
	mern   ['state'] ='disabled'

	
def front():
	global savat
	global narx
	narx  =''
	savat =''
	savat +=f"\nKurs nomi: Front-end."
	savat +=f"\nKurs davomiyligi: 5 oy."
	savat +=f"\nOylik to'lov: 600 000."
	narx  +=f"\nTo'liq kurs narxi: 3 000 000."

	back   ['state'] ='disabled'
	full   ['state'] ='disabled'
	flut   ['state'] ='disabled'
	smm    ['state'] ='disabled'
	pyt    ['state'] ='disabled'
	grdes  ['state'] ='disabled'
	mern   ['state'] ='disabled'
	
def full():
	global savat
	global narx

	narx  =''
	savat =''
	savat +=f"\nKurs nomi: Full-stack."
	savat +=f"\nKurs davomiyligi: 11 oy."
	savat +=f"\nOylik to'lov: 700 000."
	narx  +=f"\nTo'liq kurs narxi: 7 700 000."

	back   ['state'] ='disabled'
	front  ['state'] ='disabled'
	flut   ['state'] ='disabled'
	smm    ['state'] ='disabled'
	pyt    ['state'] ='disabled'
	grdes  ['state'] ='disabled'
	mern   ['state'] ='disabled'

def flut():
	global savat
	global narx

	narx  =''
	savat =''
	savat +=f"\nKurs nomi: Flutter."
	savat +=f"\nKurs davomiyligi: 6 oy."
	savat +=f"\nOylik to'lov: 500 000."
	narx  +=f"\nTo'liq kurs narxi: 3 000 000."
	
	back   ['state'] ='disabled'
	full   ['state'] ='disabled'
	front  ['state'] ='disabled'
	smm    ['state'] ='disabled'
	pyt    ['state'] ='disabled'
	grdes  ['state'] ='disabled'
	mern   ['state'] ='disabled'

def smm():
	global savat
	global narx

	narx  =''
	savat =''
	savat +=f"\nKurs nomi: SMM."
	savat +=f"\nKurs davomiyligi: 3 oy."
	savat +=f"\nOylik to'lov: 500 000."
	narx  +=f"\nTo'liq kurs narxi: 1 500 000."

	back   ['state'] ='disabled'
	front  ['state'] ='disabled'
	full   ['state'] ='disabled'
	flut   ['state'] ='disabled'
	pyt    ['state'] ='disabled'
	grdes  ['state'] ='disabled'
	mern   ['state'] ='disabled'
	
def pyt():
	global savat
	global narx

	narx  =''
	savat =''
	savat +=f"\nKurs nomi: Python."
	savat +=f"\nKurs davomiyligi: 6 oy."
	savat +=f"\nOylik to'lov: 600 000."
	narx  +=f"\nTo'liq kurs narxi: 3 600 000."

	back   ['state'] ='disabled'
	front  ['state'] ='disabled'
	full   ['state'] ='disabled'
	flut   ['state'] ='disabled'
	smm    ['state'] ='disabled'
	grdes  ['state'] ='disabled'
	mern   ['state'] ='disabled'

def grdes():
	global savat
	global narx

	narx  =''
	savat =''
	savat +=f"\nKurs nomi: Graphic-design."
	savat +=f"\nKurs davomiyligi: 4 oy."
	savat +=f"\nOylik to'lov: 600 000."
	narx  +=f"\nTo'liq kurs narxi: 2 400 000."

	back   ['state'] ='disabled'
	front  ['state'] ='disabled'
	full   ['state'] ='disabled'
	flut   ['state'] ='disabled'
	smm    ['state'] ='disabled'
	pyt    ['state'] ='disabled'
	mern   ['state'] ='disabled'


def mern():
	global savat
	global narx


	narx  =''
	savat =''
	savat +=f"\nKurs nomi: MERN."
	savat +=f"\nKurs davomiyligi: 4 oy."
	savat +=f"\nOylik to'lov: 600 000."
	narx  +=f"\nTo'liq kurs narxi: 2 400 000."

	back   ['state'] ='disabled'
	front  ['state'] ='disabled'
	full   ['state'] ='disabled'
	flut   ['state'] ='disabled'
	smm    ['state'] ='disabled'
	pyt    ['state'] ='disabled'
	grdes  ['state'] ='disabled'


def erta():
	 
	kech   ['state'] ='disabled'
	uch    ['state'] ='disabled'
	besh   ['state'] ='disabled'
	olti   ['state'] ='disabled'

def kech():
	erta   ['state'] ='disabled'
	toqqiz ['state'] ='disabled'
	onbr   ['state'] ='disabled'
	onikki ['state'] ='disabled'

def toqqiz():
	global vaqt

	vaqt =''
	vaqt   +=f"\nKurs vaqti: 9:00.\n "

	kech   ['state'] ='disabled'
	onbr   ['state'] ='disabled'
	onikki ['state'] ='disabled'
	uch    ['state'] ='disabled'
	besh   ['state'] ='disabled'
	olti   ['state'] ='disabled'	

def onbr():
	global vaqt

	vaqt   = ''
	vaqt   =f"\nKurs vaqti: 11:00.\n "

	erta   ['state'] ='disabled'
	kech   ['state'] ='disabled'
	toqqiz ['state'] ='disabled'
	onikki ['state'] ='disabled'
	uch    ['state'] ='disabled'
	besh   ['state'] ='disabled'
	olti   ['state'] ='disabled'

def onikki():
	global vaqt

	vaqt   =''
	vaqt   =f"\nKurs vaqti: 12:00.\n "
	
	erta   ['state'] ='disabled'
	kech   ['state'] ='disabled'
	toqqiz ['state'] ='disabled'
	onbr   ['state'] ='disabled'
	uch    ['state'] ='disabled'
	besh   ['state'] ='disabled'
	olti   ['state'] ='disabled'

def uch():
	global vaqt

	vaqt   =''
	vaqt   =f"\nKurs vaqti: 15:00.\n "
	
	erta   ['state'] ='disabled'
	kech   ['state'] ='disabled'
	toqqiz ['state'] ='disabled'
	onbr   ['state'] ='disabled'
	onikki ['state'] ='disabled'
	besh   ['state'] ='disabled'
	olti   ['state'] ='disabled'

def besh():
	global vaqt

	vaqt   =''
	vaqt   =f"\nKurs vaqti: 17:00.\n "

	erta   ['state'] ='disabled'	
	kech   ['state'] ='disabled'
	toqqiz ['state'] ='disabled'
	onbr   ['state'] ='disabled'
	onikki ['state'] ='disabled'
	uch    ['state'] ='disabled'
	olti   ['state'] ='disabled'

def olti():
	global vaqt

	vaqt   =''
	vaqt   =f"\nKurs vaqti: 18:30.\n "

	erta   ['state'] ='disabled'	
	kech   ['state'] ='disabled'
	toqqiz ['state'] ='disabled'
	onbr   ['state'] ='disabled'
	onikki ['state'] ='disabled'
	uch    ['state'] ='disabled'
	besh   ['state'] ='disabled'

def vaqt():
	
	erta   ['state'] ='normal'
	kech   ['state'] ='normal'
	toqqiz ['state'] ='normal'
	onbr   ['state'] ='normal'
	onikki ['state'] ='normal'
	uch    ['state'] ='normal'
	besh   ['state'] ='normal'
	olti   ['state'] ='normal'

def kurs():
	back   ['state'] ='normal'
	front  ['state'] ='normal'
	full   ['state'] ='normal'
	smm    ['state'] ='normal'
	flut   ['state'] ='normal'
	pyt    ['state'] ='normal'
	grdes  ['state'] ='normal'
	mern   ['state'] ='normal'

def res():
	res     =savat
	res    +=narx
	res    +=vaqt

	global ree
	ree     =Label(root, bg='#22CC00', fg='white',font='Arial 14 bold', borderwidth='1', relief="solid", text=f"\nTanlangan kurs: \n{res}")
	ree.grid(row='10', column='0', columnspan='13',stick='we')

def qayta():
	ree.destroy()

	back   ['state'] ='normal'
	front  ['state'] ='normal'
	full   ['state'] ='normal'
	smm    ['state'] ='normal'
	flut   ['state'] ='normal'
	pyt    ['state'] ='normal'
	grdes  ['state'] ='normal'
	mern   ['state'] ='normal'

	erta   ['state'] ='normal'
	kech   ['state'] ='normal'
	toqqiz ['state'] ='normal'
	onbr   ['state'] ='normal'
	onikki ['state'] ='normal'
	uch    ['state'] ='normal'
	besh   ['state'] ='normal'
	olti   ['state'] ='normal'



back   =Button( bg='#22CC00', fg='white',   font='Arial 12 bold', command=back,  text="                 Back-end             ")
front  =Button( bg='white',   fg='#22CC00', font='Arial 12 bold', command=front, text="                 Front-end            ")
full   =Button( bg='white',   fg='#22CC00', font='Arial 12 bold', command=full,  text="                 Full-stack           ")
flut   =Button( bg='#22CC00', fg='white',   font='Arial 12 bold', command=flut,  text="                 Flutter              ")
smm    =Button( bg='white',   fg='#22CC00', font='Arial 12 bold', command=smm,   text="                 SMM                  ")
pyt    =Button( bg='#22CC00', fg='white',   font='Arial 12 bold', command=pyt,   text="                 Python               ")
grdes  =Button( bg='white',   fg='#22CC00', font='Arial 12 bold', command=grdes, text="            Graphic-design            ")
mern   =Button( bg='#22CC00', fg='white',   font='Arial 12 bold', command=mern,  text="                 MERN                 ")

erta   =Button( bg='#22CC00', fg='white',   font='Arial 12 bold', command=erta,  text="Ertalabki")
kech   =Button( bg='#22CC00', fg='white',   font='Arial 12 bold', command=kech,  text="Kechki")

toqqiz =Button( bg='white',   fg='#22CC00', font='Arial 12 bold', command=toqqiz,text="9:00")
onbr   =Button( bg='white',   fg='#22CC00', font='Arial 12 bold', command=onbr,  text="11:00")
onikki =Button( bg='#22CC00', fg='white',   font='Arial 12 bold', command=onikki,text="12:00")
uch    =Button( bg='white',   fg='#22CC00', font='Arial 12 bold', command=uch,   text="15:00")
besh   =Button( bg='white',   fg='#22CC00', font='Arial 12 bold', command=besh,  text="17:00")
olti   =Button( bg='#22CC00', fg='white',   font='Arial 12 bold', command=olti,  text="18:30")

vaqt   =Button( bg='#22CC00', fg='white',   font='Arial 14 bold', command=vaqt,  text="Vaqtni o'zgartirish.")
kurs1  =Button( bg='#22CC00', fg='white',   font='Arial 14 bold', command=kurs,  text="Kursni o'zgartirish.")
res    =Button( bg='gray',    fg='white',   font='Arial 14 bold', command=res,   text="Yakunlash.")
qayta  =Button( bg='gray',    fg='white',   font='Arial 14 bold', command=qayta, text="Kursni qayta kiritish.")

back.grid  (row='2', column='0', stick='we', columnspan='3')
front.grid (row='2', column='3', stick='we', columnspan='3')
full.grid  (row='2', column='6', stick='we', columnspan='3')
flut.grid  (row='2', column='10',stick='we', columnspan='3')
smm.grid   (row='3', column='3', stick='we', columnspan='3')
pyt.grid   (row='3', column='0', stick='we', columnspan='3')
grdes.grid (row='3', column='6', stick='we', columnspan='3')
mern.grid  (row='3', column='10',stick='we', columnspan='3')

erta.grid  (row='5', column='0', stick='we', columnspan='3')
kech.grid  (row='6', column='0', stick='we', columnspan='3')

toqqiz.grid(row='5', column='3', stick='we', columnspan='3')
onbr.grid  (row='5', column='6', stick='we', columnspan='3')
onikki.grid(row='5', column='10',stick='we', columnspan='3')
uch.grid   (row='6', column='3', stick='we', columnspan='3')
besh.grid  (row='6', column='6', stick='we', columnspan='3')
olti.grid  (row='6', column='10',stick='we', columnspan='3')

vaqt.grid  (row='7', column='0',stick='we', columnspan='13')
kurs1.grid (row='1', column='0',stick='we', columnspan='13')
res.grid   (row='8', column='0',stick='we', columnspan='13')
qayta.grid (row='9', column='0',stick='we', columnspan='13')


root.mainloop()