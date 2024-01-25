import sys
sys.stdin = open('input.txt', 'r')

import sys

Ausar, Auset, Heru = map(int, sys.stdin.readline().split())

while Ausar != 0 and Auset != 0 and Heru != 0 :
    Ausar **= 2
    Auset **= 2
    Heru **= 2
    triangle_test = [Ausar, Auset, Heru]
    triangle_test.sort()
    if triangle_test[-1] == triangle_test[0] + triangle_test[1] :
        print('right')
    else : 
        print('wrong')
    Ausar, Auset, Heru = map(int, sys.stdin.readline().split())