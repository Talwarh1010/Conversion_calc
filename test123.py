


from logging import error
# checks if integer is more than a certain value and makes sure there isn't any letters in the number
def num_check(question, low,):
    
    valid = False
    while not valid:
        
        problem2 = "Please enter a number that is more than 0"
        problem = "Please enter a number that does not have decimals or letters"
        
        try:
        
            # Ask user to enter a number
            response = float(input(question))

            # Checks number is more than zero
            if response >= low :
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
    print("Please choose an integer and what unit it is in. When entering the unit, make sure it is the symbol")
    print()
    print("Choose what unit you want to convert this in. Make sure it is an appropiate conversion e.g. not seconds into metres or grams into cm")
    print()
    print("This calculator will convert between distance,time and weight")
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
        unit = input("what unit is it in?   ")
        my_dict = {
            "in":number * 2.54,
            "mm":number/10,
            "cm":number/1,
            "dm": number * 10,
            "ft":number * 30.48,
            "kg": number * 1000,
            "g": number/1,
            "mg":number/1000,
            "hrs": number * 3600,
            "s": number/1,
            "m": number * 100,
            "l": number * 1000,
            "ml": number/1
            }
        (float(converter)) = (unit)[my_dict]
            
        new_dict = {
            "in":float(converter) / 2.54,
            "mm":converter * 10,
            "cm":float(converter)/1,
            "dm":float(converter)/ 10,
            "ft":float(converter) / 30.48,
            "kg": float(converter) / 1000,
            "g": float(converter)/1,
            "mg":float(converter) * 1000,
            "hrs": float(converter)/ 3600,
            "s": float(converter)/1,
            "m": float(converter) / 100,
            "l": float(converter)/ 1000,
            "ml": float(converter)/1
            }
                
                
            
            
        
        new_unit = input("what unit do you want to convert this to, e.g. cm, L, g, hrs etc")
        final = new_unit[new_dict]
                
        if final == "cm":
                print("{}{} is {}{}").format(number),(unit),(final), (new_unit)
                
                    
        if final == "mm":
                
                print("{}{} is {}{}").format(number),(unit),(final), (new_unit)
            
        if final == "dm":
                
                print("{}{} is {}{}").format(number),(unit),(final), (new_unit)
                
        if final == "ft":
                print("{}{} is {}{}").format(number),(unit),(final), (new_unit)
                
        if final == "g":
                
                print("{}{} is {}{}").format(number),(unit),(final), (new_unit)
        if final == "kg":
            
                print("{}{} is {}{}").format(number),(unit),(final), (new_unit)
        if final == "mg":
                
                print("{}{} is {}{}").format(number),(unit),(final), (new_unit)
                
        if final == "hrs":
                
                print("{}{} is {}{}").format(number),(unit),(final), (new_unit)
        if final == "s":
                
                print("{}{} is {}{}").format(number),(unit),(final), (new_unit)
        if final == "m":
                
                print("{}{} is {}{}").format(number),(unit),(final), (new_unit)
        if final== "l":
                
                print("{}{} is {}{}").format(number),(unit),(final), (new_unit)
                
        if final == "ml":
                
                print("{}{} is {}{}").format(number),(unit),(final), (new_unit)


# main routine
statement_generator("WELCOME TO CONVERSION CALCULATOR", "🌟" )
first_time = input("Press <enter> to see instructions or press any key then enter to continue ")


# asks the user if it is their first time using the program and if they need the instructions displayed
if first_time =="":
    instructions()
    # puts the code into a loop
keep_going = ""
while keep_going =="":
    number = (conversion_calculator(num_check("what is the number? ", low = 1)))
    keep_going = input("press enter to continue or press any key then enter to quit")
    print()

statement_generator("Thanks for using Conversion calculator", "💝")


















































































































