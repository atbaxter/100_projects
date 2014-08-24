import time

try:
    while True:
        def unit_converter(unit,amount):
            if unit == "c":
                amount = (amount * (9 * .2)) + 32
                print ('Converting degrees Celsius to Fahrenheit')
                time.sleep(1)
                print (amount)
            elif unit == "f":
                amount = (amount - 32) * (5/9)
                print ('Converting degrees F to Celsius')
                time.sleep(1)
                print (amount)
            elif unit == 'kg':
                amount *= 2.205
                print ('Converting kg to lbs')
                time.sleep(1)
                print (amount)
            elif unit == 'lb' or unit == 'lbs':
                amount *= 0.453
                print ('Converting lbs to kg')
                time.sleep(1)
                print (amount)
                
            else:
                print('Command not recognized. Available units are lb, kg, C, and F')

        unit = input('Which unit do you want to convert? ').lower()
        amount = float(input('What is the measure of that unit? '))

        unit_converter(unit, amount)

except KeyboardInterrupt:
    pass
