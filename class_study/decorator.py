class Person:
    def __init__(self,name,age) : 
        self.__name = name           
        self.__age = age            
        print("{0} 객체가 생성되었습니다.".format(self.__name))

    def __del__(self):            
        print("{0} 객체가 제거되었습니다.".format(self.__name))

    def to_str(self):             
        return "{0}\t{1}".format(self.__name,self.__age)

    @property
    def name(self):                      #변수처럼 사용 가능 #__name필드의 필드값을 반환하는 getter역할 
        return self.__name

    @property
    def age(self):                       #변수처럼 사용 가능 #__age필드의 필드값을 반환하는 getter역할 
        return self.__age 

    @age.setter                          #변수처럼 사용 가능 #__age필드의 필드값을 반환하는 setter역할
    def age(self,age):
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age 

members = [
    Person("홍길동","20"), 
    Person("이순신","45"), 
    Person("강감찬","35")
]                     

members[0].age= 22 #변수처럼 사용하는 예

for member in members:
    print(member.to_str())