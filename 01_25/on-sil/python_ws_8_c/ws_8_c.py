class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1
    
    def save(self):
        print('데이터를 저장합니다.')

class Novel(BaseModel):
    def __init__(self, data_type, title, content, created_at, updated_at, author):
        super().__init__(data_type, title, content, created_at, updated_at)
        self.author = author
    
class Other(BaseModel):
    TYPE = 'Other Model'

    def save(self):
        print('데이터를 다른 장소에 저장합니다.')

class ExtendedModel(Novel, Other):

    def __init__(self, data_type, title, content, created_at, updated_at, author):
        super().__init__(data_type, title, content, created_at, updated_at, author)
        self.extended_type = 'Extended Model'

    def display_info(self) :
        print(self.PK)
        print(super().PK) #, super().TYPE, self.extended_type, sep='\n')

    def save(self) :
        print('데이터를 확장해서 저장합니다.')

extended_instance = ExtendedModel('앨범', '앨범명', '앨범 설명', 2021, 2023, 'Silica Gel')
print('Extended 모델 인스턴스의 PK, TYPE, extended_type 그리고 save 메서드')
extended_instance.display_info()


# hong = Novel('소설', '홍길동', '고전 소설', 1618, 1692, '허균')
# chun = Novel('소설', '춘향전', '고전 소설', 'unknown', 'unknown', '작자미상')
# print('Novel 모델 인스턴스의 PK와 save 메서드')
# print(hong.PK)
# print(chun.PK)
# hong.save()
# chun.save()
# print(hong.author)
# print(chun.author)
# print('---')

# company = Other('회사', '회사명', '회사 설명', 2000, 2023)
# print('Other 모델 인스턴스의 PK와 save 메서드')
# print(company.PK)
# company.save()
# print('---')

# print('모델 별 타입')
# print(Novel.TYPE)
# print(Other.TYPE)
# print('---')

extended_instance = ExtendedModel('앨범', '앨범명', '앨범 설명', 2021, 2023, 'Silica Gel')
print('Extended 모델 인스턴스의 PK, TYPE, extended_type 그리고 save 메서드')
extended_instance.display_info()
# extended_instance.save()
