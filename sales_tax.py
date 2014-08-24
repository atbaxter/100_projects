item = float(input("What is the cost of the item you are buying? "))
rate = float(input("What is your local tax rate (in percent)? "))

def tax_calculator(item, tax):
    global rate
    rate = rate * 0.01
    tax = (item * rate)
    total = tax + item
    print (tax)
    print (total)

tax_calculator(item, rate)
