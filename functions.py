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
    input_func()

    bucket = {1: "My", 2: 1, 3: "st favorite language in the world, that's ", 4: True, 5: 0.07}
    multiples_parameters(value = bucket)
    multiples_parameters(first_value = "Pyhon", second_value = 25, third_value = "is", forth_value = True, fifth_value = 0.007, sixty_value = None, seventy_value = 'data visualization')


def multiples_parameters(**kwargs):
    for key, value in kwargs.items():
        if value == None:
            pass
        else:
            print("The {}: {}".format(key, value))
            pass


def input_func():
    value = input("Please input the value")
    if value != None:
        print("The introduced value is: {}".format(value))
        print("The another introduced value is: ", value)


if __name__ == '__main__':
    main()