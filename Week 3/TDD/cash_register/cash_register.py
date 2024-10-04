def change(amount_due, amount_paid):
    cash = ['R200', 'R100', 'R50', 'R20', 'R10', 'R5', 'R2', 'R1', '50c', '20c', '10c', '5c']

    if amount_paid < amount_due: return 'Insufficient fund' 

    change_is = amount_due - amount_paid
