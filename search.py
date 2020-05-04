from tkinter import*
import mysql.connector
from tkinter import messagebox
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mydatabase")
mycursor=mydb.cursor()
def serchst():
	root=Tk()
	root.geometry("700x500")
	root.config(background="light green")
	rollL=Label(root,text="Enter RollNo: ")
	rollE=Entry(root,text="Enter RollNo: ")
	rollL.grid(row=2,column=2,padx="10")
	rollE.grid(row=2,column=3,ipadx="100",ipady="10",pady="10")
	
	Button(root,text="SEARCH",bg="light blue",command=lambda:serchst1(rollE,nameE,contE,marE,emailE)).grid(row=4,column=3,ipadx="50",ipady="20",pady="10")
	nameL=Label(root,text="Enter Name: ")
	nameE=Entry(root,text=" ")
	nameL.grid(row=5,column=2,padx="10")
	nameE.grid(row=5,column=3,pady="10",ipadx="100",ipady="10")
	


	
	contL=Label(root,text="Enter ContactNo: ")
	contE=Entry(root,text="Enter ContactNo: ")
	contL.grid(row=6,column=2,padx="10")
	contE.grid(row=6,column=3,ipadx="100",ipady="10",pady="10")

	marL=Label(root,text="Enter Marks: ")
	marE=Entry(root,text="Enter Marks: ")
	marL.grid(row=7,column=2,padx="10")
	marE.grid(row=7,column=3,ipadx="100",ipady="10",pady="10")
	
	emailL=Label(root,text="Enter Email: ")
	emailE=Entry(root,text="Enter Email: ")
	emailL.grid(row=8,column=2,padx="10")
	emailE.grid(row=8,column=3,ipadx="100",ipady="10",pady="10")
	root.mainloop()

def serchst1(rollE,nameE,contE,marE,emailE):

	f1=0
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
	
		
		for x in myresult:
			nameE.insert(0,x[0])
			contE.insert(0,x[2])
			marE.insert(0,x[3])
			emailE.insert(0,x[4])
			f1=1
	if f1==0:
		for x in myresult:
			if a==x[1]:
				f=1
		if f1==0:
				messagebox.showinfo("invalide","plz Enter valide RollNo....")






