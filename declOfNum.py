def declOfNum(number, titles):
    '''Функция определяет склонение в зависимости от числа.
    На вход принимет два параметра:
    number - само число
    titles - массив из трех элементов
    Пример вызова:
    declOfNum(73, ['год', 'года', 'лет'])
    Возвращает строку
    '''
    cases = [2, 0, 1, 1, 1, 2]
    return titles[2 if number%100>4 and number%100<20 else cases[number%10 if number%10<5 else 5] ]