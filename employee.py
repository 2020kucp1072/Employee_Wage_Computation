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

def calculate_full_daily_wage(hourly_wage=20, full_day_hours=8):
    """
    Description:
        Calculates the daily wage of an employee.
    Parameters:
        hourly_wage : int : Wage per hour (default: 20)
        full_day_hours : int : Number of hours in a full working day (default: 8)
    Return:
        int : Daily wage of the employee
    """
    return hourly_wage * full_day_hours

def main():
    part_time =4
    full_time =8
    welcome_message()
    present = is_employee_present()
    if present==1:
        print("Employee is Present")
        wage = calculate_full_daily_wage()
        print(f"Employee is Present, Daily Wage: {wage}")
    
    else:
        print("Employee is Absent")
        
    

if __name__ == "__main__":
    main()

