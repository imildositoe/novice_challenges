'''
:default parameters example
'''
def payment_day(working_hours, payment_hour = 25):
    '''
    calculate payment by day
    : param working_hour = amout of working hours
    '''
    global result
    result = working_hours * payment_hour 
    return result

def main():
    print("The total payment is: {}".format(payment_day(8)))
    print("The total payment is: " + str(payment_day(8) + 150))
    lambda_function()

    global bucket
    bucket = {1: "My", 2: 1, 3: "st favorite language, that's ", 4: True, 5: 0.07}
    for key, value in bucket.items():
        print("The array value of {}".format(key) + " is: {}".format(value))

    multiples_parameters(value = bucket)
    print("{}".format("-------------------Separator------------------"))
    multiples_parameters(first_value = "Pyhon", second_value = 25, third_value = "is", forth_value = True, fifth_value = 0.007 * result)

def multiples_parameters(**kwargs):
    for key, value in kwargs.items():
        print("The {}: {}".format(key, value))

def lambda_function():
    multiply = lambda a: a * result
    print ("The result of the lambda function is: {}".format(multiply(8)))

if __name__ == '__main__':
    main()