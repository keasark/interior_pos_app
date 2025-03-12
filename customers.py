from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
from time import strftime


class Customer:
    def __init__(self, CustomerFrame, variables):
        """ Initialize Customer section in GUI with Frame and Variables. """
        self.Customer_Input = variables["Customer"]
        self.Address_Input = variables["Address"]
        self.Phone_Input = variables["Phone"]

        # Customer widget
        self.lblCustomer = Label(CustomerFrame, font=("arial", 12, "bold"), text="Customer", bd=5)
        self.lblCustomer.grid(row=0, column=0, sticky=W, padx=5)

        self.txtCustomer = Entry(CustomerFrame, font=("arial", 12), textvariable=self.Customer_Input,
                                 bd=2, width=35)
        self.txtCustomer.grid(row=0, column=1, sticky="w")
        
        # Address widget
        self.lblAddress = Label(CustomerFrame, font=("arial", 12, "bold"), text="Address", bd=5)
        self.lblAddress.grid(row=1, column=0, sticky=W, padx=5)

        self.txtAddress = Entry(CustomerFrame, font=("arial", 12), textvariable=self.Address_Input,
                                bd=2, width=35)
        self.txtAddress.grid(row=1, column=1, sticky=W, padx=5)

        # Phone widget
        self.lblPhone = Label(CustomerFrame, font=("arial", 12, "bold"), text="Phone", bd=5)
        self.lblPhone.grid(row=2, column=0, sticky=W, padx=5)

        self.txtPhone = Entry(CustomerFrame, font=("arial", 12), textvariable=self.Phone_Input,
                              bd=2, width=35)
        self.txtPhone.grid(row=2, column=1, sticky=W, padx=5)



    def customerInfo(self, total_purchase):
        """ Updates customer points based on total purchase and
        saves it to 'CustomerList.txt'. """
        edge = 10  # Points conversion rate (1 point per $10)
        earned_points = int(total_purchase // edge)

        result = []
        found = False

        try:
            with open("CustomerList.txt", "r") as f:
                for line in f:
                    data = line.strip().split(', ')
                    if data and data[0].lower() == self.Customer_Input.get().lower():
                        data[3] = str(int(data[3]) + earned_points)  # Update points
                        found = True
                    result.append(", ".join(data))

        except FileNotFoundError:
            # If file doesn't exist, create a new entry
            pass

        # If the customer is not found, add them to the list
        if not found:
            result.append(f"{self.Customer_Input.get()}, {self.Address_Input.get()}, {self.Phone_Input.get()}, {earned_points}")

        # Write the updated records back to file
        with open("CustomerList.txt", "w") as f:
            f.write("\n".join(result) + "\n")

    def remove(self):
        """ Clears all customer input fields. """
        self.txtCustomer.delete(0, END)
        self.txtAddress.delete(0, END)
        self.txtPhone.delete(0, END)
        self.txtPoints.delete(0, END)
