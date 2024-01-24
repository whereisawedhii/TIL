# 계산기 함수 만들기
# 결과값 
# print(add_cal(3)) # 3
# print(add_cal(4)) # 7

# def add_cal(num) : 
#     result = result + num 
#     return result

# result = add_cal(3)
# print(result)

# UnboundLocalError: local variable 'result' referenced before assignment

# result = 0

# def add_cal1(num) : 
#     global result
#     result = result + num 
#     return result

# print(add_cal1(3)) 
# print(add_cal1(4)) 

# 같은 코드로 100개의 값을 계산해야 한다면 
# 코드도, 글로벌 변수도 100개 써야 함 

# class AddCalculator : 

#     def __init__(self, start) :
#         self.start = start

#     def add(self, num1, num2) :
#         self.num1 = num1
#         self.num2 = num2
#         return self.num1 + self.num2       

# cal_1 = AddCalculator()

# # 방법 1
# print(AddCalculator.add(cal_1, 0, 3))
# # 방법 2 - 이렇게 쓴다 !!!
# print(cal_1.add(0, 3))



class AddCalculator : 

# 인스턴스 선언과 동시에 어떤 값을 전달하고 싶을 때 
    def __init__(self, start) :
        self.start = start # self.start 에 매개변수를 할당해서 바인딩

    def add(self, num1, num2) :
        self.num1 = num1
        self.num2 = num2
        return self.num1 + self.num2     
    
cal_1 = AddCalculator(0) # self.start 에 0을 할당해서 바인딩

print(cal_1.start) # 0