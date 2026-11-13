# n = int(input("Enter a number: "))
# def oddOrEven(n):
#     if n % 2 == 1:
#         return ("Odd")
#     else:
#         return ("Even")
#
# print(oddOrEven(n))




# def is_odd(n):
#     return n % 2 == 1
# print(is_odd(15))




# year = int(input("Enter the year: "))
#
# def is_leap(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False1920
#
# print(is_leap(year))


#
# def print_triangular(n):
#     total = 0
#     for i in range (1 , n + 1):
#         total = total + i
#         print (i , total)
#
# print_triangular(5)


# def prime_number(n):
#     if n<2:
#         return False
#     for i in range(2 , n):
#         if n % i == 0:
#             return False
#     return True
#
# n = int(input("Enter a number: "))
# print(prime_number(n))



# def reverse(s):
#     result = ""
#     for ch in s:
#         result =  ch + result
#     return result
#
# print(reverse("hello world"))
#
#
# def reverse_slice(s):
#    return s[::-1]
#
# print(reverse_slice("hello world"))


# def remove_all_occurrences(sub , s ):
#     return s.replace(sub,"  ")
#
# print(remove_all_occurrences( "ll" , "hello worlld " ))



# def substitute (message , key):
#     alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
#     result = ""
#     for ch in message :
#         index = alphabet.find(ch.lower())
#         if index == -1:
#             result = result + ch
#         elif ch.isupper():
#             result= result + key[index].upper()
#         else :
#             result = result + key[index].lower()
#     return result
#
# key = "zyvüutşsrpöonmlkjiıhğgfedçcba"
# print(substitute("Hello, World!", key))


# def remove_dups(s):
#     result = ""
#     for ch in s :
#         if ch.lower() not in result.lower() :
#             result = result + ch
#     return result
#
# print(remove_dups("Hello ,, world"))

