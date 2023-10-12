# Users inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost_home = float(input("Enter the cost of your dream home: "))  # my dream cost home

first_portion = 0.25 * total_cost_home
my_money = (annual_salary*portion_saved) / 12     # output = my salary  monthly
monthly = 1  # first month
while my_money <= first_portion:
    my_startup_return = my_money * 0.04 / 12
    my_money += ((annual_salary*portion_saved) / 12) + my_startup_return
    monthly += 1


print(f"Number of months: {monthly}")
