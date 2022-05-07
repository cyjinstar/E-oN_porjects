import DB

class Menu :
    def __init__(self) -> None:
        pass

    def Select(BookLists):
        print("1. 도서 추가\n")
        print("2. 도서 검색\n")
        print("3. 도서 정보 수정\n")
        print("4. 도서 삭제\n")
        print("5. 현재 총 도서 목록 출력\n")
        print("6. 저장\n")
        print("7. 프로그램 종료\n")
        
        num = int(input("Select a menu : "))
        if num == 1 :
            Book_def.book_append()
        elif num == 2 : 
            Book_def.book_search()
        elif num == 3 : 
            pass
        elif num == 4 : 
            Book_def.book_del()
        elif num == 5 : 
            Book_def.book_print()
        elif num == 6 : 
            pass
        elif num == 7 : 
            exit()
        else : print("Wrong Number!")

class Book_def : #도서 관리 클래스
    def __init__(self) -> None:
        pass

    def book_append(): #도서 추가 메소드
        a = str(input(" 도서명 저자 출판연도 출판사명 장르 양식으로 입력하세요. "))
        DB.BookLists.append(a)

    def book_search() : #도서 검색 메소드
        searchString = str(input("Search for : "))
        for i in DB.BookLists:
            if searchString in i.split():
                print(i)

    def book_del() :
        ListIndex = int(input("목록에서 다음 순서의 도서를 제거 : "))
        del DB.BookLists[ListIndex-1]

    def book_print() :
        for i in DB.BookLists:
            print(i,"\n")

while 1 :
    print("Book Management System.\n")
    Menu.Select(DB.BookLists)