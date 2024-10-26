
def register():
    print('Registration Page')
    if len(user)==0:
        id=1000
    else:
        id=user[-1]['id']+1
    email=str(input('enter your email :'))
    f=0
    for i in user:
        if i['email']==email:
            f=1
            print('email already exists enter another one')
            register()
    if f==0:
        name=str(input('enter your name : '))
        phone=int(input('enter your number : '))
        password=input('enter the password : ')
        print('Registration Succesfull email id is your username')
        user.append({'id':id,'name':name,'email':email,'phone':phone,'password':password,'book':[]})

def login():
    usern=str(input('Enter Username : '))
    passw=input('Enter password : ')
    f=0
    u=''
    if usern=='admin' and passw=='admin':
        f=1
    for i in user:
        if usern==i['email'] and passw==i['password']:
            f=2
            u=i
    return f,u

def add_pr():
    print('ADD PRODUCT')
    if len(shop)==0:
        id=1
    else:
        id=shop[-1]['id']+1
    name=str(input('enter name : '))
    price=int(input('enter the price : '))
    stock=int(input('enter the stock availible : '))
    shop.append({'id':id,'name':name,'price':price,'stock':stock})

def view_pr():
    print('PRODUCT DETAILS')
    print("{:<5}{:<10}{:<10}{:<10}".format('ID','PRODUCTNAME','PRICE','STOCK'))
    print('_'*30)
    for i in shop:
        print("{:<5}{:<10}{:<10}{:<10}".format(i['id'],i['name'],i['price'],i['stock']))

def update_pr():
    id=int(input('enter the id : '))
    f=0
    for i in shop:
        if i['id']==id:
            price=int(input('enter the price : '))
            stock=int(input('enter the stock : '))
            i['price']=price
            i['stock']=stock
            print('Details Updated')
            f=1
    if f==0:
        print('invalid id')

def delete_pr():
    id=int(input('enter the id : '))
    f=0
    for i in shop:
        if i['id']==id:
            shop.remove(i)
            print('data deleted')
            f=1
    if f==0:
        print('Invalid id')


shop=[{'id':1,'name':'pen','price':'10','stock':'2'}]
user=[{'id':1000,'name':'roshan','email':'r@','phone':5522,'password':'abcd',}]

while True:
    print('''
          1.Register as new user
          2.Login
          3.Exit
          ''')
    ch=int(input('Enter your choice :'))
    if ch==1:
        register()

    elif ch==2:
        login()


        while True:
                print('''
                    1.add product
                    2.view product
                    3.update product
                    4.delete product
                    5.search product
                    6.exit
                    ''')
                c=int(input('Enter a choice :'))
                if c==1:
                    add_pr()


                elif c==2:
                    view_pr()

                elif c==3:
                    update_pr()
                
                elif c==4:
                    delete_pr()


    #             elif c==5:

                elif c==6:
                    break
                else:
                    print('invalid choice')
    elif ch==3:
        break
    else:
        print('invalid choice')

