from passlib.context import CryptContext
#from passlib.hash import bcrypt

pwd_cxt= CryptContext(schemes='bcrypt', deprecated='auto') #auto->if a more secure hashing algorithm is introduced, the old one will be marked as deprecated.

class Hash():
    def bcrypt(password:str):
        return pwd_cxt.hash(password) #hash is a predinef function already
    
    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password ) #verify is also predefined, it checks the provided password 