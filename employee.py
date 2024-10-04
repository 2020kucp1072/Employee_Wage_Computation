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

def calculate_daily_wage(hourly_wage,hours):
    """
    Description:
        Calculates the wage for a part-time employee.
    Parameters:
        hourly_wage : int : Wage per hour (default: 20)
        part_time_hours : int : Number of part-time working hours (default: 4)
    Return:
        int : Part-time wage of the employee
    """
    return hourly_wage * hours

def calculate_monthly_wage(working_days=20):
    """
    Description:
        Calculates the monthly wage for the employee based on working days.
    Parameters:
        working_days : int : Number of working days in a month (default: 20)
    Return:
        int : Monthly wage of the employee
    """
    return calculate_daily_wage(20,8) * working_days

def main():
    welcome_message()
    present = is_employee_present()
    if present:
        employee_type = random.choice(["full-time", "part-time"])
        if employee_type == "full-time":
            wage = calculate_monthly_wage()
        else:
            wage = calculate_daily_wage(20,4) * 20  # Assuming part-time works for 20 days
        print(f"Employee is {employee_type.capitalize()}, Monthly Wage: {wage}")
    else:
        print("Employee is Absent")

if __name__ == "__main__":
    main()
