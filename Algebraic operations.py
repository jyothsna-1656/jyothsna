import numpy as np
a=np.array(input("enter the input a:"));
b=np.array(input("enter the input b:"));
c=a+b;
d=a-b;
e=a*b
f=a/b
g=np.linalg.det(a)
h=np.linalg.inv(a)
i=np.linalg.eig(a)
j=np.max(a)
k=np.min(a)
l=np.zeros((3,3))
m=np.ones((1,2))
p=(a.transpose())
s=np.eye(3)
r=np.linalg.matrix_rank(a)
x=np.square(a)
y=np.trace(a)
print "sum:\n",c;
print "difference:\n",d;
print "multiplication of 2 matrix:\n",e
print "division of 2 matrix:\n",f
print "determinant of the matrix:",g
print "inverse of the matrix:\n",h
print "eigen values of the matrix:\n",i
print "max of a:",j
print "min of a",k
print "zero matrix:\n",l
print "one matrix:\n",m
print "transpose matrix:\n",p
print "identity matrix:\n",s
print "rank of the matrix:",r
print "square of the matrix:\n",x
print "trace of the matrix:",y



