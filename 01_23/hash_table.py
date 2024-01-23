# 정수 값 자체가 곧 해시 값
# 해시 테이블에 저장된, 나열된 순서로 pop 
# pop 해시 테이블에서 먼저 있는 값부터 출력
my_set = {3, 2, 1, 9, 100, 4, 87, 39, 10, 52}

print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set)

# 1
# 2
# 3
# 100
# 4
# 39
# 9
# 10
# 52
# 87
# set()



print(hash(1)) # 1
print(hash(1)) # 1
print(hash('a')) # 실행시마다 다름
print(hash('a')) # 실행시마다 다름