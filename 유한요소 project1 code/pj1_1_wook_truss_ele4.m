% element 4
L=4;
n_ele = 4;
n_node = n_ele + 1;
l=L/n_ele;
syms x
N=[1-x/l x/l] ;
B=[-1/l 1/l ] ;
f=zeros(n_node,1);
for i=1:n_ele
    f(i:i+1,1)=f(i:i+1,1)+int((N'*(30*x+(30*l*(i-1)))*1000),x,0,l);
end