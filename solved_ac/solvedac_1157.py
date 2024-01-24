# import sys
# sys.stdin = open('input.txt', 'r')

import sys
word = sys.stdin.readline().upper()
length = len(word)

if length == 1 :
    print(word)
    exit()

char_list = [each for each in word]
count_list = [word.count(each) for each in word]
max_num = max(count_list)
print(max_num)

best_list = [word[i] for i in range(length) if count_list[i] == max_num]
best_set = set(best_list)
best_list = list(best_set)

final_count = len(best_list)
if final_count == 1 :
    print(best_list[0])
elif final_count > 1 :
    print('?')