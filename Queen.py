class Board:

    def __init__(self,N,n=0):
        self.n=n
        self.N=N
        self.b=[]
        for i in range(N): self.b.append([0]*N)

    def display(self,title):
        print(f"\n{title}\n"+'_'*(2*self.N+1))
        for i in self.b:
            print('|',end='')
            for j in i:
                if j==2: print('0',end='|')
                else: print('_',end='|')
            print()
        print('_' * (2 * self.N + 1)+"\n")

    def placeQ(self,i,j):
        if self.b[i][j] != 0: raise AssertionError("Queen cannot be placed at the given index.")
        self.b[i]=[1]*self.N
        for k in range(self.N): self.b[k][j]=1
        s,d=(i+j),(i-j)
        for r in range(self.N):
            for c in range(self.N):
                if r+c==s or r-c==d:
                    self.b[r][c]=1
        self.b[i][j]=2

    def copy(self):
        B=Board(self.N,self.n+1)
        for i in range(B.N):
            for j in range(B.N):
                B.b[i][j]=self.b[i][j]
        return B

    def blanksIn(self,r):
        s=self.N-sum(self.b[r])
        if 2 in self.b[r]: return s+1
        else: return s

    def blank(self,n):
        for i in range(self.N):
            for j in range(self.N):
                if self.b[i][j]==0:
                    if n>0: n-=1
                    else: return i,j
        raise MemoryError("Board is full!")

class counter:

    def __init__(self, n):
        self.n = n

    def add(self, n):
        self.n += n

ctr=counter(0)

def fill(B,r):
    n=B.blanksIn(r)
    if n==0:
        return
    for i in range(n):
        x,y=B.blank(i)
        A=B.copy()
        A.placeQ(x,y)
        if(r+1==A.N):
            ctr.add(1)
            A.display(f"Arrangement {ctr.n}")
            return
        else:
            fill(A,r+1)


A=Board(int(input("N = ")))
fill(A,0)
print(f"Number of ways = {ctr.n}")