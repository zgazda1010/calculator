"""
CALCULATOR BASED ON:
https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/
"""
# Python program to create a simple GUI
# calculator using Tkinter

# import specific tkinter modules
from tkinter import Button, Entry, font as tkFont, StringVar, Tk
from calculator_modules.square import square
from calculator_modules.power import power
from calculator_modules.square_root import square_root

# globally declare the expression variable
expression = ""

BACKGROUND_RESOLUTION = "825x390"
OUTPUT_WINDOW_WIDTH = 135
OUTPUT_WINDOW_HEIGHT = 10
BUTTON_HEIGHT = 4
BUTTON_WIDTH = 28
FONT_SIZE = 9
FONT_FAMILY = 'Helvetica'


# Function to update expression
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    # validate input
    if validate_expression(num):

        # concatenation of string
        expression = expression + str(num)

        # update the expression by using set method
        equation.set(expression)


def validate_expression(new_input):
    global expression
    # Check for multiple decimal points in a number
    # if new_input == '.' and expression and '.' in expression.split()[-1]:
        # return False
    return True


# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))

        equation.set(total)

        # initialize the expression variable
        # by empty string
        # commented out, so we can make further operations on the result
        # expression = ""
        expression = total

    # if error is generate then handle
    # by the except block
    except ValueError:

        equation.set(" error ")
        expression = ""


# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")


def power_pressed():
    global expression
    expression = power(expression)
    equation.set(expression)


def square_pressed():
    global expression
    expression = square(expression)
    equation.set(expression)


def square_root_pressed():
    global expression
    expression = square_root(expression)
    equation.set(expression)


# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="black")

    # set the title of GUI window
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry(BACKGROUND_RESOLUTION)

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # declare bold Helvetica fonts
    helvetica = tkFont.Font(family=FONT_FAMILY, size=FONT_SIZE, weight=tkFont.BOLD)

    # create the text entry box for
    # showing the expression.
    expression_field = Entry(gui, textvariable=equation, font=helvetica)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    expression_field.grid(columnspan=80, ipadx=OUTPUT_WINDOW_WIDTH, ipady=OUTPUT_WINDOW_HEIGHT)

    # create a Buttons and place at a particular
    # location inside the root window.
    # when user press the button, the command or
    # function affiliated to that button is executed.

    # BUTTONS 1st ROW
    button1 = Button(gui, text=' 1 ', font=helvetica, fg='black', bg='deepskyblue1',
                     command=lambda: press(1), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', font=helvetica, fg='black', bg='deepskyblue1',
                     command=lambda: press(2), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', font=helvetica, fg='black', bg='deepskyblue1',
                     command=lambda: press(3), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    button3.grid(row=2, column=2)

    plus = Button(gui, text=' + ', font=helvetica, fg='black', bg='darkorange',
                  command=lambda: press("+"), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    plus.grid(row=2, column=3)

    # BUTTONS 2nd ROW
    button4 = Button(gui, text=' 4 ', font=helvetica, fg='black', bg='deepskyblue1',
                     command=lambda: press(4), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', font=helvetica, fg='black', bg='deepskyblue1',
                     command=lambda: press(5), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', font=helvetica, fg='black', bg='deepskyblue1',
                     command=lambda: press(6), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    button6.grid(row=3, column=2)

    minus = Button(gui, text=' - ', font=helvetica, fg='black', bg='darkorange',
                   command=lambda: press("-"), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    minus.grid(row=3, column=3)

    # BUTTONS 3rd ROW
    button7 = Button(gui, text=' 7 ', font=helvetica, fg='black', bg='deepskyblue1',
                     command=lambda: press(7), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', font=helvetica, fg='black', bg='deepskyblue1',
                     command=lambda: press(8), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', font=helvetica, fg='black', bg='deepskyblue1',
                     command=lambda: press(9), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    button9.grid(row=4, column=2)

    multiply = Button(gui, text=' * ', font=helvetica, fg='black', bg='darkorange',
                      command=lambda: press("*"), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    multiply.grid(row=4, column=3)

    # BUTTONS 4th ROW
    Decimal = Button(gui, text='.', font=helvetica, fg='black', bg='darkorange',
                     command=lambda: press('.'), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    Decimal.grid(row=5, column=0)

    button0 = Button(gui, text=' 0 ', font=helvetica, fg='black', bg='deepskyblue1',
                     command=lambda: press(0), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    button0.grid(row=5, column=1)

    equal = Button(gui, text=' = ', font=helvetica, fg='black', bg='chartreuse1',
                   command=equalpress, height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    equal.grid(row=5, column=2)

    divide = Button(gui, text=' / ', font=helvetica, fg='black', bg='darkorange',
                    command=lambda: press("/"), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    divide.grid(row=5, column=3)

    # BUTTONS 5th ROW
    clear = Button(gui, text='Clear', font=helvetica, fg='black', bg='red',
                   command=clear, height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    clear.grid(row=6, column=0)

    square_button = Button(gui, text=' x^2 ', font=helvetica, fg='black', bg='darkorange',
                           command=square_pressed,
                           height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    square_button.grid(row=6, column=1)

    power_button = Button(gui, text=' x^y ', font=helvetica, fg='black', bg='darkorange',
                          command=power_pressed, height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    power_button.grid(row=6, column=2)

    sqrt_button = Button(gui, text=' √x ', font=helvetica, fg='black', bg='darkorange',
                         command=square_root_pressed,
                         height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    sqrt_button.grid(row=6, column=3)

    # start the GUI
    gui.mainloop()
