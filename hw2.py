def numeral_1():
    lst = [1, [2, 3], 4, [[6, 7]]]

    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    new_str = ''.join(map(str, lst))
    
    new_list = []
    
    for i in new_str:
        if i in num:
            new_list.append(int(i))
            
    return new_list
    
print (numeral_2())






def numeral_2():
    lst = [1, [2, 3], 4, [[6, 7]]]
    
    new_str = ''.join(map(str, lst))

    new_str = new_str.replace('[', '')
    new_str = new_str.replace(']', '')
    new_str = new_str.replace(',', '')
    new_str = new_str.replace(' ', '')

    new_list = []
    for i in new_str:
            new_list.append(int(i))

    return new_list

print (numeral_2())

