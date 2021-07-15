import random
menu=['한식','중식','일식']
번호={'한식':"1234-1234",'일식':"3456-3456",'중식':"4567-4567"}
lunch=random.choice(menu)
#print(f"오늘 점심은 {lunch} 전화번호는 {번호[lunch]}")
print("오늘 점심 메뉴는 {0} 이고 전화번호는 {1}입니다.".format(lunch,번호[lunch]))