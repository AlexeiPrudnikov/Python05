import random
allCandies = 2021
minStep = 1
maxStep = 28
def GetStep (i, allCandies):
    while (True):
        step = int(input(f'{i + 1}-й игрок введите количество конфет, которое Вы берете:'))
        if (step < minStep) or (step > maxStep) or (step > allCandies):
            print(f'Ошибка ввода, можно взять от {minStep} до {maxStep} и меньше либо равно {allCandies} конфет.')
        else:
            return step
print('Происходит жеребьевка...')
first = random.randint(1, 2)
flag = bool(first - 1)
print(f'Ходит первым {first}-й игрок')
print(f'Осталось {allCandies} конфет')
while allCandies > 0:
    step = GetStep(int(flag), allCandies)
    allCandies -= step
    print(f'Осталось {allCandies} конфет')
    if allCandies == 0:
        print(f'{int(flag) + 1}-й игрок победил!')
    flag = not flag
