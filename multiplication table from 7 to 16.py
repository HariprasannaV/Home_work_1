"""
######## Problem  2 ###############
#Print multiplication tables from 7 to 16, each number up to 12 rows.
"""

# Loop over each table in the range 7 to 16
for tables in range(7, 17):
    # Print the header for the current table
    print(f'Table {tables}')
    # Loop over each count in the range 1 to 12
    for count in range(1, 13):
        # Print the multiplication expression and result for the current count and table
        print(f'{count} * {tables} = {count*tables}')
    # Print a blank line after each table
    print()

# Print a message indicating that all tables have been printed
print("End of Tables")
