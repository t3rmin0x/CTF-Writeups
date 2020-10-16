import base64

def decrypt(data):
    pre_dec = ''
    for x in range(len(data)):
        tmp = data[len(data) - 1 - x]
        pre_dec += chr(ord(tmp) - 5)
    
    pre_dec = base64.b64decode(pre_dec.encode())
    
    key = 0x2F
    decrypted = ''
    for x in pre_dec:
        decrypted += chr(x ^ key)

    return decrypted


# def encrypt(data): 
#     encrypted=""
#     key=0x2F
#     pre_enc=""
#     for x in data:
#         tmp = ord(x) 
#         tmp = tmp ^ key
#         pre_enc+=chr(tmp)

#     pre_enc=base64.b64encode(pre_enc.encode()).decode()
#     encrypted_data="" 
#     for x in range(0, len(pre_enc)):   
#         tmp = pre_enc[ len(pre_enc) - 1 -x ]    
#         encrypted_data+= chr(ord(tmp) + 5 )
           
#     return encrypted_data

ct = open("data.enc", 'r').read()
print(decrypt(ct))