function [dd stress_plot]= beam_structure(n_ele) % element 개수 입력받아 돌아가는 함수
% given info
L= 10; l=L/n_ele; E=210*10^9; ii=4*10^-4;  
n_node=n_ele+1;
dof_per_node=2;
n_dof=n_node * dof_per_node;  % 노드 수와 자유도를 계산

% N과 B matrix 지정
syms x
N1=(2*x^3-3*x^2*l+l^3)/l^3; N2=(x^3*l-2*x^2*l^2+x*l^3)/l^3;
N3=(-2*x^3+3*x^2*l)/l^3; N4=(x^3*l-x^2*l^2)/l^3;
N=[N1 N2 N3 N4];
B=diff(diff(N,x),x);             

% 1. local stiffness matrix  
local_k=E*ii/l^3*[12 6*l -12 6*l; 6*l 4*l^2 -6*l 2*l^2; ...
    -12 -6*l 12 -6*l; 6*l 2*l^2 -6*l 4*l^2]; 
% 2. golbal stiffness matrix K
K=zeros(n_dof);
for i=1:n_ele
    K(1+2*(i-1):2*(i-1)+4,1+2*(i-1):2*(i-1)+4) =...
        K(1+2*(i-1):2*(i-1)+4,1+2*(i-1):2*(i-1)+4)+local_k;
end

% 3. nodal force from w
f=zeros(n_dof/2,1);  m=zeros(n_dof/2,1);
w=6000*l; bs=l*w;
%defelction
for i=1:n_ele
    f(i:i+1,1)=f(i:i+1,1)+[-0.3*w*l/2-0.5*bs*(i-1) -0.7*w*l/2-0.5*bs*(i-1)]';
end
%moment
for i=1:n_ele
    m(i:i+1,1)=m(i:i+1,1)+[-w*l^2/30-w*l^2/12*(i-1) w*l^2/20+w*l^2/12*(i-1)]';
end



F=zeros(n_dof,1);
for i=1:n_dof/2
   F(1+2*(i-1),1)=f(i,1);
   F(2*i,1)=m(i,1);
end

% 4. boundary condition
d=zeros(n_dof,1);
d(1,1)=0;

% 5. displacement calculation
d(3:n_dof,1)=K(3:n_dof,3:n_dof)^-1*F(3:n_dof,1);

%6. stress calulation 
b=B;
stress=zeros(8,2);
for i=1:n_ele
      B=subs(b,x,0);
      stress(i,1)=0.1*E*B*d(1+2*(i-1):(2*i)+2,1);
   
      B=subs(b,x,l);
      B=double(B);
      stress(i,2)=0.1*E*B*d(1+2*(i-1):(2*i)+2,1);    
end
stress_plot=stress(:,2);

% displacment를 Table 형식으로 출력 
disp(' ') 
disp('deflection')
disp(' ')
for i=1:1:n_node
 fprintf('d(%d) = %10.10f \n', i , d(2*i-1) );
end

% stress를 Table 형식으로 출력
disp(' ') 
disp('Stress')
disp(' ')
for i=1:n_ele
 fprintf('sigma_ele(%d) = %.1f %.1f \n', i , stress(i,1), stress(i,2));
end

dd=[];
for i=1:n_dof/2
   dd(i)=d(2*i-1);
end
