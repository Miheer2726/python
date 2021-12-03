from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt
import requests
import bs4
import tkinter
list_marks = []
list_names = []
city_name = ""

#======================================================================================================================================
splash=Tk()
splash.after(4000,splash.destroy)
splash.configure(background="red")
splash.wm_attributes('-fullscreen','true')
msg=Label(splash,text="Student\n Management \nSystem \nBy \nMihir,Sagnik,\nPrashant & Anush", font=('arial',75,'bold'),fg='black',bg="red")
msg.pack()
splash.mainloop()
#===========================================================================================================================================
def f1():
	stud_window.deiconify()
	root.withdraw()
def f2():
	view_window_st_data.configure(state ='normal')
	view_window.deiconify()
	root.withdraw()
	view_window_st_data.delete(1.0,END)
	info=""
	con=None
	try:
		con=connect('sms.db')
		cursor=con.cursor()
		sql="select * from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		for d in data:
			info= info+" Rno = "+ str(d[0]) +", Name = " + str(d[1]) + ", Marks = " +str(d[2]) +"\n"
		view_window_st_data.configure(state ='normal') 
		view_window_st_data.insert(INSERT,info)
		view_window_st_data.configure(state ='disabled') 

	except Exception as e:
		showerror('Failure',e)

	finally:
		if con is not None:
			con.close()

def f3():
	root.deiconify()
	stud_window.withdraw()

def f4():
	root.deiconify()
	view_window.withdraw()

def f5():
	update_window.deiconify()
	root.withdraw()

def f6():
	root.deiconify()
	update_window.withdraw()
def f7():
	Delete_window.deiconify()
	root.withdraw()
	
def f8():
	root.deiconify()
	Delete_window.withdraw()
#===================================================ADD STUDENT================================================================
def f9():
	con=None
	if(add_window_ent_rno.get()== "" or add_window_ent_name.get()== "" or add_window_ent_marks.get()== ""):
		showerror("Failure","Please fillout details ")
	elif (add_window_ent_rno.get().isdigit()==False):
		showerror("Failure","Enter correct Rollno")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif (len(add_window_ent_name.get()) < 2) or (((add_window_ent_name.get()).isalpha())==False):
		showerror("Failure","Enter correct Name")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif(add_window_ent_marks.get().isdigit()==False):
		showerror("Failure","Enter correct Marks")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif int(add_window_ent_marks.get()) < 0:
		showerror("Failure","Enter correct Marks")
		add_window_ent_marks.delete(0, END)
	elif int(add_window_ent_marks.get()) > 100:
		showerror("Failure","Enter correct Marks")
		add_window_ent_marks.delete(0, END)
			
	else:
		try:
			con=connect('sms.db')
			cursor=con.cursor()
			sql= "insert into student values('%d','%s','%d')"
			rno=int(add_window_ent_rno.get())
			name=add_window_ent_name.get()
			marks=int(add_window_ent_marks.get())
			cursor.execute(sql % (rno,name,marks))
			con.commit()
			showinfo('Sucess','Record Added')
			add_window_ent_name.delete(0, END)
			add_window_ent_rno.delete(0, END)
			add_window_ent_marks.delete(0, END)
		
		except Exception as e:
			showerror('Failure',e)
#==========================================================UPDATE SSTUDENT=======================================================================================

def f10():
	con=None
	if(update_window_ent_rno.get()=="" or update_window_ent_name.get()== "" or update_window_ent_marks.get()== ""):
		showerror("Failure","Please fillout details ")
	elif (update_window_ent_rno.get().isdigit()==False):
		showerror("Failure","Enter correct Rollno")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif (len(update_window_ent_name.get()) <= 2) or (((update_window_ent_name.get()).isalpha())==False):
		showerror("Failure","Enter correct Name")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif(update_window_ent_marks.get().isdigit()==False):
		showerror("Failure","Enter correct Marks")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif int(update_window_ent_marks.get()) < 0:
		showerror("OOPS!", "Marks can't be negative")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif int(update_window_ent_marks.get()) > 100:
		showerror("OOPS!", "Marks can't be greater than 100")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	
	else:
		try:
			con=connect("sms.db")
			cursor=con.cursor()
			sql="update student set name='%s',marks='%d' where rno='%d' "
			rno = int(update_window_ent_rno.get())
			name = update_window_ent_name.get()
			marks = int(update_window_ent_marks.get())
			cursor.execute(sql % (name,marks,rno))
			if cursor.rowcount > 0:
				showinfo("Success", "Record Updated Successfully!")
				con.commit()
				update_window_ent_name.delete(0, END)
				update_window_ent_rno.delete(0, END)
				update_window_ent_marks.delete(0, END)
			else:
				showerror("Error!", "Record doesn't exists to be updated") 
		   

		except Exception as e:
			showerror("OOPS",e)
			con.rollback()
		finally:
			if con is not None:
				con.close()

#===========================================================DELETE STUDENT==================================================
def f11():
	con=None
	if(Delete_window_ent_rno.get()==""):
		showerror("Failure","Please fillout details ")
	elif (Delete_window_ent_rno.get().isdigit()==False):
		showerror("Failure","Enter correct Rollno")
		Delete_window_ent_rno.delete(0, END)
	else:

		try:
			con=connect("sms.db")
			cursor=con.cursor()
			sql="delete from student where rno='%d'"
			rno = int(Delete_window_ent_rno.get())
			cursor.execute(sql % (rno))
			if cursor.rowcount > 0:
				showinfo("Sucess","Record deleted")
				con.commit()
				Delete_window_ent_rno.delete(0, END)
			else:
				showerror("failure","Record does not exist ")    

		except Exception as e:
			showerror("issue ",e)
			con.rollback()
		finally:
			if con is not None:
				con.close()
					
#=====================================================CHARTS=================================================================
def f12():
	
	con=None
	try:
		con=connect('sms.db')
		cursor=con.cursor()
		sql="select marks from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		for d in data:	
			list_marks.append(int(str(d[0])))
		
	except Exception as e:
		print(e)
	finally:
		if con is not None:
			con.close()

	try:
		con=connect('sms.db')
		cursor=con.cursor()
		sql="select name from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		for d in data:	
			list_names.append(str(d[0]))
		
	except Exception as e:
		print(e)
	finally:
		if con is not None:
			con.close()


	plt.bar(list_names, list_marks, width = 0.6, color = ['red', 'green', 'cyan', 'orange','blue'])
	plt.title("Analysis")
	plt.xlabel("Students")
	plt.ylabel("Marks")
	plt.show()


#=================================================================================================
try:
	wa="https://ipinfo.io/"
	res=requests.get(wa)
	data=res.json()
	city_name=data['city']

except Exception as e:
	print("isssue",e)
#==========================================================================================================================	
try:
	a1= "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2= "&q=kalyan" 
	a3= "&appid="+"c6e315d09197cec231495138183954bd"

	wa=a1+a2+a3
	res=requests.get(wa)
	data=res.json()
	temperature=data['main']['temp']

except Exception as e:
	print("isssue",e)
#============================================================================================================================
try:
	wa="https://www.brainyquote.com/quote_of_the_day"
	res=requests.get(wa)
	data=bs4.BeautifulSoup(res.text,'html.parser')
	info=data.find('img',{'class':'p-qotd'})
	qtd=info['alt']

except Exception as e:
	print("isssue",e)	
#===============================================================================================================================

root=Tk()
root.title("S.M.S")

root.geometry("1550x800+0+0")

image1=PhotoImage(file=r"D:\PYTHON\IP\mihir.gif")
Image_lb1=Label(root,image=image1)
Image_lb1.place(x=0,y=0)


btn_add=Button(root,text="Add",font=('Arial',20,'bold'),width=10,fg='black',borderwidth=9,command=f1)
btn_view=Button(root,text="View",font=('Arial',20,'bold'),width=10,fg='black',borderwidth=9,command=f2)
btn_update=Button(root,text="Update",font=('Arial',20,'bold'),width=10,fg='black',borderwidth=9,command=f5)
btn_delete=Button(root,text="Delete",font=('Arial',20,'bold'),width=10,fg='black',borderwidth=9,command=f7)
btn_charts=Button(root,text="Charts",font=('Arial',20,'bold'),width=10,fg='black',borderwidth=9,command=f12)
lbl_loc=Label(root,text="Location : "+city_name,font=('Arial',20,'bold'),fg='black')
lbl_temp=Label(root,text="Temp : "+ str(temperature)+"\u00B0" ,font=('Arial',20,'bold'),fg='black')
lbl_Quote=Label(root,text="QOTD : "+ qtd,font=('Arial',20,'bold'),fg='black',wraplength=500)
btn_add.pack(pady=10)
btn_view.pack(pady=10)
btn_update.pack(pady=10)
btn_delete.pack(pady=10)
btn_charts.pack(pady=10)
lbl_loc.place(x=8,y=460)
lbl_temp.place(x=380,y=460)
lbl_Quote.place(x=8,y=510)

#=========================================================================================================================

stud_window=Toplevel(root)
stud_window.title("Add St.")
stud_window.geometry("1550x800+0+0")

Image_lb2=Label(stud_window,image=image1)
Image_lb2.place(x=0,y=0)


add_window_lbl_rno= Label(stud_window,text="Enter Roll No",font=('Arial',20,'bold'))
add_window_ent_rno=Entry(stud_window,bd=5,font=('Arial',20,'bold'))
add_window_lbl_name=Label(stud_window,text="Enter Name",font=('Arial',20,'bold'))
add_window_ent_name=Entry(stud_window,bd=5,font=('Arial',20,'bold'))
add_window_lbl_marks=Label(stud_window,text="Enter Marks",font=('Arial',20,'bold'))
add_window_ent_marks=Entry(stud_window,bd=5,font=('Arial',20,'bold'))
add_window_btn_save=Button(stud_window,text="Save",font=('Arial',20,'bold'),borderwidth=9,command=f9)
add_window_btn_back=Button(stud_window,text="Back",font=('Arial',20,'bold'),borderwidth=9,command=f3)


add_window_lbl_rno.pack(pady=10)
add_window_ent_rno.pack(pady=10)
add_window_lbl_name.pack(pady=10)
add_window_ent_name.pack(pady=10)
add_window_lbl_marks.pack(pady=10)
add_window_ent_marks.pack(pady=10)
add_window_btn_save.pack(pady=10)
add_window_btn_back.pack(pady=10)
stud_window.withdraw()

#===============================================================================================================================
view_window=Toplevel(root)
view_window.title("View st")
view_window.geometry("1550x800+0+0")
Image_lb3=Label(view_window,image=image1)
Image_lb3.place(x=0,y=0)


view_window_st_data=ScrolledText(view_window,width=40,height=15,font=('Arial',18,'bold'), foreground = 'dark blue')
view_window_btn_back=Button(view_window,text="Back",font=('Arial',20,'bold'),borderwidth=9,command=f4)
view_window_st_data.pack(pady=10)
view_window_btn_back.pack(pady=10)
view_window.withdraw()

#================================================================================================================================

update_window=Toplevel(root)
update_window.title("Update St.")
update_window.geometry("1550x800+0+0")
Image_lb4=Label(update_window,image=image1)
Image_lb4.place(x=0,y=0)


update_window_lbl_rno= Label(update_window,text="Enter Roll No",font=('Arial',20,'bold'))
update_window_ent_rno=Entry(update_window,bd=5,font=('Arial',20,'bold'))
update_window_lbl_name=Label(update_window,text="Enter Name",font=('Arial',20,'bold'))
update_window_ent_name=Entry(update_window,bd=5,font=('Arial',20,'bold'))
update_window_lbl_marks=Label(update_window,text="Enter Marks",font=('Arial',20,'bold'))
update_window_ent_marks=Entry(update_window,bd=5,font=('Arial',20,'bold'))
update_window_btn_save=Button(update_window,text="Update",font=('Arial',20,'bold'),borderwidth=9,command=f10)
update_window_btn_back=Button(update_window,text="Back",font=('Arial',20,'bold'),borderwidth=9,command=f6)


update_window_lbl_rno.pack(pady=10)
update_window_ent_rno.pack(pady=10)
update_window_lbl_name.pack(pady=10)
update_window_ent_name.pack(pady=10)
update_window_lbl_marks.pack(pady=10)
update_window_ent_marks.pack(pady=10)
update_window_btn_save.pack(pady=10)
update_window_btn_back.pack(pady=10)
update_window.withdraw()

#=================================================================================================================================

Delete_window=Toplevel(root)
Delete_window.title("Delete St.")
Delete_window.geometry("1550x800+0+0")
Image_lb5=Label(Delete_window,image=image1)
Image_lb5.place(x=0,y=0)



Delete_window_lbl_rno= Label(Delete_window,text="Enter Roll No",font=('Arial',20,'bold'))
Delete_window_ent_rno=Entry(Delete_window,bd=5,font=('Arial',20,'bold'))
Delete_window_btn_save=Button(Delete_window,text="Delete",font=('Arial',20,'bold'),borderwidth=9,command=f11)
Delete_window_btn_back=Button(Delete_window,text="Back",font=('Arial',20,'bold'),borderwidth=9,command=f8)

Delete_window_lbl_rno.pack(pady=10)
Delete_window_ent_rno.pack(pady=10)
Delete_window_btn_save.pack(pady=10)
Delete_window_btn_back.pack(pady=10)
Delete_window.withdraw()

def f12():
	if askokcancel("Quit","Do you want to Quit?"):
		root.destroy()

root.protocol("WM_DELETE_WINDOW",f12)
root.mainloop()
