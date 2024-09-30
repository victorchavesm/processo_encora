def make_change(n):
    # Create a list to store the unique combinations
    result = []

    # Iterate over the number of quarters
    for quarters in range(n // 25 + 1):
        remaining_after_quarters = n - quarters * 25
        # Iterate over the number of dimes
        for dimes in range(remaining_after_quarters // 10 + 1):
            remaining_after_dimes = remaining_after_quarters - dimes * 10
            # Iterate over the number of nickels
            for nickels in range(remaining_after_dimes // 5 + 1):
                remaining_after_nickels = remaining_after_dimes - nickels * 5
                # The remaining amount is the number of pennies
                pennies = remaining_after_nickels

                # Add the combination to the list
                result.append([quarters, dimes, nickels, pennies])

    # Print the results
    for combination in result:
        print(combination)


# Test with different values of n
n = 12
make_change(n)
