#Task1:Number systems changing
import math
#import cmath
#myuai
print("Welcome.Please choose a number: ")
print("1.Roman numbers")
print("2.Binary")
print("8.Octal")
print("10.Decimal")
print("16.Hexadecimal")

beforeFromProcess = int(input("Ilk ededin tipini daxil edin: "))
firstNumber = input("Ilk ededi daxil edin: ")
afterFromProcess = int(input("Almaq istediyiniz tipi daxil edin: "))

class numberSystemChanging:
    def __init__(self,beforeFromProcess,firstNumber,afterFromProcess):
        self.beforeFromProcess = beforeFromProcess
        self.afterFromProcess = afterFromProcess
        self.firstNumber = firstNumber
        if(beforeFromProcess!=16 and beforeFromProcess!=1):
            firstNumber = int(firstNumber)
            number = 0
            while(firstNumber>0):
                number += ((firstNumber//pow(10,int(math.log(firstNumber,10))))*pow(beforeFromProcess,int(math.log(firstNumber,10))))
                firstNumber=firstNumber%pow(10,int(math.log(firstNumber,10)))
            self.firstNumber = number
        elif(beforeFromProcess==1):
            number = 0
            dict1 = {
                "I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100, 
                "D":500,
                "M":1000
                }
            for i in range(0,len(firstNumber)-1):
                if(dict1[firstNumber[i]]<dict1[firstNumber[i+1]]):
                    number -= dict1[firstNumber[i]]
                else:
                    number += dict1[firstNumber[i]]
            number += dict1[firstNumber[len(firstNumber)-1]]
            self.firstNumber = number
        else:
            number=0
            for i in range(0,len(firstNumber)):
                k = 0
                if(firstNumber[i]=='A'):
                    k=10
                elif(firstNumber[i]=='B'):
                    k=11
                elif(firstNumber[i]=='C'):
                    k=12
                elif(firstNumber[i]=='D'):
                    k=13
                elif(firstNumber[i]=='E'):
                    k=14
                elif(firstNumber[i]=='F'):
                    k=15
                else:
                    k=int(firstNumber[i])
                number += k*pow(16,len(firstNumber)-1-i)
            self.firstNumber = number
    def toBinary(self):
        bit = ""
        while(int(self.firstNumber)>0):
            bit = str(int(self.firstNumber)%2) + bit
            self.firstNumber = int(self.firstNumber)//2
        self.firstNumber = bit
        print(self.firstNumber)
    def toOctal(self):
        octal = ""
        while(int(self.firstNumber)>0):
            octal = str(int(self.firstNumber)%8) + octal
            self.firstNumber = int(self.firstNumber)//8
        self.firstNumber = octal
        print(self.firstNumber)   
    def toHexadecimal(self):
        hexa = ""
        while(int(self.firstNumber)>0):
            if(int(self.firstNumber)%16==10):
                hexa = 'A' + hexa
            elif(int(self.firstNumber)%16==11):
                hexa = 'B' + hexa
            elif(int(self.firstNumber)%16==12):
                hexa = 'C' + hexa
            elif(int(self.firstNumber)%16==13):
                hexa = 'D' + hexa
            elif(int(self.firstNumber)%16==14):
                hexa = 'E' + hexa
            elif(int(self.firstNumber)%16==15):
                hexa = 'F' + hexa
            else:
                hexa = str(int(self.firstNumber)%16) + hexa
            self.firstNumber = int(self.firstNumber)//16
        self.firstNumber = hexa
        print(self.firstNumber) 
    def toRoman(self):
        length = int(math.log(int(self.firstNumber),10))+1
        if(int(self.firstNumber)>3999 and int(self.firstNumber)<1):
            print("This number doesn't exist in Roman numbers")
            return 0
        dict1 = {"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"VII":7,"VIII":8,"IX":9,"X":10,"XX":20,
                 "XXX":30,"XL":40,"L":50,"LX":60,"LXX":70,"LXXX":80,"XC":90,"C":100,"CC":200,
                 "CCC":300,"CD":400,"D":500,"DC":600,"DCC":700,"DCCC":800,"CM":900,"M":1000,
                 "MM":2000,"MMM":3000}
        answer = ""
        keys = []
        i = 0
        while(int(self.firstNumber)>0):
            first = (int(self.firstNumber)//pow(10,length-1))*pow(10,length-1)
            keys.append([key for key,val in dict1.items() if val == first])
            answer += keys[i][0]
            self.firstNumber = int(self.firstNumber)%pow(10,length-1)
            length-=1
            i+=1
        self.firstNumber = answer
        print(self.firstNumber)
            
obj = numberSystemChanging(beforeFromProcess, firstNumber, afterFromProcess)
if(afterFromProcess==2):
    obj.toBinary()
elif(afterFromProcess==8):
    obj.toOctal()
elif(afterFromProcess==10):
    print(obj.firstNumber)
elif(afterFromProcess==1):
    obj.toRoman()
else:
    obj.toHexadecimal()



'''
###########################################################################
#Alqoritm dersindeki tapsiriqlardan#
###########################################################################
#Kvadrat tenliyin helli 
a,b,c=int(input()),int(input()),int(input())
D = pow(b,2)-4*a*c
if(D>=0):
    X1 = (-b-math.sqrt(D))/(2*a)
    X2 = (-b+math.sqrt(D))/(2*a)
    print(X1,X2)
else:
    A = -b/(2*a)
    B = math.sqrt(abs(D))/(2*a)
    complex1 = complex(A,B)
    print(complex1.real,"+",complex1.imag,"i",end="\n")
    print(complex1.real,"-",complex1.imag,"i",end="\n")

#A[NxN] matrisinde her setrdeki en boyuk eded
'''

#Factorial rekkursiv
'''
def factorial(n):
    s=n
    if(n==0 or n==1):
        return 1
    else:
        s=s*factorial(n-1)
        n=n-1
    return s
print(factorial(6))
'''