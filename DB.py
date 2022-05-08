with open('input.txt','rt') as f: #데이터베이스 파일을 가져오는 모듈
    BookLists = f.readlines()
BookLists = [line.rstrip('\n') for line in BookLists]
