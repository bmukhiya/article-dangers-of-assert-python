import re
regemail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regpassword = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
def user_verify(token,email,password):
    flag = 0
    assert re.fullmatch(regemail,email),"Email Invalid"
    assert re.search(regpassword,password), "Password Invalid"
    assert re.search("^token\:.?[a-z0-9]",token), "token is Invalid"
    
    return  print("User Successfully Logged In")

user_verify("token:","abc@abc.com","Assert123@")