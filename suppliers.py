import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import requests

class SuppliersClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Vendor Management System | Developed by Umar Farooq")
        self.root.config(bg="white")
        self.root.focus_force()

        # Variables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_supp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_ptype = StringVar()

        # Search Frame
        search_frame = LabelFrame(self.root, text="Search Supplier", font=("goudy old style", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        search_frame.place(x=250, y=20, width=600, height=70)

        cmb_search = ttk.Combobox(search_frame, textvariable=self.var_searchby, values=("Select", "Email", "Name", "Contact"),
                                  state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)
        Entry(search_frame, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=10)
        Button(search_frame, text="Search", font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2",
               command=self.search_supplier).place(x=410, y=8, width=150, height=30)

        # Title
        Label(self.root, text="Supplier Details", font=("goudy old style", 15), bg="#0f4d7d", fg="white").place(x=50,
                                                                                                                  y=100,
                                                                                                                  width=1000)

        # Row 1
        Label(self.root, text="Supp ID", font=("goudy old style", 15), bg="white").place(x=50, y=150)
        Label(self.root, text="Gender", font=("goudy old style", 15), bg="white").place(x=350, y=150)
        Label(self.root, text="Contact", font=("goudy old style", 15), bg="white").place(x=750, y=150)

        Entry(self.root, textvariable=self.var_supp_id, font=("goudy old style", 15), bg="lightyellow").place(x=150,
                                                                                                               y=150,
                                                                                                               width=180)

        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female", "Other"),
                                  state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0)

        Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(x=850,
                                                                                                               y=150,
                                                                                                               width=180)

        # Row 2
        Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=50, y=190)
        Label(self.root, text="Email", font=("goudy old style", 15), bg="white").place(x=350, y=190)
        Label(self.root, text="Ptype", font=("goudy old style", 15), bg="white").place(x=750, y=190)

        Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=150,
                                                                                                            y=190,
                                                                                                            width=180)
        Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15), bg="lightyellow").place(x=500,
                                                                                                              y=190,
                                                                                                              width=180)
        Entry(self.root, textvariable=self.var_ptype, font=("goudy old style", 15), bg="lightyellow").place(x=850,
                                                                                                              y=190,
                                                                                                              width=180)

        # Row 3
        Label(self.root, text="Address", font=("goudy old style", 15), bg="white").place(x=50, y=270)

        self.txt_sup_address = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_sup_address.place(x=150, y=270, width=300, height=60)

        # Buttons
        Button(self.root, text="Save", font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2",
               command=self.add_supplier).place(x=500, y=305, width=110, height=28)
        Button(self.root, text="Update", font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2",
               command=self.update_supplier).place(x=620, y=305, width=110, height=28)
        Button(self.root, text="Delete", font=("goudy old style", 15), bg="#f44336", fg="white", cursor="hand2",
               command=self.delete_supplier).place(x=740, y=305, width=110, height=28)
        Button(self.root, text="Clear", font=("goudy old style", 15), bg="#607d8b", fg="white", cursor="hand2",
               command=self.clear_entries).place(x=860, y=305, width=110, height=28)

        # Suppliers Details
        supplier_frame = Frame(self.root, bd=3, relief=RIDGE)
        supplier_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly = Scrollbar(supplier_frame, orient=VERTICAL)
        scrollx = Scrollbar(supplier_frame, orient=HORIZONTAL)
        self.SupplierTables = ttk.Treeview(supplier_frame,
                                           columns=("supid", "name", "email", "gender", "contact", "ptype", "address"),
                                           yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SupplierTables.xview)
        scrolly.config(command=self.SupplierTables.yview)
        self.SupplierTables.heading("supid", text="Supplier ID")
        self.SupplierTables.heading("name", text="Name")
        self.SupplierTables.heading("email", text="Email")
        self.SupplierTables.heading("gender", text="Gender")
        self.SupplierTables.heading("contact", text="Contact")
        self.SupplierTables.heading("ptype", text="Ptype")
        self.SupplierTables.heading("address", text="Address")
        self.SupplierTables["show"] = "headings"

        self.SupplierTables.column("supid", width=90)
        self.SupplierTables.column("name", width=100)
        self.SupplierTables.column("email", width=100)
        self.SupplierTables.column("gender", width=100)
        self.SupplierTables.column("contact", width=100)
        self.SupplierTables.column("ptype", width=100)
        self.SupplierTables.column("address", width=100)
        self.SupplierTables.pack(fill=BOTH, expand=1)

    def add_supplier(self):
        data = {
            "supid": self.var_supp_id.get(),
            "gender": self.var_gender.get(),
            "contact": self.var_contact.get(),
            "name": self.var_name.get(),
            "email": self.var_email.get(),
            "ptype": self.var_ptype.get(),
            "address": self.txt_sup_address.get("1.0", "end-1c")
        }

        response = requests.post("http://127.0.0.1:5000/suppliers", json=data)

        if response.status_code == 200:
            messagebox.showinfo("Success", "Supplier added successfully!")
            self.clear_entries()
            # Update this function based on your requirements
            # self.load_suppliers()
        else:
            messagebox.showerror("Error", "Failed to add supplier.")

    def update_supplier(self):
        sup_id = self.var_supp_id.get()

        if not sup_id:
            messagebox.showwarning("Warning", "Please enter a Supplier ID.")
            return

        data = {
            "gender": self.var_gender.get(),
            "contact": self.var_contact.get(),
            "name": self.var_name.get(),
            "email": self.var_email.get(),
            "ptype": self.var_ptype.get(),
            "address": self.txt_sup_address.get("1.0", "end-1c")
        }

        response = requests.put(f"http://127.0.0.1:5000/suppliers/{sup_id}", json=data)

        if response.status_code == 200:
            messagebox.showinfo("Success", "Supplier updated successfully!")
            self.clear_entries()
            # Update this function based on your requirements
            # self.load_suppliers()
        else:
            messagebox.showerror("Error", "Failed to update supplier. Supplier not found.")

    def delete_supplier(self):
        sup_id = self.var_supp_id.get()

        if not sup_id:
            messagebox.showwarning("Warning", "Please enter a Supplier ID.")
            return

        response = requests.delete(f"http://127.0.0.1:5000/suppliers/{sup_id}")

        if response.status_code == 200:
            messagebox.showinfo("Success", "Supplier deleted successfully!")
            self.clear_entries()
            # Update this function based on your requirements
            # self.load_suppliers()
        else:
            messagebox.showerror("Error", "Failed to delete supplier. Supplier not found.")

    def search_supplier(self):
        search_by = self.var_searchby.get()
        search_txt = self.var_searchtxt.get()

        if search_by == "Select" or not search_txt:
            messagebox.showwarning("Warning", "Please select a search option and enter search text.")
            return

        data = {
            "search_by": search_by.lower(),  # Convert to lowercase to match API endpoint
            "search_txt": search_txt
        }

        response = requests.post("http://127.0.0.1:5000/suppliers/search", json=data)

        if response.status_code == 200:
            suppliers = response.json()
            # Update your GUI to display the search results, e.g., populate a Treeview or update labels
            print(suppliers)  # Adjust this based on your GUI requirements
        else:
            messagebox.showerror("Error", "Failed to search for suppliers.")

    def clear_entries(self):
        self.var_supp_id.set("")
        self.var_gender.set("")
        self.var_contact.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_ptype.set("")
        self.txt_sup_address.delete("1.0", tk.END)

if __name__ == "__main__":
    root = Tk()
    obj = SuppliersClass(root)
    root.mainloop()

