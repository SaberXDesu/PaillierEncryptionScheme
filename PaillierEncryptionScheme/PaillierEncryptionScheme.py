import sympy
import sys


#Encryption function
def Encryption(m,r,g,n):
    c=((g**m)*(r**n))%(n**2)
    return c

#Decryption function
def Decryption(lamb,n,c,mu):
    cLamb=(c**lamb)%(n**2)
    L_n=(cLamb-1)/n
    m=(L_n*mu)%n
    return m

#Variables
p = int(input("Choose your p: "))
q = int(input("Choose your q: "))
n = p*q
EulerTotient =(p-1)*(q-1)
g=n+1
lamb = (EulerTotient)
mu =0

#Getting mu
while True:
    try:
        mu = sympy.mod_inverse(EulerTotient,n)
        break
    except ValueError:
        mu=0
        print("You will not be able to decrypt message when mu=0")
        break

#Prints variables
print("p = %d, "%(p)+"q = %d, "%(q) + ("n = %d ")%(n)+ "EulerTotient = %d, "%(EulerTotient) + "g = %d, "%(g) + "lambda = %d, "%(lamb) + "mu = %d"%(mu))


#User types encrypt or decrypt
answer = input("encrypt or decrypt? ")

#Encrypt message m and get ciphertext c
if(answer=="encrypt"):
    m=int(input("Choose m: "))
    r=int(input("Choose r: "))
    c=Encryption(m,r,g,n)
    print("Your encryption message is: %d"%(c))

#Decrypt ciphertext c and get message m
if(answer=='decrypt'):
    c=int(input("Choose c: "))
    m=Decryption(lamb,n,c,mu)
    print("Your decryption message is: %d"%(m))

