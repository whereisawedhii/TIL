class Account :
    count = 0 
    bank = '우리은행' 
    category = '예금/적금'

    def __init__(self, name) :
        self.name = name 
        Account.count += 1
        print(f'안녕하세요 {name} 고객님, {Account.count}번째 가입자입니다.')

    def show_count(self) :
        print(f'가입한 고객은 {self.name}이고, 총 계좌수는 {self.count}입니다.')
    
    @classmethod
    def change_category(cls, name) : 
        cls.category = '대출'

    # @staticmethod : 
    

customer1 = Account('문태성')
# customer2 = Account('갓삼성')
customer3 = Account('배고픈')
customer4 = Account('피곤한')

customer1.show_count()

print(customer1.category)
Account.change_category('대출')
print(customer1.category)

