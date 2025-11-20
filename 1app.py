# Word Problem: The School Portal Login System
# Your school is creating a new online portal for students to sign up for accounts. The login system needs a function that accepts two pieces of information from the user:
# Their email address
# Their password
# Before creating the new account, the function must verify that the email and password follow school rules:
# The email must be a string and must contain an "@" symbol.
# The password must also be a string.
# The password must be at least 8 characters long.
# The password must include at least one number.
# The password must include at least one uppercase letter.
# If ANY of these rules are broken, the function should return an error message explaining what went wrong.
# If EVERYTHING is good, the function should return a dictionary that represents the newly created user.

def valid(email, password):
    if not isinstance(email, str) or not isinstance(password, str):
        return "Invalid: Email and password must be strings"
    if "@" not in email:
        return "incorrect email format"
    if len(password) < 8:
        return "Error: password mus be at least 8 characters long!"
    if not any(ch.isdigit() for ch in password):
        return "Error: password must include at least 1 number"
    if not any(ch.isupper() for ch in password):
        return "Error: password must include at least one uppercase letter"
    return{'email': email, 'password': password}
print(valid("test@gmail.com", "123456789Qe"))


# def valid(email, password):
#     if "@" not in email:
#         return"invalid email format"
#     if len(password) <= 8 and password.isdigit not in password:
#         for i in password:
#             if i.isupper in password:
#                  return"invalid password"
#             print("invalid password")
#         if len(password) >= 8 and password.isdigit:
#             return"valid password format!"
#         print("your", password, "is valid")
# valid("test@gmail.com", "q135wsfshg")
   

            

        
      


       


    

        