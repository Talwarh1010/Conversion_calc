# Ask the user for an amount and unit of measurement (eg: 10 cm)


from logging import error
def num_check(question, low,):
    
    valid = False
    while not valid:
        
        problem2 = "Please enter a number that is more than 0"
        problem = "Please enter a number that does not have decimals or letters"
                                                                        
        try:
        
            # Ask user to enter a number
            response = int(input(question))

            # Checks number is more than zero
            if response >= low :
                return response

            # Outputs error if input is invalid
            else:
                print(problem2)
                print()
                
        except ValueError:
            print(problem)

def instructions():
    statement_generator("Instructions / information" , "=")
    print()
    print("Please choose an integer and what unit it is in")
    print()
    print("choose what unit you want to convert this in. Make sure it is an appropiate conversion e.g. not seconds into metres or grams into cm")
    print()
    print("This calculator will convert between distance,time and weight")
    print()
    print("complete as many calculations as necessary. press <enter> at the end of each calculations or press any key then enter to quit.")
    print()
    return ""

            
def statement_generator(text, decoration):

    
    
    
    # Make string with five characters
    ends = decoration * 5
    
    # add decoration to start and end of statement
    statement = "{} {} {}". format(ends, text, ends)
    
    print()
    print(statement)
    print()
    
    
    return ""

def conversion_calculator(number):
        print()
        
        print()
        unit = input(str("what unit is it in?   "))
        print()
        print()
        if unit == "in":
                new1 = number * 2.54
        if unit  == "mm":
                new1 = number/10
        if unit  == "cm":
                new1 = number/1
        if unit  == "dm":
                new1 = number * 10
        if unit  == "ft":
                new1 = number / 30.48
        if unit  == "kg":
                new1 == number * 1000
        if unit  == "g":
                new1 = number/1
        if unit  == "mg":
                new1 = number/1000
        if unit  =="hrs":
                new1= number * 3600
        if unit  == "s":
                new1 = number/1
        if unit  == "m":
                new1 = number *100
        
            
            
            
            
                    
        new = input("what unit do you want to convert this to? e.g. cm, ft,🍗?  ")
        if new == "in":
                final = new1 / 2.54
                print("{}{} in inches is {:.2f}".format(number,unit,final))
                
                
        if new == "cm":
                final = new1/1
                print("{}{}in cm is {:.2f}".format(number,unit, final))
                
                    
        if new == "mm":
                final = new1/10
                print("{}{} in millimeters is {:.2f}".format(number,unit,final))    
            
        if new == "dm":
                final = new1*10
                print("{}{}   in decimeters is {:.2f}".format(number,unit,final))    
                
        if new == "ft":
                final = new1*30.4
                print("{}{}  in feet is {:.2f}".format(number,unit,final))
        if new == "g":
                final = new1/1
                print("{}{}   in grams is {:.2f}".format(number,unit,final))
        if new == "kg":
                final = new1 * 1000
                print("{}{}    in kilograms is {:.2f}".format(number,unit,final))
        if new == "mg":
                final = new1/1000
                print("{}{}   in milligrams is {:.2f}".format(number,unit,final))
                
        if new == "hrs":
                final = new1 / 3600
                print("{}{}   in hours is {:.2f}".format(number,unit,final))
        if new == "s":
                final = new1/1
                print("{}{}   in seconds is {:.2f}".format(number,unit,final))
        if new == "m":
                final = new1 / 100
                print("{}{}   in metres is {:.2f}".format(number,unit,final))



statement_generator("WELCOME TO CONVERSION CALCULATOR", "🌟" )
first_time = input("Press <enter> to see instructions or press any key then enter to continue ")



if first_time =="":
    instructions()
    
keep_going = ""
while keep_going =="":
    number = (conversion_calculator(num_check("what is the number? ", low = 1)))
    keep_going = input("press enter to continue or press any key then enter to quit")
    print()

statement_generator("Thanks for using Conversion calculator", "💝")



















































































































