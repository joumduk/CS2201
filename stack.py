#Stack

def stack_empty(S):
    if len(S)==0:
        return True
    else:
        return False
def StackPush(S,x):
    S.append(x)
    
def StackPop(S):
    if stack_empty(S):
        raise Exception ('underflow')
    else:
        val=S[len(S)-1]
        S.remove(len(S))
        return val
#A=[]
#print StackPop(A)
#print StackPush(A,6)
#print A
