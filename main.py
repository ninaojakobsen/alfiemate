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
                ten = [0]
                one = [1]
                cent = inp[3:5]

            if num < 10 and num >= 0:
                one = inp[0]
                cent = inp[2:4]

            print(thou)
            print(hun)
            print(ten)
            print(one)
            print(cent)
            
            thoudict = {
                "0": "",
                "1": "One Thousand",
                "2": "Two Thousand",
                "3": "Three Thousand",
                "4": "Four Thousand",
                "5": "Five Thousand",
                "6": "Six Thousand",
                "7": "Seven Thousand",
                "8": "Eight Thousand",
                "9": "Nine Thousand" }

            hundict = {
                "0": "",
                "1": "One Hundred",
                "2": "Two Hundred",
                "3": "Three Hundred",
                "4": "Four Hundred",
                "5": "Five Hundred",
                "6": "Six Hundred",
                "7": "Seven Hundred",
                "8": "Eight Hundred",
                "9": "Nine Hundred" }

            if ten == "1":
                teen = ten + one

                teensdict = {
                    "10", "Ten",
                    "11", "Eleven",
                    "12", "Twelve",
                    "13", "Thirteen",
                    "14", "Fourteen",
                    "15", "Fifteen",
                    "16", "Sixteen",
                    "17", "Seventeen",
                    "18", "Eighteen",
                    "19", "Nineteen" }

                print(thoudict[thou])

            if ten != "1":

                tendict = {
                    "0": "",
                    "2": "Twenty",
                    "3": "Thirty",
                    "4": "Forty",
                    "5": "Fifty",
                    "6": "Sixty",
                    "7": "Seventy",
                    "8": "Eighty",
                    "9": "Ninety" }

                onedict = {
                    "0": "",
                    "1": "One",
                    "2": "Two",
                    "3": "Three",
                    "4": "Four",
                    "5": "Five",
                    "6": "Six",
                    "7": "Seven",
                    "8": "Eight",
                    "9": "Nine" } 
                

                #if one != "1":

                #if one == "1": 

                

