def make_change(n):
    """
    The function below will generate all unique combinations of coins (quarters, dimes, nickels, and pennies) 
    that sum up to the given amount n.
    - Obtain the input n, which is the total amount in cents.
    - Iterate over the possible number of quarters (25 cents each).
    - For each number of quarters, iterate over the possible number of dimes (10 cents each).
    - For each number of dimes, iterate over the possible number of nickels (5 cents each).
    - Calculate the remaining amount as pennies (1 cent each).
    - Store each unique combination of coins in a list.
    - Print each combination.
    """

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
