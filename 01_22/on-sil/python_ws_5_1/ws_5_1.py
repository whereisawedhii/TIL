# 아래 함수를 수정하시오.
def reverse_string(a):
    b = reversed(a)
    output = ''.join(b)
    return output

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
