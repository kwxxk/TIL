function [u,l,sigma]=truss_structure(n_ele) 
% element 개수 입력 /  ele_length, displacement, sigma 반환 함수 

% given info: E,A,L
L= 6; l=L/n_ele; E=70e9; A=5e-4;
n_node=n_ele+1; 
dof_per_node=1;
n_dof=n_node * dof_per_node;  % 노드 수와 자유도 계산

syms x
N=[1-x/l x/l] ;
B=[-1/l 1/l ] ;             % N과 B matrix 지정
 
% 1. local stiffness matrix  
local_k=A*E/l*[1 -1 ; -1 1]; % local k 생성
 
% 2. golbal stiffness matrix K
K=zeros(n_dof);
for i=1:n_ele
    K(i:i+1,i:i+1) = K(i:i+1,i:i+1)+local_k;
end
 
% 3. nodal force from Ts 
f=zeros(n_node,1);
for i=1:n_ele
    f(i:i+1,1)=f(i:i+1,1)+int((N'*(20*x+(20*l*(i-1)+10))*1000),x,0,l);
end
 
% 4. boundary condition
u=zeros(n_node,1);
u(1,1)=0;

% 5. displacement calculation
u(2:n_node,1)=K(2:n_node,2:n_node)^-1*f(2:n_node,1);

%6. stress calulation 
sigma=zeros(n_ele,1);
for i=1:n_ele
sigma(i,1)=E*B*u(i:i+1,1);
end
 
% displacment 를 table 형식으로 출력 
disp(' ') 
disp('Nodal displacement')
disp(' ')
for i=1:1:n_node
 fprintf('u(%d) = %10.10f \n', i , u(i) );
end
 
% Stress를 table 형식으로 출력 
disp(' ') 
disp('Stress')
disp(' ')
for i=1:n_ele
 fprintf('sigma(%d) = %.1f \n', i , sigma(i) );
end
