import random
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A']
n=[1,2,3,4,5,6,7,8,9,0]
c=['!','@','#','$','*']
print("!Welcome to Arul's Password Generator!")
nofa=int(input("How many letters do you want in your password: "))
nofn=int(input("How many numbers do you want in your password: "))
nofc=int(input("How many chars do you want in your password: "))
password=[]
for i in range(0,nofa):
    p=password.append(random.choice(a))
for j in range(0,nofn):
    ap=random.randint(n[0],len(n)-1)
    pa=password.append(str(ap))
for k in range (0,nofc):
    pas=password.append(random.choice(c))
random.shuffle(password)
s_password=""
for i in password:
    s_password+=i

print("Your password is :\n",s_password)
