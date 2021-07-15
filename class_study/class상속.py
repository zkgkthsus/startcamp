class Parent:
    
    def __init__(self,family_name) :  
        self.__family_name = family_name          
        print("Parent 클래스의 __init__()...")

    @property
    def family_name(self):
        return self.__family_name   

class Child(Parent):      #Parent클래스 상속 
    
    def __init__(self,first_name,last_name) :  
        Parent.__init__(self,last_name)         #부모클래스의 __family_name 필드를 매개변수 last_name으로 초기화
        #super().__init()(last_name)    #부모클래스를 불러오는 super()호출과 생성자메서드(__init__())호출을 사용하면 위(line14)와 동일한 효과 발생
        self.__first_name = first_name         #매개변수 first_name에 의해 초기화됨
        print("Child 클래스의 __init__()...")

    @property
    def first_name(self):
        return self.__first_name   

    @first_name.setter
    def first_name(self,first_name):
        self.__first_name = first_name

    @property
    def name(self):  #name은 Parent클래스의 family_name속성의 반환 값과 Child 클래스의 first_name 속성의 반환값을 문자열로 만들어 반환
        return "{0} {1}".format(self.family_name,self.first_name)    

child=Child("길동","홍")

print(child.family_name)  #홍 출력
print(child.first_name)   # 길동 출력
print(child.name)         #홍 길동 출력
print("=======>")
child.first_name="길순"
print(child.name)         #홍 길순 출력


           