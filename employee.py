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

def calculate_wage_with_conditions(max_hours=100, max_days=20):
    """
    Description:
        Calculates wages based on a condition of max working hours or days.
    Parameters:
        max_hours : int : Maximum working hours allowed in a month (default: 100)
        max_days : int : Maximum working days allowed in a month (default: 20)
    Return:
        int : Total wage based on hours or days worked.
    """
    total_hours = 0
    total_days = 0
    total_wage = 0
    while total_hours < max_hours and total_days < max_days:
        hours_worked = random.choice([4, 8])
        total_hours += hours_worked
        total_wage += calculate_daily_wage(20,8) if hours_worked == 8 else calculate_daily_wage(20,4)
        total_days += 1
    return total_wage

def main():
    welcome_message()
    present = is_employee_present()
    if present:
        wage = calculate_wage_with_conditions()
        print(f"Total Wage based on hours and days condition: {wage}")
    else:
        print("Employee is Absent")

if __name__ == "__main__":
    main()
