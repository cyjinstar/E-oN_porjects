from posixpath import split
import DB
import time

#마지막주차_기차표예매_프로그램

class Menu : #메뉴 클래스
    def __init__(self) -> None:
        pass

    def Select(TrainList) :
        print("1. 빠른시간 기차 검색 및 예매")
        print("2. 전체 기차 시간표 출력")
        print("3. 나의 예매")
        print("4. 프로그램 종료\n")
        
        inum = input("목록에서 수행할 기능을 입력하세요. : ")
        num = int(inum)
        if num == 1 :
            print(Train_def.Train_search(TrainList))
        elif num == 2 : 
            Train_def.Train_print(TrainList)
        elif num == 3 : 
            Train_def.Train_book()
        elif num == 4 : 
            Train_def.Train_save()
            exit()
        else : print("\n잘못된 명령입니다.\n")
        Menu.Select(DB.TrainList)

class Train_def : #
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
            searchKey = (input("시간(00:00) 출발역 도착역 열차 종류를 입력해주세요")).split()
            s = searchKey[0].replace(":","").lstrip("0")
            searchlist = []
            searchlist.clear()
            cnt = 0
            for i in Tlist:
                splitList = i.split()
                if splitList[1] == searchKey[1] and splitList[3] == searchKey[2] :
                    if splitList[4] == searchKey[3] : 
                        for number in range(len(i.split())):
                            if number == 0 :
                                sn = splitList[number].replace(":","").lstrip("0")
                                if int(sn) >= int(s) and int(splitList[5]) != 0:
                                    searchlist.append(' '.join(splitList))
                                    print(i)
            cnt = Tlist.index(searchlist[0])
            print(cnt, searchlist[0])
            return int(cnt)

        except IndexError :
            print("잘못된 양식입니다!")
            time.sleep(1)
            Menu.Select(DB.TrainList)
    
    def Train_book() :
        reservation = int(input("위 열차로 예매하시겠습니까? yes = 1 no = 0\n"))
        if reservation :
            pass

    def Train_save() : 
        with open('TrainList.txt','wt') as f:
            f.writelines("시간_출발_도착_열차종류_잔여좌석수\n")
            for i in DB.TrainList :
                f.writelines(i)
                f.write("\n")


try : Menu.Select(DB.TrainList)

except : 
    print("\n잘못된 양식입니다. 올바른 값을 선택해주십쇼.\n")
    Menu.Select(DB.TrainList)