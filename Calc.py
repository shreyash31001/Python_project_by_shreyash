# We are now going to build a simple calculator app using tkinter
from tkinter import *
#f_num = 0
root = Tk()
root.title("A simple calculator") # title 
e = Entry(root,width=50,borderwidth=5)
# columnspan is used for determing how many columns will the number span or occupy.
e.grid(row=0,column=0,columnspan=3, padx=10, pady=10)
# define function
def button_click(number):
    #e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
def button_erase():
    e.delete(0,END)
def button_add():
    first_number = e.get()
    global f_num 
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0,END)
def button_equal_to():
    second_number = e.get()
    e.delete(0,END)
    if math == "addition":
          e.insert(0,f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0,f_num - int(second_number))
    elif math == "multiply":
        e.insert(0,f_num * int(second_number))
    elif math == "divison":
        e.insert(0,f_num / int(second_number))

def button_subtract():
    first_number = e.get()
    global f_num 
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num 
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0,END)
    
def button_divide():
    first_number = e.get()
    global f_num 
    global math
    math = "divison"
    f_num = int(first_number)
    e.delete(0,END)
    


    

# Define buttons

button_1 = Button(root,text="1",pady=40,padx=50,command=lambda:button_click(1))
button_2 = Button(root,text="2",pady=40,padx=50,command=lambda:button_click(2))
button_3 = Button(root,text="3",pady=40,padx=50,command=lambda:button_click(3))
button_4 = Button(root,text="4",pady=40,padx=50,command=lambda:button_click(4))
button_5 = Button(root,text="5",pady=40,padx=50,command=lambda:button_click(5))
button_6 = Button(root,text="6",pady=40,padx=50,command=lambda:button_click(6))
button_7 = Button(root,text="7",pady=40,padx=50,command=lambda:button_click(7))
button_8 = Button(root,text="8",pady=40,padx=50,command=lambda:button_click(8))
button_9 = Button(root,text="9",pady=40,padx=50,command=lambda:button_click(9))
button_0 = Button(root,text="0",pady=40,padx=50,command=lambda:button_click(0))
# Define buttons part 2
button_plus = Button(root, text="+",padx=50,pady=40,command=button_add)
# button_equal_to is the main command where the real operations are performed 
# when the equal to sign is clicked upon. The operation is performed , when
# the value of math is compared or matches the conditions given in the if-else statements
button_equal = Button(root, text="=",pady=40,padx=50,command=button_equal_to) 
button_clear = Button(root, text="Clear",pady=40,padx=99,command=button_erase)

button_minus = Button(root, text="-",padx=50,pady=40,command=button_subtract)
button_mult = Button(root, text="*",padx=50,pady=40,command=button_multiply)
button_div = Button(root, text="/",padx=50,pady=40,command=button_divide)


# Positioning the buttons

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4, column=0)

# Positioning the buttons part 2
button_plus.grid(row=4,column=1,columnspan=1)
button_equal.grid(row=4,column=2,columnspan=1)
button_clear.grid(row=5,column=0,columnspan=2)

button_minus.grid(row=6,column=0)
button_mult.grid(row=6,column=1)
button_div.grid(row=6,column=2)

root.mainloop()