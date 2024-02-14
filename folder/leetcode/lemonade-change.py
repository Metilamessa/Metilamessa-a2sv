class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt5 = 0
        cnt10 = 0
        cnt20 = 0
        n = len(bills)

        for i in range(n):
            if bills[i] == 5:
                cnt5+=1
            elif bills[i]==10:
                if cnt5:
                    cnt10 += 1
                    cnt5 -= 1
                else:
                    return False
            else:
                if cnt10 and cnt5:
                    cnt20+=1
                    cnt10-=1
                    cnt5-=1
                elif cnt5 >= 3:
                    cnt20+=1
                    cnt5-=3
                else:
                    return False
                
        return True
        