
'''
    @Author: VEMULA DILEEP
    @Date: 30-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:45
    @Title : Employee Wage Computation Program using Class Methods for various Use Cases (UC1 - UC7)
'''

import random

class EmployeeWageComputation:
    def __init__(self, wage_per_hour=20, full_day_hour=8, part_time_hour=4):
        self.wage_per_hour = wage_per_hour
        self.full_day_hour = full_day_hour
        self.part_time_hour = part_time_hour

    # UC1: Check Employee is Present or Absent
    def is_employee_present(self):
        """
        Description:
            Checks if the employee is present or absent using a random function.
        Return:
            bool : True if employee is present, otherwise False.
        """
        return random.choice([True, False])

    # UC2: Calculate Daily Employee Wage
    def calculate_daily_wage(self):
        """
        Description:
            Calculates daily wage for a full-time employee.
        Return:
            int : Daily wage calculated based on full-day hours.
        """
        return self.wage_per_hour * self.full_day_hour

    # UC3: Add Part-Time Employee and Wage
    def calculate_part_time_wage(self):
        """
        Description:
            Calculates daily wage for a part-time employee.
        Return:
            int : Daily wage calculated based on part-time hours.
        """
        return self.wage_per_hour * self.part_time_hour

    # UC4: Solving using Switch Case (if-else in Python)
    def calculate_wage_based_on_type(self, emp_type):
        """
        Description:
            Calculates wage based on employee type (full-time or part-time).
        Parameters:
            emp_type : str : 'full' for full-time, 'part' for part-time.
        Return:
            int : Wage calculated based on employee type.
        """
        if emp_type == 'full':
            return self.calculate_daily_wage()
        elif emp_type == 'part':
            return self.calculate_part_time_wage()
        else:
            return 0

    # UC5: Calculating Wages for a Month (Assuming 20 working days)
    def calculate_monthly_wage(self, emp_type):
        """
        Description:
            Calculates monthly wage based on the employee type.
        Parameters:
            emp_type : str : 'full' for full-time, 'part' for part-time.
        Return:
            int : Monthly wage calculated based on 20 working days.
        """
        daily_wage = self.calculate_wage_based_on_type(emp_type)
        return daily_wage * 20

    # UC6: Calculate Wages Until a Condition is Reached (100 hours or 20 days)
    def calculate_wage_with_conditions(self):
        """
        Description:
            Calculates wages until a condition is met, either 100 hours or 20 days.
        Return:
            int : Total wage based on conditions.
        """
        total_wage = 0
        total_hours = 0
        total_days = 0

        while total_hours < 100 and total_days < 20:
            if self.is_employee_present():
                daily_hours = random.choice([self.full_day_hour, self.part_time_hour])
                total_hours += daily_hours
                total_wage += daily_hours * self.wage_per_hour
            total_days += 1
        
        return total_wage

    # UC7: Refactor Code to Use Class Methods
    def display_welcome_message(self):
        """
        Description:
            Displays a welcome message for the Employee Wage Computation program.
        """
        print("Welcome to Employee Wage Computation Program")


def main():
    # Creating an instance of the class
    emp_wage_computation = EmployeeWageComputation()

    # UC1: Checking employee presence
    emp_wage_computation.display_welcome_message()
    print("Is employee present:", emp_wage_computation.is_employee_present())

    # UC2: Calculating daily wage for full-time employee
    print("Daily Wage for Full-time:", emp_wage_computation.calculate_daily_wage())

    # UC3: Calculating daily wage for part-time employee
    print("Daily Wage for Part-time:", emp_wage_computation.calculate_part_time_wage())

    # UC4: Wage based on employee type (Full-time/Part-time)
    emp_type = 'full'
    print(f"Daily wage for {emp_type}-time employee:", emp_wage_computation.calculate_wage_based_on_type(emp_type))

    # UC5: Monthly wage for full-time employee
    print("Monthly Wage for Full-time:", emp_wage_computation.calculate_monthly_wage(emp_type))

    # UC6: Wages until condition is met
    print("Total wage until condition is met (100 hours or 20 days):", emp_wage_computation.calculate_wage_with_conditions())


if __name__ == "__main__":
    main()
