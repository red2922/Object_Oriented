from tkinter import *

class TheaterWindow():
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title = ("TheaterWindow")

        #Creating the frames
        self.top_frame = Frame(self.main_window)
        self.second_frame = Frame(self.main_window)
        self.third_frame = Frame(self.main_window)
        self.fourth_frame = Frame(self.main_window)
        self.fifth_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)

        #Creating the Labels Top Frame
        self.Tickets_Sold = Label(self.top_frame, text = 'Tickets Sold', width = 30)
        self.Revenue = Label(self.top_frame, text = 'Revenue', width = 30)

        #Packing the Top Frame
        self.Tickets_Sold.pack(side = "left")
        self.Revenue.pack(side = "right")
        self.top_frame.pack()

        #Creating the Labels and Entry Second Frame
        self.AdultLabel = Label(self.second_frame, text = "Adult ticket price")
        self.AdultEntry = Entry(self.second_frame, width = 10)

        #Created a AdultRev varible that is a StringVar
        self.AdultRev = StringVar()

        self.AdultGross = Label(self.second_frame, text = "Gross Rev. Adult: ")
        self.AdultGrossRev = Label(self.second_frame, textvariable = self.AdultRev)

        #Packing Second Frame
        self.AdultLabel.pack(side = "left")
        self.AdultEntry.pack(side = "left")

        self.AdultGross.pack(side = "right")
        self.AdultGrossRev.pack(side = "right")
        self.second_frame.pack()

        #Labels and Entry for Third Frame
        self.NumAdultSoldLabel = Label(self.third_frame, text = "Number of adult tickets sold")
        self.NumAdultSoldEntry = Entry(self.third_frame, width = 10)

        #Created a AdultNetRev varible that is a string var
        self.AdultNetRev = StringVar()

        self.Net_label = Label(self.third_frame, text = "Net Rev. Adult: ")
        self.AdultNetRevLabel = Label(self.third_frame, textvariable = self.AdultNetRev)

        #Packing Third Frame
        self.NumAdultSoldLabel.pack(side = "left")
        self.NumAdultSoldEntry.pack(side = "left")

        self.Net_label.pack(side = "right")
        self.AdultNetRevLabel.pack(side = "right")

        self.third_frame.pack()

        #Fourth Frame
        self.Child_label_tic = Label(self.fourth_frame, text = "Child ticket price")
        self.Child_entry_tic = Entry(self.fourth_frame, width = 10)

        self.child_gross = StringVar()

        self.Child_Label_Gross = Label(self.fourth_frame, text = "Gross Rev. Child: ")
        self.Child_Label_Gross_tot = Label(self.fourth_frame, textvariable = self.child_gross)

        #Packing Fourth Frame
        self.Child_label_tic.pack(side = "left")
        self.Child_entry_tic.pack(side = "left")

        self.Child_Label_Gross.pack(side = "right")
        self.Child_Label_Gross_tot.pack(side = "right")

        self.fourth_frame.pack()

        #Fifth Frame
        self.Child_Num = Label(self.fifth_frame, text = "Number of child tickets sold")
        self.Child_entry = Entry(self.fifth_frame, width = 10)

        self.child_net_rev = StringVar()

        self.net_child = Label(self.fifth_frame, text = "Net Rev. Child: ")
        self.net_child_rev = Label(self.fifth_frame, textvariable = self.child_net_rev)

        #Pack Fifth Frame
        self.Child_Num.pack(side = "left")
        self.Child_entry.pack(side = "left")

        self.net_child.pack(side = "right")
        self.net_child_rev.pack(side = "right")

        self.fifth_frame.pack()

        #Final Frame
        self.calculate_button = Button(self.bottom_frame, text = "Calculate Revenues", command = self.get_Adult_Gross)
        self.Total_Gross_Label = Label(self.bottom_frame, text = "Total Gross Rev: ")
        self.Total_gross_Rev = StringVar
        self.Total_net_rev = StringVar

        self.Total_Gross_Rev = Label(self.bottom_frame, textvariable = self.Total_gross_Rev, width = 10)

        self.Total_net_Label = Label(self.bottom_frame, text = "Total Net Rev: ")
        self.Total_Net_Rev = Label(self.bottom_frame, textvariable = self.Total_net_rev, width = 10)

        self.clear_button = Button(self.bottom_frame, text = "Clear",command = self.clear, width = 5)

        #Packing Final frame
        self.calculate_button.pack(side = "left")
        self.Total_Gross_Label.pack(side = "left")
        self.Total_Gross_Rev.pack(side = "left")
        self.Total_net_Label.pack(side = "left")
        self.Total_Net_Rev.pack(side = "left")
        self.clear_button.pack(side = "right")

        self.bottom_frame.pack()

        mainloop()



    #Functions
    def get_Adult_Gross(self):
        s1 = float(self.AdultEntry.get())
        s2 = float(self.NumAdultSoldEntry.get())
        gross = s1 * s2
        self.AdultRev.set(gross)


    def clear(self):
        self.AdultRev.set(' ')
        self.AdultNetRev.set(' ')
        self.child_gross.set(' ')
        self.child_net_rev.set(' ')
        self.Total_gross_Rev.set(' ')
        self.Total_net_rev.set(' ')

#COVER LIST WIDGITS

#TheaterWin = TheaterWindow()



class JoeAuto():
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title = ("Automotive Window")

        self.top_frame = Frame(self.main_window)
        self.middle_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)

        self.title = Label(self.top_frame, text = 'Joe\'s Automotive')

        self.check_var1 = IntVar()
        self.check_var2 = IntVar()
        self.check_var3 = IntVar()
        self.check_var4 = IntVar()
        self.check_var5 = IntVar()
        self.check_var6 = IntVar()
        self.check_var7 = IntVar()

        self.check_var1.set(0)
        self.check_var2.set(0)
        self.check_var3.set(0)
        self.check_var4.set(0)
        self.check_var5.set(0)
        self.check_var6.set(0)
        self.check_var7.set(0)

        self.cb1 = Checkbutton(self.middle_frame, text = 'Oil change -- $30.00', variable = self.check_var1)
        self.cb2 = Checkbutton(self.middle_frame, text = 'Lube Job -- $20.00', variable = self.check_var2)
        self.cb3 = Checkbutton(self.middle_frame, text ='Radiator flush -- $40.00', variable = self.check_var3)
        self.cb4 = Checkbutton(self.middle_frame, text = 'Transmission flush -- $100.00', variable = self.check_var4)
        self.cb5 = Checkbutton(self.middle_frame, text = 'Inspection -- $35.00', variable = self.check_var5)
        self.cb6 = Checkbutton(self.middle_frame, text = 'Muffler replacement -- $200.00', variable = self.check_var6)
        self.cb7 = Checkbutton(self.middle_frame, text = 'Tire rotation -- $20.00',variable = self.check_var7)


        self.totalButton = Button(self.bottom_frame, text = 'Total ', command = self.select_option)
        self.totalLabel = Label(self.bottom_frame, text = 'The Total is ')

        self.value = StringVar()
        self.messageLabel = Label(self.bottom_frame, textvariable = self.value)

        #Packing Top frame
        self.title.pack()


        #Packing Middle frame
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        #Packing the Bottom frame
        self.totalButton.pack(side = 'left')
        self.totalLabel.pack(side = 'left')

        self.messageLabel.pack(side = 'left')

        #Packing the frame and creating the main loop
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        mainloop()

    def select_option(self):
        total = 0
        if self.check_var1.get() == 1:
            total += 30.00
        if self.check_var2.get() == 1:
            total += 20.00
        if self.check_var3.get() == 1:
            total += 40.00
        if self.check_var4.get() == 1:
            total += 100.00
        if self.check_var5.get() == 1:
            total += 35.00
        if self.check_var6.get() == 1:
            total += 200.00
        if self.check_var7.get() == 1:
            total += 20.00

        self.value.set('$' + str(total))

gui_menu = JoeAuto()

