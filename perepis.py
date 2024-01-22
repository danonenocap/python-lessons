f=open('Perepis2.txt','r', encoding='utf-8-sig')
people = 0
old = 0
for line in f:
    fio = line.split()
    year = fio[3][-4:]
    year = int(year)
    if year < 1978:
        print(fio[0])
        people +=1


print('older: ', old)
print("people: ", people)

f.close()


