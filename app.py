def main():
    text = "Python language"
    print(len(text))

    concatenated = text.join(("is the best language", "in the world"))
    concatenated = text + " is not going to die soon"
    concatenated = concatenated[6:len(concatenated)]
    concatenated = concatenated[4:]
    concatenated = concatenated[:-4]
    count = concatenated.count("o")
    is_in = "not" in concatenated
    
    print(concatenated)
    print(count)
    print(is_in)

if __name__ == '__main__':
    main()