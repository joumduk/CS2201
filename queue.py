#Stack


def QueueEmpty(Q):
    if len(Q)==0:
        return True
    else:
        return False

def Enqueue(Q,x):
    Q.append(x)
def Dequeue(Q):
    x=Q[0];
    Q.remove(Q[0])
    return x

A=[]
print QueueEmpty(A)
print A
print Enqueue(A,6)
print Enqueue(A,5)
print A
print Dequeue(A)
print A
