def gcd(a, b):
    gcd_val = 0
    for i in range(1, a-1):
        if a%i == 0 and b%i == 0:
            gcd_val = i
    return gcd_val

def prime_check(n):
    if(n == 2):
        return True
    elif((n < 2) or ((n % 2) == 0)):
        return False
    elif(n > 2):
        for i in range(2, n):
            if not(n % i):
                return False
    return True

def select_primitive(n):
    cop = []
    print("Select a co-prime: ")
    for i in range(n):
        if gcd(i,n) == 1:
            cop.append(i)
    return cop

def key_generation(q, pr, x):
    return (pr**x) % q

print("-##- Diffie-Hellman key exchange algorithm -##-")
while(1):
    q = int(input("Enter a prime number: "))
    if not(prime_check(q)):
        continue
    else:
        break
pr = select_primitive(q)
print(pr, sep = " ")
while(1):
    p_root = int(input("Select one of the primitive roots from above list: "))
    if p_root not in pr:
        continue
    else:
        break

print("Abhishek's Key generation: ")
xA = int(input("Enter private key of Abhishek: "))
yA = key_generation(q, p_root, xA)
print("Bunty's Key generation: ")
xB = int(input("Enter private key of Bunty: "))
yB = key_generation(q, p_root, xB)
kA = (yB**xA) % q
kB = (yA**xB) % q
print("Public Key of Abhishek : {}" .format(yA))
print("Secret Key of Abhishek : {}" .format(kA))
print("Public Key of Bunty    : {}" .format(yB))
print("Secret Key of Bunty    : {}" .format(kB))
