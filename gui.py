from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
from time import strftime


class POS:
    def __init__(self, root):
        self.root = root
        self.root.title("LUX FURNITURE - Point of Sales")
        self.root.geometry("1330x788+0+0")
        self.root.configure(background="#bfa982")

        # STRINGVAR VARIABLES ----------------------------------
        # Employee Info
        Employee_Input = StringVar()
        Date_Input = StringVar()
        # Customer Info
        Customer_Input = StringVar()
        Address_Input = StringVar()
        Phone_Input = StringVar()
        Points_Input = StringVar()
        # Purchase Info
        Change_Input = StringVar()
        Cash_Input = StringVar()
        Tax_Input = StringVar()
        Fees_Input = StringVar()
        Discount_Input = StringVar()
        SubTotal_Input = StringVar()
        Total_Input = StringVar()
        Item = StringVar()
        Qty = StringVar()
        Amount = StringVar()
        choice = StringVar()
        # Signature Info
        Sign_Input = StringVar()

        # Photo Images --------------------------------
        self.ArmChair = PhotoImage(file="images/armchair.png")
        self.VinSofa = PhotoImage(file="images/vintage-sofa.png")
        self.CafeChair = PhotoImage(file="images/coffee-chair.png")
        self.ChatChair = PhotoImage(file="images/chat-chair.png")
        self.MagChair = PhotoImage(file="images/magazine-chair.png")
        self.LongSofa = PhotoImage(file="images/long-sofa.png")
        self.HangChair = PhotoImage(file="images/hanging-chair.png")
        self.BeachChair = PhotoImage(file="images/beach-chair.png")

        self.GameChair = PhotoImage(file="images/game-chair.png")
        self.VrChair = PhotoImage(file="images/vr-chair.png")
        self.HamChair = PhotoImage(file="images/hammock-chair.png")
        self.FlowerChair = PhotoImage(file="images/flower-chair.png")
        self.VelChair = PhotoImage(file="images/velvet-chair.png")
        self.Lounge = PhotoImage(file="images/lounge.png")
        self.KoreanSofa = PhotoImage(file="images/korean-sofa.png")
        self.OfficeChair = PhotoImage(file="images/office-chair.png")

        self.DoctorChair = PhotoImage(file="images/doctor-chair.png")
        self.FutureChair = PhotoImage(file="images/future-chair.png")
        self.GreenSofa = PhotoImage(file="images/green-sofa.png")
        self.SofaSet = PhotoImage(file="images/sofa-set.png")
        self.OvalChair = PhotoImage(file="images/oval-chair.png")
        self.LuxurySofa = PhotoImage(file="images/luxury-sofa.png")
        self.PremiumChair = PhotoImage(file="images/premium-chair.png")
        self.SeaSofa = PhotoImage(file="images/seaview-sofa.png")

        self.RoyalSofa = PhotoImage(file="images/royal-sofa.png")
        self.RedSofa = PhotoImage(file="images/red-sofa.png")
        self.RoyalBed = PhotoImage(file="images/royal-bed.png")
        self.VinBed = PhotoImage(file="images/vintage-bed.png")
        self.ClassBed = PhotoImage(file="images/classic-bed.png")
        self.RedBed = PhotoImage(file="images/red-bed.png")
        self.WhiteBed = PhotoImage(file="images/white-bed.png")
        self.KidBed = PhotoImage(file="images/kid-bed.png")


        # CREATE MAIN FRAMES -------------------------------
        MainFrame = Frame(self.root, bg="#bfa982")
        MainFrame.grid(padx=8, pady=5)

        EmployeeFrame = Frame(MainFrame, bg="#827e74", bd=5, width=1240, height=60,
                              padx=4, pady=4, relief=RIDGE)
        EmployeeFrame.pack(side=TOP)

        ItemFrame = Frame(MainFrame, bg="#916820", bd=5, width=1348, height=160,
                          padx=4, pady=4, relief=RIDGE)
        ItemFrame.pack()

        DataFrame = Frame(MainFrame, bg="#69665f", bd=5, width=1348, height=160,
                          padx=4, pady=4, relief=RIDGE)
        DataFrame.pack()

        ButtonFrame = Frame(MainFrame, bg="#bfa982", bd=0, width=1348, height=160,
                            padx=4, pady=4, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        ItemFrameLEFTCOVER = LabelFrame(ItemFrame, bg="#a6a49f", bd=5, width=800, height=300,
                                        padx=4, pady=4, text="Items", font=("arial", 12, "bold"),
                                        relief=RIDGE)
        ItemFrameLEFTCOVER.pack(side=LEFT)

        ItemFrameRIGHTCOVER = LabelFrame(ItemFrame, bg="#916820", bd=5, width=800, height=300,
                                         padx=4, pady=4, font=("arial", 12, "bold"), fg="white",
                                         text="Receipt Details", relief=RIDGE)
        ItemFrameRIGHTCOVER.pack(side=RIGHT)

        ChangeButtonFrame = LabelFrame(ItemFrameLEFTCOVER, bg="#827e74", bd=5, width=800, height=300,
                                       padx=4, pady=4, font=("arial", 12, "bold"), fg="white",
                                       text="MODERN FURNITURE", relief=RIDGE)
        ChangeButtonFrame.pack(side=TOP, padx=4)

        ReceiptFrame = Frame(ItemFrameRIGHTCOVER, bd=5, width=200, height=400, padx=1, pady=5,
                             relief=RIDGE)
        ReceiptFrame.pack(side=RIGHT, padx=4)

        CustomerFrame = Frame(DataFrame, bd=5, width=360, height=140, relief=RIDGE)
        CustomerFrame.grid(row=0, column=0, padx=5)

        CalFrame = Frame(DataFrame, bd=5, width=432, height=140, relief=RIDGE)
        CalFrame.grid(row=0, column=1, padx=5)

        ChangeFrame = Frame(DataFrame, width=500, height=140, pady=2, relief=RIDGE)
        ChangeFrame.grid(row=0, column=2, padx=5)

        RemoveFrame = Frame(ButtonFrame, width=400, bg="#bfa982", height=140, pady=4, relief=RIDGE)
        RemoveFrame.grid(row=1, column=0, padx=5)

        # Display Employee Frame & Widgets
        Employee(EmployeeFrame, Employee_Input, Date_Input)

        # Display Customer Frame & Widgets
        Customer(CustomerFrame, Customer_Input, Address_Input, Phone_Input, Points_Input)

        # Display Calculation Frame & Widgets
        Calculation(CalFrame, ChangeFrame, SubTotal_Input, Tax_Input, Fees_Input, Discount_Input,
                    Total_Input, choice, Cash_Input, Change_Input, Sign_Input)


        # FUNCTIONS for IMAGES ---------------------------------------------------
        Tax = 2.5

        # Row 1 ------------------------------------------------------------------
        def ArmChair():
            ItemCost = 299
            self.POS_records.insert("", tk.END, values=("Armchair", "1", "299"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 299)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 299) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 299) + ((ItemCost - 299) * Tax) / 100)))

        def VinSofa():
            ItemCost = 199
            self.POS_records.insert("", tk.END, values=("Vintage Sofa", "1", "199"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 199)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 199) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 199) + ((ItemCost - 199) * Tax) / 100)))

        def CafeChair():
            ItemCost = 249
            self.POS_records.insert("", tk.END, values=("Coffee Chair", "1", "249"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 249)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 249) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 249) + ((ItemCost - 249) * Tax) / 100)))

        def ChatChair():
            ItemCost = 149
            self.POS_records.insert("", tk.END, values=("Chat Chair", "1", "149"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 149)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 149) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 149) + ((ItemCost - 149) * Tax) / 100)))

        def MagChair():
            ItemCost = 259
            self.POS_records.insert("", tk.END, values=("Magazine Chair", "1", "259"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 259)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 259) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 259) + ((ItemCost - 259) * Tax) / 100)))

        def LongSofa():
            ItemCost = 1599
            self.POS_records.insert("", tk.END, values=("Long Sofa", "1", "1599"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 1599)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 1599) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 1599) + ((ItemCost - 1599) * Tax) / 100)))

        def HangChair():
            ItemCost = 259
            self.POS_records.insert("", tk.END, values=("Hanging Chair", "1", "259"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 259)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 259) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 259) + ((ItemCost - 259) * Tax) / 100)))

        def BeachChair():
            ItemCost = 329
            self.POS_records.insert("", tk.END, values=("Beach Chair", "1", "329"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 329)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 329) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 329) + ((ItemCost - 329) * Tax) / 100)))

        # GameChair, VrChair, HamChair, FlowerChair, VelChair, Lounge, KoreanSofa, OfficeChair
        # Row 2 ------------------------------------------------------------------
        def GameChair():
            ItemCost = 649
            self.POS_records.insert("", tk.END, values=("Gaming Chair", "1", "649"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 649)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 649) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 649) + ((ItemCost - 649) * Tax) / 100)))

        def VrChair():
            ItemCost = 849
            self.POS_records.insert("", tk.END, values=("VR Chair", "1", "849"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 849)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 849) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 849) + ((ItemCost - 849) * Tax) / 100)))

        def HamChair():
            ItemCost = 329
            self.POS_records.insert("", tk.END, values=("Hammock Chair", "1", "329"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 329)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 329) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 329) + ((ItemCost - 329) * Tax) / 100)))

        def FlowerChair():
            ItemCost = 349
            self.POS_records.insert("", tk.END, values=("Flower Chair", "1", "349"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 349)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 349) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 349) + ((ItemCost - 349) * Tax) / 100)))

        def VelChair():
            ItemCost = 429
            self.POS_records.insert("", tk.END, values=("Velvet Chair", "1", "429"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 429)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 429) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 429) + ((ItemCost - 429) * Tax) / 100)))

        def Lounge():
            ItemCost = 329
            self.POS_records.insert("", tk.END, values=("Lounge Chair", "1", "329"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 329)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 329) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 329) + ((ItemCost - 329) * Tax) / 100)))

        def KoreanSofa():
            ItemCost = 529
            self.POS_records.insert("", tk.END, values=("Korean Sofa", "1", "529"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 529)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 529) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 529) + ((ItemCost - 529) * Tax) / 100)))

        def OfficeChair():
            ItemCost = 259
            self.POS_records.insert("", tk.END, values=("Office Chair", "1", "259"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 259)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 259) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 259) + ((ItemCost - 259) * Tax) / 100)))

        # DoctorChair, FutureChair, GreenSofa, SofaSet, OvalChair, LuxurySofa, PremiumChair, SeaSofa
        # Row 3 ------------------------------------------------------------------
        def DoctorChair():
            ItemCost = 1399
            self.POS_records.insert("", tk.END, values=("Doctor Chair", "1", "1399"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 1399)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 1399) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 1399) + ((ItemCost - 1399) * Tax) / 100)))

        def FutureChair():
            ItemCost = 359
            self.POS_records.insert("", tk.END, values=("Future Chair", "1", "359"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 359)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 359) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 359) + ((ItemCost - 359) * Tax) / 100)))

        def GreenSofa():
            ItemCost = 569
            self.POS_records.insert("", tk.END, values=("Green Sofa", "1", "569"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 569)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 569) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 569) + ((ItemCost - 569) * Tax) / 100)))

        def SofaSet():
            ItemCost = 3599
            self.POS_records.insert("", tk.END, values=("Sofa Set", "1", "3599"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 3599)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 3599) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 3599) + ((ItemCost - 3599) * Tax) / 100)))

        def OvalChair():
            ItemCost = 399
            self.POS_records.insert("", tk.END, values=("Oval Red Chair", "1", "399"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 399)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 399) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 399) + ((ItemCost - 399) * Tax) / 100)))

        def LuxurySofa():
            ItemCost = 5689
            self.POS_records.insert("", tk.END, values=("Luxury Sofa", "1", "5689"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 5689)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 5689) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 5689) + ((ItemCost - 5689) * Tax) / 100)))

        def PremiumChair():
            ItemCost = 2589
            self.POS_records.insert("", tk.END, values=("Premium Chair", "1", "2589"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 2589)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 2589) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 2589) + ((ItemCost - 2589) * Tax) / 100)))

        def SeaSofa():
            ItemCost = 2589
            self.POS_records.insert("", tk.END, values=("Seaview Outdoor Sofa", "1", "2589"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 2589)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 2589) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 2589) + ((ItemCost - 2589) * Tax) / 100)))

        # RoyalSofa, RedSofa, RoyalBed, VinBed, ClassBed, RedBed, WhiteBed, KidBed
        # Row 4 ------------------------------------------------------------------
        def RoyalSofa():
            ItemCost = 4999
            self.POS_records.insert("", tk.END, values=("Royal Sofa", "1", "4999"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 4999)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 4999) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 4999) + ((ItemCost - 4999) * Tax) / 100)))

        def RedSofa():
            ItemCost = 2569
            self.POS_records.insert("", tk.END, values=("Red Sofa", "1", "2569"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 2569)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 2569) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 2569) + ((ItemCost - 2569) * Tax) / 100)))

        def RoyalBed():
            ItemCost = 12569
            self.POS_records.insert("", tk.END, values=("Royal Bed", "1", "12569"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 12569)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 12569) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 12569) + ((ItemCost - 12569) * Tax) / 100)))

        def VinBed():
            ItemCost = 10569
            self.POS_records.insert("", tk.END, values=("Vintage Bed", "1", "10569"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 10569)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 10569) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 10569) + ((ItemCost - 10569) * Tax) / 100)))

        def ClassBed():
            ItemCost = 11569
            self.POS_records.insert("", tk.END, values=("Classic Bed", "1", "11569"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 11569)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 11569) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 11569) + ((ItemCost - 11569) * Tax) / 100)))

        def RedBed():
            ItemCost = 8569
            self.POS_records.insert("", tk.END, values=("Red Bed", "1", "8569"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 8569)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 8569) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 8569) + ((ItemCost - 8569) * Tax) / 100)))

        def WhiteBed():
            ItemCost = 7569
            self.POS_records.insert("", tk.END, values=("White Bed", "1", "7569"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 7569)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 7569) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 7569) + ((ItemCost - 7569) * Tax) / 100)))

        def KidBed():
            ItemCost = 1569
            self.POS_records.insert("", tk.END, values=("Kid Bed", "1", "1569"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str("$ %.2f" % (ItemCost - 1569)))
                Tax_Input.set(str("$ %.2f" % (((ItemCost - 1569) * Tax) / 100)))
                Total_Input.set(str("%.2f" % ((ItemCost - 1569) + ((ItemCost - 1569) * Tax) / 100)))



        # FUNCTIONS for BUTTONS --------------------------
        def delete():  # Remove an item
            ItemCost = 0.0
            CashInput = float(Cash_Input.get())
            TotalInput = Total_Input.get()
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])

            SubTotal_Input.set(str("$ %.2f" % (ItemCost)))
            Tax_Input.set(str("$ %.2f" % ((ItemCost * Tax / 100))))
            Fees_Input.set(str("$ %.2f" % ((ItemCost * 2.0 / 100))))
            Discount_Input.set(str("$ %.2f" % ((ItemCost * 10 / 100))))
            Points_Input.set(str("%.2f" % (ItemCost // 100)))

            # Calculate and Display the new Total Cost after updating the Discount
            TotalInput = str((ItemCost - (ItemCost * 10 / 100) + ((ItemCost * Tax / 100) +
                                                                  (ItemCost * 2.0 / 100))))
            Total_Input.set(str("%.2f" % ((ItemCost - (ItemCost * 10 / 100) + ((ItemCost * Tax / 100) +
                                                                               (ItemCost * 2.0 / 100))))))

            # Calculate and Display the change money on screen
            Change_Input.set(str("$ %.2f" % (CashInput - (ItemCost - (ItemCost * 10 / 100) +
                                                          ((ItemCost * Tax / 100) + (ItemCost * 2.0 / 100))))))
            selectedItem = (self.POS_records.selection()[0])
            self.POS_records.delete(selectedItem)

        def giveChange():
            Fees = 2.0
            # for every $100 purchase, customer will get 1 point
            edge = 100
            # for the current Marketing campaign, current discount is 10%
            discount = 10/100
            ItemCost = 0.0

            CashInput = float(Cash_Input.get())

            EmployeeInput = Employee_Input.get()
            DateInput = Date_Input.get()
            CustomerInput = Customer_Input.get()
            AddressInput = Address_Input.get()
            PhoneInput = Phone_Input.get()
            PointsInput = Points_Input.get()
            TotalInput = Total_Input.get()

            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])

            # Calculate the Fees, Points and Discount
            Fees_Input.set(str("$ %.2f" % (ItemCost * 2.0 / 100)))
            Points_Input.set(str("%.2f" % (ItemCost // 100)))
            Discount_Input.set(str("$ %.2f" % (ItemCost * 10 // 100)))

            # Calculate and Display the new Total Cost after updating the Discount
            TotalInput = str((ItemCost - (ItemCost * 10 / 100) + ((ItemCost * Tax / 100) +
                                                                      (ItemCost * 2.0 / 100))))
            Total_Input.set(str("%.2f" % ((ItemCost - (ItemCost * 10 / 100) + ((ItemCost * Tax / 100) +
                                                                      (ItemCost * 2.0 / 100))))))

            # Calculate and Display the change money on screen
            Change_Input.set(str("$ %.2f" % (CashInput - (ItemCost - (ItemCost * 10 / 100) + ((ItemCost * Tax / 100) +
                                                                      (ItemCost * 2.0 / 100))))))

            if Cash_Input.get() == "0":
                Change_Input.set("")
                Method_of_Pay()

            # Save Employee service records into Records File
            Employee.records(EmployeeInput, DateInput, CustomerInput, AddressInput, PhoneInput, TotalInput)

            # Save Receipt Details of the transaction into Records File
            f = open("Records.txt", "a+")
            f.write("Receipt Details ---\n\n")
            for row_id in self.POS_records.get_children():
                row = self.POS_records.item(row_id)['values']
                f.writelines(str(row))
                f.write("\n")
            f.write("\n-----------------------\n")
            f.close()


            # Customer.customerInfo(CustomerInput, AddressInput, PhoneInput, PointsInput, TotalInput)

        def iExit():
            iExit = tkinter.messagebox.askyesno("Point of Sales", "Do you want to quit the program?")
            if iExit > 0:
                root.destroy()
                return 0

        def Method_of_Pay():
            if choice.get() == "Cash":
                self.txtCost.focus()
                Cash_Input.set("")
            elif choice.get() == "Cash":
                Cash_Input.set("0")
                Change_Input.set("")


        def reset():
            # Assign employee variable
            employee = Employee(EmployeeFrame, Employee_Input, Date_Input)
            # Assign customer variable
            customer = Customer(CustomerFrame, Customer_Input, Address_Input, Phone_Input, Points_Input)
            # Assign calculation variable
            calculation = Calculation(CalFrame, ChangeFrame, SubTotal_Input, Tax_Input, Fees_Input, Discount_Input,
                        Total_Input, choice, Cash_Input, Change_Input, Sign_Input)

            # Remove the current value in employee entry
            employee.remove()
            # Remove the current value in customer entry
            customer.remove()
            # Remove the current value in calculation entry
            calculation.remove()

            # Clear all current items in Treeview table
            for item in self.POS_records.get_children():
                self.POS_records.delete(item)


        # BUTTONS ---------------------------------------------------------------------------
        # Pay button
        self.btnPay = Button(RemoveFrame, padx=2, bg="#d68d09", fg='white', font=("arial", 12, "bold"),
                             text="PAY", bd=5, width=10, height=1, command=giveChange)
        self.btnPay.grid(row=0, column=0, padx=90, pady=2)

        # Remove Item button
        self.btnRemoveItem = Button(RemoveFrame, padx=2, bg="#d68d09", fg='white', font=("arial", 12, "bold"),
                                    text="REMOVE", bd=5, width=10, height=1, command=delete)
        self.btnRemoveItem.grid(row=0, column=1, padx=90, pady=2)

        # Reset button
        self.btnReset = Button(RemoveFrame, padx=2, bg="#d68d09", fg='white', font=("arial", 12, "bold"),
                               text="RESET", bd=5, width=10, height=1, command=reset)
        self.btnReset.grid(row=0, column=2, padx=90, pady=2)

        # Exit button
        self.btnExit = Button(RemoveFrame, padx=2, bg="#d68d09", fg='white', font=("arial", 12, "bold"),
                              text="EXIT", bd=5, width=10, height=1, command=iExit)
        self.btnExit.grid(row=0, column=3, padx=90, pady=2)


        # TREEVIEW widget -------------------------------------------------------------------------        
        scroll_x = Scrollbar(ReceiptFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(ReceiptFrame, orient=VERTICAL)

        self.POS_records = ttk.Treeview(ReceiptFrame, height=20, columns=("Item", "Qty", "Amount"),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.POS_records.heading("Item", text="Item")
        self.POS_records.heading("Qty", text="Qty")
        self.POS_records.heading("Amount", text="Amount")

        self.POS_records["show"] = "headings"

        self.POS_records.column("Item", width=120)
        self.POS_records.column("Qty", width=100)
        self.POS_records.column("Amount", width=100)

        self.POS_records.pack(fill=BOTH, expand=1)
        self.POS_records.bind("<ButtonRelease-1>")

        # IMAGE BUTTONS --------------------------------------------------------------------
        # DoctorChair, FutureChair, GreenSofa, SofaSet, OvalChair, LuxurySofa, PremiumChair, SeaSofa
        # RoyalSofa, RedSofa, RoyalBed, VinBed, ClassBed, RedBed, WhiteBed, KidBed

        ImgButtons = ["btnArmChair", "btnVinSofa", "btnCafeChair", "btnChatChair", "btnMagChair",
                      "btnLongSofa", "btnHangChair", "btnBeachChair", "btnGameChair", "btnVrChair",
                      "btnHamChair", "btnFlowerChair", "btnVelChair", "btnLounge", "btnKoreanSofa",
                      "btnOfficeChair", "btnDoctorChair", "btnFutureChair", "btnGreenSofa", "btnSofaSet",
                      "btnOvalChair", "btnLuxurySofa", "btnPremiumChair", "btnSeaSofa", "btnRoyalSofa",
                      "btnRedSofa", "btnRoyalBed", "btnVinBed", "btnClassBed", "btnRedBed",
                      "btnWhiteBed", "btnKidBed"]

        Coffee = [self.ArmChair, self.VinSofa, self.CafeChair, self.ChatChair, self.MagChair,
                  self.LongSofa, self.HangChair, self.BeachChair, self.GameChair, self.VrChair,
                  self.HamChair, self.FlowerChair, self.VelChair, self.Lounge, self.KoreanSofa,
                  self.OfficeChair, self.DoctorChair, self.FutureChair, self.GreenSofa, self.SofaSet,
                  self.OvalChair, self.LuxurySofa, self.PremiumChair, self.SeaSofa, self.RoyalSofa,
                  self.RedSofa, self.RoyalBed, self.VinBed, self.ClassBed, self.RedBed,
                  self.WhiteBed, self.KidBed]

        Columns = [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]
        Rows = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4]
        Commands = [ArmChair, VinSofa, CafeChair, ChatChair, MagChair, LongSofa, HangChair, BeachChair,
                    GameChair, VrChair, HamChair, FlowerChair, VelChair, Lounge, KoreanSofa, OfficeChair,
                    DoctorChair, FutureChair, GreenSofa, SofaSet, OvalChair, LuxurySofa, PremiumChair,
                    SeaSofa, RoyalSofa, RedSofa, RoyalBed, VinBed, ClassBed, RedBed, WhiteBed, KidBed]

        #for r in range(4):
        for r, col, btn, cof, com in zip(Rows, Columns, ImgButtons, Coffee, Commands):
            self.btn = Button(ChangeButtonFrame, padx=3, image=cof, width=95, height=95, bd=2, command=com)
            self.btn.grid(row=r, column=col, padx=4, pady=2)


class Employee:
    def __init__(self, EmployeeFrame, Employee_Input, Date_Input):
        # EMPLOYEE FRAME ------------------------------------------------------------
        # Employee widget
        self.lblEmployee = Label(EmployeeFrame, bg="#827e74", fg="white", font=("arial", 12, "bold"),
                                 text="Employee", bd=5)
        self.lblEmployee.grid(row=0, column=0, padx=4, pady=2)

        self.txtEmployee = Entry(EmployeeFrame, font=("arial", 12, "bold"), textvariable=Employee_Input,
                                 bd=2, width=50)
        self.txtEmployee.grid(row=0, column=1, padx=4, pady=2)

        # Blank Label
        self.lblBlank1 = Label(EmployeeFrame, bg="#827e74", text="                    ", bd=5)
        self.lblBlank1.grid(row=0, column=2, padx=4, pady=2)
        self.lblBlank2 = Label(EmployeeFrame, bg="#827e74", text="                    ", bd=5)
        self.lblBlank2.grid(row=0, column=3, padx=4, pady=2)
        self.lblBlank3 = Label(EmployeeFrame, bg="#827e74", text="                    ", bd=5)
        self.lblBlank3.grid(row=0, column=4, padx=4, pady=2)

        # Date widget
        self.lblDate = Label(EmployeeFrame, bg="#827e74", fg="white", font=("arial", 12, "bold"),
                             text="Date", bd=5)
        self.lblDate.grid(row=0, column=5, padx=4, pady=2)
        # Create an instance of datetime module
        # date = dt.datetime.now()
        # Format the date
        # format_date = f"{date:%a, %b %d %Y}"
        time_string = strftime('%A %d %B - %H:%M:%S %p')
        # Display the date in a a label widget
        self.txtDate = Entry(EmployeeFrame, font=("arial", 12, "bold"), textvariable=Date_Input, bd=2,
                             width=47, justify="center")
        self.txtDate.insert(END, time_string)
        self.txtDate.grid(row=0, column=6, padx=4, pady=2)

    def records(EmployeeInput, DateInput, CustomerInput, AddressInput, PhoneInput, TotalInput):
        f = open("Records.txt", "a+")
        f.write("\nEmployee: " + EmployeeInput + "\n")
        f.write("Date: " + DateInput + "\n\n")
        f.write("Customer: " + CustomerInput + "\n")
        f.write("Address: " + AddressInput + "\n")
        f.write("Phone: " + PhoneInput + "\n")
        f.write("Total Purchase: $" + TotalInput + "\n")
        f.write("\n")
        f.close()

    def remove(self):
        self.txtEmployee.delete(0, END)
        self.txtDate.delete(0, END)


class Customer:
    def __init__(self, CustomerFrame, Customer_Input, Address_Input, Phone_Input, Points_Input):
        # CUSTOMER FRAME ------------------------------------------------------------
        # Customer widget
        self.lblCustomer = Label(CustomerFrame, font=("arial", 12, "bold"), text="Customer", bd=5)
        self.lblCustomer.grid(row=0, column=0, sticky=W, padx=5)

        self.txtCustomer = Entry(CustomerFrame, font=("arial", 12, "bold"), textvariable=Customer_Input,
                                 bd=2, width=35)
        self.txtCustomer.grid(row=0, column=1, sticky=W, padx=5)

        # Address widget
        self.lblAddress = Label(CustomerFrame, font=("arial", 12, "bold"), text="Address", bd=5)
        self.lblAddress.grid(row=1, column=0, sticky=W, padx=5)

        self.txtAddress = Entry(CustomerFrame, font=("arial", 12, "bold"), textvariable=Address_Input,
                                bd=2, width=35)
        self.txtAddress.grid(row=1, column=1, sticky=W, padx=5)

        # Phone widget
        self.lblPhone = Label(CustomerFrame, font=("arial", 12, "bold"), text="Phone", bd=5)
        self.lblPhone.grid(row=2, column=0, sticky=W, padx=5)

        self.txtPhone = Entry(CustomerFrame, font=("arial", 12, "bold"), textvariable=Phone_Input,
                              bd=2, width=35)
        self.txtPhone.grid(row=2, column=1, sticky=W, padx=5)

        # Points widget
        self.lblPoints = Label(CustomerFrame, font=("arial", 12, "bold"), text="Points", bd=5)
        self.lblPoints.grid(row=3, column=0, sticky=W, padx=5)

        self.txtPoints = Entry(CustomerFrame, font=("arial", 12, "bold"), textvariable=Points_Input,
                               bd=2, width=35)
        self.txtPoints.grid(row=3, column=1, sticky=W, padx=5)


    def customerInfo(CustomerInput, AddressInput, PhoneInput, PointsInput, TotalInput):
        edge = 10
        point = int(TotalInput // edge)
        result = ""
        with open("CustomerList.txt") as f:
            for line in f:
                if line.lower().startswith((CustomerInput.lower() + ",")):
                    l = line.split(', ')
                    l[3] = str(int(l[3]) + point)
                    line = ", ".join(l)
                    result += line + "\n"
                else:
                    result += CustomerInput + ", " + AddressInput + ", " + PhoneInput + ", " + str(point) + "\n"
        f = open("CustomerList.txt", 'w')
        f.write(result)
        f.close()


    def remove(self):
        self.txtCustomer.delete(0, END)
        self.txtAddress.delete(0, END)
        self.txtPhone.delete(0, END)
        self.txtPoints.delete(0, END)


class Calculation:
    def __init__(self, CalFrame, ChangeFrame, SubTotal_Input, Tax_Input, Fees_Input, Discount_Input, Total_Input,
                 choice, Cash_Input, Change_Input, Sign_Input):
        # ENTRY & LABEL WIDGET ------------------------------------------------------------
        # Sub Total widget
        self.lblSubTotal = Label(CalFrame, font=("arial", 12, "bold"), text="Total Sales", bd=5)
        self.lblSubTotal.grid(row=0, column=0, sticky=W, padx=5)

        self.txtSubTotal = Entry(CalFrame, font=("arial", 12, "bold"), textvariable=SubTotal_Input,
                                 bd=2, width=20)
        self.txtSubTotal.grid(row=0, column=1, sticky=W, padx=5)

        # Tax widget
        self.lblTax = Label(CalFrame, font=("arial", 12, "bold"), text="Tax", bd=5)
        self.lblTax.grid(row=1, column=0, sticky=W, padx=5)

        self.txtTax = Entry(CalFrame, font=("arial", 12, "bold"), textvariable=Tax_Input,
                            bd=2, width=20)
        self.txtTax.grid(row=1, column=1, sticky=W, padx=5)

        # Fees (Packaging & Delivery Fees) widget
        self.lblFees = Label(CalFrame, font=("arial", 12, "bold"), text="Fees", bd=5)
        self.lblFees.grid(row=2, column=0, sticky=W, padx=5)

        self.txtFees = Entry(CalFrame, font=("arial", 12, "bold"), textvariable=Fees_Input,
                             bd=2, width=20)
        self.txtFees.grid(row=2, column=1, sticky=W, padx=5)

        # Discount widget
        self.lblDiscount = Label(CalFrame, font=("arial", 12, "bold"), text="Discount", bd=5)
        self.lblDiscount.grid(row=3, column=0, sticky=W, padx=5)

        self.txtDiscount = Entry(CalFrame, font=("arial", 12, "bold"), textvariable=Discount_Input,
                                 bd=2, width=20)
        self.txtDiscount.grid(row=3, column=1, sticky=W, padx=5)

        # --------------------------------------------------------------------------
        # ENTRY & LABEL WIDGET -------------------------------------------------------------

        # Total Charge widget
        self.lblTotal = Label(ChangeFrame, font=("arial", 12, "bold"), text="Charge", bd=5)
        self.lblTotal.grid(row=0, column=0, sticky=W, padx=5)

        self.txtTotal = Entry(ChangeFrame, font=("arial", 12, "bold"), textvariable=Total_Input,
                              bd=2, width=20, justify="right")
        self.txtTotal.grid(row=0, column=1, sticky=W, padx=5)

        # Method of Payment widget
        self.lblMoP = Label(ChangeFrame, font=("arial", 12, "bold"), text="Method of Payment", bd=5)
        self.lblMoP.grid(row=1, column=0, sticky=W, padx=5)

        self.cboMop = ttk.Combobox(ChangeFrame, font=("arial", 12, "bold"), width=18, state="readonly",
                                   textvariable=choice, justify=RIGHT)
        self.cboMop['values'] = ("", "Cash", "Visa", "Master Card")
        self.cboMop.current(0)
        self.cboMop.grid(row=1, column=1, sticky=W, padx=5)

        # Cash widget
        self.lblCost = Label(ChangeFrame, font=("arial", 12, "bold"), text="Customer Payment", bd=5)
        self.lblCost.grid(row=2, column=0, sticky=W, padx=5)

        self.txtCost = Entry(ChangeFrame, font=("arial", 12, "bold"), textvariable=Cash_Input,
                             bd=2, width=20, justify=RIGHT)
        self.txtCost.grid(row=2, column=1, sticky=W, padx=5)
        self.txtCost.insert(0, "0")

        # Change widget
        self.lblChange = Label(ChangeFrame, font=("arial", 12, "bold"), text="Change", bd=5)
        self.lblChange.grid(row=3, column=0, sticky=W, padx=5)

        self.txtChange = Entry(ChangeFrame, font=("arial", 12, "bold"), textvariable=Change_Input,
                               bd=2, width=20, justify=RIGHT)
        self.txtChange.grid(row=3, column=1, sticky=W, padx=5)

        # SIGNATURE widget
        self.lblSign = Label(ChangeFrame, font=("arial", 12, "bold"), text="Signature", bd=5)
        self.lblSign.grid(row=0, column=2, sticky=W, padx=5)

        self.txtSign = Entry(ChangeFrame, font=("arial", 12, "bold"), textvariable=Sign_Input,
                             bd=2, width=15, justify=RIGHT)
        self.txtSign.grid(row=1, column=2, sticky=W, padx=5)

    def remove(self):
        self.txtSubTotal.delete(0, END)
        self.txtTax.delete(0, END)
        self.txtFees.delete(0, END)
        self.txtDiscount.delete(0, END)
        self.txtTotal.delete(0, END)
        self.txtTotal.delete(0, END)
        self.txtCost.delete(0, END)
        self.txtChange.delete(0, END)
        self.txtSign.delete(0, END)


if __name__ == '__main__':
    root = Tk()
    application = POS(root)
    root.mainloop()
