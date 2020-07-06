from tkinter import*
from tkinter import ttk
import pymysql
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("student management system")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student management system",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="green",fg="pink")
        title.pack(side=TOP,fill=X)

      

       #...........MANAGE FRAME..........
 
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=90,width=400,height=650)
        
        m_title=Label(Manage_Frame,text="MANAGE STUDENTS",font=("times new roman",20,"bold"),bg="crimson",fg="White")
        m_title.grid(row=0,columnspan=2,pady=20)
        
        lbl_roll=Label(Manage_Frame,text="Roll No.",font=("times new roman",20,"bold"),bg="crimson",fg="White")
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")


        
        lbl_name=Label(Manage_Frame,text="Name",font=("times new roman",20,"bold"),bg="crimson",fg="White")
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        
        lbl_email=Label(Manage_Frame,text="Email",font=("times new roman",20,"bold"),bg="crimson",fg="White")
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        
        lbl_gender=Label(Manage_Frame,text="Gender",font=("times new roman",20,"bold"),bg="crimson",fg="White")
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,font=("times new roman",13,"bold"),state="readonly")
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4,column=1,padx=20,pady=20)


        lbl_contact=Label(Manage_Frame,text="Contact",font=("times new roman",20,"bold"),bg="crimson",fg="White")
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_contact=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        
        lbl_Dob=Label(Manage_Frame,text="D.O.B",font=("times new roman",20,"bold"),bg="crimson",fg="White")
        lbl_Dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_Dob=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        
        lbl_addr=Label(Manage_Frame,text="Address",font=("times new roman",20,"bold"),bg="crimson",fg="White")
        lbl_addr.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        txt_addr=Text(Manage_Frame,width=30,height=4,font=("",10))
        txt_addr.grid(row=7,column=1,padx=20,pady=10,sticky="w")

        #..........BUTTONS............

        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=8,y=550,width=380)

        Addbtn=Button(btn_Frame,text="Add",width=8).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="update",width=8).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="delete",width=8).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_Frame,text="clear",width=8).grid(row=0,column=3,padx=10,pady=10)
        
        #...........DETAIL FRAMES............

        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=90,width=800,height=650)

        
        lbl_search=Label(Detail_Frame,text="Search By",font=("times new roman",20,"bold"),bg="crimson",fg="White")
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,font=("times new roman",13,"bold"),width=10,state="readonly")
        combo_search['values']=("Roll","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=20)
        

        txt_search=Entry(Detail_Frame,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="search",width=8,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="showall",width=8,pady=5).grid(row=0,column=4,padx=10,pady=10)

        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=760,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)
        Student_table.heading("roll",text="Roll No.")
        Student_table.heading("name",text="Name")
        Student_table.heading("email",text="Email")
        Student_table.heading("gender",text="Gender")
        Student_table.heading("contact",text="Contact")
        Student_table.heading("dob",text="D.O.B")
        Student_table.heading("address",text="Address")
        Student_table['show']='headings'
        Student_table.column("roll",width=100)
        Student_table.column("name",width=100)
        Student_table.column("email",width=100)
        Student_table.column("gender",width=100)
        Student_table.column("contact",width=100)
        Student_table.column("dob",width=100)
        Student_table.column("address",width=150)
        Student_table.pack(fill=BOTH,expand=1)

   


root = Tk()
obj = Student(root)
root.mainloop()    
