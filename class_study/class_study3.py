class Person: #클래스 정의
    pass


member= Person() #멤버 객체 생성 #클래스 이름과 동일한 person()을 생성자 메서드라 부름

if isinstance(member,Person): #첫번째 인자가 두번째 인자의 인스턴스인지 확인하는 조건문
    print("member는 Person의 인스턴스 입니다")