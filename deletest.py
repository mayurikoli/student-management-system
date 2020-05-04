from tkinter import*
import mysql.connector
from tkinter import messagebox
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mydatabase")
mycursor=mydb.cursor()
def delete_re():
	root6=Tk()
	root6.geometry("600x400")
	root6.config(background="light green")
	rollL=Label(root6,text="Enter ROLLNO: ")
	rollE=Entry(root6,text="Enter RollNo: ")
	rollL.grid(row=2,column=4,padx="10")
	rollE.grid(row=3,column=5,ipadx="100",ipady="10",pady="10")
	Button(root6,text="DELETEST",bg="red",command=lambda:deletere(rollE)).grid(row=5,column=4,ipadx="50",ipady="20",pady="10")
	root6.mainloop()
def deletere(rollE):
	fl=0
	f5=0
	a=rollE.get()
	print(a)
	sql="SELECT * FROM STUDENT WHERE rollno=%s"
	val=(a,)

	mycursor.execute(sql,val)
	myresult=mycursor.fetchall()
	if rollE.get()=="":
		f1=1
		messagebox.showinfo("invalide","plz Enter valide RollNo....")
		print("invalide")
	else:
		print(a)
		sql="DELETE FROM student WHERE rollno=%s"
		adr1=(a,)
		mycursor.execute(sql,adr1)
		mydb.commit()
		f5=1
		f1=0
		
	if f5==1:
		messagebox.showinfo("valide","delete Successfully....")
	if f5==0:
		messagebox.showinfo("invalide","Invalide")
		




		
	