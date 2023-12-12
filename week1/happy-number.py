sys.set_int_max_str_digits(1<<27)
class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited_before = set()
        while n > 0 and n not in visited_before:
            
            if n == 1:
                return True
            visited_before.add(n)
            temp = 0
            while n != 0:

                digit = n % 10
                digit_square = pow(digit, 2)
                temp +=digit_square
                n = n // 10
            n =temp
        return False
#         digits = []   
#         converted = str(n)
#         for i in converted:
#             visited_before = set()
#             while int(i)>0 and i not in visited_before:
                
#                 visited_before.add(i)
#                 square = pow(int(i), 2)
#                 digits.append(square)
#                 s = sum(digits)
#                 i = str(s)
#                 if i == "1":
            #         return True
            
            # return False
        