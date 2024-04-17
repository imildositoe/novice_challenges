from itertools import count

def sequence_number_generator(low, high):
    while low <= high:
        yield low
        low += 1

def main():
    number_list = []
    for number in sequence_number_generator(0, 10):
        number_list.append(number)
        
    print(number_list)


    sequence = count(start = 2.5, step = 0.5)
    while (next(sequence) <= 8):
        print(next(sequence))
        
        if (sequence == 7):
            print('Breaking...')
            break


if __name__ == '__main__':
    main()
