#Lists

"""
Getatrr(--)-
Python, it is getattr(Object, Function)(Vars)
Example of using this method below. Again, this is assuming the user isn't going to enter in an invalid command!

This can be done a bit shorter by just catching an exception (you could also catch TypeError):
"""

if __name__ == '__main__':
    l=[]
    for _ in range(int(input())):
        comman,*args=input().split()
        try:
            getattr(l,comman)(*(int(x)for x in args))
        except AttributeError:
            print(l)