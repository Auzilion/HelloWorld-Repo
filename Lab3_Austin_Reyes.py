income = int(input("What is your income?"))
status = input("Are you Married? (y/n)")

if income>95375 and status=="n":
    taxrate=("You make too much for this calculator to work.")
elif income>190750 and status=="y":
    taxrate=("You make too much for this caculator to work.")
elif income in range(0, 11001) and status=="n":
    taxrate="10%"
elif income in range(0,22001) and status=="y":
    taxrate="10%"
elif income in range(11000, 44726) and status=="n":
    taxrate="12%"
elif income in range(22001, 89451) and status=="y":
    taxrate="12%"
elif income in range(44726, 95376) and status=="n":
    taxrate="22%"
elif income in range(89451, 190701) and status=="y":
    taxrate="22%"
print(taxrate)