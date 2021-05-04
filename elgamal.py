import math
import random

def gcd(a, b):
    gcd_val = 0
    for i in range(1, a-1):
        if a%i == 0 and b%i == 0:
            gcd_val = i
    return gcd_val

def select_coprime(n):
    cop = []
    print("Select a co-prime: ")
    for i in range(n):
        if gcd(i,n) == 1:
            cop.append(i)
    return cop

def get_inverse(e, phi_n):
    for i in range(phi_n):
        if (e*i)%phi_n == 1:
            return i

def key_generation():
    print("::Elgamal Key Generation Procedure::")
    p = int(input("Enter a large prime number (p): "))
    copE = select_coprime(p)
    print(copE, sep = " ")
    while (1):
        d = int(input("Enter one of the above integers (d): "))
        if d not in copE:
            continue
        else:
            break
    e1 = copE[0]
    e2 = (e1**d) % p
    #r = random.choice(copE)
    r = 8
    return e1, e2, p, d, r

def elgemal_encryption(plain, e1, e2, p, r):
    cipher1 = (e1**r) % p
    cipher2 = (plain*(e2**r)) % p
    return cipher1, cipher2

def elgamal_decryption(cipher1, cipher2, d, p):
    cd = (cipher1**d) % p
    invCD = get_inverse(cd, p)
    plain = (cipher2 * invCD) % p
    return plain

print("-##- El-Gamal Encryption and Decryption algorithm -##-")
e1, e2, p, d, r = key_generation()
plaintext = int(input("Enter plaintext integer: "))
cipher1, cipher2 = elgemal_encryption(plaintext, e1, e2, p, r)
print("Cipher Text: ")
print("C1->{}" .format(cipher1))
print("C2->{}" .format(cipher2))
plain = elgamal_decryption(cipher1, cipher2, d, p)
print("Plain Text: {}" .format(plain))
