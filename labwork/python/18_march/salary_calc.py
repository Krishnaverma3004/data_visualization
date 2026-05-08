basic_salary = float(input("Enter your basic salary: "))
hra = float(input("Enter HRA in %: "))
bonus = float(input("Enter the bonus: "))

total_HRA = basic_salary * hra / 100
total_salary = basic_salary + total_HRA + bonus

print("Total HRA:", total_HRA)
print("Total monthly salary:", total_salary)
