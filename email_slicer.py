def main():
    print("Welcome to the email slicer")
    print("")

    email=input("What is your email addrss? ")

    (username, domain) = email.split("@")
    (domain, extension) = domain.split(".")

    #use comma instead of plus sign / concatenate
    
    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)


main()



