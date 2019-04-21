"""
Author: Joe Xu
Takes the radius of a sphere (a floating-point number) as input and output the
sphere's diameter, circumference, surface, area, and volume.
"""
import math

def main():
    """
    Inputs the radius of the sphere and calculates other dimensions
    """
    radius = float(input("Enter the radius of the sphere: "))
    print("The diameter is %.2f" % (2.0*radius))
    print("The circumference is %.2f" % (2.0*radius*math.pi))
    print("The surface area is %.2f" % (4*math.pi*radius**2.0))
    print("The volume is %.2f" % (4.0/3.0*math.pi*radius**3))

if __name__ == "__main__":
    main()