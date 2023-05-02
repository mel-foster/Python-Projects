#!/usr/bin/env python3.7

# AWS Service List for Week 12 project
# Create a list of services using Python. IE: S3, Lambda, EC2, ETC.

# 1) The list should be empty
my_list = []

# 2) populate the list using append or insert.
my_list.append('Api Gateway')
my_list.append('Cloud9')
my_list.append('CloudWatch')
my_list.append('DynamoDB')
my_list.append('EC2')
my_list.append('IAM')
my_list.append('Key Management System')
my_list.append('Lambda')
my_list.append('S3')
my_list.append('SNS')
my_list.append('VPC')
my_list.append('Xray')

# 3.Print the list and the length of the list.
print("AWS List: ", (my_list))
print("the length of the list is: ", len(my_list))

# 4.Remove two specific services from the list by name or by index.
del my_list [9:11]

# 5.Print the new list and the new length of the list.
print("AWS List: ", (my_list))
print("the length of the list is: ", len(my_list))

# 6.Push your code to GitHub