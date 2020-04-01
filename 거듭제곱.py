def power(x, n): ## power(x의 n승) 이름의 함수 선언
    if n == 0: ## x의 0승일 경우
        return 1 ## 1로 리턴
    return x * power(x, n-1)
    ## 다시 power함수를 호출 (총 n번 호출하는 것이 됨)
    ## 따라서, x를 n회 곱한 값을 최종적으로 리턴

print(power(2,10)) ##2의 10 승 출력