import DB

class Menu :
    def __init__(self) -> None:
        pass

    def Select(BookLists):
        print("1. 도서 추가")
        print("2. 도서 검색")
        print("3. 도서 정보 수정")
        print("4. 도서 삭제")
        print("5. 현재 총 도서 목록 출력")
        print("6. 저장")
        print("7. 프로그램 종료\n")
        
        num = int(input("Select a menu : "))
        if num == 1 :
            Book_def.book_append()
        elif num == 2 : 
            Book_def.book_search()
        elif num == 3 : 
            Book_def.book_rewrite()
        elif num == 4 : 
            Book_def.book_del()
        elif num == 5 : 
            Book_def.book_print()
        elif num == 6 : 
            Book_def.book_save()
        elif num == 7 : 
            Book_def.book_save()
            exit()
        else : print("Wrong Number!")

class Book_def : #도서 관리 클래스
    def __init__(self) -> None:
        pass

    def book_append(): #도서 추가 메소드
        a = str(input(" 도서명 저자 출판연도 출판사명 장르 양식으로 입력하세요.\n"))
        DB.BookLists.append(a)

    def book_search() : #도서 검색 메소드
        inum = int(input("1. 도서명\n2. 저자\n3. 출판연도\n4. 장르\n"))
        searchString = str(input("검색어를 입력하세요.\n"))
        for i in DB.BookLists:
            booklist = i.split()
            for number in range(len(i.split())):
                if (number+1) % inum == 0 :
                    if booklist[number] == searchString :
                        print(i)

    def book_rewrite() :
        ListIndex = int(input("목록의 수정할 도서 번호를 입력하세요 : "))
        print(DB.BookLists[ListIndex-1])
        a = str(input(" 도서명 저자 출판연도 출판사명 장르 양식으로 입력하세요. \n"))
        del DB.BookLists[ListIndex-1]
        DB.BookLists.insert(ListIndex-1, a)

    def book_del() :
        ListIndex = int(input("목록에서 다음 순서의 도서를 제거 : "))
        del DB.BookLists[ListIndex-1]

    def book_print() :
        inx = 1
        for i in DB.BookLists:
            print(inx,".",i,"\n")
            inx+=1

    def book_save() :
        with open('input.txt','wt') as f:
            for i in DB.BookLists :
                f.writelines(i)
                f.write("\n")

while 1 :
    print("Book Management System.\n")
    Menu.Select(DB.BookLists)