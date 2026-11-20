# myList = [ 76, 92.3 , "hello" , True , 4 , 76 ]
#
#
# myList.append("apple") #sonuna bu değeri eledik
# myList.append(76)
# myList.insert(3 , "cat")  # belirttiğimiz konuma bu değeri ekledik
# myList.insert(0 , 99 ) # eklerken listeyi kaydırır genel olarak
# print(myList)
#
# print(myList.index("hello")) # hellonun sırasını verdi
#
# print(myList.count(76))  #listede kaç tane bu içerik var onu gösterir
#
# myList.remove(76)  #tek tek siler ilk baştakinden itibaren
#
# print(myList)
#
# myList.pop(myList.index(True))  #pop ile silmek için index lazım o yüzden önce index bulduk sonra sildi
# print(myList)
from itertools import count


# def  sum_of_squares(number_list):
#     total = 0
#     for number in number_list:
#         total = total + number**2
#     return total                     # tanımladığımız değer ve return aynı hizada olmalı
#
# my_list = [ 3 , 4 , 5 ]
# print(sum_of_squares(my_list))


# def sum_evens(number_list):
#     sum = 0
#     for number in number_list:
#         if number % 2 == 0:
#             sum = sum + number
#     return sum
#
# my_List = [ 1 , 2 , 3 , 4 ,5 , 6 , 7 , 8 , 9 ]
# print(sum_evens(my_List))



# def count_five_letter(words):
#     counter = 0
#     for word in words:
#         if len (word) == 5:
#             counter += 1
#     return counter
#
# my_List = [ "apple" , "cat" , "lemon" , "python" , "tiger", "12345" ]
# print(count_five_letter(my_List))



# def sum_until_even(numbers):
#     sum = 0
#     for number in numbers:
#         if number % 2 == 0:
#             break
#
#         sum += number
#     return sum
#
# my_lst = [ 1 , 3 , 3 , 7 , 5 , 6 ]
# print(sum_until_even(my_lst))



# def count_until_sam(words):
#     count = 0
#     for word in words:
#         count = count + 1
#         if word == 'sam':
#             break
#     return count
#
# my_list = [ " joe" , "ali" , " veli ", "sam" , "sami"]
# print(count_until_sam(my_list))



# def replace( s , old , new ):
#     pieces = s.split(old)
#     return new.join(pieces)
#
#
# def test(actual , expected ):
#     if actual == expected:
#         print("PASSED")
#     else:
#         print("FAILED")
#
# test(replace( "Mississippi" , "i" , "I" ),"MIssIssIppI")


#
# def max_value_list(num_list):
#     max_value = num_list[0]
#     for num in num_list:
#         if num > max_value:
#             max_value = num
#     return max_value
#
#
# print(max_value_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(max_value_list([5 , -40 , 0 , 4 , 8 , -35156455 , 2 ]))