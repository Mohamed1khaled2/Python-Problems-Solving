# Users inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost_home = float(input("Enter the cost of your dream home: "))  # my dream cost home
semi_annual = float(input("Enter the semi-annual raise, as a decimal: "))


start = 6  # start about increase my salary
first_portion = int(0.25 * total_cost_home)
my_money = int((annual_salary * portion_saved) / 12)  # output = my salary  monthly
monthly = 1  # first month
while my_money <= first_portion:
    my_startup_return = int(my_money * 0.04 / 12)
    # I mean after to six month or twelve and so on
    if monthly == start:
        annual_salary += int((semi_annual * annual_salary))
        start += 6  # my because my increase my salary every six months
    my_money += int((annual_salary * portion_saved) / 12 + my_startup_return)
    monthly += 1

print(f"Number of months: {monthly} and {my_money}")
