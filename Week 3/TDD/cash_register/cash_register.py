def change(amount_due, amount_paid):
    cash = ['R200', 'R100', 'R50', 'R20', 'R10', 'R5', 'R2', 'R1', '50c', '20c', '10c', '5c']

    if amount_due > amount_paid: return 'Insufficient funds'

    change_is = amount_due - amount_paid

    # Find a combination of cash denominations
    combination = find_combination(cash, change_is)

    return combination

def find_combination(cash, change_is):
    values = [int(value[1:]) * 100 if 'c' not in value else int(value[:-1]) for value in cash]
    combination = []

    # Sort in descending order (highest denomination first)
    sort_list = sorted(values, reverse=True)

    for value in sort_list:
        # Use the current denomination as many times as possible
        while change_is >= value:
            change_is -= value
            # Find the corresponding denomination in the cash list
            corresponding_denotation = cash[values.index(value)]
            combination.append(corresponding_denotation)

    
    result = {}
    
    # Count occurrences of each denomination and store them in a dictionary
    for money in combination:
        if money in result:
            result[money] += 1
        else:
            result[money] = 1

    return 'There is no change' if len(result) == 0 else result

