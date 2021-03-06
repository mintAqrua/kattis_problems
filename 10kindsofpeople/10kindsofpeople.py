


r,c=map(int,raw_input().split())

grid=[raw_input() for _ in xrange(r)]

moves={(1,0),(0,1)}

class uf(object):
	def __init__(self,n):
		self.parent=range(n)
	def find(self,u):
		#self.make(u)
		if self.parent[u]==u:
			return u
		self.parent[u]=self.find(self.parent[u])
		return self.parent[u]
	def make(self,u):
		if u not in self.parent:
			self.parent[u]=u
	def union(self,u,v):
		#self.make(u)
		#self.make(v)
		u,v=map(self.find,[u,v])
		if u!=v:
			if u>v:
				u,v=v,u
			self.parent[v]=u
	def connected(self,u,v):
		return self.find(u)==self.find(v)


def inbound(x,y):
	return 0<=x<r and 0<=y<c

lookup=uf(r*c)

for i in xrange(r):
	for j in xrange(c):
		for dx,dy in moves:
			x=i+dx
			y=j+dy
			if inbound(x,y) and grid[x][y]==grid[i][j]:
				lookup.union(i*c+j,x*c+y)

n=int(raw_input())

sub1=lambda x: x-1

for _ in xrange(n):
	r1,c1,r2,c2=map(int,raw_input().split())
	r1,c1,r2,c2=map(sub1,[r1,c1,r2,c2])
	if grid[r1][c1]!=grid[r2][c2]:
		print 'neither'
	else:
		res=lookup.connected((r1*c+c1),(r2*c+c2))
		if res:
			print 'decimal' if grid[r1][c1]=='1' else 'binary'
		else:
			print 'neither'






