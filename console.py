import os
import sys
os.system('clear')
cwd = os.getcwd()
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
except:
    e = 'e'
print('''Welcome to Aidan OS console
What do you want to do? well run help to find out!
console version 0.1''')
while True:
    cwd = os.getcwd()
    if u == True:
        a = input(f'{usernamee}:{cwd}# ')
    else:
        a = input(f'{cwd}# ')
    oa = Convert(a)
    a = oa[0]
    if a == None:
        e = 'ee'
    elif a == 'help':
        print('''commands:
help: brings help
cd: moves directories
debug: this command is in beta
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
    else:
        print('Thats not a command! Please use help for a list of commands!')
