request = {'form' : {'username' : 'Brian', 'password' : 'secret'}}
db = []

def process_form(request):
        #old
        #password = request['form'].get('password')

        #old
        #if len(password) > 5:
        if len(password := request['form'].get('password')) > 5:
            db.append(password)
            return 'Added user!'
        else:
            return 'Password is too short!'

print(process_form(request))
print(db)
