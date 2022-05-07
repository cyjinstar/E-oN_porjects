import DB

class Menu :
    def __init__(self) -> None:
        pass

    def Select(BookLists):
        num = int(input("Select a menu : "))
        if num == 1 :
            Book_def.book_append()

        elif num == 2 : 
            Book_def.book_search()

        elif num == 3 : 
            pass
        elif num == 4 : 
            pass
        elif num == 5 : 
            pass
        elif num == 6 : 
            pass
        elif num == 7 : 
            exit()
        else : print("Wrong Number!")

class Book_def :
    def __init__(self) -> None:
        pass

    def book_append():
        a = str(input(" 도서명 저자 출판연도 출판사명 장르 양식으로 입력하세요. "))
        DB.BookLists.append(a)

    def book_search() :
        searchString = str(input("Search for : "))
        for i in DB.BookLists:
            if searchString in i.split():
                print(i)


def DBtoList(listA):
    DBlists = [line.rstrip('\n') for line in listA]
    return DBlists

while 1 :
    Menu.Select(DB.BookLists)