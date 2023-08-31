"""
######## Problem  3 ###############
#Print Chess board (alternate black and white squares)
#print('\u25A0') - will print white Square. You can use "B" to print black squares
"""

# Looping over the rows of the chessboard
for row in range(0,8):
    # Looping over the columns of the chessboard
    for column in range(0,8):
        # Checking if the sum of the row and column is even or odd
        if (row + column) % 2 == 0:
            # Printing a black square if the sum is even
            print('\u25A0', end=" ")
        else:
            # Printing a white square if the sum is odd
            print('\u25A1', end=" ")
    # Move to the next line after printing all columns in a row
    print()
