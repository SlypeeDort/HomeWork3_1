calls = 0
def count_calls():
    global calls
    calls +=1
def string_info():
    string = input('Введите слово ')
    print(len(string),string.lower(), string.upper())
    count_calls()

def  is_contains():
    string = input('Введите слово ')
    list_to_search =['ban', 'BaNaN', 'urBAN']
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() == string.lower():
            check = True
            break
        else:
            check = False
    print(check)
    count_calls()


print(string_info())
print(is_contains())
print(calls)