import math  

def main():
    side_a = int(input("Enter length of Side A:"))
    side_b = int(input("Enter length of side B:"))
    result = pythag(side_a, side_b)
    print("The hypotenuse C is:", result)

def pythag(A,B):
    Sum_of_Squares = A**2 + B**2
    C = math.sqrt(Sum_of_Squares)
    return C


main()
