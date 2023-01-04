import string

import pyperclip





class T_Crypt:
    
     chars = [i for i in string.printable+" "]
     

     
     encypttext = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '4', '', '(', 'd', '3', 'f', 'g', 'h', '1', 'j', 'k', 'l', 'm', 'n', '0', 'p', '9', 'r', '5', '7', 'u', 'v', 'w', 'x', 'y', 'z', '4', 'B', '(', 'D', '3', 'F', 'G', 'H', '1', 'J', 'K', 'L', 'M', 'N', '0', 'p', '9', 'R', '5', '7', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ', '\t', '\n', '\r', '\x0b', '\x0c', ' ']
     

     
     def __init__(self, message=None):
         
          self.message = message
          

          

          
     def encrypt(self):
         
          if self.message != "":
              
               msg = self.message.upper()
               
               e_msg = ""
               
               for i in msg:
                   
                    e_msg+=self.encypttext[self.chars.index(i)]
                    
               return e_msg
           
          else:
              
              print("You need to enter a message")
              

              
def init():
    
    print("Input the message you want to encrypt\n")
    
    message = input()
    
    a = T_Crypt(message)
    
    msg = a.encrypt()
    
    print(msg)
    
    print("________________\n")
    
    print("do you want to copy the encrypted text? Y/N ")
    
    ans = input()
    
    if ans.upper() == "Y":
        
        pyperclip.copy(msg)
        
    print("Do you want to encrypt new message Y")
    
    ans = input()
    
    if ans.upper() == "Y":
        
        init()
        

        
init()
