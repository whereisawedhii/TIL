# with open("./input.txt", "r") as file:
#     input_data = file.read().splitlines()

# num = int(input_data[0])

# for i in range(num) :
#     a, b = map(int, input_data[i+1].split())
#     result = a + b
#     print(result)

num = int(input())

for i in range(num) : 
    a, b = map(int,input().split())
    result = a + b
    print(result)