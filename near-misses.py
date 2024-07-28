'''
 * Title: Looking for Fermat’s Last Theorem Near Misses
 * File Name: near-misses.py
 * List of External Files to run the program: None
 * List of External Files the program creates: None
 * Names of Programmers: Jagadish Sagi, Navadeep Gottigundala
 * Email Address of Programmers: jagadishsagi@lewisu.edu, navadeepgottigunda@lewisu.edu
 * Course and Sections: Software Engineering, SU24-CPSC-60500-001
 * Date: 28th July 2024.
 * Explanation: 
    * Program to find the Fermat's Last Theorem Near Misses. The Program takes valid inputs from the user (n and k).
    * And finds the near misses of the form x^n + y^n = z^n, where x, y, z, n are positive integers with the following constraints for n and x, y.
    * 2 < n < 12 and 10 <= x <= k and 10 <= y <= k. 
    * For each miss, the program computes the relative miss, prints new smallest relative miss every time and finally printing the Smallest relative miss overall.
'''


'''
 * Function to validate the inputs entered by the User.
 * If the input is invalid, the function will throw a ValueError Exception.
'''
def validate_inputs(n, k):
    if n < 2 or n > 12:
        raise ValueError('n must be between 2 and 12')
    if k <= 10:
        raise ValueError('k must be greater than 10')

'''
 * Function to read and validate the inputs provided by the User.
 * If the input is invalid, a ValueError Exception will be thrown to the User.
'''
def read_inputs():
    # Reading the Exponent value to a variable.
    n = int(input("Please enter the exponent ( 2 < n < 12 ): "))

    # Printing blank line for visibility to the User.
    print()

    # Reading the Limit value to a variable.
    k = int(input("Please enter the limit for x and y ( k > 10 ): "))
    
    # Printing blank line for visibility to the User.
    print()

    # Validating the Inputs.
    validate_inputs(n, k)

    # Returning the validated inputs to the main function.
    return n, k

'''
 * Function to find the Fermat's Last theorem near misses from the inputs provided by the User.
'''
def fermats_last_theorem_near_misses(n, k):
    # Variable that holds the smallest miss and smallest relative miss, the default value is inifinity for both variables.
    smallest_miss, smallest_relative_miss = float('inf'), float('inf')

    # Variable that holds the x, y, z values of the smallest relative miss.
    smallest_relative_miss_x, smallest_relative_miss_y, smallest_relative_miss_z = None, None, None

    # Constant value that is used for printing output in a more user-friendly way.
    relative_miss_output_separator = "-" * 150

    # Trying out different possible combinations of x values to find the smallest relative miss.
    for x in range(10, k + 1):
        # Trying out different possible combinations of y values to find the smallest relative miss.
        for y in range(10, k + 1):
            # Variable holding the sum of the powers.
            x_and_y_power_sum = (x ** n) + (y ** n)

            # Variable holding the floor value of z.
            z = int(x_and_y_power_sum ** (1/n))

            # Find the lower and upper bounds of the sum of the powers.
            lower_bound = (z ** n)
            upper_bound = ( (z + 1) ** n )

            # Find the difference between the sum of the powers and the bounds.
            lower_bound_miss = abs(x_and_y_power_sum - lower_bound)
            upper_bound_miss = abs(upper_bound - x_and_y_power_sum)

            # Find the smallest difference between the sum of the powers and the bounds.
            miss = min(lower_bound_miss, upper_bound_miss)

            # Find the relative miss.
            relative_miss = miss / x_and_y_power_sum

            # If the relative miss is less than the smallest relative miss so far, then update the smallest relative miss and the corresponding values.
            if relative_miss < smallest_relative_miss:
                # Updating Smallest miss.
                smallest_miss = miss

                # Updating Smallest relative miss.
                smallest_relative_miss = relative_miss

                # Updating Smallest relative miss x, y, z values.
                smallest_relative_miss_x, smallest_relative_miss_y, smallest_relative_miss_z = x, y, z

                # Printing the separator for visibility to the User.
                print(relative_miss_output_separator)
                # Printing the new smallest relative miss and the corresponding values.
                print(f"\n Found new Smallest Relative Miss with x: {x}, y: {y}, z: {z}, actual miss: {smallest_miss}, relative miss: {relative_miss:.6f} \n")

    # Printing the Overall Smallest relative miss and the corresponding values after all the iterations to the User.
    print(relative_miss_output_separator)
    print(f"\n Overall Smallest relative miss after all iterations - x: {smallest_relative_miss_x}, y: {smallest_relative_miss_y}, z: {smallest_relative_miss_z}, miss: {smallest_miss}, relative miss: {smallest_relative_miss:.6f}\n")
    print(relative_miss_output_separator)

# Main Block, where the execution begins.
if __name__ == "__main__":
    '''
     * As part of the Loop, we are going to read the inputs from the User.
     * There is a possibility, that the User enters incorrect input, so in case if the User enters invalid input, we are going to try again.
     * The user will be given three attempts to enter valid input. 
     * If the user enters valid input, we are going break from the loop and call the fermats_last_theorem_near_misses function.
     * If the user fails to enter valid input 3 times, we are going to exit the program.
    '''
    for attempt in range(1, 4):
        try:
            # Reading the inputs from the User.
            n, k = read_inputs()
        except ValueError as e:
            # Printing the exception to the User.
            print(f"You've entered invalid input during attempt: {attempt} and the following exception is thrown: {e}")
            print(f"\nYou have {3 - attempt} attempt(s) left\n\n")

            # Since, the User has entered invalid inputs 3 times, we are going to exit the program.
            if attempt == 3:
                print("You've exhausted all the attempts to enter valid input.")
                # This is to ensure that the Window doesn't close automatically, and the user can view the output.
                input("\nPress Enter to exit...")
                exit(1)
        else:
            break

    # Call the Function to find the near misses.
    fermats_last_theorem_near_misses(n, k)

    # This is to ensure that the Window doesn't close automatically, and the user can view the output.
    input("\nPress Enter to exit...")