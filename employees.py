from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
from time import strftime


from tkinter import *
from time import strftime


class Employee:
    def __init__(self, EmployeeFrame, variables):
        """ Initialize Employee section in GUI with Frame and Variables. """
        self.Employee_Input = variables["Employee"]
        self.Date_Input = variables["Date"]
        self.Customer_Input = variables["Customer"]
        self.Address_Input = variables["Address"]
        self.Phone_Input = variables["Phone"]
        self.Total_Input = variables["Total"]

        # Employee Label & Entry
        self.lblEmployee = Label(EmployeeFrame, bg="#827e74", fg="white", font=("arial", 12, "bold"),
                                 text="Employee Name:", bd=5)
        self.lblEmployee.grid(row=0, column=0, padx=5, pady=2)

        self.txtEmployee = Entry(EmployeeFrame, font=("arial", 12), textvariable=self.Employee_Input,
                                 bd=2, width=65)
        self.txtEmployee.grid(row=0, column=1, padx=5, pady=2)

        # Date Label & Entry
        self.lblDate = Label(EmployeeFrame, bg="#827e74", fg="white", font=("arial", 12, "bold"),
                             text="Date:", bd=5)
        self.lblDate.grid(row=0, column=2, padx=10, pady=2)

        self.Date_Input.set(strftime('%A %d %B - %H:%M:%S %p'))
        self.txtDate = Entry(EmployeeFrame, font=("arial", 12), textvariable=self.Date_Input,
                             bd=2, width=27, justify="center", state="readonly")
        self.txtDate.grid(row=0, column=3, padx=5, pady=2)

    def records(self):
        """Updates employee service records."""
        try:
            with open("Records.txt", "a+") as f:
                f.write("Receipt Details ---\n\n")
                f.write(f"Employee: {self.Employee_Input.get()}\n")
                f.write(f"Date: {self.Date_Input.get()}\n")
                f.write(f"Customer: {self.Customer_Input.get()}\n")
                f.write(f"Address: {self.Address_Input.get()}\n")
                f.write(f"Phone: {self.Phone_Input.get()}\n")
                f.write(f"Total: {self.Total_Input.get()}\n")
                f.write("\n-----------------------\n")
        except Exception as e:
            print(f"Error writing to file: {e}")



    def remove(self):
        # Clears Employee input fields. 
        self.txtEmployee.delete(0, END)
