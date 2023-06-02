'''
:default parameters example
'''
def payment_day(working_hours, payment_hour = 25):
    '''
    calculate payment by day
    : param working_hour = amout of working hours
    '''
    return working_hours * payment_hour

def main():
    print("The total payment is: {}".format(payment_day(8)))
    print("The total payment is: " + str(payment_day(8) + 150))

if __name__ == '__main__':
    main()