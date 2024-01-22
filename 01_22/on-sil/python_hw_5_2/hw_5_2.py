# 아래 함수를 수정하시오.
# a에서 b의 개수를 센다 - str
# 리스트화 + count 
def count_character(a, b):
    char_list = [i for i in a]
    num = char_list.count(b)
    return num

result = count_character("Hello, World!", "o")
print(result)  # 2
