"""
Author: Joe Xu
Takes the initial height of a ball. Takes the "bounciness" factor. Takes the 
number of times the ball bounces.
Outputs the total distance traveled by the ball.
"""
import math


# potentially do some upward bounces
def main():
    """
    Calculates the total distance a ball travels
    """
    height = float(input("Initial height of ball: "))
    # bounciness = float(input("Bounciness of the ball (Percentage): "))
    bounciness = .6
    bounces = int(input("Number of times the ball bounces: "))

    distance = 0
    for i in range(bounces):
        # distance of fall downwards
        distance += height
        # distance of bounce upwards
        height *= bounciness
        distance += height

    print(distance)


if __name__ == "__main__":
    main()
