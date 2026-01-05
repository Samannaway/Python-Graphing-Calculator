from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry("300x300")
root.title("Graphing Calculator")


# configuring rows and columns
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)




columnFlag = 0
input_string = "" # used globally for orthogonal persistence
display_var = StringVar(value="") # The 'State' linked to the UI so that we don't have a orthogonal persistence error


finalVariableList = [] # final list to be imported




#button recognition function
def whichButton(input):


    global input_string


    print(type(input))
    input_string+=input
    display_var.set(input_string)
    print(f"Current String: {input_string}")
buttonFlag = 0




# final function for making the list of powers and the coefficients associated with them
def endButton():


    print(input_string)
    variableList = input_string.split(" ")
    print(variableList)


    for i in variableList:
        newStr = i.replace("x", "").split("^")
        print(newStr)
        finalVariableList.append(newStr)


#configuring the UI buttons which will be displayed on tkinter
for i in range(10):
    button = Button(text=f"{i}", height=2, width=5, command=lambda i=i: whichButton(str(i)))
    button.grid(column=columnFlag, row=int(i/3)+3, padx=5, pady=5)


    print(columnFlag)
   
    if columnFlag < 2:
        columnFlag+=1
    else:
        columnFlag = 0
   
# mappin other functional buttons
variableButton = Button(text="VAR", height=2, width=10, command=lambda i=i: whichButton("x"))
variableButton.grid(column=1, row=6, padx=5, pady=5)


powerButton = Button(text="POW", height=2, width=10, command=lambda i=i: whichButton("^"))
powerButton.grid(column=2, row=6, padx=5, pady=5)


plusButton = Button(text="+", height=2, width=5, command=lambda i=i: whichButton(" +"))
plusButton.grid(column=5, row=5, padx=5, pady=5)


minusButton = Button(text="-", height=2, width=5, command=lambda i=i: whichButton(" -"))
minusButton.grid(column=5, row=4, padx=5, pady=5)




ansButton = Button(text="ANS", height=2, width=5, command=lambda i=i: endButton())
ansButton.grid(column=3, row=6, padx=5, pady=5)


root.mainloop()




class interFaceOutput():
    def finalListReturn():
        return finalVariableList