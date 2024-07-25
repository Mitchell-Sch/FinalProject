"""

Author:  Mitchell Schindler
Date written: 07/19/24
Assignment:   Module 06 Programming Assignment Part I
Short Desc:   A GUI program that converts between fahrenheit and celsius.


"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
bgColor = "#ADD8E6"
fList = []
cList = []

class Temperature(EasyFrame):
    def __init__(self):
        #Initializes variables used for conversion of temperatures
        self.F = 0
        self.convertedTemp = ""
        self.C = 0
        
        #Starts the window
        EasyFrame.__init__(self)
        self.setBackground(bgColor)

        #Labels and temperature input:
        #Creates the main title label
        self.titleLabel = self.addLabel(text = "Temperature Calculator",
                                        font = ("TkMenuFont", 25),
                                        row = 1, column = 0,
                                        columnspan = 2,
                                        sticky = "NSEW",
                                        background = bgColor)

        #Label prompting the user to enter a temperature
        self.tempLabel = self.addLabel(text = "Enter a tempurature:",
                                       row = 2, column = 0,
                                       sticky = "NSEW",
                                       background = bgColor)

        #Input that takes a temperature from the user
        self.tempInput = self.addTextField(text = "",
                                           row = 2, column = 1,
                                           sticky = "NSEW")

        #Label that displays the converted temperature
        self.tempLabel = self.addLabel(text = "Converted tempurature: " + str(self.convertedTemp),
                                       row = 4, column = 0,
                                       columnspan = 2,
                                       sticky = "NSEW",
                                       background = bgColor)
        
        #Label that alerts the user if they entered an invalid number
        self.errorLabel = self.addLabel(text = "Error: value entered wasn't a valid number. Please enter a valid number.\n Examples: \"0\", \"3.1415\", \"-7\"",
                                        row = 6, column = 0,
                                        columnspan = 2,
                                        sticky = "NSEW",
                                        background = bgColor,
                                        foreground = bgColor)
        
        #Adds the image widget to the main screen
        self.tempImageLabel = self.addLabel(text = "",
                                            row = 0, column = 0,
                                            columnspan = 2,
                                            sticky = "NSEW",
                                            background = bgColor)
        fileName1 = "Temperature.png"
        self.image1 = PhotoImage(file = fileName1)
        self.image1 = self.image1.subsample(2) #Makes the image smaller
        self.tempImageLabel["image"] = self.image1


        #Buttons:
        #Converts entered temperature to Celsius
        self.FtoCButton = self.addButton(text = "Convert to Celsius",
                                         row = 3, column = 0,
                                         command = self.FtoC)
                                        
        #Converts entered temperature to Fahrenheit
        self.CtoFButton = self.addButton(text = "Convert to Fahrenheit",
                                         row = 3, column = 1,
                                         command = self.CtoF)

        #Adds the converted temperature to a list, in both fahrenheit and celsius
        self.addTempButton = self.addButton(text = "Add temperature to list",
                                            row = 5, column = 0,
                                            command = self.addTemp,
                                            state = "disabled")

        #Exits the program
        self.exitButton = self.addButton(text = "Exit",
                                            row = 7, column = 0,
                                            command = self.exitProgram)

        #Opens the window to view statistics about the temperatures
        self.window2Button = self.addButton(text = "See Statistics",
                                            row = 5, column = 1,
                                            command = self.window2,
                                            state = "disabled")


    #Functions for the buttons:
    #Converts from fahrenheit to celsius
    def FtoC(self):
        try:
            self.errorLabel["foreground"] = bgColor
            self.addTempButton["state"] = "normal"
            self.F = float(self.tempInput.getText() )
            self.C = 5/9 * (self.F - 32)
            self.convertedTemp = self.C
            self.tempLabel["text"] = ("Converted tempurature: " + str(self.convertedTemp) + "°")
        except ValueError:
            self.errorLabel["foreground"] = "white"
            

    #Converts from celsius to fahrenheit
    def CtoF(self):
        try:
            self.addTempButton["state"] = "normal"
            self.C = float(self.tempInput.getText())
            self.F = 9/5 * self.C + 32
            self.convertedTemp = self.F
            self.tempLabel["text"] = ("Converted tempurature: " + str(self.convertedTemp) + "°")
        except ValueError:
            self.errorLabel["foreground"] = "white"

    #Exits the program        
    def exitProgram(self):
        self.master.destroy()

    #Adds the temperature to a list
    def addTemp(self):
        self.window2Button["state"] = "normal"
        fList.append(round(self.F, 4) )
        cList.append(round(self.C, 4) )




    #Creates the statistics window
    def window2(self):
        #Initializing variables for later calculations
        fTotal = 0
        cTotal = 0
        fAvg = 0
        cAvg = 0
        fMode = 0
        cMode = 0
        tempoFList = []
        tempoCList = []
        
        #Initializing the window
        root = tk.Toplevel()
        root.title("Temperature Calculator")
        root.configure(background = bgColor)
        
        #Creates the image in the window
        tempImageFile = PhotoImage(file = "Calculator.png")
        imageFile = tempImageFile.subsample(3, 3)
        photoLabel = tk.Label(root,
                                  text = "",
                                  image = imageFile,
                                  bg = bgColor)
        photoLabel.configure(image = imageFile)
        photoLabel.grid(row = 0, column = 1)
        
        #Creates the title label for the window
        titleLabel = tk.Label(root,
                              text = "Statistics\nWindow",
                              bg = bgColor,
                              fg = "white",
                              font = ("TkMenuFont", 25) ).grid(row = 1, column = 1)

        #Creates the list of all temperatures entered, displayed in celsius
        celsiusLabel = tk.Label(root,
                                text = ("Celsius:\n"),
                                bg = bgColor,
                                fg = "white",
                                font = ("TkMenuFont", 13) )
        for temp in range(len(cList) ):
            celsiusLabel["text"] = (celsiusLabel["text"] + str(cList[temp]) + "\n")
            tempoCList.append(cList[temp])
            cTotal += cList[temp]
        cAvg = cTotal / len(cList)
        celsiusLabel.grid(row = 2, column = 0)
        
        #Creates the list of all temperatures entered, displayed in fahrenheit
        fahrenheitLabel = tk.Label(root,
                                   text = "Fahrenheit:\n",
                                   bg = bgColor,
                                   fg = "white",
                                   font = ("TkMenuFont", 13) )
        for temp in range(len(fList) ):
            fahrenheitLabel["text"] = (fahrenheitLabel["text"] + str(fList[temp]) + "\n")
            tempoFList.append(fList[temp])
            fTotal += fList[temp]
        fAvg = fTotal / len(fList)
        fahrenheitLabel.grid(row = 2, column = 2)

        #Shows the average temperature of the ones entered, showed in fahrenheit and celsius
        avgLabel = tk.Label(root,
                            text = "Average temperature:\n" + str(round(fAvg, 4) ) + "° Fahrenheit\n" + \
                            str(round(cAvg, 4) ) + "° Celsius\n",
                            bg = bgColor,
                            fg = "white",
                            font = ("TkMenuFont", 13) ).grid(row = 3, column = 1)

        #Computes the mode in fahrenheit
        if len(tempoFList) == 1:
            fMode = tempoFList[0]
            
        elif len(tempoFList) == 2:
            fMode = (tempoFList[0] + tempoFList[1] ) / 2
            
        else:
            if len(tempoFList) % 2 == 0:
                while len(tempoFList) > 2:
                    tempoFList.pop(0)
                    tempoFList.pop(-1)
                    fMode = (tempoFList[0] + tempoFList[1] ) / 2
                    
            else:
                while len(tempoFList) > 1:
                    tempoFList.pop(0)
                    tempoFList.pop(-1)
                    fMode = tempoFList[0]
                    
        #Computes the mode in celsius     
        cMode = 5/9 * (fMode - 32)

        #Displays the mode in fahrenheit and celsius
        modeLabel = tk.Label(root,
                             text = "Mode temperature:\n" + str(round(fMode, 4) ) + \
                             "° Fahrenheit\n" + str(round(cMode, 4) ) + "° Celsius\n",
                             bg = bgColor,
                             fg = "white",
                             font = ("TkMenuFont", 13) ).grid(row = 4, column = 1)
        

        #Start 2nd window
        root.mainloop()

#Main loop
if __name__ == "__main__":
    Temperature().mainloop()
