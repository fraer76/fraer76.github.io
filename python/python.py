print("hello world")
def f(x):
    xx=x
    st3=''
    while(xx>0):
        st3=st3+str(xx%3)
        xx=xx//3
        st3=st3[::-1]
        print(st3)
        st3=st3.replace('0','3')

        print(st3)
        st3=st3.replace('2','0')
        print(st3)
        st3=st3.replace('3','2')
        print(st3)
        a=int(st3,3)
        print(a)

f(35)