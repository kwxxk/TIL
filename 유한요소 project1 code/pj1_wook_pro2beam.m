% beam structure nodal force
% 2018100643 강욱

clear
clc

L=8; E=210E9; v=0.3; I=4e-4;

% N과 B matrix 지정
syms x
N1=(2*x^3-3*x^2*l+l^3)/l^3; N2=(x^3*l-2*x^2*l^2+x*l^3)/l^3;
N3=(-2*x^3+3*x^2*l)/l^3; N4=(x^3*l-x^2*l^2)/l^3;
N=[N1 N2 N3 N4];
B=diff(diff(N,x),x);             

%  local stiffness matrix  
local_k=E*ii/l^3*[12 6*l -12 6*l; 6*l 4*l^2 -6*l 2*l^2; ...
    -12 -6*l 12 -6*l; 6*l 2*l^2 -6*l 4*l^2]; 
% golbal stiffness matrix K
K=zeros(n_dof);
for i=1:n_ele
    K(1+2*(i-1):2*(i-1)+4,1+2*(i-1):2*(i-1)+4) =...
        K(1+2*(i-1):2*(i-1)+4,1+2*(i-1):2*(i-1)+4)+local_k;
end