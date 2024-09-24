from one_name_main import fun1

print("I am a code that runs directly inside twonamemain.py")
fun1()
if __name__ == "__main__":
    print("Two name==main.py is running directly")
else:
    print("Two name==main.py is imported and not running directly")