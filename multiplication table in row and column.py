"""
######## Problem  4  ###############

#print a multiplication table like below.
#get user intput for start and end numbers.
#the following example uses 1 to 5.

     1  2  3  4  5
  ********************
1 |  1  2  3  4  5
2 |  2  4  6  8 10
3 |  3  6  9 12 15
4 |  4  8 12 16 20
5 |  5 10 15 20 25

"""

# Get the starting and ending numbers from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Print the header row for the multiplication table
print("  ", end=" ")
for table in range(start, end+1):
    print(table, end="\t")
print("\n")

# Print a line of asterisks to separate the header row from the table
print('*'*20)

# Loop over each number in the range and print its multiplication table
for table in range(start, end+1):
    # Print the number followed by a vertical bar to start a new row
    print(table, end="\t")
    # Loop over each count in the range and print the product of the two numbers
    for count in range(start, end+1):
        print(table*count, end="\t")
    # Move to the next line after printing all products for a given number
    print("\n")
