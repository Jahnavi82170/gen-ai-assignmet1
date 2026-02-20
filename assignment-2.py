#program is check student  attendance percentage
# try is used to test block of code of errors or used to handle runtime errors 
try:
    #input function used to  take input as text
    #int function convert into a number
    attendance = int(input("Enter attendance percentage: "))
    # here we use conditional statements 
    #to check the attendence percentage and print the message
    #if the condition is true then it will print the message 
    # #if the condition is false then it will check the next condition and print the message accordingly
    if attendance >= 75:
        print("Attendance OK ")
    elif attendance >= 60:
        print("Warning Improve attendance")
    else:
        print("Shortage of attendance ")
# except block is used to handle the error if the user input is not a number then it will print the message
except ValueError:
    print("Attendance must be numeric.")