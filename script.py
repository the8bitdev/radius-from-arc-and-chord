import math

# costants
precision = 20 # bigger is more precise but uses more resources
maxiter = 2**16 # max iterations (set -1 for infinite but can freeze)

# variables
approx = float(0) # initial approximation (can probably be optimized)
x = float(0) # half of the central angle

# inputs
arc = float(input("Insert arc length: "))
chord = float(input("Insert chord length: "))

# input checks
if arc > 0 and chord > 0:
    if arc > chord:

        # iterate until x is an acceptable angle (positive and under 360°)
        while x <= 0 or x > 2 * math.pi:
            approx += 1
            x = approx
            i = int(0)

            # iterate until x is precise enough or max iterations are reached
            while (((arc / chord) * math.sin(x) - x > 10 ** (-1*precision)) or ((arc / chord) * math.sin(x) - x < -1 * (10 ** (-1*precision)))) and i != maxiter:
                x -= (((arc / chord) * math.sin(x)) - x) / (((arc / chord) * math.cos(x)) - 1)
                i += 1

        x *= 2

        # outputs
        print("\nCompleted after", i, "iterations")
        print("Radius =", arc / x)
        print("Angle =", x, "radians")
        print("Angle =", x * (180 / math.pi), "degrees")

    else:
        print("ERROR: Arc length must be greater than chord length")
else:
    print("ERROR: Both arc and chord length must be greater than 0")