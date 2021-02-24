def A():
    print("A")

def B():
    def C():
        print('C')
    print('B')
    A()
    C()