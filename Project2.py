age=float(input("What is your age? "))
hage=age*360
dage=hage*7
dyears=dage//360
dleftover=dage%360
dmonths=dleftover//30
ddays=dleftover%30
cage=hage//9
cyears=cage//360
cleftover=cage%360
cmonths=cleftover//30
cdays=cleftover%30
hrfill=3*(((age**2-47)/7)+12)
hrage=hrfill*360
hryears=hrage//360
hrleftover=hrage%360
hrmonths=hrleftover//30
hrdays=hrleftover%30
print(f"Your Dog age is: {dyears} Years, {dmonths} Months, and {ddays:.0f} Days.")  
print(f"Your Cat age is: {cyears} Years, {cmonths} Months, and {cdays:.0f} Days.")
print(f"Your Horse age is: {hryears} Years, {hrmonths} Months, and {hrdays:.0f} Days.")