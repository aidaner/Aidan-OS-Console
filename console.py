import os
import requests
import sys
import time
os.system('clear')
v = 0.2
r = ''
cwd = os.getcwd()
cwdo = cwd
def Convert(string):
    li = list(string.split(" "))
    return li
try:
    f = open(cwd + '/aidanos/installed.txt', 'r')
    f.close()
    f = open(cwd + '/aidanos/account/username.txt')
    u = True
    usernamee = f.read()
    f.close()
    print('Your from Aidan OS!')
except:
    print('You are not from Aidan OS but thats fine you can still use this!')
print('''Welcome to Aidan OS console
What do you want to do? well run help to find out!
console version 0.2''')
while True:
    cwd = os.getcwd()
    if u == True:
        a = input(f'{usernamee}:{cwd}# ')
    else:
        a = input(f'{cwd}# ')
    oa = Convert(a)
    a = oa[0]
    if a == '':
        e = 'ee'
    elif a == 'help':
        print('''commands:
help: brings help
cd: moves directories
debug: this command is in beta
rm: it removes a file
update: updates the console if it needs to
exit: to exit the console
end of help''')
    elif a == 'cd':
        try:
            if oa[1] == '':
                print('Error! You didnt not specify a directory!')
            else:
                try:
                    os.chdir(oa[1])
                except:
                    print('Failed to change directories! Either the directory does not exist or something went wrong with the command!')
        except:
            print('Error! You didnt not specify a directory!')
    elif a == 'debug':
        try:
            if oa[1] == '':
                print('Please say Y/N if you want to enable debug for the console')
            elif oa[1] == 'y':
                print('okay but this will do nothing because this in beta!')
            elif oa[1] == 'n':
                print('okay but this will do nothing because this in beta!')
            else:
                print('Error thats not y or n')
        except:
            print('Please say Y/N if you want to enable debug for the console')
    elif a == 'exit':
        sys.exit()
    elif a == 'rm':
        try:
            if oa[1] == '':
                print('Use this command to del something!')
            else:
                os.system('rm ' + oa[1])
        except:
            print('Use this command to del something!')
    elif a == 'update':
        r = requests.get(url = 'https://raw.githubusercontent.com/aidaner/Aidan-OS-Console/version/version.html')
        r = r.json()
        if int(r) > v:
            print(f'Your on the latest version of Aidan OS console! Version {str(v)}')
        else:
            print('Your not on the latest version of Aidan OS console')
            print(f'Your version {str(v)}. The latest version is {r}')
            time.sleep(3)
            print('Updating . . .')
            if u == True:
                os.chdir(cwdo + '/aidanos/extra/')
                os.system('rm console.py')
                os.system('wget https://raw.githubusercontent.com/aidaner/Aidan-OS-Console/main/console.py')
                os.chdir(cwdo)
                print('Done do exit then run it again to restart the console!')
            else:
                os.system('rm console.py')
                os.system('wget https://raw.githubusercontent.com/aidaner/Aidan-OS-Console/main/console.py')
                print('Done do exit then run it again to restart the console!')
    
    
    else:
        print('Thats not a command! Please use help for a list of commands!')
