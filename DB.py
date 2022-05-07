with open('input.txt','rt') as f:
    BookLists = f.readlines()

BookLists = [line.rstrip('\n') for line in BookLists]
