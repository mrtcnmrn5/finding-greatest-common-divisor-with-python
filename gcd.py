def gcd(num1,num2):
    num1_div=[]
    num2_div=[]
    for i in range(1,num1+1):
        if(num1%i == 0):
            num1_div.append(i)
            for j in num1_div:
                if(num2%j == 0):
                    num2_div.append(j)
    return max( num2_div)
    
num1=int(input("num1: "))
num2=int(input("num2: "))
print("Greatest Common Divisor: ",gcd(num1,num2))
