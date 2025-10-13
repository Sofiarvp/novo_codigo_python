print('questao 1')
i=0
for i in range (1,11):
    if i==5:
        print(i)
        break

print('questao 2')
i=0
for i in range (1,11):
    if i%2!=0:
        print(i)
        continue

print('questao 3')
i=0
for i in range (1,21):
    while True:
        if i<=15:
            print(i)
        break
    
print('questao 4')
nomes=['Ana', 'Maria', 'Aluska', 'Sofia', 'Pedro', 'Adolfo']
for nome in nomes:
    if nome.startswith('A'):
        continue
    else:
        print(nome)
        
print('questao 5')
i=11
while i>=8:
    i-=1
    print (i)
    
print('questao 6')
i=1
while i<=15:
    if i%3==0:
        i+=1
        continue
print(i)
i+=1

            
    

