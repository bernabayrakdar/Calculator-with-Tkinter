from tkinter import * #import all in tkinter

window = Tk() #create tkinter object
window.geometry("280x280") # size of window

elements = [] #list of entered numbers
operation = [] #list of operations

def get_Entry(number):
    entry = calc.get() + number
    calc.delete(0, END) #from the beginning to the end delete all
    calc.insert(0, entry) #from the beginning to the end insert entry

def Calculate(string):
    entry = calc.get() #get entry
    operation.append(string) #add what you want to do(+, -, *, /)operation list

    if len(elements) == 0 : #if you entered first number
        elements.append(int(entry))
        calc.delete(0, END)

    if(string == "="): #if you give numbers and want to see the result

            if (operation[0] == "+"):
                calc.delete(0, END)
                elements.append(elements[0] + int(entry))
                elements.pop(0)
                calc.insert(0,elements)
                operation.clear()

            elif (operation[0] == "-"):
                calc.delete(0, END)
                elements.append(elements[0] - int(entry))
                elements.pop(0)
                calc.insert(0,elements)
                operation.clear()

            elif (operation[0] == "*"):
                calc.delete(0, END)
                elements.append(elements[0] * int(entry))
                elements.pop(0)
                calc.insert(0, elements)
                operation.clear()

            elif (operation[0] == "/"):
                calc.delete(0, END)
                elements.append(elements[0] / int(entry))
                elements.pop(0)
                calc.insert(0, elements)
                operation.clear()

    else:
        calc.delete(0,END)

def delete():
    calc.delete(0, END)
    operation.clear()
    elements.clear()

calc = Entry(window, width="30") #the part of enter numbers
calc.insert(0,"") #first element is empty
calc.grid(row=0, columnspan=4, padx=50,pady=10) #create 4 columns at row 0

#creating all buttons

B1 = Button(text="1",width=5,height=3, command = lambda: get_Entry(str(1)))
B1.grid(row=1, column=0)
B2 = Button(text="2", width=5,height=3, command = lambda: get_Entry(str(2)))
B2.grid(row=1, column=1)
B3 = Button(text="3", width=5,height=3, command = lambda: get_Entry(str(3)))
B3.grid(row=1, column=2)
add_button = Button(text = "+", width=5,height=3, command = lambda: Calculate(str("+")))
add_button.grid(row=1, column=3)

B4 = Button(text="4", width=5,height=3, command = lambda: get_Entry(str(4)))
B4.grid(row=2, column=0)
B5 = Button(text="5", width=5,height=3, command = lambda: get_Entry(str(5)))
B5.grid(row=2, column=1)
B6 = Button(text="6", width=5,height=3, command = lambda: get_Entry(str(6)))
B6.grid(row=2, column=2)
ext_button = Button(text = "-", width=5,height=3, command = lambda: Calculate(str("-")))
ext_button.grid(row=2, column=3)

B7 = Button(text="7", width=5,height=3, command = lambda: get_Entry(str(7)))
B7.grid(row=3, column=0)
B8 = Button(text="8", width=5,height=3, command = lambda: get_Entry(str(8)))
B8.grid(row=3, column=1)
B9 = Button(text="9", width=5,height=3, command = lambda: get_Entry(str(9)))
B9.grid(row=3, column=2)
multiplication_button = Button(text = "*", width=5,height=3, command = lambda: Calculate(str("*")))
multiplication_button.grid(row=3, column=3)

ac_button = Button(text = "AC", width=5,height=3, command = delete)
ac_button.grid(row=4, column=0)
B0 = Button(text="0", width=5,height=3, command = lambda: get_Entry(str(0)))
B0.grid(row=4, column=1)
equal_button = Button(text = "=", width=5,height=3, command =lambda: Calculate(str("=")))
equal_button.grid(row=4,column=2)
division_button = Button(text = "/", width=5,height=3, command = lambda: Calculate(str("/")))
division_button.grid(row=4, column=3)

window.mainloop() #this made window appear in screen