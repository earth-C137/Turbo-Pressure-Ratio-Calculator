#!/usr/bin/env python3
import tkinter as tk

#This function builds the tkinter window.
def tk_window():
    #This is a variable that stores the desired font style for easy re-use.
    font_style = ('Times', 18)
    window = tk.Tk()
    window.minsize(200,200)
    window.title('Turbo pressure ratio calculator')
    input_label = tk.Label(window, font=font_style,
                           text='What is your turbo pressure gauge reading '
                           'in PSI?')
    input_label.grid(row=0, column=0)
    pressure_input = tk.Entry(window, font=font_style, justify='center')
    pressure_input.grid(row = 2, column = 0)
    input_label2 = tk.Label(window, font=font_style, text='What is your '
                            'elevation in feet?')
    input_label2.grid(row=3)
    elevation_input = tk.Entry(window,font=font_style, justify='center')
    elevation_input.grid(row=4)
    output_label = tk.Label(window, text='', font=font_style)
    output_label.grid(row=6)
    #This function is inside tk_window fuction
    #and houses the button click logic.
    def button_click():
        #These are variables that hold the inputs.
        pressure = pressure_input.get()
        elevation = elevation_input.get()
        #This is to handle error and logic.
        try:
            if float(pressure) >= 0 and float(elevation) >= -500:
                #This variable calls the function that calculates
                #pressure ratio and stores the value.
                pressure_ratio = turbo_pr_calculator(float(pressure),
                                                     int(elevation))
                output_label.config(text='Your current pressure ratio is: '
                                    + str(pressure_ratio))
            else:
                output_label.config(text='Please enter the turbo pressure as '
                                    'a number greater than zero and '
                                    'elevation greater than -500.')
        except Exception as e:
            output_label.config(text='Please make sure turbo pressure and '
                                'elevation are entered as numbers!!')
    #This adds the button and uses the button_click function.
    button = tk.Button(window, text='Click Me!!',font=font_style,
                       command=button_click)
    button.grid(row=5, column=0)
    window.mainloop()

#This function calculates the turbo pressure ratio and returns the value.
#The function takes two arguments: gauge pressure and elevation.
def turbo_pr_calculator(gPressure, elevation):
    #Air pressure above sea level can be calculated as:
    #p = 101325 (1 + -2.209E-5 * h)**5.25588
    #Where:
    #-2.209E-5 is
    #(-.0065 degrees K/meter divided by standard temp sea level kelvin)
    #p = air pressure (Pa)
    #h = altitude above sea level (M)
    # 1 pascal = .0001450 psi
    # 1 foot = .3048 meters
    atmosphericPressure = ((101325 * .0001450)
                           * (1 - .00002209 * (elevation * .3048)) ** 5.25588)
    pRatio = (gPressure + atmosphericPressure)/atmosphericPressure
    return round(pRatio, 1)
if __name__ == '__main__':
    tk_window()
