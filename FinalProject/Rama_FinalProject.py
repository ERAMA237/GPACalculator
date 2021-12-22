from tkinter import *
# from tkinter we are importing everything.
import math
# in order to use mathmetical functions we are importing math.

window = Tk()
window.title("Lets Calculate your Masters GPA!")
# we are setting our root to window to tk and our title for window.

lbl1 = Label(window,text="What was your first final percentage grade?")
# we are creating a new label which will ask the user for the first
# percentage grade.
lbl1.pack()
# we are centering our label on top of the first entry and below the first label.

e1 = Entry(window, textvariable = StringVar())
# we are promting the user for the first entry which will be a string variable.
e1.pack()
# we are centering or packing the first entry.


lbl2 = Label(window,text="What was your second final percentage grade?")
# we are creating a new label which will ask the user for the second
# percentage grade.
lbl2.pack()
# we are centering the label below the first entry.


e2 = Entry(window,textvariable = StringVar())
# we are promting the user for the second entry which will be a string variable.
e2.pack()
# we are packing or centering our second entry below our second label.


def retrieve_gpa():
    Answer = float((percent_grade(e1.get()) + percent_grade(e2.get()))/2)
    new_window = Toplevel(window)
    new_window.title("GPA is down below!")
    display_gpa = Label(new_window, text = "")
    display_gpa.configure(text = "Your GPA is " + str(Answer) + ".")
    display_gpa.pack()
    # here our code takes both floats percentage grade entries and divides them by two
    # to obtain our final gpa.
    # then we create a new window with our gpa converted to a string and
    # packing or centering the whole string in the new window.


def percent_grade(grades):
    # this function of our program converts grade to gpa points
    # we first set our variable through a if loop which is inside a while loop
    # we set the while loop to true and anything else will return nothing.
    while True:
        if float(grades) >= 93 and float(grades) <=110:
            return 4.0
        elif float(grades) >=90 and float(grades) <=93:
            return 3.7
        elif float(grades) >=87 and float(grades) <=90:
            return 3.3
        elif float(grades) >=83 and float(grades) <=87:
            return 3.0
        elif float(grades) >=80 and float(grades) <=83:
            return 2.7
        elif float(grades) >=77 and float(grades) <=80:
            return 2.3
        elif float(grades) >=73 and float(grades) <=77:
            return 2.0
        elif float(grades) >=70 and float(grades) <=73:
            return 1.7
        elif float(grades) >=67 and float(grades) <=70:
            return 1.3
        elif float(grades) >=65 and float(grades) <=67:
            return 1.0
        return 0.0
    return None

    
btn = Button(window, text ="Click here for your GPA!", command=retrieve_gpa)
# we are creating a new button within the window or root, which will state
# click here for your gpa, after the button is click it will refer the defined
# function retrieve gpa, which will accumulate our final gpa.
btn.pack()
# we are packing or centering our button.

window.mainloop()
# we are setting our root or window into a infinite loop. 


