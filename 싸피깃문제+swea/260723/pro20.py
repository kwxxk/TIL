# email = input()

# # print(email)
# mailindex = email.find('@')
# if mailindex == -1:
#     print("Invalid email")
# else:
#     print(email[mailindex +1:])

def extra_domain(email):
    #find로 @위치 찾아야함
    email_index = email.find('@')
    if email_index == -1:
        return ("Invalid email")
    
    domain = email[email_index +1:]
    return domain

email = input()
result = extra_domain(email)
print(result)