"""
Напишите функцию, которая будет возвращать переданное в качестве параметра n число словами

Input -> 435467
Output -> четыреста тридцать пять тысяч четыреста шестьдесят семь
"""

def user_input(message, min_elem, max_elem):
    input_error: bool = True
    while input_error:
        try:
            number = int(input(message))
        except:
            print("Вы ввели не число!")
        else:
            if min_elem <= number <= max_elem:
                input_error = False
            else:
                print("Вы ввели число, не соответствующее условию!")
    return number

def number_by_words(input_number):
    number_of_digits = len(str(input_number))
    result_list = []
    dictinory_simbols = {'1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь',
                        '9':'девять','10':'десять','11':'одиннадцать','12':'двенадцать','13':'тринадцать',
                        '14':'четырнадцать','15':'пятнадцать','16':'шестнадцать','17':'семнадцать',
                        '18':'восемнадцать','19':'девятнадцать','20':'двадцать','30':'тридцать','40':'сорок',
                        '50':'пятьдесят','60':'шестьдесят','70':'семьдесят','80':'восемьдесят','90':'девяносто',
                        '100':'сто','200':'двести','300':'триста','400':'четыреста','500':'пятьсот','600':'шестьсот',
                        '700':'семьсот','800':'восемьсот','900':'девятьсот','1000':'тысяча','1000000':'миллиона'}
    list_number = [str(input_number)[i] for i in range(number_of_digits)]
    list_number.reverse()
    #print(list_number)
    for i in range(number_of_digits):
        list_number[i] = int(list_number[i])
    
    for i in range(number_of_digits):
        if i == 0 and number_of_digits > 1:
            
            # если число от 10 до 10
            if list_number[i + 1] == 1:
                if list_number[0] == 0: result_list.insert(0,dictinory_simbols['10'])
                if list_number[0] == 1: result_list.insert(0,dictinory_simbols['11'])
                if list_number[0] == 2: result_list.insert(0,dictinory_simbols['12'])
                if list_number[0] == 3: result_list.insert(0,dictinory_simbols['13'])
                if list_number[0] == 4: result_list.insert(0,dictinory_simbols['14'])
                if list_number[0] == 5: result_list.insert(0,dictinory_simbols['15'])
                if list_number[0] == 6: result_list.insert(0,dictinory_simbols['16'])
                if list_number[0] == 7: result_list.insert(0,dictinory_simbols['17'])
                if list_number[0] == 8: result_list.insert(0,dictinory_simbols['18'])
                if list_number[0] == 9: result_list.insert(0,dictinory_simbols['19'])
            else:
                if list_number[0] == 1: result_list.insert(0,dictinory_simbols['1'])
                if list_number[0] == 2: result_list.insert(0,dictinory_simbols['2'])
                if list_number[0] == 3: result_list.insert(0,dictinory_simbols['3'])
                if list_number[0] == 4: result_list.insert(0,dictinory_simbols['4'])
                if list_number[0] == 5: result_list.insert(0,dictinory_simbols['5'])
                if list_number[0] == 6: result_list.insert(0,dictinory_simbols['6'])
                if list_number[0] == 7: result_list.insert(0,dictinory_simbols['7'])
                if list_number[0] == 8: result_list.insert(0,dictinory_simbols['8'])
                if list_number[0] == 9: result_list.insert(0,dictinory_simbols['9'])
        
        # Если число от 1 до 9
        elif i == 0 and number_of_digits == 1:
            if list_number[0] == 1: result_list.insert(0,dictinory_simbols['1'])
            if list_number[0] == 2: result_list.insert(0,dictinory_simbols['2'])
            if list_number[0] == 3: result_list.insert(0,dictinory_simbols['3'])
            if list_number[0] == 4: result_list.insert(0,dictinory_simbols['4'])
            if list_number[0] == 5: result_list.insert(0,dictinory_simbols['5'])
            if list_number[0] == 6: result_list.insert(0,dictinory_simbols['6'])
            if list_number[0] == 7: result_list.insert(0,dictinory_simbols['7'])
            if list_number[0] == 8: result_list.insert(0,dictinory_simbols['8'])
            if list_number[0] == 9: result_list.insert(0,dictinory_simbols['9'])
        
        # Если число от 20 до 99
        if i == 1 and list_number[1] != 1:
            if list_number[1] == 2: result_list.insert(0,dictinory_simbols['20'])
            if list_number[1] == 3: result_list.insert(0,dictinory_simbols['30'])
            if list_number[1] == 4: result_list.insert(0,dictinory_simbols['40'])
            if list_number[1] == 5: result_list.insert(0,dictinory_simbols['50'])
            if list_number[1] == 6: result_list.insert(0,dictinory_simbols['60'])
            if list_number[1] == 7: result_list.insert(0,dictinory_simbols['70'])
            if list_number[1] == 8: result_list.insert(0,dictinory_simbols['80'])
            if list_number[1] == 9: result_list.insert(0,dictinory_simbols['90'])
        
        # Если число 100 до 999
        if i == 2:
            if list_number[2] == 1: result_list.insert(0,dictinory_simbols['100'])
            if list_number[2] == 2: result_list.insert(0,dictinory_simbols['200'])
            if list_number[2] == 3: result_list.insert(0,dictinory_simbols['300'])
            if list_number[2] == 4: result_list.insert(0,dictinory_simbols['400'])
            if list_number[2] == 5: result_list.insert(0,dictinory_simbols['500'])
            if list_number[2] == 6: result_list.insert(0,dictinory_simbols['600'])
            if list_number[2] == 7: result_list.insert(0,dictinory_simbols['700'])
            if list_number[2] == 8: result_list.insert(0,dictinory_simbols['800'])
            if list_number[2] == 9: result_list.insert(0,dictinory_simbols['900'])

        # Тысячные разряды
        if i == 3 and number_of_digits > 4:
            # если число от 10 до 19
            if list_number[i + 1] == 1:
                if list_number[3] == 0: result_list.insert(0,dictinory_simbols['10'] + ' тысяч')
                if list_number[3] == 1: result_list.insert(0,dictinory_simbols['11'] + ' тысяч')
                if list_number[3] == 2: result_list.insert(0,dictinory_simbols['12'] + ' тысяч')
                if list_number[3] == 3: result_list.insert(0,dictinory_simbols['13'] + ' тысяч')
                if list_number[3] == 4: result_list.insert(0,dictinory_simbols['14'] + ' тысяч')
                if list_number[3] == 5: result_list.insert(0,dictinory_simbols['15'] + ' тысяч')
                if list_number[3] == 6: result_list.insert(0,dictinory_simbols['16'] + ' тысяч')
                if list_number[3] == 7: result_list.insert(0,dictinory_simbols['17'] + ' тысяч')
                if list_number[3] == 8: result_list.insert(0,dictinory_simbols['18'] + ' тысяч')
                if list_number[3] == 9: result_list.insert(0,dictinory_simbols['19'] + ' тысяч')
            else:
                if list_number[3] == 1: result_list.insert(0,dictinory_simbols['1'] + ' тысяча')
                if list_number[3] == 2: result_list.insert(0,dictinory_simbols['2'] + ' тысячи')
                if list_number[3] == 3: result_list.insert(0,dictinory_simbols['3'] + ' тысячи')
                if list_number[3] == 4: result_list.insert(0,dictinory_simbols['4'] + ' тысячи')
                if list_number[3] == 5: result_list.insert(0,dictinory_simbols['5'] + ' тысяч')
                if list_number[3] == 6: result_list.insert(0,dictinory_simbols['6'] + ' тысяч')
                if list_number[3] == 7: result_list.insert(0,dictinory_simbols['7'] + ' тысяч')
                if list_number[3] == 8: result_list.insert(0,dictinory_simbols['8'] + ' тысяч')
                if list_number[3] == 9: result_list.insert(0,dictinory_simbols['9'] + ' тысяч')
        
        # Если число от 1 до 9
        elif i == 3 and number_of_digits == 4:
            if list_number[3] == 1: result_list.insert(0,dictinory_simbols['1'] + ' тысяча')
            if list_number[3] == 2: result_list.insert(0,dictinory_simbols['2'] + ' тысячи')
            if list_number[3] == 3: result_list.insert(0,dictinory_simbols['3'] + ' тысячи')
            if list_number[3] == 4: result_list.insert(0,dictinory_simbols['4'] + ' тысячи')
            if list_number[3] == 5: result_list.insert(0,dictinory_simbols['5'] + ' тысяч')
            if list_number[3] == 6: result_list.insert(0,dictinory_simbols['6'] + ' тысяч')
            if list_number[3] == 7: result_list.insert(0,dictinory_simbols['7'] + ' тысяч')
            if list_number[3] == 8: result_list.insert(0,dictinory_simbols['8'] + ' тысяч')
            if list_number[3] == 9: result_list.insert(0,dictinory_simbols['9'] + ' тысяч')
        
        # Если число от 20 до 99
        if i == 4 and list_number[4] != 1:
            if list_number[4] == 2: result_list.insert(0,dictinory_simbols['20'])
            if list_number[4] == 3: result_list.insert(0,dictinory_simbols['30'])
            if list_number[4] == 4: result_list.insert(0,dictinory_simbols['40'])
            if list_number[4] == 5: result_list.insert(0,dictinory_simbols['50'])
            if list_number[4] == 6: result_list.insert(0,dictinory_simbols['60'])
            if list_number[4] == 7: result_list.insert(0,dictinory_simbols['70'])
            if list_number[4] == 8: result_list.insert(0,dictinory_simbols['80'])
            if list_number[4] == 9: result_list.insert(0,dictinory_simbols['90'])
        
        # Если число 100 до 999
        if i == 5:
            if list_number[5] == 1: result_list.insert(0,dictinory_simbols['100'])
            if list_number[5] == 2: result_list.insert(0,dictinory_simbols['200'])
            if list_number[5] == 3: result_list.insert(0,dictinory_simbols['300'])
            if list_number[5] == 4: result_list.insert(0,dictinory_simbols['400'])
            if list_number[5] == 5: result_list.insert(0,dictinory_simbols['500'])
            if list_number[5] == 6: result_list.insert(0,dictinory_simbols['600'])
            if list_number[5] == 7: result_list.insert(0,dictinory_simbols['700'])
            if list_number[5] == 8: result_list.insert(0,dictinory_simbols['800'])
            if list_number[5] == 9: result_list.insert(0,dictinory_simbols['900'])

        # Миллионные разряды
        if i == 6 and number_of_digits > 7:
            # если число от 10 до 10
            if list_number[i + 1] == 1:
                if list_number[6] == 0: result_list.insert(0,dictinory_simbols['10'] + ' миллионов')
                if list_number[6] == 1: result_list.insert(0,dictinory_simbols['11'] + ' миллионов')
                if list_number[6] == 2: result_list.insert(0,dictinory_simbols['12'] + ' миллионов')
                if list_number[6] == 3: result_list.insert(0,dictinory_simbols['13'] + ' миллионов')
                if list_number[6] == 4: result_list.insert(0,dictinory_simbols['14'] + ' миллионов')
                if list_number[6] == 5: result_list.insert(0,dictinory_simbols['15'] + ' миллионов')
                if list_number[6] == 6: result_list.insert(0,dictinory_simbols['16'] + ' миллионов')
                if list_number[6] == 7: result_list.insert(0,dictinory_simbols['17'] + ' миллионов')
                if list_number[6] == 8: result_list.insert(0,dictinory_simbols['18'] + ' миллионов')
                if list_number[6] == 9: result_list.insert(0,dictinory_simbols['19'] + ' миллионов')
            else:
                if list_number[6] == 1: result_list.insert(0,dictinory_simbols['1'] + ' миллион')
                if list_number[6] == 2: result_list.insert(0,dictinory_simbols['2'] + ' миллиона')
                if list_number[6] == 3: result_list.insert(0,dictinory_simbols['3'] + ' миллиона')
                if list_number[6] == 4: result_list.insert(0,dictinory_simbols['4'] + ' миллиона')
                if list_number[6] == 5: result_list.insert(0,dictinory_simbols['5'] + ' миллионов')
                if list_number[6] == 6: result_list.insert(0,dictinory_simbols['6'] + ' миллионов')
                if list_number[6] == 7: result_list.insert(0,dictinory_simbols['7'] + ' миллионов')
                if list_number[6] == 8: result_list.insert(0,dictinory_simbols['8'] + ' миллионов')
                if list_number[6] == 9: result_list.insert(0,dictinory_simbols['9'] + ' миллионов')
        
        # Если число от 1 до 9
        elif i == 6 and number_of_digits == 7:
            if list_number[6] == 1: result_list.insert(0,dictinory_simbols['1'] + ' миллион')
            if list_number[6] == 2: result_list.insert(0,dictinory_simbols['2'] + ' миллиона')
            if list_number[6] == 3: result_list.insert(0,dictinory_simbols['3'] + ' миллиона')
            if list_number[6] == 4: result_list.insert(0,dictinory_simbols['4'] + ' миллиона')
            if list_number[6] == 5: result_list.insert(0,dictinory_simbols['5'] + ' миллионов')
            if list_number[6] == 6: result_list.insert(0,dictinory_simbols['6'] + ' миллионов')
            if list_number[6] == 7: result_list.insert(0,dictinory_simbols['7'] + ' миллионов')
            if list_number[6] == 8: result_list.insert(0,dictinory_simbols['8'] + ' миллионов')
            if list_number[6] == 9: result_list.insert(0,dictinory_simbols['9'] + ' миллионов')
        
        # Если число от 20 до 99
        if i == 7 and list_number[7] != 1:
            if list_number[7] == 2: result_list.insert(0,dictinory_simbols['20'])
            if list_number[7] == 3: result_list.insert(0,dictinory_simbols['30'])
            if list_number[7] == 4: result_list.insert(0,dictinory_simbols['40'])
            if list_number[7] == 5: result_list.insert(0,dictinory_simbols['50'])
            if list_number[7] == 6: result_list.insert(0,dictinory_simbols['60'])
            if list_number[7] == 7: result_list.insert(0,dictinory_simbols['70'])
            if list_number[7] == 8: result_list.insert(0,dictinory_simbols['80'])
            if list_number[7] == 9: result_list.insert(0,dictinory_simbols['90'])
        
        # Если число 100 до 999
        if i == 8:
            if list_number[8] == 1: result_list.insert(0,dictinory_simbols['100'])
            if list_number[8] == 2: result_list.insert(0,dictinory_simbols['200'])
            if list_number[8] == 3: result_list.insert(0,dictinory_simbols['300'])
            if list_number[8] == 4: result_list.insert(0,dictinory_simbols['400'])
            if list_number[8] == 5: result_list.insert(0,dictinory_simbols['500'])
            if list_number[8] == 6: result_list.insert(0,dictinory_simbols['600'])
            if list_number[8] == 7: result_list.insert(0,dictinory_simbols['700'])
            if list_number[8] == 8: result_list.insert(0,dictinory_simbols['800'])
            if list_number[8] == 9: result_list.insert(0,dictinory_simbols['900'])
    print(*result_list)


user_number = user_input(message = "Введите число от 1 до 1 000 000 000: ", min_elem = 1, max_elem = 1000000000)


number_by_words(user_number)



