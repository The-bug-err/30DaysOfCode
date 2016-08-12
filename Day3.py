"""
Usage :	Just copy paste the content of the script in the iPython interperter,
		or just call the script. The scripts written are only for
		study purpose.

Author:	Vivek Rana

Date:	--2016

About Script:
		Write some thing about script here.
"""

def main():
        mealCost = eval(input("Enter Meal Cost : "))
        tipPercent = eval(input("Enter tip Percentage : "))
        taxPercent = eval(input("Enter tax Percentage : "))
        tip = mealCost * tipPercent/100
        tax = mealCost * taxPercent/100
        total = mealCost + tip + tax
        print("The total meal cost is",round(total),"dollars.")
        return 

if __name__ == '__main__':
        main()
        input("Press any button to exit.")
