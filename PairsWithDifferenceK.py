
def pairsWithDifference(array, k):
    count = 0
    output = []
    dic = {ele : 0 for ele in array}
    for ele in array:
        if ((ele-k) in dic.keys() and dic[ele-k]!=1):
            pair= (ele,ele-k)
            dic[ele] =1
            output.append(pair)
            count += 1
        if ((ele+k) in dic.keys() and dic[ele+k]!=1):
            pair= (ele,ele+k)
            dic[ele] =1
            output.append(pair)
            count += 1
    return dic,count,output


if __name__ == "__main__":
   x,y,output = pairsWithDifference([1,7,5,9,2,12,3],2)
   print (x,y,output,sep ="\n")



