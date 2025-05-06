from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
        def __init__(self,root):

                self.root=root
                self.root.geometry("1530x790+0+0")
                self.root.title("face Recognition System")

                # @@@@@@@@@@@@@@@@@@@@@@@@@@@2varables@@@@@@@@@@@@@@@@@@@@@@@@
                self.var_dep=StringVar()
                self.var_couse=StringVar()
                self.var_year=StringVar()
                self.var_semester=StringVar()
                self.var_std_id=StringVar()
                self.var_std_name=StringVar()
                self.var_div=StringVar()
                self.var_roll=StringVar()
                self.var_gender=StringVar()
                self.var_dob=StringVar()
                self.var_email=StringVar()
                self.var_phone=StringVar()
                self.var_address=StringVar()
                self.var_teacher=StringVar()




     #FIRST IMAGE
                img=Image.open(r"C:\Users\prave\Desktop\face recognition system\college_images\r.jpg")
                img = img.resize((510, 130), Image.Resampling.LANCZOS)
                self.photoimg=ImageTk.PhotoImage(img)

                f_lbl=Label(self.root,image=self.photoimg)
                f_lbl.place(x=0,y=0,width=500,height=130)
    #2nd img
                img1=Image.open(r"C:\Users\prave\Desktop\face recognition system\college_images\smart-attendance.jpg")
                img1= img1.resize((510, 130), Image.Resampling.LANCZOS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                f_lbl=Label(self.root,image=self.photoimg1)
                f_lbl.place(x=425,y=0,width=500,height=130)
    #3nrd img
                img2=Image.open(r"C:\Users\prave\Desktop\face recognition system\college_images\r.jpg")
                img2 = img2.resize((510, 130), Image.Resampling.LANCZOS)
                self.photoimg2=ImageTk.PhotoImage(img2)

                f_lbl=Label(self.root,image=self.photoimg2)
                f_lbl.place(x=900,y=0,width=500,height=130)
 #background
                img3=Image.open(r"C:\Users\prave\Desktop\face recognition system\college_images\bg.jpg")
                img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                bg_img=Label(self.root,image=self.photoimg3)
                bg_img.place(x=0,y=130,width=1530,height=710)

                title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",27,"bold"),bg="white",fg="dark green")
                title_lbl.place(x=0,y=0,width=1430,height=45)



                main_frame=Frame(bg_img,bd=2,bg="white")
                main_frame.place(x=0,y=50,width=1480,height=600)

#left   
                left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
                left_frame.place(x=10,y=10,width=760,height=580)

                img_left=Image.open(r"C:\Users\prave\Desktop\face recognition system\college_images\iStock-182059956_18390_t12.jpg")
                img_left = img_left.resize((710, 130), Image.Resampling.LANCZOS)
                self.photoimg_left=ImageTk.PhotoImage(img_left)

                f_lbl=Label(left_frame,image=self.photoimg_left)
                f_lbl.place(x=5,y=0,width=720,height=130)
#current couse
                current_curse_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="CURRENT COURSE",font=("times new roman",12,"bold"))
                current_curse_frame.place(x=5,y=135,width=720,height=125)

#department
                dep_label=Label(current_curse_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
                dep_label.grid(row=0,column=0,padx=10)
#combo box
                dep_combo=ttk.Combobox(current_curse_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),width=20,state="readonly")
                dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")        
                dep_combo.current(0)
                dep_combo.grid(row=0,column=1,padx=2,pady=10)
#course 
                course_label=Label(current_curse_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
                course_label.grid(row=0,column=2,padx=10,sticky=W)
#combo box
                course_combo=ttk.Combobox(current_curse_frame,textvariable=self.var_couse,font=("times new roman",13,"bold"),width=20,state="readonly")
                course_combo["values"]=("Select Course","FE","SE","TE","BE")        
                course_combo.current(0)
                course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
#year   
                year_label=Label(current_curse_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
                year_label.grid(row=1,column=0,padx=10,sticky=W)
#combo box
                year_combo=ttk.Combobox(current_curse_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),width=20,state="readonly")
                year_combo["values"]=("Select Year","2021-22","2022-23","2023-24","2024-25")        
                year_combo.current(0)
                year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
#semester
                semester_label=Label(current_curse_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
                semester_label.grid(row=1,column=2,padx=10,sticky=W)
#combo box
                semester_combo=ttk.Combobox(current_curse_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),width=20,state="readonly")
                semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")        
                semester_combo.current(0)
                semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


#class student  information
                class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
                class_student_frame.place(x=5,y=250,width=720,height=300)
#stud Id        
                studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
                studentId_label.grid(row=0,column=0,padx=10,sticky=W)

                studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
                studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
#stud name
                studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
                studentName_label.grid(row=0,column=2,padx=10,sticky=W)

                studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
                studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
#class division
                classdiv_label=Label(class_student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
                classdiv_label.grid(row=1,column=0,padx=10,sticky=W)

                # classdiv_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
                # classdiv_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        #gender combo
                gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),width=18,state="readonly")
                gender_combo["values"]=("A","B","C",)        
                gender_combo.current(0)
                gender_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
 #rollno        
                rollno_label=Label(class_student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
                rollno_label.grid(row=1,column=2,padx=10,sticky=W)

                rollno_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
                rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
                
                
#gender 
                gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
                gender_label.grid(row=2,column=0,padx=10,sticky=W)

                
        #gender combo
                gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),width=18,state="readonly")
                gender_combo["values"]=("Male","Female","Other",)        
                gender_combo.current(0)
                gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
    #dob        
                dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
                dob_label.grid(row=2,column=2,padx=10,sticky=W)

                dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
                dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        
        
    #Email
                email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
                email_label.grid(row=3,column=0,padx=10,sticky=W)

                email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
                email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
    #phone
                phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
                phone_label.grid(row=3,column=2,padx=10,sticky=W)

                phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
                phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
    #adress
                adress_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
                adress_label.grid(row=4,column=0,padx=10,sticky=W)

                adress_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
                adress_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
    #Teacher name
                teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
                teacher_label.grid(row=4,column=2,padx=10,sticky=W)

                teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
                teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

    # Radiobutton
                self.var_radio1=StringVar()
                radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
                radiobtn1.grid(row=6,column=0)


                radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
                radiobtn2.grid(row=6,column=1)

     # Buttonframe
                btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
                btn_frame.place(x=0,y=200,width=715,height=35)

                savebtn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
                savebtn.grid(row=0,column=0)

                updatebt=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
                updatebt.grid(row=0,column=1)

                deletbt=Button(btn_frame,text="Delete",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
                deletbt.grid(row=0,column=2)

                resetbt=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
                resetbt.grid(row=0,column=3)
    # buttonframe2
                btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
                btn_frame1.place(x=0,y=235,width=715,height=35)
    #take photo
                takephotobt=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
                takephotobt.grid(row=0,column=0)
    #update photo
                updatephotobt=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
                updatephotobt.grid(row=0,column=1)







        
 #right 
                right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
                right_frame.place(x=780,y=10,width=720,height=580)
    #rigt sidw image
                img_right=Image.open(r"C:\Users\prave\Desktop\face recognition system\college_images\gettyimages-1022573162.jpg")
                img_right = img_right.resize((710, 130), Image.Resampling.LANCZOS)
                self.photoimg_right=ImageTk.PhotoImage(img_right)

                f_lbl=Label(right_frame,image=self.photoimg_right)
                f_lbl.place(x=5,y=0,width=720,height=130)

#====================search system===========================
                search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
                search_frame.place(x=5,y=135,width=700,height=700)

                searchbar_label=Label(search_frame,text="Search By",font=("times new roman",15,"bold"),bg="red",fg="white")
                searchbar_label.grid(row=0,column=0,padx=5,sticky=W)
#seach c        ombobox
                search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),width=12,state="readonly")
                search_combo["values"]=("Select","Roll No","Phone No")        
                search_combo.current(0)
                search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

                # enrey

                search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
                search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
    #            button
                searcht=Button(search_frame,text="Search",width=15,font=("times new roman",10,"bold"),bg="blue",fg="white")
                searcht.grid(row=0,column=3)

                showallbt=Button(search_frame,text="Show All",width=15,font=("times new roman",10,"bold"),bg="blue",fg="white")
                showallbt.grid(row=1,column=3)
#@@@@@@@@@@@@@@@@@@@@@@@@@ TAble frame @@@@@@@@@@@@@@@@
                table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
                table_frame.place(x=5,y=230,width=710,height=320)

                scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

                self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","roll","gender","div","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.config(command=self.student_table.xview)
                scroll_y.config(command=self.student_table.yview)

                self.student_table.heading("dep",text="Department",)
                self.student_table.heading("course",text="Course")
                self.student_table.heading("year",text="Year")
                self.student_table.heading("sem",text="Semester")
                self.student_table.heading("id",text="StudentId")
                self.student_table.heading("name",text="Name")
                self.student_table.heading("roll",text="Roll No")
                self.student_table.heading("gender",text="Gender")
                self.student_table.heading("div",text="Division")
                self.student_table.heading("dob",text="DOB")
                self.student_table.heading("email",text="Email")
                self.student_table.heading("phone",text="Phone")
                self.student_table.heading("address",text="Address")
                self.student_table.heading("teacher",text="Teacher")
                self.student_table.heading("photo",text="PhotoSampleStatus")
                self.student_table["show"]="headings"

                self.student_table.column("dep",width=100)
                self.student_table.column("course",width=100)
                self.student_table.column("year",width=100)
                self.student_table.column("sem",width=100)
                self.student_table.column("id",width=100)
                self.student_table.column("name",width=100)
                self.student_table.column("roll",width=100)
                self.student_table.column("gender",width=100)
                self.student_table.column("div",width=100)
                self.student_table.column("dob",width=100)
                self.student_table.column("email",width=100)
                self.student_table.column("phone",width=100)
                self.student_table.column("address",width=100)
                self.student_table.column("teacher",width=100)
                self.student_table.column("photo",width=100)

                self.student_table.pack(fill=BOTH,expand=1)
                self.student_table.bind("<ButtonRelease>",self.get_cursor )
                self.fetch_data()

                # ++++++++++++++++++++++++++++++++++++++++++function declarartion++++++++++++++++++++

        def add_data(self):
                if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                    messagebox.showerror("Error","All Fields are required",parent=self.root)
                else:
                    try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="8040face",database="face_recognizer")
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                                                
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_couse.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_id.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get()
                                                                                                                                        
                                                                                                                ))                               
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("success","Student details has been added successfully")
                    except Exception as es:
                        messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                        
        
        #######fech dat+++++++++++++
        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="8040face",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select* from student")
                data=my_cursor.fetchall()
                if len(data)!=0:
                      self.student_table.delete(*self.student_table.get_children())
                      for i in data:
                            self.student_table.insert("",END,values=i)
                      conn.commit()
                conn.close()
        #####################get cursor#################
        def get_cursor(self,event=""):
                cursor_focus=self.student_table.focus()
                content=self.student_table.item(cursor_focus)
                data=content["values"]
                self.var_dep.set(data[0]),
                self.var_couse.set(data[1]),
                self.var_year.set(data[2]),
                self.var_semester.set(data[3]),
                self.var_std_id.set(data[4]),
                self.var_std_name.set(data[5]),
                self.var_div.set(data[6]),
                self.var_roll.set(data[7]),
                self.var_gender.set(data[8]),
                self.var_dob.set(data[9]),
                self.var_email.set(data[10]),
                self.var_phone.set(data[11]),
                self.var_address.set(data[12]),
                self.var_teacher.set(data[13]),
                self.var_radio1.set(data[14])
        
        # update function
        def update_data(self):
                if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                    messagebox.showerror("Error","All Fields are required",parent=self.root)
                else:
                    try:
                        update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                        if update>0:
                              conn=mysql.connector.connect(host="localhost",username="root",password="8040face",database="face_recognizer")
                              my_cursor=conn.cursor()
                              my_cursor.execute("update student Set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                                self.var_couse.get(),
                                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                                self.var_std_id.get()
                                                                                                                                                                                                                        
                                                                                                                                                                                                                                ))
                        else:
                            if not update:
                                return
                        messagebox.showinfo("Success","Student deatils successfully update completed",parent=self.root)
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                    except Exception as es:
                        messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        #reset
        def reset_data(self):
              self.var_dep.set("Select Department")
              self.var_couse.set("Select Course")
              self.var_year.set("Select Year")
              self.var_semester.set("Select Semester")
              self.var_std_id.set("")
              self.var_std_name.set("")
              self.var_div.set("Select Division")
              self.var_roll.set("")
              self.var_gender.set("Male")
              self.var_dob.set("")
              self.var_email.set("")
              self.var_phone.set("")
              self.var_address.set("")
              self.var_teacher.set("")
              self.var_radio1.set("")
              self.var_dep.set("")
# #delete buton
        def delete_data(self):
            if self.va_std_id.get()=="":
                messagebox.showerror("Error","Student id must be required",parent=self.root)
            else:
                try:
                    Delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                    if Delete>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="8040face",database="face_recognizer")
                        my_cursor=conn.cursor()
                        sql="delete from Student where Student_id=%s"
                        val=(self.va_std_id.get(),)
                        my_cursor.execute(sql,val)
                    else:
                        if not Delete:
                            return
                        
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Delete","Successfully Deleted student details",parent=self.root)
                except Exception as es:
                        messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


#+++++++++++++++++++++++++++++++++===== Generate dataset or take photo+++++++++++++++++++++++++
        def generate_dataset(self):
                if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                    messagebox.showerror("Error","All Fields are required",parent=self.root)
                else:
                    try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="8040face",database="face_recognizer")
                        my_cursor=conn.cursor()
                        my_cursor.execute("select* from student")
                        myresult=my_cursor.fetchall()
                        id=0
                        for X in myresult:
                             id+=1
                        my_cursor.execute("update student Set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                                self.var_couse.get(),
                                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                                self.var_std_id.get()==id+1
                                                                                                                                                                                                                        
                                                                                                                                                                                                                                ))
                        conn.commit()
                        self.fetch_data()
                        self.reset_data()
                        conn.close()

                        # ++++++ load photo from open cv+++++++++
                        face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                        def face_cropped(img):
                             gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                             faces=face_classifier.detectMultiScale(gray,1.3,5)
                             #scaling factor=1.3
                             #min neighbor=5
                             for(x,y,w,h) in faces:
                                  face_cropped=img[y:y+h,x:x+w]
                                  return face_cropped
                        cap=cv2.VideoCapture(0)
                        img_id=0
                        while True:
                             ret,my_frame=cap.read()
                             if face_cropped(my_frame) is not None:
                                  img_id+=1
                                  face=cv2.resize(face_cropped(my_frame),(450,450))
                                  face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                  file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                                  cv2.imwrite(file_name_path,face)
                                  cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                  cv2.imshow("Crooped face",face)
                             if cv2.waitKey(1)==13 or int(img_id)==100:
                                  break
                        cap.release()
                        cv2.destroyAllWindows()
                        messagebox.showinfo("Result","generating datasets completed!!!!")
                    except Exception as es:
                                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
   


                        

                
if __name__ == "__main__":
        root=Tk()
        obj=Student(root)
        root.mainloop()