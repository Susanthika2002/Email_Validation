#The program checks whether the user-provided email is following the validity conditions or not
email=input("Enter your email:") # user can provide mail
j=k=d=0
#email should consist of at least 6 characters.
if len(email)>=6:
# The First character should be an alphabet
    if email[0].isalpha():
#"@" should be present only once in an email.
        if ("@" in email) and (email.count("@")==1):
#"." character should be present from the last third or fourth and present once
            if (email[-3]==".")^(email[-4]=="."):
                for i in email:
                  if i.isalpha():
#The character should not be uppercase
                    if i.isupper():
                        j=1
#The space should not be given in the email
                  elif i.isspace():
                    k=1
#Email can have numbers 
                  elif i.isdigit():
                    continue
#Email can have @,_ and . characters
                  elif i=="." or i=="@" or i=="_":
                    continue
#Any special characters other than (@,.,_)
                  else:
                    d=1
                if k==1 or j==1 or d==1:
                  print("Wrong email 5 ")
                else:
                  print("Right email")
            else:
                print("Wrong email 4")
        else:
            print("Wrong email 3")
    else:
        print("Wrong email 2")
else:
    print("Wrong email 1")
