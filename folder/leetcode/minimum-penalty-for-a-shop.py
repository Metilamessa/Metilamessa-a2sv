class Solution:
    def bestClosingTime(self, customers: str) -> int:
        suf=[0] 
        pre=[0] 
        summ1=0 
        summ2=0 
        # j=len(customers)-1 
 
        N_no=0 
        all_yes=customers.count('Y') 
        N_yes=0 
        ans=all_yes 
        j=0 
 
        for i in range(len(customers)): 
            if customers[i]=='Y': 
                N_yes+=1 
            elif customers[i]=="N": 
                N_no+=1 
 
            if ans>(all_yes-N_yes+N_no): 
                j=i+1 
                ans=all_yes-N_yes+N_no 
             
        return j