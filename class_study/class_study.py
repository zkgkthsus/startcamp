members = [
    {"name":"홍길동","age":"20"}, #name과 age를 키로 하는 딕셔너리
    {"name":"이순신","age":"45"}, #객체 3개 생성 및 members 리스트 객체의 항목으로 구성
    {"name":"강감찬","age":"35"}
]

for member in members:
   print("{0}\t{1}".format(member["name"],member["age"])) 
#딕셔너리 객체는 한명의 정보만 다룸
#딕셔너리 객체를 모아 리스트를 구성하고 그 리스트를 통해 멤버의 관리를 진행가능   