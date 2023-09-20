from tkinter import *
import tkinter.messagebox
#A frame is a container that holds other widgit
'''class MyGUI:

    def __init__(self):
        self.main_window = Tk()
        self.main_window.title('My First GUI') #Name of window. These too will always be here
        

        self.top_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)

        self.label1 = Label(self.top_frame, text = 'Hello World', borderwidth = 1, relief = 'solid')
        self.label2 = Label(self.top_frame, text = 'Computer', borderwidth=1, relief='solid')
        self.label3 = Label(self.top_frame, text = 'BIOS', borderwidth=1, relief='solid')

        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        
#Use .pack() to display the labels
        self.label4 = Label(self.bottom_frame, text='Hello World', borderwidth=1, relief='solid')
        self.label5 = Label(self.bottom_frame, text='Computer', borderwidth=1, relief='solid')
        self.label6 = Label(self.bottom_frame, text='BIOS', borderwidth=1, relief='solid')

        self.label4.pack(side = 'left')
        self.label5.pack(side = 'left')
        self.label6.pack(side = 'left')


        self.top_frame.pack()
        self.bottom_frame.pack()

        mainloop()


my_gui = MyGUI()'''


'''
class MyGUI:

    def __init__(self):
        self.main_window = Tk()
        self.main_window.title('My Second GUI')

        self.my_button = Button(self.main_window, text = 'Click Me!', command = self.do_something)

        self.quit_button = Button(self.main_window, text = 'Quit', command = self.main_window.destroy)
#remember to pack or it will not be able to display
        self.my_button.pack()
        self.quit_button.pack()


        mainloop()


#callback function. Must import tkinkter.messagebox
    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking me.') #This second part is essentially a print statement


my_gui = MyGUI()
'''
'''
class MyGUI:

    def __init__(self):
        self.main_window = Tk()
        self.main_window.title('My Third GUI')

        self.frame1 = Frame(self.main_window)
        self.frame2 = Frame(self.main_window)
        self.frame3 = Frame(self.main_window)

        self.label1 = Label(self.frame1, text = 'Hello World',borderwidth = 2, relief = 'solid')

        self.label1.pack()
        self.frame1.pack()

        mainloop()


my_gui = MyGUI()
'''

#Getting input using entry widget
class MyGUI_THREE:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("My First GUI")

        self.top_frame = Frame(self.main_window)
        self.middle_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)

        self.prompt_label = Label(self.top_frame, text = 'Enter a distance in kilometers')
        self.kilo_entry = Entry(self.top_frame, width = 10)

        self.prompt_label.pack(side = 'left')
        self.kilo_entry.pack(side = 'left')

        self.value = StringVar()
        self.desc_label = Label(self.middle_frame, text = 'Converted to Miles : ')
        self.miles_label = Label(self.middle_frame, textvariable = self.value )

        self.desc_label.pack(side = 'left')
        self.miles_label.pack(side = 'left')

        self.convert_button = Button(self.bottom_frame, text = 'Convert', command = self.convert_kilos)
        self.clear_button = Button(self.bottom_frame, text = 'Clear', command = self.clear)

        self.convert_button.pack(side = 'left')
        self.clear_button.pack(side ='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        mainloop()

    def convert_kilos(self):
        kilo = float(self.kilo_entry.get())
        miles = kilo * 0.614
        self.value.set(miles)

    def clear(self):
        self.value.set("")


#gui = MyGUI_THREE()


class Average_GUI():
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("My fourth GUI")

        self.one_frame = Frame(self.main_window)
        self.two_frame = Frame(self.main_window)
        self.three_frame = Frame(self.main_window)
        self.four_frame = Frame(self.main_window)
        self.five_frame = Frame(self.main_window)

        self.prompt_label_one = Label(self.one_frame, text ='Enter a score in for test One')
        self.first_entry = Entry(self.one_frame, width = 10)

        self.prompt_label_two = Label(self.two_frame, text = 'Enter a score in for test Two')
        self.second_entry = Entry(self.two_frame, width = 10)

        self.prompt_label_three = Label(self.three_frame, text = 'Enter a score in for test Three')
        self.third_entry = Entry(self.three_frame, width = 10)


        self.value = StringVar()
        self.prompt_label_four = Label(self.four_frame, text = 'Average')
        self.average_label = Label(self.four_frame,  )


    def convert(self):
        s1 = float(self.first_entry.get())
        s2 = float(self.second_entry.get())
        s3 = float(self.third_entry.get())
        avg = (s1 + s2 + s3)/3
        self.value.set(avg)

class RadioButton:
    #Can only choose one out of all options
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("My First GUI")

        self.top_Frame = Frame(self.main_window)
        self.bottom_Frame = Frame(self.main_window)

        self.radio_var = IntVar()

        self.radio_var.set(1)

        self.rb1 = RadioButton(self.top_Frame, text = 'Option 1', variable = self.radio_var, value = 1)
        self.rb2 = RadioButton(self.top_Frame, text = 'Option 2', variable = self.radio_var, value = 2)
        self.rb3 = RadioButton(self.top_Frame, text = 'Option 3', variable = self.radio_var, value = 3)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.ok_button = Button(self.bottom_Frame, text = 'OK', comand = self.select_option)
        self.quit_button = Button(self.bottom_Frame, text = 'Quit', command = self.main_window.destroy)

        self.ok_button.pack()
        self.quit_button.pack()

        self.top_Frame.pack()
        self.bottom_Frame.pack()

        mainloop()

    def select_option(self):
        if self.radio_var.get() == 1:
            message = "Option One"
        elif self.radio_var.get() == 2:
            message = "Option Two"
        elif self.radio_var.get() == 3:
            message = "Option Three"

        tkinter.messagebox.showinfo('Selection',message)

radio_GUI = RadioButton()

