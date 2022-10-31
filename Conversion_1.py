


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
        valid = False
        while not valid:
            distance_list = ["km", "m", "dm" "ft", "in", "mm", "cm"]
            weight_list = ["kg", "g", "mg"]
            time_list = ["hrs", "s"]
            volume_list = ["l", "ml"]
            
            metric = input(str("What are you converting e.g. distance, time, weight or volume? ").lower())
            if metric in ["distance", "d", "time", "t", "weight", "w", "volume", "v"]:
                break
            else:
                print()
                print("Please enter a valid conversion type")
                print()
                
        # what unit it is in
        
        valid1 = False
        while not valid1:
            unit = input("what unit is it in?   ").lower()
            if metric in ["distance", "d"] and unit in distance_list:
                break
            elif metric in ["weight", "w"] and  unit in weight_list:
                break
            elif metric in ["time", "t"] and unit in time_list:
                break
            elif metric in ["volume", "v"] and  unit in volume_list:
                break
            
            else :
                print()
                print("please input a valid unit to convert from")
                print()
                
        # what they want to convert to
        valid1 = False
        while not valid1:
            new_unit = input("what unit do you want to convert this to?  e.g. cm, l, g, hrs etc   ").lower()
            if metric in ["distance", "d"] and unit in distance_list and new_unit in distance_list:
                break
            elif metric in ["weight", "w"] and  unit in weight_list and new_unit in weight_list:
                break
            elif metric in ["time", "t"] and unit in time_list and new_unit in time_list:
                break
            elif metric in ["volume", "v"] and  unit in volume_list and new_unit in volume_list:
                break
            
            else :
                print()
                print("please input a valid unit to convert to")
                print()
        
        # python dictionary that converts input into a common metric unit depending on the unit they enter. E.g if they enter inches,
        # then I will convert it into cm, so when they want to convert it to any other metric unit, I can just convert using cm
        distance1 = {
                    "in":number * 2.54,
                    "mm" :number/10,
                    "cm" :number/1,
                    "dm" : number * 10,
                    "ft" :number * 30.48,
                    "m" : number * 100,
                    "km" : number * 100000
                    }
        weight1 = {
                    "kg" : number * 1000,
                    "g" : number/1,
                    "mg" :number/1000,
                    
                    }
        time1 = {
                    "hrs" : number * 3600,
                    "s" : number/1,
                    }
        volume1 = {
                    "l": number * 1000,
                    "ml" : number / 1
                    }
        # uses the dictionary to convert
        if metric == "distance" or metric == "d":
                converter = distance1[unit]
                
                
        elif metric == "weight" or metric == "w":
                converter = weight1[unit]
                
        elif metric == "time" or metric == "t":
                converter = time1[unit]
                
        elif metric =="volume" or metric == "v":
                converter = volume1[unit]
                
        # python dictionary that converts value into another unit
        distance2 = {
            "in" :converter / 2.54,
            "mm":converter * 10,
            "cm":converter/1,
            "dm":converter/ 10,
            "ft":converter / 30.48,
            "m": converter / 100,
            "km": converter/ 100000

        }
        weight2 = {
            "kg"  : converter / 1000,
            "g"  : converter/1,
            "mg" :converter * 1000,
            
        }
        time2 = {
            "hrs" : converter/ 3600,
            "s" : converter/1,
        }
        volume2  = {
            "l"  : converter/ 1000,
            "ml"  : converter/1
        }
        # uses the dictionary to convert
        
        if metric == "distance" or metric == "d" and distance2.get(new_unit):
                final = distance2[new_unit]
            
        elif metric == "weight" or metric == "w" and weight2.get(new_unit):
                final = weight2[new_unit]
                
        elif metric == "time" or metric == "t" and time2.get(new_unit):
                final = time2[new_unit]
                
        elif metric == "volume" or metric == "v" and volume2.get(new_unit):
                final = volume2[new_unit]
                
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

















































































































