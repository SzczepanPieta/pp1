with open("07-FileHandling/random.txt", 'r') as fp:
    print("File name: random.txt")
    lines = len(fp.readlines())
    print('Number of lines:', lines)

fp.close()