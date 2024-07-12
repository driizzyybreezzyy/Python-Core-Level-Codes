class SignUp:
    def __init__(self, fn, ln, un, pwd):
        self.fn = fn
        self.ln = ln
        self.un = un
        self.pwd = pwd
        self.validate_password()

    def validate_password(self):
        while True:
            if (
                len(self.pwd) < 8
                or len(self.pwd) > 16
                or not any(c.islower() for c in self.pwd)
                or not any(c.isupper() for c in self.pwd)
                or not any(c.isdigit() for c in self.pwd)
                or not any(c in '!@#$%^&*()_+{}:;<>,.?~' for c in self.pwd)
            ):
                retry = input("Password does not meet criteria. Do you want to try again? (yes/no): ")
                if retry.lower() == "yes":
                    self.pwd = input("Enter a new password: ")
                else:
                    raise InvalidPasswordError("User Didn't define password properly")
            else:
                print("Password successfully set.")
                break

class SignIn:
    def __init__(self, un, pwd):
        self.un = un
        self.pwd = pwd

    def login_check(self, sign_up_instance):
        if self.un == sign_up_instance.un and self.pwd == sign_up_instance.pwd:
            print("----------------------------------------------------------------")
            print("Welcome,", sign_up_instance.fn, sign_up_instance.ln)
        else:
            raise InvalidLoginError("Invalid username or password.")
        
class InvalidPasswordError(Exception):
    pass

class InvalidLoginError(Exception):
    pass


class Main:
    def __init__(self):
        fn = input("First Name: ")
        ln = input("Last Name: ")
        un = input("Username: ")
        pwd = input("Password: ")

        try:
            sign_up_instance = SignUp(fn, ln, un, pwd)
        except InvalidPasswordError as e:
            print(e)
            return

        print("\nSign in:")
        un = input("Username: ")
        pwd = input("Password: ")

        sign_in_instance = SignIn(un, pwd)

        try:
            sign_in_instance.login_check(sign_up_instance)
            print("Login successful.\n")
        except InvalidLoginError as e:
            print(e)

objectMain =Main()