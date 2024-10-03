"""
    @Author: VEMULA DILEEP
    @Date: 02-10-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 17:30
    @Title: Employee Wage Computation Program
"""

def welcome_message():
    """
    Description:
        Displays a welcome message for the Employee Wage Computation Program.
    Return:
        None
    """
    print("Welcome to Employee Wage Computation Program")

import random

def is_employee_present():
    """
    Description:
        Checks whether the employee is present or absent using random.
    Return:
        bool : True if employee is present, False if absent
    """
    return random.randint(0,1)

def main():
    welcome_message()
    present = is_employee_present()
    if present==1:
        print("Employee is Present")
    else:
        print("Employee is Absent")

if __name__ == "__main__":
    main()

