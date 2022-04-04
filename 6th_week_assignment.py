import math

def calcpiece(a, b):
    answer = math.factorial(a+b)/(math.factorial(a)*math.factorial(b))
    int(answer)
    return answer

piece = input("How many pieces? :")
p = int(piece)
a = b = total = answer = 0 # a는 1조각짜리, b는 2조각 짜리

while 1 :
    a = p-(2*b)
    if (a < 0) :
        break
    answer = calcpiece(a,b)
    total += answer
    b += 1

print("Can be devided in {}" .format(int(total)))