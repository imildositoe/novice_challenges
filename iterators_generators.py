def sequence_number_generator(low, high):
    while low <= high:
        yield low
        low += 1

def main():
    number_list = []
    for number in sequence_number_generator(0, 5):
        number_list.append(number)
    print(number_list)

if __name__ == '__main__':
    main()