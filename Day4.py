"""
Usage :	Just copy paste the content of the script in the iPython interperter,
		or just call the script. The scripts written are only for
		study purpose.

Author:	Vivek Rana

Date:	12-Aug-2016

About Script:
		Write some thing about script here.
		https://www.hackerrank.com/challenges/30-conditional-statements
"""

def main():
        N = int(input("Enter value for N : ").strip())
        if (N%2 == 0) and ((N in (2,3,4,5)) or N > 20 ):
                print("Not Weird")
        else:
                print("Weird")
        return 

if __name__ == '__main__':
	main()
	input("Press any button to exit.")
