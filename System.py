from posixpath import split
import DB

#마지막주차_기차표예매_프로그램

class Menu : #메뉴 클래스
    def __init__(self) -> None:
        pass

    def Select(TrainList) :
        print("1. 빠른시간 기차 검색 및 예매")
        print("2. 전체 기차 시간표 출력")
        print("3. 나의 예매")
        print("4. 프로그램 종료\n")
        
        num = int(input("목록에서 수행할 기능을 입력하세요. : "))
        if num == 1 :
            Train_def.Train_search(TrainList)
        elif num == 2 : 
            Train_def.Train_print(TrainList)
        elif num == 3 : 
            Train_def.Train_book()
        elif num == 4 : 
            Train_def.Train_save()
            exit()
        else : print("\n잘못된 명령입니다.\n")
        Menu.Select(DB.TrainList)

class Train_def : #도서 관리 클래스
    def __init__(self) -> None:
        pass

    def Train_print(Tlist) : #전체 기차표 출력 함수
        inx = 1
        print("\n출발시간,출발지,도착지,열차종류,잔여좌석수")
        for i in Tlist:
            splitList = i.split()
            for number in range(len(i.split())):
                if (number+1) % 5 == 0 :
                    if splitList[number+1] == "0" :
                        splitList[number+1] = "매진"
            print(' '.join(splitList))

    def Train_search(Tlist) :
        try :
            print("열차 검색")
            searchlist = []
            searchKey = (input("시간(00:00) 출발역 도착역 열차 종류를 입력해주세요")).split()
            s = searchKey[0].replace(":","").lstrip("0")
            for i in Tlist:
                splitList = i.split()
                for number in range(len(i.split())):
                    if number == 0 :
                        sn = splitList[number].replace(":","").lstrip("0")
                        if int(sn) >= int(s) :
                            searchlist.append(' '.join(splitList))
                    

        except IndexError :
            print("잘못된 양식입니다!")
            Menu.Select(DB.TrainList)

    
    def Train_book() :
        pass

    def Train_save() : 
        with open('TrainList.txt','wt') as f:
            f.writelines("시간_출발_도착_열차종류_잔여좌석수\n")
            for i in DB.TrainList :
                f.writelines(i)
                f.write("\n")


Menu.Select(DB.TrainList)