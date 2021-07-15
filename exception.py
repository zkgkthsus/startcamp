data_list = list(range(1,10)) # 1에서 10까지의 범위 리스트로 저장

print("data_list: {0}".format(data_list))# data_list 출력확인

try:
    num = int(input("인덱스로 사용할 숫자를 입력하세요")) # 인자값 입력
    print("[{0}]:{1}".format(num,data_list[num])) #인자값 및 인자값 대입후 출력
except IndexError as exception: # IndexError 발생시 캐치하여 exception에 저장
    print(exception)  #
except ValueError as exception: # ValueError 발생시 캐치하여 exception에 저장
    print(exception)  #
except Exception as exception: # Exception 발생시 캐치하여 exception에 저장
    print(exception)  #          