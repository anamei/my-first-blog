print('Hello,Django girls')
name='Ana Mei'
if name == 'Ola':
        print('Hey Ola')
elif name == 'Sonja':
    print('Hey Sonja')
else:
    print('Hey anonymous!')
def hi():
    print('Hi there!')
    print('How are you?')
    hi()
def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja')
    else:
        print('Hi anonymous')
hi('Leandra')
def hi(name):
    print('Hi' + name +'!')
hi('Rachel')
girls = ['Rachel','Monica','Phoebe','Ola','You']
for name in girls:
    hi(name)
    print('Next girl')
for i in range(1, 6):
    print(i)
