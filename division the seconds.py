seconds = int(input("Enter the number of seconds\n"))
hours = seconds // 3600
min = seconds % 3600 //60
sec = seconds % 3600 % 60
print(f"number of hours is {hours} and number of minutes is {min} and number of seconds is {sec}")
