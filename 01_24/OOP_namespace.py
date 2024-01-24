class Person :
    name = 'unknown'

    # 인스턴스 변수 name 을 print 함
    def talk(self) : 
        print(self.name)

p1 = Person()
p1.talk() # 인스턴스에 name이 없음 - 클래스에서 찾아 unknown 출력 

p2 = Person()
p2.name = 'kim' # 인스턴스 변수 name 할당
p2.talk() # kim 출력 

print(Person.name) # unknown
print(p1.name) # unknown
print(p2.name) # kim

p2.ssafy = 11 
print(p2.ssafy) # 11
