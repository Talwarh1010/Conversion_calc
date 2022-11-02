# checks if integer is more than a certain value and makes sure there isn't any letters in the number
def num_check(question, low,):
    
    
    valid = False
    while not valid:
        
        problem2 = "Please enter a number that is more than 0"
        problem = "Please enter a number that does not have  letters"
        
        try:
        
            # Ask user to enter a number
            response = float(input(question))

            # Checks number is more than zero
            if response > low :
                return response

            # Outputs error if input is invalid
            else:
                print(problem2)
                print()
                
        except ValueError:
            print(problem)
# informs the user about how to use the calculator 
def instructions():
    statement_generator("Instructions / information" , "=")
    print()
    print("Please choose an integer and what unit it is in. When entering the unit, make sure it is the symbol E.g m for meters")
    print()
    print("Choose what unit you want to convert this in. Make sure it is an appropiate conversion e.g. not seconds into metres or grams into cm")
    print()
    print("This calculator will convert between distance,time and weight")
    print()
    print("The units allowed are inches, milimeters, centimeters, decimeters, feet and meters")
    print()
    print("Kilograms, grams, miligrams, litres, and millitres")
    print()
    print("Hours and seconds")
    print()
    print("complete as many calculations as necessary. press <enter> at the end of each calculations or press any key then enter to quit.")
    print()
    return ""

# makes the heading and ending more pleasing to view
def statement_generator(text, decoration):
    
    # Make string with five characters
    ends = decoration * 5
    
    # add decoration to start and end of statement
    statement = "{} {} {}". format(ends, text, ends)
    
    print()
    print(statement)
    print()
    
    
    return ""
# converts between time, distances and time
def conversion_calculator(number):
        print()      
        print()
        # dictionary
        distance1 = {
                    "in": 2.54,
                    "mm" :10,
                    "cm" :1,
                    "dm" :  10,
                    "ft" : 30.48,
                    "m" : 100,
                    "km" :  100000
                    }
        weight1 = {
                    "kg" :  1000,
                    "g" : 1,
                    "mg" :1000,
                    
                    }
        time1 = {
                    "hrs" : 3600,
                    "s" : 1,
                    }
        volume1 = {
                    "l": 1000,
                    "ml" : 1
                    }
        # list of valid units
        distance_list = ["km", "m", "dm" "ft", "in", "mm", "cm"]
        weight_list = ["kg", "g", "mg"]
        time_list = ["hrs", "s"]
        volume_list = ["l", "ml"]
            
        # what unit it is in, and converts it into the common unit
        valid1 = False
        while not valid1:
            unit = input("what unit is it in?   ").lower()
            if unit in distance_list:
                converter = number * distance1[unit]
                break
            elif  unit in weight_list:
                converter = number *  weight1[unit]
                
                break
            elif  unit in time_list:
                converter = number * time1[unit]
                break
            elif   unit in volume_list:
                converter = number * volume1[unit]
                break
            
            else :
                print()
                print("please input a valid unit to convert from")
                print()
                
        # what they want to convert to and converts to the result and checks if user inputs a valid unit
        valid1 = False
        while not valid1:
            print()
            new_unit = input("what unit do you want to convert this to?  e.g. cm, l, g, hrs etc   ").lower()
            if  unit in distance_list and new_unit in distance_list:
                final = converter / distance1[new_unit]
                break
            elif   unit in weight_list and new_unit in weight_list:
                final =  converter / weight1[new_unit]
                break
            elif  unit in time_list and new_unit in time_list:
                final =  converter / time1[new_unit]
                break
            elif   unit in volume_list and new_unit in volume_list:
                final =  converter / volume1[new_unit]
                break
            else :
                    print("please imput a valid unit to convert to")
                    
        print("{}{} is {:.2f}{}".format(number,unit,final,new_unit))
# main routine
statement_generator("WELCOME TO CONVERSION CALCULATOR", "🌟" )
first_time = input("Press <enter> to see instructions or press any key then enter to continue ")

# asks the user if it is their first time using the program and if they need the instructions displayed
if first_time =="":
    instructions()

    # puts the code into a loop
keep_going = ""
while keep_going =="":
    number = (conversion_calculator(num_check("what is the number? ", low = 0)))
    keep_going = input("press enter to continue or press any key then enter to quit")
    print()

statement_generator("Thanks for using Conversion calculator", "💝")















































































































