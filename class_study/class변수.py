class Person:
    count=0  #클래스 변수 설정

    def __init__(self,name,age) : #객체가 생성될때 마다 호출되는 __init__메서드에 
        self.__name = name           
        self.__age = age
        Person.count += 1         # 좌편의 문장 추가    
        print("{0} 객체가 생성되었습니다.".format(self.__name))

    def __del__(self):            
        print("{0} 객체가 제거되었습니다.".format(self.__name))

    def to_str(self):             
        return "{0}\t{1}".format(self.__name,self.__age)

    @property
    def name(self):                      
        return self.__name

    @property
    def age(self):                       
        return self.__age 

    @age.setter                          
    def age(self,age):
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age     

    @classmethod
    def get_info(cls):             #클래스 참조 정보가 인자로 넘어올 매개변수    
        return "현재 Person클래스의 인스턴스는 총 {0}개 입니다".format(cls.count)
members = [
    Person("홍길동","20"), 
    Person("이순신","45"), 
    Person("강감찬","35")
] 

#print("현재 Person클래스의 인스턴스는 총 {0}개 입니다".format(Person.count))

print(Person.get_info())   #Person 클래스를 통하여 호출