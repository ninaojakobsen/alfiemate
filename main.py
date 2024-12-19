# ----------------------------------------------------------------------------------
#
# Title:   Cheque Mate
# Version: 1.3
# Date:    December 19, 2024
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
check = ""
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
    
# Error checking
    
    if check.isdecimal() == False:
        valid = False
        print("Invalid input. Your amount must:")
        print("""- Only contain numbers and one decimal place (\".\")
- The amount must be between $9999.99 and $0.01
- The decimal place must be followed by two numbers (ex. $123.40
  not $123.4)""")
              
    if check.isdecimal() == True:
              
        if "." not in inp:
            valid = False
            print("Invalid input. Your amount must:")
            print("""- Only contain numbers and one decimal place (\".\")
- The amount must be between $9999.99 and $0.01
- The decimal place must be followed by two numbers (ex. $123.40
  not $123.4)""")
          
        if "." in inp:

            if inp.count(".") > 1:
                valid = False
                print("Invalid input. Your amount must:")
                print("""- Only contain numbers and one decimal place (\".\")
- The amount must be between $9999.99 and $0.01
- The decimal place must be followed by two numbers (ex. $123.40
  not $123.4)""")

            if inp.count(".") == 1:
                
                num = float(inp)

                if num >= 10000 or num <= 0 or inp.count(".") > 1 or "." not in inp or inp[0] == ".":
                    valid = False
                    print("Invalid input. Your amount must:")
                    print("""- Only contain numbers and one decimal place (\".\")
- The amount must be between $9999.99 and $0.01
- The decimal place must be followed by two numbers (ex. $123.40
  not $123.4)""")

                else:
                    if inp[-3] != ".":
                        print("Invalid input. Your amount must:")
                        print("""- Only contain numbers and one decimal place (\".\")
- The amount must be between $9999.99 and $0.01
- The decimal place must be followed by two numbers (ex. $123.40
  not $123.4)""")
                

        if check.isdecimal() == True and inp.count(".") == 1 and num > 0 and num < 10000 and inp[-3] == "." and inp[0] != ".":
            valid = True 
            print("Input is valid.")

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

            # Going from numbers to words
            
            thoudict = ("", "One Thousand ", "Two Thousand ", "Three Thousand ", "Four Thousand ", "Five Thousand ", "Six Thousand ", "Seven Thousand ", "Eight Thousand ", "Nine Thousand ")

            hundict = ("", "One Hundred ", "Two Hundred ", "Three Hundred ", "Four Hundred ", "Five Hundred ", "Six Hundred ", "Seven Hundred ", "Eight Hundred ", "Nine Hundred ")


            # If the number has a teen in it 
            
            if ten == 1:
                ten = str(ten)
                one = str(one)
                teen = ten + one
                teen = int(teen)
                teen = teen - 10
                ten = int(ten)
                
                teensdict =  ("Ten ", "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ",  "Eighteen ", "Nineteen ")

                if num >= 1000 and num < 10000:
                    print(thoudict[thou] +  hundict[hun] + teensdict[teen] + "and " + cent + "/100")

                if num >= 100 and num < 1000:
                    print(hundict[hun] + teensdict[teen] + "and " + cent + "/100")

                if num >= 10 and num < 100:
                    print(teensdict[teen] + "and " + cent + "/100") 

            if ten != 1:

                tendict = ("", "", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety ") 

                onedict = ("", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine ") 


            # Dollars
             
                if num > 1:
                    if num >= 1000 and num < 10000:
                        print(thoudict[thou] + hundict[hun] + tendict[ten] + onedict[one] + "and " + cent + "/100")
                        
                    if num >= 100 and num < 1000:
                        print(hundict[hun] + tendict[ten] + onedict[one] + "and " + cent + "/100")

                    if num >= 10 and num < 100:
                        print(tendict[ten] + onedict[one] + "and " + cent + "/100")

                    if num >= 1 and num < 10:
                        print(onedict[one] + "and " + cent + "/100")

            # Dollar

                if num == 1:
                    if num >= 1 and num < 10:
                        print(onedict[one] + "and " + cent +  "/100")


            # 0 Dollars and some cents

                if thou == 0 and hun == 0 and ten == 0 and one == 0:
                    print(cent + "/100")



                

                
