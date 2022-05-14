try:
    with open('TrainList.txt','rt') as f: #데이터베이스 파일을 가져오는 모듈
        TrainList = f.readlines()
    TrainList = [line.rstrip('\n') for line in TrainList]
    del TrainList[0]
except:
    print("TrainList.txt가 없거나 손상되었습니다.")
