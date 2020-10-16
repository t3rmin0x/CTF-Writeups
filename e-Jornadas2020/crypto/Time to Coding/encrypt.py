import base64


def encrypt(data): 
    encrypted=""
    key=0x2F
    pre_enc=""
    for x in data:
        tmp = ord(x) 
        tmp = tmp ^ key
        pre_enc+=chr(tmp)

    pre_enc=base64.b64encode(pre_enc)
    encrypted_data="" 
    for x in range(0, len(pre_enc)):   
        tmp = pre_enc[ len(pre_enc) - 1 -x ]    
        encrypted_data+= chr(ord(tmp) + 5 )
           
    return encrypted_data
