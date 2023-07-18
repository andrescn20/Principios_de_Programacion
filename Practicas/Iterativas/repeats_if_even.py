##User inputs an integer
##If the integer is even, the program prints the integer
##If the ingeger is odd, the program finishes
##The program repeats until the user inputs an odd integer

input_number = int(input("Enter an integer: "))
while input_number % 2 == 0:
    print(input_number)
    input_number = int(input("Enter an integer: "))
print("You entered an odd integer. The program has finished.")
