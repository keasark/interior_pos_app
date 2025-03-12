from tkinter import *
from tkinter import ttk, messagebox
from time import strftime
from tkinter import Tk, Canvas, Scrollbar, Frame, StringVar, LabelFrame, LEFT, RIGHT, TOP, BOTTOM, RIDGE

import pandas as pd
from tkinter import PhotoImage, Button

from employees import Employee
from customers import Customer
from calculation import Calculation



class POS:
    def __init__(self, root):
        self.root = root
        self.root.title("INTERIOR STORE - Point of Sales Management Software")
        self.root.geometry("1270x688+0+0")
        self.root.configure(background="#bfa982")

        # Create a Canvas and Scrollbar
        self.canvas = Canvas(self.root, bg="#bfa982")
        self.scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a Frame inside the Canvas
        self.MainFrame = Frame(self.canvas, bg="#bfa982")
        self.canvas.create_window((0, 0), window=self.MainFrame, anchor="nw")

        # Update scroll region after widgets are added
        self.MainFrame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))


        # Define frames with attributes
        frames = {
            "EmployeeFrame": (0, "#827e74", 1240, 60),
            "ItemFrame": (1, "#916820", 1348, 80),
            "DataFrame": (2, "#69665f", 1348, 80),
            "ButtonFrame": (3, "#bfa982", 1348, 80)}
        
        # Create frame objects and store them in a dictionary
        self.frames = {
            name: Frame(self.MainFrame, bg=color, bd=5, width=w, height=h, padx=4, pady=4, relief=RIDGE)
            for name, (row, color, w, h) in frames.items()}
        

        # Grid layout for frames inside MainFrame
        for name, (row, _, _, _) in frames.items():
            self.frames[name].grid(row=row, column=0, sticky="ew", padx=4, pady=5)


        # StringVar Variables
        vars_list = ["Employee", "Date", "Change", "Cash", "Tax", "Fees", "Discount", "SubTotal", "Total", "Item", "Qty", "Amount", "choice", "Sign", "Customer", "Address", "Phone", "Point"]
        self.variables = {var: StringVar() for var in vars_list}
        

        # Initialize components
        self.employee = Employee(self.frames["EmployeeFrame"], self.variables)

        CustomerFrame = Frame(self.frames["DataFrame"], bd=5, width=360, height=140, relief=RIDGE)
        CustomerFrame.grid(row=0, column=0, padx=5)
        self.customer = Customer(CustomerFrame, self.variables)

        CalFrame = Frame(self.frames["DataFrame"], bd=5, width=432, height=140, relief=RIDGE)
        CalFrame.grid(row=0, column=1, padx=5, pady=5)  

        ChangeFrame = Frame(self.frames["DataFrame"], bd=5, width=500, height=140, relief=RIDGE)
        ChangeFrame.grid(row=0, column=2, padx=5, pady=5)  

        Calculation(CalFrame, ChangeFrame, self.variables["SubTotal"], self.variables["Tax"], 
                    self.variables["Fees"], self.variables["Discount"], self.variables["Total"], 
                    self.variables["choice"], self.variables["Cash"], self.variables["Change"], 
                    self.variables["Sign"])
        

        # Define Item Frame covers
        ItemFrameLEFTCOVER = LabelFrame(self.frames["ItemFrame"], bg="#a6a49f", bd=5, width=800, height=80,
                                        padx=4, pady=4, text="Products", fg="white", font=("arial", 12, "bold"), relief=RIDGE)
        ItemFrameLEFTCOVER.grid(row=0, column=0, sticky="nsew")

        ItemFrameRIGHTCOVER = LabelFrame(self.frames["ItemFrame"], bg="#916820", bd=5, width=800, height=80,
                                         padx=4, pady=4, font=("arial", 12, "bold"), fg="white",
                                         text="Receipt", relief=RIDGE)
        ItemFrameRIGHTCOVER.grid(row=0, column=1, sticky="nsew")
        ItemFrameRIGHTCOVER.grid_rowconfigure(0, weight=1)  # Allow it to resize dynamically


        # Change Button Frame inside ItemFrameLEFTCOVER
        self.frames["ChangeButtonFrame"] = LabelFrame(ItemFrameLEFTCOVER, bg="#827e74", bd=5, width=800, height=80,
                                                      padx=4, pady=4, font=("arial", 12, "bold"), fg="white",
                                                      text="Bathroom Facilities", relief=RIDGE)
        self.frames["ChangeButtonFrame"].grid(row=1, column=0, padx=4)


        self.frames["ButtonFrame"].grid(row=3, column=0, sticky="ew")  # Ensure proper positioning


        # Load product data from CSV file
        file_path = "product_price.csv"
        df = pd.read_csv(file_path)

        # Create image list dynamically
        self.images = [(row["name"], PhotoImage(file=f"images/{row['name'].lower().replace(' ', '-')}.png"), row["price"]) for _, row in df.iterrows()]

        
        # Generate image buttons
        for r, (name, img, cost) in enumerate(self.images):
            Button(self.frames["ChangeButtonFrame"], image=img, height=60, width=60,
                   command=lambda n=name, c=cost: self.add_item(n, c)).grid(row=r//6, column=r%6, padx=6, pady=2)

        self.ItemFrame = Frame(ItemFrameRIGHTCOVER, bd=5, relief=RIDGE, height=300)  # Reduce height
        self.ItemFrame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")


        # Create Treeview widget (Receipt area)
        self.POS_records = ttk.Treeview(
            self.ItemFrame, columns=("Item", "Qty", "Amount"), show="headings")


        # Display Buttons
        actions = [("PAY", self.giveChange), ("REMOVE", self.delete), ("RESET", self.reset), ("EXIT", self.iExit)]
        for i, (text, cmd) in enumerate(actions):
            btn = Button(self.frames["ButtonFrame"], text=text, command=cmd, width=10, height=1,
                         font=("arial", 12, "bold"), bg="#d68d09", fg='white', bd=5)
            btn.grid(row=0, column=i, padx=90, pady=2)


        # Treeview (Receipt)
        scroll_x, scroll_y = Scrollbar(ItemFrameRIGHTCOVER, orient=HORIZONTAL), Scrollbar(self.frames["ItemFrame"], orient=VERTICAL)

        # Create Treeview widget (Receipt section) with grid
        self.POS_records = ttk.Treeview(
            self.ItemFrame, columns=("Item", "Qty", "Amount"), show="headings")
        self.POS_records.grid(row=0, column=0, sticky="nsew")

        self.POS_records.heading("#0", text="Item")  # Rename the default first column
        self.POS_records.column("#0", width=200, anchor="w")  # Set width, align left

        scroll_x = Scrollbar(self.ItemFrame, orient=HORIZONTAL, command=self.POS_records.xview)
        scroll_y = Scrollbar(self.ItemFrame, orient=VERTICAL, command=self.POS_records.yview)

        self.POS_records.heading("Item", text="Item")  # Set the default identifier column name
        self.POS_records.column("#0", width=200, anchor="w")    # Adjust its width
        
        for col in ["Qty", "Amount"]:
            self.POS_records.heading(col, text=col)
            self.POS_records.column(col, width=80)

        self.POS_records.grid(row=0, column=0, padx=4, pady=4, sticky="nsew")


        # Configure the grid for resizing behavior
        self.ItemFrame.grid_rowconfigure(0, weight=1)
        self.ItemFrame.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(6, weight=1)  
        self.root.grid_columnconfigure(0, weight=1)
        

    def calculate_totals(self):
        """Calculates and updates Discount, Fees, Tax, Total, and Change."""
        tax_rate = 0.0825  # Texas Tax 8.25%
        fees_rate = 0.02   # 2% Fees
        discount_rate = 0.10  # 10% Discount
        edge = 100  # Conversion factor for points

        # Retrieve ItemCost
        try:
            ItemCost = float(self.variables["SubTotal"].get().strip()) if self.variables["SubTotal"].get() else 0.0
        except ValueError:
            ItemCost = 0.0

        # Apply discount
        discount_amount = ItemCost * discount_rate
        discounted_price = ItemCost - discount_amount

        # Calculate Tax and Fees
        tax = discounted_price * tax_rate
        fees = discounted_price * fees_rate
        total_with_fees = discounted_price + tax + fees

        # Update StringVar values
        self.variables["Discount"].set(f"{discount_amount:.2f}")
        self.variables["Fees"].set(f"{fees:.2f}")
        self.variables["Tax"].set(f"{tax:.2f}")
        self.variables["Total"].set(f"{total_with_fees:.2f}")
        self.variables["Change"].set(f"{float(self.variables['Cash'].get() or 0) - total_with_fees:.2f}")
        self.variables["choice"].set(f"{ItemCost // edge:.2f}")  # Convert total into points

    def update_records(self, action="Receipt Details"):
        """Updates the Records.txt file with the latest transaction details."""
        with open("Records.txt", "a") as f:
            f.write(f"\n{action} ---\n\n")
            f.write(f"Employee: {self.variables['Employee'].get()}\n")
            f.write(f"Date: {self.variables['Date'].get()}\n")
            f.write(f"Customer: {self.variables['Customer'].get()}\n")
            f.write(f"Address: {self.variables['Address'].get()}\n")
            f.write(f"Phone: {self.variables['Phone'].get()}\n")
            f.write("\nItems Purchased:\n")

            # Save all items in the receipt
            for row_id in self.POS_records.get_children():
                row = self.POS_records.item(row_id)['values']
                f.writelines(str(row) + "\n")

            f.write("\n-----------------------\n")

    def giveChange(self):
        """Handles payment calculations and updates records when the PAY button is clicked."""
        self.calculate_totals()
        self.employee.records()
        self.update_records("Receipt Details")

        # Prevent stacking when pressing PAY multiple times
        if self.variables["Cash"].get() == "0":
            self.variables["Change"].set("")

    def delete(self):
        """Removes the selected item from the Treeview and updates calculations."""
        selected = self.POS_records.selection()
        if selected:
            for item in selected:
                self.POS_records.delete(item)

        # Update the subtotal after deletion
        total = sum(float(self.POS_records.item(child, "values")[2]) for child in self.POS_records.get_children())
        self.variables["SubTotal"].set(f"{total:.2f}")

        # Recalculate values
        self.calculate_totals()
        
        # Update records
        self.update_records("Updated Receipt Details")

        print("Item deleted, and records updated.")


    def reset(self):
        """Resets all fields in the POS system."""
        for var in self.variables.values():
            var.set("")
        for item in self.POS_records.get_children():
            self.POS_records.delete(item)
        print("Reset complete.")

    def iExit(self):
        """Closes the application."""
        self.root.destroy()


    # Functions for Item Buttons
    def add_item(self, name, cost):
        """Adds an item to the POS system and updates subtotal."""
        self.POS_records.insert("", "end", values=(name, "1", cost))

        # Store total value
        total = sum(float(self.POS_records.item(child, "values")[2]) for child in self.POS_records.get_children())
        self.variables["SubTotal"].set(f"{total:.2f}")

