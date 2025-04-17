"""
COMP.CS.100 The first Python program of programming 1.
Creator: Ujunwa Edum
Student id number: 153062092
"""
def factorial(n):
    """Calculates the factorial of a given positive integer n.

    Parameters:
    n (int): The number for which the factorial is to be calculated.

    Returns:
    int: The factorial of n.
    """
    result =1
    for num in range(1,n+1):
        result *= num
    return result
def calculate_lottery(total_balls, balls_drawn):
    """
        Calculates the probability of guessing all drawn lottery balls correctly.

        Parameters:
            total_balls (int): Total number of balls in the lottery.
            balls_drawn (int): Number of balls drawn in the lottery.

        Returns:
            int: The number of possible trials.
        """
    lottery_num = factorial(total_balls)
    lottery_den = factorial(total_balls - balls_drawn) * factorial(balls_drawn)
    lottery = lottery_num / lottery_den
    result = int(round(lottery))
    return result

def main():
    total_balls = int(input("Enter the total number of lottery balls: "))
    balls_drawn= int(input("Enter the number of the drawn balls: "))
    if total_balls < 0 or balls_drawn < 0:
        print ("The number of balls must be a positive number.")
        return
    if total_balls < balls_drawn:
        print("At most the total number of balls can be drawn.")
        return
    prob = calculate_lottery(total_balls,balls_drawn)
    print(f"The probability of guessing all {balls_drawn} balls correctly is 1/{prob}")
if __name__ == "__main__":
    main()