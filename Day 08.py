# Dictionaries and Maps

contact_diary = dict()
for _ in range(int(input())):
    contact = list(input().split())
    contact_diary[contact[0]] = contact[1]
while True:
    try:
        search = str(input())
        if search in contact_diary:
            number = contact_diary[search]
            print('{}={}'.format(search,number))
        else:
            print('Not found')
    except:
        break
    