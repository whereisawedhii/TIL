'''
'''
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
dna_arr = []
for _ in range(N):
    dna = input()
    dna_arr.append(dna)

result = 0
for _ in range(N):
    if not dna_arr:
        break
    dna_dict = {}
    for l in range(N):
        case = dna_arr.pop()
        cnt = 0
        covered_list = [case]
        for dna in dna_arr:
            for j in range(M):
                if not (case[j] == dna[j] or case[j] == '.' or dna[j] == '.'):
                    break
            else:
                covered_list.append(dna)
                cnt += 1
        dna_dict[tuple(covered_list)] = cnt
        dna_arr = [case]+dna_arr

    dna_dict_reverse = sorted(dna_dict.items(), reverse=True,key=lambda item: item[1])


    for item in dna_dict_reverse:
        cnt = 0
        for covered in item[0]:
            if covered in dna_arr:
                dna_arr.pop(dna_arr.index(covered))
                cnt += 1
        if cnt:
            result += 1

print(result)