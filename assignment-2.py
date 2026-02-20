#program is to e 
try:
    attendance = int(input("Enter attendance percentage: "))

    if attendance >= 75:
        print("Attendance OK ")
    elif attendance >= 60:
        print("Warning Improve attendance")
    else:
        print("Shortage of attendance ")

except ValueError:
    print("Attendance must be numeric.")