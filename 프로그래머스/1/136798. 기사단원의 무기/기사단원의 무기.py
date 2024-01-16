def solution(number, limit, power):
    num_list= []
    for i in range(1,number+1):
        num_1=0
        for j in range(1,int(i**(0.5))+1):
            if i%j==0:
                num_1+=1
                if j**2 !=i:
                    num_1+=1
            
            if num_1>limit:
                num_1=power
                break
        num_list.append(num_1)
            
    return sum(num_list)
            
                    
                