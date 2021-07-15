class Person:
    def __init__(self,name,age) : # self는 객체공간의 참조 전달 
        self.name = name          # name과 age 매개변수를 이용해 self가 가르키는 객체공간에 name,age필드를 생성
        self.age = age            # 3,4는 캡슐화 된 필드가 필요할 수 있음 => 입력 시 유효성 검사를 할 수 없으므로 잘못된 값이 저장될 수 있음
        print("{0} 객체가 생성되었습니다.".format(self.name))

    def __del__(self):            # self는 객체공간의 참조 전달
        print("{0} 객체가 제거되었습니다.".format(self.name))

    def to_str(self):             #name 필드와 age필드를 문자열로 반환
        return "{0}\t{1}".format(self.name,self.age)

members = [
    Person("홍길동","20"), #name과 age를 키로 하는 딕셔너리
    Person("이순신","45"),  #객체 3개 생성 및 members 리스트 객체의 항목으로 구성
    Person("강감찬","35")
]        

for member in members:
    print(member.to_str()) # Person.to_str():member객체의 to_str메서드를 호출해 반환된 문자값을 출력
#member = Person("홍길동",20)

#print("{0}\t{1}".format(member.name,member.age))

#print(dir(member))