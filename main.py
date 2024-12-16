# ----------------------------------------------------------------------------------
#
# Title:   Cheque Mate
# Version: 1.1
# Date:    December 13, 2024
#
# Author:  Nina Jakobsen
# Course:  ICS3U
# School:  Glebe Collegiate Institute, Ottawa
# Teacher: Mr. Giansante
#
# Description:  This program coverts numerical money to their word equivalent.
#
# ------------------------------------------------------------------------------------


#  Setting up intial values

valid = False
inp = ""
num = 0
cent = "0"
thou = "0"
hun = "0"
ten = "0"
one = "0"
teen = "0"

# Getting user input

while valid == False:
    print("")
    inp = input("Please enter the amount ($0.01 to $9999.99):$")
    check = inp.replace(".","")
    cent = inp[-3:6]
    
# Error checking
    
    if check.isdecimal() == False:
        valid = False
        print("Error. Please do not enter any spaces, letters (A-Z),")
        print("or special charcters (exlcuding \".\")")

    if check.isdecimal() == True:
        # Must fix the ".0.99" float issue!!!!!!!!!!
        num = float(inp)

        if num >= 10000:
            valid = False
            print("Error. The amount you entered is too large.")

        if num <= 0:
            valid = False
            print("Error. The amount you entered is too small.")

        if inp.count(".") > 1:
            valid = False
            print("Error. Please only include \".\" maximum one time")
            print("to seperate dollars and cents.")

        if "." not in inp:
            valid = False
            print("Error. You must include \".\" to seperate dollars")
            print("from cents (ex. $24.50 or $10.00)")

        if inp[0] == ".":
            valid = False
            print("Error. You cannot begin your value with \".\" (ex.")
            print("$0.44 not $.44).")

        else:
            if inp[-3] != ".":
                print("Error. You must include 2 digits after the decimal")
                print("ex. $123.40 not $123.4")


        if check.isdecimal() == True and inp.count(".") == 1 and num > 0 and num < 10000 and inp[-3] == "." and inp[0] != ".":
            valid = True 
            print("Valid")

# Generating output

        if valid == True:

            # Seperating thousands, hundreds, tens, ones, and cents.
            
            if num < 10000 and num >= 1000:
                thou = inp[0]
                hun = inp[1]
                ten = inp[2]
                one = inp[3]
                cent = inp[5:7]

            if num < 1000 and num >= 100:
                hun = inp[0]
                ten = inp[1]
                one = inp[2]
                cent = inp[4:8]

            if num < 100 and num >= 10:
                ten = inp[0]
                one = inp[1]
                cent = inp[3:5]

            if num < 10 and num >= 0:
                one = inp[0]
                cent = inp[2:4]

            thou = int(thou)
            hun = int(hun)
            ten = int(ten)
            one = int(one) 

            print(thou)
            print(hun)
            print(ten)
            print(one)
            print(cent)

            # Going from numbers to words
            
            thoudict = ("", "One Thousand", "Two Thousand", "Three Thousand", "Four Thousand", "Five Thousand", "Six Thousand", "Seven Thousand", "Eight Thousand", "Nine Thousand")

            hundict = ("", "One Hundred", "Two Hundred", "Three Hundred", "Four Hundred", "Five Hundred", "Six Hundred", "Seven Hundred", "Eight Hundred", "Nine Hundred")


            # If the number has a teen in it 
            
            if ten == 1:
                teen = ten + one
                teen = int(teen)
                teen = teen - 10

                teensdict = ("Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",  "Eighteen", "Nineteen")

                if num >= 1000 and num < 10000:
                    print(thoudict[thou] + " " + hundict[hun] + " and " + teensdict[teen] + " Dollars and " + cent + "/100 Cents")

                if num >= 100 and num < 1000:
                    print(hundict[hun] + " and " + teensdict[teen] + " Dollars and " + cent + "/100 Cents")

                if num >= 10 and num < 100:
                    print(teensdict[teen] + "Dollars and " + cent + "/100 Cents") 

            if ten != 1:

                tendict = ("", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety") 

                onedict = ("", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine") 


            # Dollars
             
                if one != 1:
                    if num >= 1000 and num < 10000:
                        print(thoudict[thou] + " " + hundict[hun] + " and " + tendict[ten] + " " + onedict[one] + " Dollars and " + cent + "/100 Cents")
                        
                    if num >= 100 and num < 1000:
                        print(hundict[hun] + " and " + tendict[ten] + " " + onedict[one] + " Dollars and " + cent + "/100 Cents")

                    if num >= 10 and num < 100:
                        print(tendict[ten] + " " + onedict[one] + " Dollars and " + cent + "/100 Cents")

                    if num >= 1 and num < 10:
                        print(onedict[one] + " Dollars and " + cent + "/100 Cents")

            # Dollar

                if one == 1:
                    if num >= 1000 and num < 10000:
                        print(thoudict[thou] + " " + hundict[hun] + " and " + tendict[ten] + " " + onedict[one] + " Dollar and " + cent + "/100 Cents")
                        
                    if num >= 100 and num < 1000:
                        print(hundict[hun] + " and " + tendict[ten] + " " + onedict[one] + " Dollar and " + cent + "/100 Cents")

                    if num >= 10 and num < 100:
                        print(tendict[ten] + " " + onedict[one] + " Dollar and " + cent + "/100 Cents")

                    if num >= 1 and num < 10:
                        print(onedict[one] + " Dollar and " + cent +  "/100 Cents") 



                

                
