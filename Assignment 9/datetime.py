from datetime import datetime
dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
dob = datetime.strptime(dob_input, '%Y-%m-%d')
current_date = datetime.now()
time_difference = current_date - dob
weeks = time_difference.days // 7
days = time_difference.days % 7
seconds = time_difference.total_seconds()

print("You have lived for:")
print(f"{weeks} weeks, {days} days, and {seconds} seconds.")
