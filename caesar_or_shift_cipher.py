
#this is to check the commit

#thi is to check commit in sub branch

def encrypt(text,s, decip): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            if decip:
                result +=  chr((ord(char) - s-65) % 26 + 65)    
            else:
                result +=  chr((ord(char) + s-65) % 26 + 65)    
            
            
  
        # Encrypt lowercase characters 
        elif(char.islower()): 
            if decip:
                result += chr((ord(char) - s - 97) % 26 + 97)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
  
    return result 
  
#check the above function 
text = "phhw ph diwhu wkh wrjd sduwb"
s = 3
decip = True
print("Text  : ",text )
print("Shift : ",str(s)) 
print("Cipher: ",encrypt(text,s, decip))
