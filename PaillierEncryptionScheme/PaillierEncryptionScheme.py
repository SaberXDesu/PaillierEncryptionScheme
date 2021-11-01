import sympy
import optparse

#Set variables
def setVariables(x,y):
    p = x
    q = y
    n = p*q
    EulerTotient =(p-1)*(q-1)
    g=n+1
    lamb = (EulerTotient)
    mu = getMu(EulerTotient,n)
    print(mu)

    print("p = %d, "%(p)+"q = %d, "%(q) + ("n = %d ")%(n)+ "EulerTotient = %d, "%(EulerTotient) + "g = %d, "%(g) + "lambda = %d, "%(lamb) + "mu = %d"%(mu)) #Print variables
    variables =[p,q,n,EulerTotient,g,lamb,mu] 
    return(variables)

#Set mu
def getMu(EulerTotient, n):
    mu=0
    print(EulerTotient)
    print(n)
    while True:
        try:
            mu = sympy.mod_inverse(EulerTotient,n)
            print('this %d'%(mu))
            break
        except ValueError:
            mu=0
            print("You will not be able to decrypt message when mu=0")
            break
    return mu

def secondQuery(result):
    answer = input("encrypt or decrypt? ")
    
    #Encrypt message m and get ciphertext c
    if(answer=="encrypt"):
        m=int(input("Choose m: "))
        r=int(input("Choose r: "))
        c=Encryption(m,r,result[4],result[2]) #Encryption(m,r,g,n)
        print("Your encryption message is: %d"%(c))
    
    #Decrypt ciphertext c and get message m
    if(answer=='decrypt'):
        c=int(input("Choose c: "))
        m=Decryption(result[5],result[2],c,result[6]) #Decryption(lambda,n,c,mu)
        print("Your decryption message is: %d"%(m))

#Call Encryption function
def Encryption(m,r,g,n):
    c=((g**m)*(r**n))%(n**2)
    return c

#Call Decryption function
def Decryption(lamb,n,c,mu):
    cLamb=(c**lamb)%(n**2)
    L_n=(cLamb-1)/n
    m=(L_n*mu)%n
    return m

def main():
        parser = optparse.OptionParser('Choose p & q: '+'--InputP <Your P> --InputQ <Your Q>')
        parser.add_option('--InputP', dest='YourP', type='int', help='specify p')
        parser.add_option('--InputQ', dest='YourQ', type='int', help='specify q')
        (options, args) = parser.parse_args()
        YourP = options.YourP
        YourQ = options.YourQ
        if (YourP <0 | YourQ <0):
            print(parser.usage)
            exit(0)
        result = []
        result = setVariables(YourP,YourQ)
        secondQuery(result)


if __name__== '__main__':
    main()
