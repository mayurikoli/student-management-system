from tkinter import*
import mysql.connector
from tkinter import messagebox
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mydatabase")
mycursor=mydb.cursor()



def up():
	root4=Tk()
	root4.geometry("700x500")
	root4.config(background="light green")
	rollL2=Label(root4,text="Enter RollNo: ")
	rollE2=Entry(root4,text="Enter RollNo: ")
	rollL2.grid(row=2,column=2,padx="10")
	rollE2.grid(row=2,column=3,ipadx="100",ipady="10",pady="10")
	
	Button(root4,text="FIND",bg="light blue",command=lambda:up1(rollE2,nameE2,contE2,marE2,emailE2)).grid(row=4,column=3,ipadx="50",ipady="20",pady="10")

	nameL2=Label(root4,text="Enter Name: ")
	nameE2=Entry(root4,text="")
	nameL2.grid(row=5,column=2,padx="10")
	nameE2.grid(row=5,column=3,pady="10",ipadx="100",ipady="10")
	
	contL2=Label(root4,text="Enter ContactNo: ")
	contE2=Entry(root4,text="Enter ContactNo: ")
	contL2.grid(row=6,column=2,padx="10")
	contE2.grid(row=6,column=3,ipadx="100",ipady="10",pady="10")

	marL2=Label(root4,text="Enter Marks: ")
	marE2=Entry(root4,text="Enter Marks: ")
	marL2.grid(row=7,column=2,padx="10")
	marE2.grid(row=7,column=3,ipadx="100",ipady="10",pady="10")
	
	emailL2=Label(root4,text="Enter Email: ")
	emailE2=Entry(root4,text="Enter Email: ")
	emailL2.grid(row=8,column=2,padx="10")
	emailE2.grid(row=8,column=3,ipadx="100",ipady="10",pady="10")
	
	
	
	
	
	Button(root4,text="UPDATEINFO",bg="light blue",command=lambda:updateinfo(rollE2,nameE2,contE2,marE2,emailE2)).grid(row=9,column=3,ipadx="50",ipady="20",pady="10")

	
	root4.mainloop()
def up1(rollE2,nameE2,contE2,marE2,emailE2):

	f1=0
	f5=0
	a=rollE2.get()
	print(a)
	sql="SELECT * FROM STUDENT WHERE rollno=%s"
	val=(a,)

	mycursor.execute(sql,val)
	myresult=mycursor.fetchall()
	if rollE2.get()=="":
		f1=1
		messagebox.showinfo("invalide","plz Enter valide RollNo....")
		print("invalide")
	else:
	
		
		for x in myresult:
			nameE2.insert(0,x[0])
			contE2.insert(0,x[2])
			marE2.insert(0,x[3])
			emailE2.insert(0,x[4])
			f1=1
	if f1==0:
		for x in myresult:
			if a==x[1]:
				f=1
		if f1==0:
				messagebox.showinfo("invalide","plz Enter valide RollNo....")

def updateinfo(rollE2,nameE2,contE2,marE2,emailE2):
	a=rollE2.get()
	print(a)
	b=nameE2.get()
	c=contE2.get()
	d=marE2.get()
	e=emailE2.get()
	'''rollE2.insert(0,a)
	nameE2.insert(0,b)
	contE2.insert(0,c)
	marE2.insert(0,d)
	emailE2.insert(0,e)'''
	sql="UPDATE student SET rollno=%s WHERE name=%s"
	val=(a,b)
	mycursor.execute(sql,val)
	mydb.commit()
	#messagebox.showinfo("updated","info Updated...........")
	sql="UPDATE student SET contact=%s WHERE name=%s"
	val=(c,b)
	mycursor.execute(sql,val)
	mydb.commit()
	#messagebox.showinfo("updated ","info Updated...........")
	sql="UPDATE student SET marks=%s WHERE name=%s"
	val=(d,b)
	mycursor.execute(sql,val)
	mydb.commit()
	#messagebox.showinfo("updated ","info Updated...........")
	sql="UPDATE student SET email=%s WHERE name=%s"
	val=(e,b)
	mycursor.execute(sql,val)
	mydb.commit()
	messagebox.showinfo("updated ","info Updated...........")






	