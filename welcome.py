from  deletest import*
from  search import*
from updt import*
from tkinter import*
import mysql.connector
from tkinter import messagebox
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mydatabase")
mycursor=mydb.cursor()




def info():
	root1=Tk()
	root1.geometry("600x400")
	root1.config(background="light green")
	
	
	nameL1=Label(root1,text="Enter Name: ")
	rollL1=Label(root1,text="Enter RollNo: ")
	contL1=Label(root1,text="Enter ContactNo: ")
	marL1=Label(root1,text="Enter Marks: ")
	emailL1=Label(root1,text="Enter Email: ")
	
	nameE1=Entry(root1,text="Enter Name: ")
	rollE1=Entry(root1,text="Enter RollNo: ")
	contE1=Entry(root1,text="Enter ContactNo: ")
	marE1=Entry(root1,text="Enter Marks: ")
	emailE1=Entry(root1,text="Enter Email: ")
	
	nameL1.grid(row=1,column=2,padx="10")
	rollL1.grid(row=2,column=2,padx="10")
	contL1.grid(row=3,column=2,padx="10")
	marL1.grid(row=4,column=2,padx="10")
	emailL1.grid(row=5,column=2,padx="10")
	

	
	nameE1.grid(row=1,column=3,pady="10",ipadx="100",ipady="10")
	rollE1.grid(row=2,column=3,ipadx="100",ipady="10",pady="10")
	contE1.grid(row=3,column=3,ipadx="100",ipady="10",pady="10")
	marE1.grid(row=4,column=3,ipadx="100",ipady="10",pady="10")
	emailE1.grid(row=5,column=3,ipadx="100",ipady="10",pady="10")
	Button(root1,text="ADD",bg="light blue",command=lambda:addf(nameE1,rollE1,contE1,marE1,emailE1)).grid(row=6,column=3,ipadx="50",ipady="20",pady="10")

def addf(nameE1,rollE1,contE1,marE1,emailE1):
	if nameE1.get()=="" or rollE1.get()=="" or contE1.get()=="" or marE1.get()=="" or emailE1.get()=="":
		messagebox.showinfo("Invalide","Plz Fill All Details")
	else:
		a=nameE1.get()
		b=rollE1.get()
		c=contE1.get()
		d=marE1.get()
		e=emailE1.get()
		sql="INSERT INTO student(name,rollno,contact,marks,email)VALUES(%s,%s,%s,%s,%s)"
		val=(a,b,c,d,e)
		mycursor.execute(sql,val)
		mydb.commit()
		messagebox.showinfo("valide","add Successfully....")









def datafill():
	
	root3=Tk()
	root3.geometry("700x500")
	root3.config(background="light green")
	Button(root3,text="ADD NEW STUDENT",bg="light blue",command=info).grid(row=0,column=5,ipadx="50",ipady="20",pady="10")
	Button(root3,text="UPDATE_STUDENT",bg="light blue",command=up).grid(row=1,column=5,ipadx="50",ipady="20",pady="10")
	Button(root3,text="DELETE_STUDENT",bg="light blue",command=delete_re).grid(row=2,column=5,ipadx="50",ipady="20",pady="10")
	Button(root3,text="SEARCH_STUDENT",bg="light blue",command=serchst).grid(row=3,column=5,ipadx="50",ipady="20",pady="10")
	Button(root3,text="SHOW_STUDENT_DATA",bg="light blue",command=show).grid(row=4,column=5,ipadx="50",ipady="20",pady="10")
	Button(root3,text="LOGOUT",bg="light blue").grid(row=5,column=5,ipadx="50",ipady="20",pady="10")
	root3.mainloop()




def show():
	root5=Tk()
	root5.title("All Properties")
	root5.config(background="light pink")
	root5.geometry("800x800")

	heading=Label(root5,text="STUDENT INFO",bg="light green")
	heading.config(font=("Courier",24))
	heading.grid(row=1,column=0,columnspan=4)

	mycursor.execute("SELECT * FROM student")
	myresult=mycursor.fetchall()
	i=6
	heading=Label(root5,text="NAME",bg="light green")
	heading.config(font=("Courier",15))

	heading.grid(row=2,column=1,pady="10",padx="10")

	heading1=Label(root5,text="ROLLNO",bg="light green")
	heading1.config(font=("Courier",15))

	heading1.grid(row=2,column=2,pady="10",padx="10")

	heading2=Label(root5,text="CONTACT",bg="light green")
	heading2.config(font=("Courier",15))
	heading2.grid(row=2,column=3,pady="10",padx="10")

	heading3=Label(root5,text="MARKS",bg="light green")
	heading3.config(font=("Courier",15))
	heading3.grid(row=2,column=4,pady="10",padx="10")

	heading4=Label(root5,text="EMAIL",bg="light green")
	heading4.config(font=("Courier",15))
	heading4.grid(row=2,column=5,pady="10",padx="10")
                
	for x in myresult:
		heading=Label(root5,text=x[0],bg="light pink")
		heading.config(font=("Courier",15))

		heading.grid(row=i,column=1)

		heading1=Label(root5,text=x[1],bg="light pink")
		heading1.config(font=("Courier",15))

		heading1.grid(row=i,column=2)

		heading2=Label(root5,text=x[2],bg="light pink")
		heading2.config(font=("Courier",15))
		heading2.grid(row=i,column=3)

		heading3=Label(root5,text=x[3],bg="light pink")
		heading3.config(font=("Courier",15))
		heading3.grid(row=i,column=4)

		heading4=Label(root5,text=x[4],bg="light pink")
		heading4.config(font=("Courier",15))
		heading4.grid(row=i,column=5)
		i=i+1



	root5.mainloop()











	


	#print(x[2])
	





def loginst():
	root2.destroy()
	root=Tk()
	root.geometry("700x500")
	root.config(background="light green")
	Button(root,text="LOGIN",bg="light blue",command=datafill).grid(row=6,column=5,ipadx="50",ipady="20",pady="10")
	Button(root,text="REGISTER",bg="light blue").grid(row=7,column=5,ipadx="50",ipady="20",pady="10")

	root.mainloop()



root2=Tk()
root2.geometry("600x400")
root2.config(background="light pink")
title=Label(root2,text="WELCOME USER",bg="blue")
title.config(font=("Courier",24))
title.grid(row=0,column=5,columnspan=5,pady="10",ipadx="50")
Button(root2,text="PROCEED",bg="red",command=loginst).grid(row=1,column=5,ipadx="50",ipady="20",pady="10")
root2.mainloop()

