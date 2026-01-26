
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        s=sorted(arr)  #SORTINF THE ARR
        mind=float("inf") #used to find the least min value 
        fin=[]
        for i in range(0,len(arr)-1):
            mind=min(mind,abs(s[i+1]-(s[i])))
        for i in range(0,len(arr)-1):
            if abs(s[i+1]-s[i])==mind:#comparing the i, j with the least min value
                fin.append([s[i],s[i+1]])#appending the ouput 
        return fin
