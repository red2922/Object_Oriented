#Write a recursive function that takes a list of numbers as an input and returns the product of all the numbers in the list.

#Sample Input: [2,3,4,5]

#Output: 120

#def product(list = []):
 #   if len(list) == 0:
  #      return 1
   # else:
    #    return list.pop() * product(list)

#print(product([2,3,4,5]))
import datetime
from tkinter import *

# now() to get current date
current_time = datetime.datetime.now()

# To get current year
current_time.year
# To get current day
current_time.day
# To get current month
current_time.month

class YearCalculator():
    def __init__(self):

        self.main_window = Tk()
        self.main_window.title = "Main Window"

        self.firstFrame = Frame(self.main_window)
        self.secondFrame = Frame(self.main_window)
        self.thirdFrame = Frame(self.main_window)
        self.fourthFrame = Frame(self.main_window)
        self.lastFrame = Frame(self.main_window)


        self.NameLabel = Label(self.firstFrame, text = 'Name')
        self.NameEntry = Entry(self.firstFrame,width = 10)

        self.YearLabel = Label(self.secondFrame, text = 'Year')
        self.YearEntry = Entry(self.secondFrame, width = 10)

        self.MonthLabel = Label(self.thirdFrame, text = 'Month')
        self.MonthEntry = Entry(self.thirdFrame, width = 10)

        self.DayLabel = Label(self.fourthFrame, text = 'Day')
        self.DayEntry = Entry(self.fourthFrame, width = 10)

        self.age = StringVar()
        self.CalculateButton = Button(self.lastFrame,text = 'CalculateAge', command = self.findAge)
        self.stringLabel = Label(self.lastFrame, textvariable = self.age)


        self.NameLabel.pack(side = LEFT)
        self.NameEntry.pack(side = RIGHT)

        self.YearLabel.pack(side = LEFT)
        self.YearEntry.pack(side = RIGHT)

        self.MonthLabel.pack(side = LEFT)
        self.MonthEntry.pack(side = RIGHT)

        self.DayLabel.pack(side = LEFT)
        self.DayEntry.pack(side = RIGHT)

        self.CalculateButton.pack()
        self.stringLabel.pack()

        self.firstFrame.pack()
        self.secondFrame.pack()
        self.thirdFrame.pack()
        self.fourthFrame.pack()
        self.lastFrame.pack()


        mainloop()

    def findAge(self):
        year = int(current_time.year) - int(self.YearEntry.get())
        self.age.set(str(self.NameEntry.get()) + ' your age is ' + str(year))

year = YearCalculator()