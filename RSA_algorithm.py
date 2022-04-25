#Moaaz_Rashed
#############################################
#key Generation
#    1-choose two prime numbers P, Q. 3,7
#    2-compute n , n=p*q= 3*7=21
#    3-compute φ(n)😁 , φ(n)=(p-1)(q-1) = 2*6=12 #aw2at byt2al 3alyha euler
#    4-chosse e, 1 < e < φ, must be coprime with phy gcd(e,φ) let e=5
#    public key= (e, n) (5, 21)
#    private key= (d, n)(d, 21) e*d mode φ(n)=1 #3l4an ngeeb d value OR d = e^-1 mod φ(n) >modular multiplication inverse >>>d = 5 OR d = (k*Φ(n) + 1) / e for some integer k
#    encryotion >> C = P^e mod n
#    decryption >> P = C^d mod n
#################################################################################################################################
#RSA algorithm >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# import math
 
# message = int(input("Enter the message to be encrypted: ")) 
 
# p = 11
# q = 7
# e = 3
 
# n = p*q
 
# def encrypt(me):
#     en = math.pow(me,e)
#     c = en % n
#     print("Encrypted Message is: ", c)
#     return c
 
# print("Original Message is: ", message)
# c = encrypt(message)

#    
###########################################################################################################################3
# key Generation >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP
# import binascii
 
# keyPair = RSA.generate(3072)
 
# pubKey = keyPair.publickey()
# print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
# pubKeyPEM = pubKey.exportKey()
# print(pubKeyPEM.decode('ascii'))
 
# print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
# privKeyPEM = keyPair.exportKey()
# print(privKeyPEM.decode('ascii'))
 
# #encryption
# msg = 'A message for encryption'
# encryptor = PKCS1_OAEP.new(pubKey)
# encrypted = encryptor.encrypt(msg)
# print("Encrypted:", binascii.hexlify(encrypted))

