filename = 'database.txt'
def register():
    """A function for the registration of user"""
    db = open(filename,'r')
    
#    creating the database which is a dictionary containing the username as the key and passsword as the value
    username = input('create username: ')
    password = input('Create  password: ')
    password1 = input('Confirm password: ')
    lines = db.readlines()
    usernames = []
    passwords = []
    for line in lines:
        username_lst, password_lst = line.split(',')
        username_lst = username_lst.strip()
        password_lst = password_lst.strip()
        usernames.append(username_lst)
        passwords.append(password_lst)
    profile_dict = dict(zip(usernames,passwords))

    # the logic begind the registration
    if username in usernames:
        print('Username exist, create another username.') 
        register()   
    elif password1 != password:
        print('password does not match, please restart')
        register()
    elif len(password) <= 6:
        print('Password is too short, please create another.')
        register()
    else:
        db=open(filename, 'a')
        db.write(f" {username},{password} \n")
        print('success')
    db.close()

def access():
    """A function that enables the user to login into the application"""
    db = open(filename,'r')
    username = input('enter username: ')
    password = input('enter password: ')
    
    if len(username)>1 and len(password) >1:
        
        lines = db.readlines()
        usernames = []
        passwords = []
        for line in lines:
            username_lst, password_lst = line.split(',')
            username_lst = username_lst.strip()
            password_lst = password_lst.strip()
            usernames.append(username_lst)
            passwords.append(password_lst)
        profile_dict = dict(zip(usernames,passwords))
        
        # the logic behind the login
        if username in usernames:
            try:
                if password == profile_dict[username]:
                    print('login success')
                    print(f"Hi, {username}!")
                else:
                    print("incorrect password,")
                    access()
            except:
                print('login error')
                home()
        else:
            print('this username does not exist')
            home()
    else:
        print('please enter a value')

def home(option = None):
    """The home page function"""
    option = input("Login | signup: ")
    if option == "login":
        access()
    elif option == "signup":
        register()
    else:
        print("please enter an option")
        home()
        
home()
    
       
    
    
    