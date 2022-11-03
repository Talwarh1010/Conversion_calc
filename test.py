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
                    "mm" :0.1,
                    "cm" :1,
                    "dm" :  10,
                    "ft" : 30.48,
                    "m" : 100,
                    "km" :  100000
                    }
        weight1 = {
                    "kg" :  1000,
                    "g" : 1,
                    "mg" :0.001,
                    }
        time1 = {
                    "hrs" : 3600,
                    "s" : 1,
                    }
        volume1 = {
                    "l": 1000,
                    "ml" : 1
                    }
        # combined dictionary
        combined_unit = distance1  | weight1  | time1  |  volume1
    
        # what unit it is in, and converts it into the common unit
        valid1 = False
        while not valid1:
            unit = input("what unit is it in?   ").lower()
            if unit in combined_unit:
                converter = number * combined_unit[unit]
                break
            else:
                print("please use a valid unit to convert from")
        # what unit the user wants to convert to is converted using dictionaries. Also checks if user does not try to convert between conversion types
        valid1 = False
        while not valid1:
            if unit in distance1:
                new_unit = input("what unit do you want to convert this to?  e.g. cm, km, mm, dm, etc   ").lower()
                if  unit in distance1 and new_unit in distance1:
                    final = converter / distance1[new_unit]
                    break
            
            if unit in weight1:
                new_unit = input("what unit do you want to convert this to?  e.g. g, mg, kg etc   ").lower()
                if   unit in weight1 and new_unit in weight1:
                        final =  converter / weight1[new_unit]
                        break
                    
            if unit in time1:
                new_unit = input("what unit do you want to convert this to?  e.g s or hrs   ").lower()
                if   unit in time1 and new_unit in time1:
                        final =  converter / time1[new_unit]
                        break
            
            if unit in volume1:
                    new_unit = input("what unit do you want to convert this to?  e.g ml or l  ").lower()
                    if   unit in volume1 and new_unit in volume1:
                        final =  converter / volume1[new_unit]
                        break
            else :
                    print("please imput a valid unit to convert to")
        
        # prints results
        print("{}{} is {:.3f}{}".format(number,unit,final,new_unit))
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















































































































