print('Hello, Django Girls')
if 3>2: 
    print('it works')
if 5>2:
    print('5 is indeed grater than 2')
else:
    print('5 is not grather than 2')

name = 'sonja'
if name =='ola':
    print('hey ola')
elif name == 'sonja':
    print ('hey sonja')
else:
    print('hey anonymus')
#cambiar el volumen si está muy bajo
volume = 57
if volume <20:
    print('its a kinda quiet')
elif 20<=volume <=40:
    print('its nice for background music')
elif 40<=volume<60:
    print('perfect! i can hear all details')
elif 60<=volume <80:
    print('nice for parties')
elif 80<=volume<100:
    print('a bit loud')
else:
    print('me duelen los oidos :(')

def hi():
    print('hi there')
    print('how are you')
hi()

def hi(name):
    if name =='ola':
        print('hey ola')
    elif name == 'sonja':
        print ('hey sonja')
    else:
        print('hey anonymus')
hi('pedro')

def hi(name):
    print('hi '+name+'!')
hi('rachel')
#bucles


def hi(name):
    print('hi '+name+'!')
girls=['rachel', 'mónica', 'phoebe', 'ola', 'you']
for name in girls:
    hi(name)
    print('next girl')

for i in range(1,6):
    print(i)