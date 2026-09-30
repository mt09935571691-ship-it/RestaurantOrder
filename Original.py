order = {'pizza': 1800, 'HotDog': 1000, 'stake': 2000}

def x(order):
    c = 0
    name = input('نام خود را وارد کنید:\n')
    print('خوش آمدی',name)

    a = input('شفارش خود را وارد کنید :\n')
    a = a.split()

    b =input('تعداد سفارش را وارد کنید :\n')
    b = b.split()

    for i in range(len(a)):
        if a[i] == 'pizza':
            c = c + order['pizza'] * int(b[i])
        if a[i] == 'HotDog':
            c = c + order['HotDog'] * int(b[i])
        if a[i] == 'stake':
            c = c + order['stake'] * int(b[i])

    print('نام :',name)
    print('نوع سفارش :',a)
    print(c,'مبلغ پرداختی :')
x(order)