#!/usr/bin/env python3.7

import random #Import the Random module which will generate numbers based on a range provided

def ec2_range(num_chars): 
    return "".join(chr(random.randint(26,125)) for i in range(num_chars)) 
    
ec2_count =int(input("Enter the number of AWS EC2 Instances Needed. *Note: You will be prompted to complete requested information to generate name for total request(s).")) #Enter the number of EC2 Instances and the counter will be triggered for each request.

#List Authorized Departments: Marketing, Accounting, and FinOps

depts = ["Accounting", "FinOps", "Marketing"]
count = 0 #Count used to define the number of requested random names by the user

while count != ec2_count:
    if count < ec2_count:
        print("Please select from one of the authorized departments: Accounting, FinOps, or Marketing, ")
        ec2_name = str(input("\nEnter Department Name: ")) #User Prompt to enter name of EC2 to link to their dept
    if ec2_name in depts:
        print(ec2_name + ec2_range(13))
        print("\n")
        count +=1
    elif not ec2_name in depts: #Error:User did not enter correct dept, misspelled, or uppercase character(s)
        ec2_name =str(input("\nError: Incorrect Department or verify spelling. Note: Dept. Name is Case Sensitive. Please, try again and select from one of the following departments: Accounting, FinOps, or Marketing\n")
        if ec2_name in depts: #confirm new entry is correct
            print(ec2_name + ec2_range(13)) #confirmation print statement has both requirements of  dept name and generated character
            count += 1
        else:
            print("\nYou are not authorized to use this program!”) # User still didn’t enter the correct name so they are told they are not authorized")
            print("\nPlease obtain the required authorization and rerun the program once again, Thank You!")
            break
    
#Confirmation of request being completed
    print('\nYour Request has been COMPLETED and ' +str(count) + ' randomly generated name(s) were created!')
    
