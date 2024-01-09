import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from suppliers import SuppliersClass
class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Vendor Management System | Developed by Umar Farooq")
        self.root.config(bg = "white")
        
        # ===title=====
        self.icon_title=PhotoImage (file="images/logo1.png")
        title = Label(self.root, text="Vendor Management System",image=self.icon_title,compound=LEFT, font=("times new roman", 40, "bold"),bg="#010c48",fg="white" ,anchor="w",padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)
        #===Logout Button====
        btn_logout=Button(self.root, text="Logout", font=("times new roman",15,"bold"),bg="red",cursor="hand2").place(x=1150,y=10,height=50, width=150)
        #===Clock===
        self.lbl_clock = Label(self.root, text="Welcome to Vendor Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=("times new roman", 15),bg="#4d636d",fg="white" )
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        #====Left Menu==
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200), Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        LeftMenu=Frame(self.root, bd=2,relief=RIDGE,bg = "white")
        LeftMenu.place(x=0,y=102, width=200,height=565)
        lbl_menuLogo=Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)
        self. icon_side=PhotoImage (file="images/side.png")
        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        btn_supplier = Button(LeftMenu, text="Supplier",command=self.suppliers, image=self.icon_side, compound=LEFT,padx=5,anchor="w",font=("times new roman", 20,"bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_category = Button(LeftMenu, text="Category", image=self.icon_side, compound=LEFT,padx=5,anchor="w",font=("times new roman", 20,"bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_product = Button(LeftMenu, text="Product", image=self.icon_side, compound=LEFT,padx=5,anchor="w",font=("times new roman", 20,"bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_exit = Button(LeftMenu, text="Exit", image=self.icon_side, compound=LEFT,padx=5,anchor="w",font=("times new roman", 20,"bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP,fill=X)
       #===Contet===
        self.lb1_supplier=Label(self.root,text="Total Suppliers\n[ 0 ]",bg="#33bbf9",bd=5,relief=RIDGE,fg="white",font=("goudy old style",20,"bold"))
        self.lb1_supplier.place(x=300, y=120,height=150, width=300)
        self.lb1_category=Label(self.root,text="Total Categories\n[ 0 ]",bg="#ff5722",bd=5,relief=RIDGE,fg="white",font=("goudy old style",20,"bold"))
        self.lb1_category.place(x=650, y=120,height=150, width=300)
        self.lb1_product=Label(self.root,text="Total Products\n[ 0 ]",bg="#ffc107",bd=5,relief=RIDGE,fg="white",font=("goudy old style",20,"bold"))
        self.lb1_product.place(x=1000, y=120,height=150, width=300)
       #====Footer===
        lbl_footer = Label(self.root, text="VMS Vendor management system | Developed by Umar Farooq\nFor any support please contact +923025366826", font=("times new roman", 12),bg="#4d636d",fg="white" )
        lbl_footer.pack(side=BOTTOM,fill=X)
    def suppliers(self):
        self.new_win = Toplevel(self.root)
        self.new_obj= SuppliersClass(self.new_win)


if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
