class Person:
    count=0  

    def __init__(self,name,age) :  
        self.__name = name           
        self.__age = age
        Person.count += 1         
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
    def get_info(cls):                
        return "현재 Person클래스의 인스턴스는 총 {0}개 입니다".format(cls.count)

    def __gt__(self,other):  #greater than 연산자
        return self.__age > other.__age               #self의 __age필드가 other의 __age필드 보다 크면 True 반환

    def __ge__(self,other):
        return self.__age >= other.__age               #self의 __age필드가 other의 __age필드 보다 크거나 같은면 True 반환 

    def __lt__(self,other):
        return self.__age < other.__age               #self의 __age필드가 other의 __age필드 보다 작으면 True 반환            
        
    def __le__(self,other):
        return self.__age <= other.__age               #self의 __age필드가 other의 __age필드 보다 작거나 같은면 True 반환
        
    def __eq__(self,other):
        return self.__age == other.__age               #self의 __age필드가 other의 __age필드와 같으면 True 반환

    def __ne__(self,other):
        return self.__age != other.__age               #self의 __age필드가 other의 __age필드와 다르면  True 반환    

members = [
    Person("홍길동","20"), 
    Person("이순신","45"), 
    Person("강감찬","35")
] 

cnt=len(members)
i=0
while True:
    print("member[{0}] > member[{1}] =>{2}".format(i,i+1,members[i]>members[i+1]))  #members[i]>members[i+1]는 
    i+=1                                                                            #def __gt__(self,other):
    if i == cnt - 1:                                                                  #return self.__age > other.__age 메서드를 호출 
        print("member[{0}] > member[{1}] =>{2}".format(i,i+1,members[i]>members[0]))  #위 __gt__ 의 return과 동일한 구성을 사용했기에 호출됨
        break