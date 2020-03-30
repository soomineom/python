coffee = 0

def coffee_machine(button):
    print()
    print('#1.자동/ 뜨거운 물 준비');
    print('#2.자동/ 종이컵 준비');

    if button == 1:
        print('#3.보통커피')
    elif button == 2:
        print('#3.설탕커피')
    elif button == 3:
        print('#3.블랙커피')
    else:
        print('#3.아무거나')

    print('#4.물');
    print('#5.스푼');
    print()

coffee = int(input('A손님 -> 1.보통/ 2.설탕 / 3.블랙: '))
coffee_machine(coffee)
print('커피~~\n')

coffee = int(input('B손님 -> 1.보통/ 2.설탕 / 3.블랙: '))
coffee_machine(coffee)
print('커피~~\n')

coffee = int(input('C손님 -> 1.보통/ 2.설탕 / 3.블랙: '))
coffee_machine(coffee)
print('커피~~\n')