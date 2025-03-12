from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
from time import strftime


class Calculation:
    def __init__(self, CalFrame, ChangeFrame, SubTotal_Input, Tax_Input, Fees_Input, Discount_Input, Total_Input,
                 choice, Cash_Input, Change_Input, Sign_Input):
        # Sub Total Widget
        self.lblSubTotal = Label(CalFrame, font=("arial", 12, "bold"), text="Total Price", bd=5)
        self.lblSubTotal.grid(row=0, column=0, sticky=W, padx=5)
        self.txtSubTotal = Entry(CalFrame, font=("arial", 12, "bold"), textvariable=SubTotal_Input, bd=2, width=20)
        self.txtSubTotal.grid(row=0, column=1, sticky=W, padx=5)

        # Discount Widget 
        self.lblDiscount = Label(CalFrame, font=("arial", 12, "bold"), text="Discount", bd=5)
        self.lblDiscount.grid(row=1, column=0, sticky=W, padx=5)
        self.txtDiscount = Entry(CalFrame, font=("arial", 12, "bold"), textvariable=Discount_Input, bd=2, width=20)
        self.txtDiscount.grid(row=1, column=1, sticky=W, padx=5)

        # Tax Widget
        self.lblTax = Label(CalFrame, font=("arial", 12, "bold"), text="Tax", bd=5)
        self.lblTax.grid(row=2, column=0, sticky=W, padx=5)
        self.txtTax = Entry(CalFrame, font=("arial", 12, "bold"), textvariable=Tax_Input, bd=2, width=20)
        self.txtTax.grid(row=2, column=1, sticky=W, padx=5)

        # Fees Widget 
        self.lblFees = Label(CalFrame, font=("arial", 12, "bold"), text="Fees", bd=5)
        self.lblFees.grid(row=3, column=0, sticky=W, padx=5)
        self.txtFees = Entry(CalFrame, font=("arial", 12, "bold"), textvariable=Fees_Input, bd=2, width=20)
        self.txtFees.grid(row=3, column=1, sticky=W, padx=5)

        # Total Charge Widget
        self.lblTotal = Label(ChangeFrame, font=("arial", 12, "bold"), text="Total Payment", bd=5)
        self.lblTotal.grid(row=0, column=0, sticky=W, padx=5)
        self.txtTotal = Entry(ChangeFrame, font=("arial", 12, "bold"), textvariable=Total_Input, bd=2, width=20, justify="right")
        self.txtTotal.grid(row=0, column=1, sticky=W, padx=5)

        # Received Payment (Cash) Widget
        self.lblCost = Label(ChangeFrame, font=("arial", 12, "bold"), text="Received Payment", bd=5)
        self.lblCost.grid(row=2, column=0, sticky=W, padx=5)
        self.txtCost = Entry(ChangeFrame, font=("arial", 12, "bold"), textvariable=Cash_Input, bd=2, width=20, justify=RIGHT)
        self.txtCost.grid(row=2, column=1, sticky=W, padx=5)
        self.txtCost.insert(0, "0")

        # Change Widget 
        self.lblChange = Label(ChangeFrame, font=("arial", 12, "bold"), text="Change", bd=5)
        self.lblChange.grid(row=3, column=0, sticky=W, padx=5)
        self.txtChange = Entry(ChangeFrame, font=("arial", 12, "bold"), textvariable=Change_Input, bd=2, width=20, justify=RIGHT)
        self.txtChange.grid(row=3, column=1, sticky=W, padx=5)

        # Signature Input 
        self.lblSign = Label(ChangeFrame, font=("arial", 12, "bold"), text="Signature", bd=5)
        self.lblSign.grid(row=4, column=0, sticky=W, padx=5)
        self.txtSign = Entry(ChangeFrame, font=("arial", 12, "bold"), textvariable=Sign_Input, bd=2, width=20, justify=RIGHT)
        self.txtSign.grid(row=4, column=1, sticky=W, padx=5)

    def remove(self):
        """Clears all input fields."""
        self.txtSubTotal.delete(0, END)
        self.txtTax.delete(0, END)
        self.txtFees.delete(0, END)  
        self.txtDiscount.delete(0, END)  
        self.txtTotal.delete(0, END)
        self.txtCost.delete(0, END)
        self.txtChange.delete(0, END)
        self.txtSign.delete(0, END)  

