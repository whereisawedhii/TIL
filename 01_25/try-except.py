# # ZeroDivisionError
# try : 
#     result = 10 / 0
# except ZeroDivisionError: 
#     print('0으로 나눌 수 없습니다')

# # NameError
# try : 
#     print(name)
# # 다양한 예외처리 불가 
# except : 
#     print('0으로 나눌 수 없습니다')

# # ValueError
# try : 
#     num = (int(input('숫자입력 :')))
# except ValueError :
#     print('숫자가 아닙니다')

# a : ValueError
# 0 : ZeroDivisionError

try :
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
except BaseException: 
    print('숫자를 넣어')
except ZeroDivisionError: 
    print('0으로 나누기가 될 것 같아?')
except (ValueError, ZeroDivisionError): 
    print('알 수 없는 에러 발생')
