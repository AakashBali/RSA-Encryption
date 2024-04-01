import random
import math
import binascii
import codecs

def randomNum():
    num = random.randint(32768,65535)
    prime_res = isPrime(num)
    if(prime_res == False):
        num = randomNum()
        return num
    return num

def isPrime(n):
    flag = False
    for i in range(2,n):
        if((n % 2) == 0):
            flag = True
            break
        if((n % i) == 0):
            flag = True
            break
    if flag:
        return False
    else:
        return True

def randomE(Phi_N):
    e = random.randint(0,32767)
    if(e<Phi_N and (math.gcd(e,Phi_N) == 1) and ((e%2) != 0) ):
        return e
    else:
        final_e = randomE(Phi_N)
        return final_e

def encrypt(N,e,msg):
    temp = []
    text = []
    encrypted_msg = []
    temp = [msg[i:i+3] for i in range(0, len(msg), 3)]
    print(temp)
    for i in temp:
        str = codecs.encode(i,'utf-8')
        hex_str = int(str.hex(),base=16)
        text.append(hex_str)
    for j in text:
        msg_encrypt = pow(j,e,N)
        encrypted_msg.append(msg_encrypt)
    return encrypted_msg

def decrypt(received_msg,N,e,d):
    msg_int = []
    decrypted_Msg = []
    for i in received_msg:
        msg = pow(i,d,N)
        msg_int.append(msg)
    temp_hex = []
    for j in msg_int:
        hex_str = hex(j)
        hex_str = hex_str.upper()
        temp_hex.append(hex_str[2:])
    for ele in temp_hex:
        binary_str = binascii.unhexlify(ele)
        decrypted_Msg.append(str(binary_str,'utf-8','ignore'))
        original_Msg = ''.join([str(n) for n in decrypted_Msg])
    return original_Msg

def sign_text(Text,N,d):
    temp_text = []
    signed_msg = []
    chunked_text = [Text[i:i+3] for i in range(0, len(Text), 3)]
    for i in chunked_text:
        encoded_str = codecs.encode(i,'utf-8')
        hex_str = int(encoded_str.hex(),base=16)
        temp_text.append(hex_str)
    for j in temp_text:
        msg_signing = pow(j,d,N)
        signed_msg.append(msg_signing)
    return signed_msg

def verify_sign(Text,N,e):
    Temp_txt = []
    verified_Sig = []
    for i in Text:
        temp = pow(i,e,N)
        Temp_txt.append(temp)
    temp_hex = []
    for j in Temp_txt:
        hex_str = hex(j)
        hex_str = hex_str.upper()
        temp_hex.append(hex_str[2:])
    for ele in temp_hex:
        binary_str = binascii.unhexlify(ele)
        verified_Sig.append(str(binary_str,'utf-8','ignore'))
        original_Msg = ''.join([str(n) for n in verified_Sig])
    return original_Msg
        
p = randomNum()
q = randomNum()

N = p*q
phi_N = (p-1)*(q-1)
e = randomE(phi_N)

d = pow(e,-1,phi_N)

print(p)
print(q)
print(N)
print(phi_N)
print(e)
print(d)

My_text = "Hey There! How are you?"
Encrypted_Msg = encrypt(1707770783,3341621,My_text)
print("Encrypted Text Is: ")
print(Encrypted_Msg)

received_enc_msg = [2659982115, 2461935287, 46941385, 2041400215, 1173804479, 793986685, 1761062085, 1150948241, 1577039938, 2445072442]
Decrypted_Msg = decrypt(received_enc_msg,2814546143,4313,1190899577)
print("Decrypted Text Is: " + Decrypted_Msg)

Text_to_sign = "Aakash Bali"
Signed_text = sign_text(Text_to_sign,2814546143,1190899577)
print("Signed Text is: ")
print(Signed_text)

Received_Signed_Text =  [550459883, 1652367565, 1125150248, 469456115, 1434128791]
Verified_Text = verify_sign(Received_Signed_Text,1707770783,3341621)
print("Verified Sign Is: " +Verified_Text)