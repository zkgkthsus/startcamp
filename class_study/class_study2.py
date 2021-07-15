def create(name,age):               #매개변수에 인자를 전달받아 딕셔너리 객체를 생성 및 반환하는 함수
    return {"name":name,"age":age}  #멤버 정보 생성이 필요할 때마다 호출하여 사용

def to_str(person):                                   #인자로 전달 받은 딕셔너리 객체의 값을 문자열로 반환하는 함수
    return "{0}\t{1}".format(person["name"],person["age"]) 

members = [
    create("홍길동","20"), #name과 age를 키로 하는 딕셔너리
    create("이순신","45"),  #객체 3개 생성 및 members 리스트 객체의 항목으로 구성
    create("강감찬","35")
]
for member in members:
    print(to_str(member))