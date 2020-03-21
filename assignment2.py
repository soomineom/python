while (True): ##계속 반복해서 실행됨
    print('============')
    print('자판기')

    money = int(input('돈을 넣어주세요. (예: 1000) : ')) ##넣을 돈을 입력받음
    ##int변환으로 문자열에서 10진수로 변환
    juice = ['1.포도 쥬스: 100원', '2.오렌지 쥬스: 200원', '3.환타 쥬스: 300원'] ##쥬스 리스트를 정의한다

    print('----------')
    for i in range (0,3,1): ##for문 이용해서 3개의 항목 출력 반복
        print(juice[i]) ##juice 리스트를 출력한다
    print('----------')

    choice = int(input('음료를 골라 주세요 (1~3번 중 선택) : ')) ##음료를 선택/입력 받는다
    amount = int(input('몇 개를 원하시나요? (예: 1) :')) ##음료 수량을 입력 받는다

    if (choice == 1): ##1번을 선택 했을 때 실행
        price = 100
        change = money - (price * amount) ##거스름돈은 처음에 입력 받은 돈에서 (주스 가격 * 수량)을 뺀 것
        print('포도 쥬스 100원, 거스름돈 %d원 입니다' %change)
    elif (choice == 2): ##2번을 선택 했을 때 실행
        price = 200
        change = money - (price * amount)
        print('오렌지 쥬스 200원, 거스름돈 %d원 입니다' %change)
    elif (choice == 3): ##3번 선택 시 실행
        price = 300
        change = money - (price * amount)
        print('환타 쥬스 300원, 거스름돈 %d원 입니다' %change)