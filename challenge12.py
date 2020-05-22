# Lists

L = list()
for _ in range(int(input())):
    cmd = input().split()
    command = cmd[0]
    args = cmd[1:]
    if len(cmd) > 1:
        eval('L.{0}{1}'.format(command,tuple(map(int,args))))
    elif command == 'print':
        print(L)
    else:
        eval('L.{0}()'.format(command))