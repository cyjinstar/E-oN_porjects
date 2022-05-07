class Menu :
    def __init__(self) -> None:
        pass

    def Select(Book_DB):
        num = int(input("Select a menu : "))
        if num == 1 :
            Book_def.book_append(Book_DB)
        elif num == 2 : 
            pass
        elif num == 3 : 
            pass
        elif num == 4 : 
            pass
        elif num == 5 : 
            pass
        elif num == 6 : 
            pass
        elif num == 7 : 
            pass
        else : print("Wrong Number!")

class Book_def :
    def __init__(self) -> None:
        pass

    def book_append(inputlist):
        a = str(input(" 도서명 저자 출판연도 출판사명 장르 양식으로 입력하세요. "))
        Book_DB.append(a)

        

class DBIO :
    def __init__(self, listA):
        self.listA = listA

    def DBtoList(listA):
        DBlists = [line.rstrip('\n') for line in listA]
        return DBlists

Book_DB = []
with open('input.txt','rt') as f:
    for line in f:
        print(DBIO.DBtoList(f.readlines()))
        Book_DB = DBIO.DBtoList(f.readlines())

Menu.Select(Book_DB)