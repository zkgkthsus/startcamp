class Person:
    def __init__(self,name,age) : # self는 객체공간의 참조 전달 
        self.__name = name          #__를 통해 프라이빗 필드로 설정 
        self.__age = age            # 3,4는 캡슐화 된 필드가 필요할 수 있음 => 입력 시 유효성 검사를 할 수 없으므로 잘못된 값이 저장될 수 있음
        print("{0} 객체가 생성되었습니다.".format(self.__name))

    def __del__(self):            # self는 객체공간의 참조 전달
        print("{0} 객체가 제거되었습니다.".format(self.__name))

    def to_str(self):             #name 필드와 age필드를 문자열로 반환
        return "{0}\t{1}".format(self.__name,self.__age)

    def get_name(self):             #__name필드의 값을 반환하는 getter메서드
        return self.__name          #__name필드에 대해서는 getter메서드만 제공

    def get_age(self):
        return self.__age           #__age필드의 값을 반환하는 getter메서드 

    def set_age(self,age):
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age  

members = [
    Person("홍길동","20"), 
    Person("이순신","45"), 
    Person("강감찬","35")
]                     

members[0].set_age(-20)  # line 20이 정상 작동하는 지 확인하기 위한 문장

for member in members:
    print(member.to_str())

    #결과 값에 Traceback (most recent call last):
 # File "c:\Users\wnehd\OneDrive\바탕 화면\python\class_study5.py", line 30, in <module>
 #   members[0].set_age(-20)  # line 20이 정상 작동하는 지 확인하기 위한 문장
 # File "c:\Users\wnehd\OneDrive\바탕 화면\python\class_study5.py", line 21, in set_age
 #   raise TypeError("나이는 0이상의 값만 허용합니다.")
 #라고 에러 메세지가 뜨지만 현 진행상황에서는 정상작동 범주 안임