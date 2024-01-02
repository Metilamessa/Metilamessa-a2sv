class Solution:
    def smallestNumber(self, num: int) -> int:
        is_negative = False
        
        if num < 0:
            is_negative = True
            num = -1 * num
        List = []
        if num == 0:
            return 0
        while num > 0:
            List.append(num%10)
            num = num//10
        if  not is_negative:
            List.sort()
            i = 0
            while List[i] == 0:
                i+=1
            List[i],List[0] = List[0], List[i]
            ans = "".join(list(map(str,List)))
            return int(ans)
        else:
            List.sort(reverse = True)
            ans = "".join(list(map(str,List)))
            print(ans)
            return -1 * int(ans)



        