""" Задача #1: множественная форма числительных
Одна из самых популярных задач при разработке программных продуктов с интерфейсом на русском языке - это согласование числительных множественного числа: 1 студент, 2 студента, 3 студента, 11 студентов т.д. Выводить информацию вида “На курс зачислено 11 студент” - выглядит совсем не красиво.

Твоя задача написать функцию plural_form согласования окончаний существительных в зависимости от переданного числа. Функция должна принимать 4 параметра:

число
форма слова 1
форма слова 2
форма слова 3
Функция должна возвращать строку вида {число} {нужная форма}. Например, 

plural_form(1, ‘яблоко’, ‘яблока’, ‘яблок’) - 1 яблоко
plural_form(2, ‘яблоко’, ‘яблока’, ‘яблок’) - 2 яблока
plural_form(11, ‘студент’, ‘студента’, ‘студентов’) - 11 студентов
plural_form(15, ‘студент’, ‘студента’, ‘студентов’) - 15 студентов
plural_form(3, ‘студент’, ‘студента’, ‘студентов’) - 3 студента """

# Задача #1


def plural_form(number, form_1, form_2, form_3):
    """ Согласование окончаний  числительный множественного числа. 
    :param number: кол-во объектов
    :param form_1: форма единственного числа
    :param form_2: форма множественного числа до 4 объектов
    :param form_3: форма множественного числа от 5 объектов
    """

    if int(str(number)[-1]) <= 0 or int(str(number)[-1]) >= 5:
        nessesary_form = form_3
    elif int(str(number)[-1]) > 0 and int(str(number)[-1]) <= 1:
        nessesary_form = form_1
    else:
        int(str(number)[-1]) > 1 and int(str(number)[-1]) <= 4
        nessesary_form = form_2
    return(f'{number} { nessesary_form}')


# Тест функции 1
print(plural_form(50555, 'яблоко', 'яблока', 'яблок'))
# Тест функции 2
print(plural_form(50555, 'Студент', 'Студента', 'Студентов'))


""" Задача #2: FizzBuzz
Еще одна популярная задача - FizzBuzz: если число делится на 3, то нужно вывести Fizz, если на 5, то Buzz, если на 3 и на 5, то FizzBuzz.
Задача - написать программу, которая выводит сумму чисел из диапазона от 1000 до 20000 включительно, которые делятся и на 3 и на 5. """


def check_divisuion(min, max):
    """ Проверка деления чисел на 3 и 5 и суммирование числового ряда 
    :param min: нижняя граница диапазона
    :param max: верхняя граница диапазона
    """
    members_sum = 0
    new_list = []  # лист в который сохраняются числа которые делятся 3 и на 5
    for el in range(min, max + 1):
        if (el % 3 == 0) and (el % 5 == 0):
            new_list.append(el)
    for members in new_list:
        members_sum += members
    return(members_sum)


print(check_divisuion(1000, 20000))

# Второе задание сделал в двух версиях потому, что вывод FizzBuzz, Buzz, Fizz  на больших диапазонах
# занимает слишком много места.


def check_divisuion_v2(min, max):
    """ Проверка деления чисел на 3 и 5 и суммирование числового ряда
    и вывод призанака при делении на 3  Fizz, на 5 Buzz и на 3 и 5 FizzBuzz
    :param min: нижняя граница диапазона
    :param max: верхняя граница диапазона
    """
    members_sum = 0
    new_list = []
    for el in range(min, max + 1):
        if (el % 3 == 0) and (el % 5 == 0):
            print(f'{el} = FizzBizz')
            new_list.append(el)
        elif (el % 3 == 0):
            print(f'{el} = Fizz')
        elif (el % 5 == 0):
            print(f'{el} = Bizz')
        else:
            el
    for members in new_list:
        members_sum += members
    return(members_sum)

# Тест вывода работы функции
print(check_divisuion_v2(1, 50))

""" Задача #3: Последовательность Фибоначчи
Последовательность Фибоначчи - это числовой ряд в котором каждое следующее число равно сумме двух предыдущих.
Например, последовательность для первых 10 чисел, начиная с 1 выглядит так :1, 1, 2, 3, 5, 8, 13, 21, 34, 55 """

def fibonacci_sequence(zero_step, first_step, border):
    """ Определение последовательности Фибоначчи 
    с определенного элемента

    :param zero_step: начальный элемент последовательности
    :param first_step: следующий элемент последовательности
    :param border: граница проверяемых элементов
    """
    next_step = 0
    list_value = [zero_step, first_step]
    while next_step < border:
        next_step = zero_step + first_step
        zero_step = first_step
        first_step = next_step
        if next_step < border:
            list_value.append(next_step)
    return(list_value)

# Создаем новый лист и передаем в него результат функции
new_list = fibonacci_sequence(1, 1, 10000000)
print(new_list)
# Лист для четных элементов последовательности
even_list = [] 
for new_list_el in new_list:
    if new_list_el % 2 == 0: # проверка  элементов на четность
        even_list.append(new_list_el)
    
#Вывод результатов для теста 
print(len(new_list)) # Количество элементов в последовательности;
print(sum(even_list)) # Сумму всех четных элементов;
print(even_list) # Все четные элементы
print(len(even_list)) # Количество четных элементов в последовательности
print(new_list[-2]) # Предпоследнее число последовательности
