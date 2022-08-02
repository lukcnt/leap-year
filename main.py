# Input of the year that will be worked.
year = int(input("Which year do you want to check? "))

# Coniditional which points if is a leap year or not.
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")