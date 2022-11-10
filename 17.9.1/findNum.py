controlNum = ''    
while controlNum.isdigit() == False: # проверяем что введено число
    controlNum = input ("введите число: ")

with open ('fileinput.txt', 'r') as data: # считываем данные из файла
    info = data.readlines()

newList = []
str1 = ''
for i in range(len(info)): # формируем список в котором только числа
    for j in info[i]:
        if j.isdigit() == True:
            str1 = str1 + j
    if len(str1) > 0:
        newList.append(str1)
    str1 = ''
print (f'List = {newList}')

def SortOfList(lst1): # функция сортирует список
    for i in range(1,len(lst1)):       
        for j in range(i): 
            if (int(lst1[i]) < int(lst1[j])):
                tmp = lst1[i]
                for k in range (i, j, -1):
                    lst1[k] = lst1[k-1]               
                lst1[j] = tmp               
    return lst1

sortedList = SortOfList(newList)   
        
print (f'sortedList = {sortedList}')     

def BinarySearch(array, usersNum): # двоичный поиск по условиям задачи
    middle = int(len(array) / 2)
    if int(array[middle]) < usersNum:
        for i in range(middle, len(array)-1):           
            if int(array[i]) < usersNum and int(array[i+1]) >= usersNum:
                print (f'индекс в массиве {i}')
                break
    else:
        for i in range(middle):
            if int(array[i]) < usersNum and int(array[i+1]) >= usersNum:
                print (f'индекс в массиве {i}') 
                break
    if usersNum <= int(array[0]) or usersNum >= int(array[len(array)-1]):
        print('нет такой позиции3')

BinarySearch(sortedList, int(controlNum))
        