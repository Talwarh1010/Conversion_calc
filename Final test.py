



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
        # ask what converting between
        metric = input("What are you converting e.g. distance, time or weight? ")
        # what unit it is in
        unit = (input("what unit is it in?   "))
        # what they want to convert to
        new_unit = input("what unit do you want to convert this to?  e.g. cm, l, g, hrs etc   ")
        
        # python dictionary that converts input into a common metric unit depending on the unit they enter. E.g if they enter inches,
        # then I will convert it into cm, so when they want to convert it to any other metric unit, I can just convert using cm
        distance1 = {
            "in".lower:number * 2.54,
            "mm".lower:number/10,
            "cm".lower:number/1,
            "dm".lower: number * 10,
            "ft".lower:number * 30.48,
            "m".lower: number * 100,
            "km".lower: number * 100000

            }
        weight1 = {
            "kg".lower: number * 1000,
            "g".lower: number/1,
            "mg".lower:number/1000,
            "l".lower(): number * 1000,
            "ml".lower: number/1
            }
        time1 = {
            "hrs".lower: number * 3600,
            "s".lower: number/1,
            
            }
        
        initial_key_error = False
        converter = -1
        # uses the dictionary to convert
        try: 
            if metric == "distance" or metric == "d":
                converter = distance1[unit]
                
                
            elif metric == "weight" or metric == "w":
                converter = weight1[unit]
                
            elif metric == "time" or metric == "t":
                converter = time1[unit]

            else:
                converter = -2
        except KeyError:
            initial_key_error = True
        # python dictionary that converts value into another unit
        distance2 = {
            "in".lower or distance2 == "kg".upper:converter / 2.54,
            "mm".lower or distance2 == "kg".upper:converter * 10,
            "cm".lower or distance2 == "kg".upper:converter/1,
            "dm".lower or distance2 == "kg".upper:converter/ 10,
            "ft".lower or distance2 == "kg".upper:converter / 30.48,
            "m".lower or distance2 == "kg".upper:  converter / 100,
            "km".lower or distance2 == "kg".upper: converter/ 100000

        }
        weight2 = {
            "kg".lower or weight2 == "kg".upper: converter / 1000,
            "g".lower or weight2 == "g".upper: converter/1,
            "mg".lower or weight2 == "kg".upper:converter * 1000,
            "l".lower() or weight2 == "kg".upper: converter/ 1000,
            "ml".lower or weight2 == "kg".upper: converter/1
        }
        time2 = {
            "hrs".lower or time2 == "kg".upper: converter/ 3600,
            "s".lower or time2 == "kg".upper: converter/1,
            
        }
        key_error_present = False
        final = "Not invalid"
        # uses the dictionary to convert
        try: 
            if metric == "distance" or metric == "d" and distance2.get(new_unit):
                final = distance2[new_unit]
            
            elif metric == "weight" or metric == "w" and weight2.get(new_unit):
                final = weight2[new_unit]
                
            elif metric == "time" or metric == "t" and time2.get(new_unit):
                final = time2[new_unit]

                
            else:
                final = "invalid"
        except KeyError:
            key_error_present = True
        # checks if they are converting correctly
        
        if key_error_present == True or final == "invalid" or initial_key_error == True or converter == -2:
            wrong = "Please don't convert between distance, time and weight. E.g. I want to convert between weight, but you enter cm \n use VALID units, read the instructions for what units are allowed"
            print()
            print(wrong)
            print()
        # otherwise it will output the proper results
        else:
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
    number = (conversion_calculator(num_check("what is the number? ", low = 1)))
    keep_going = input("press enter to continue or press any key then enter to quit")
    print()

statement_generator("Thanks for using Conversion calculator", "💝")
















































































































