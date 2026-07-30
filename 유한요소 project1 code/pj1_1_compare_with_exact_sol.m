clc,clear
%% exact solution
E=70e9; A=5e-4;
x=0:0.00001:6;
ue = ((-10/3)*1000*x.^3-5*1000*x.^2+420000*x)/(A*E);
subplot(121)
plot(x,ue)
set(gcf,'Color','w');
%% FEM_displacement plot
hold on 
[u_1,l_1,sigma_1]= truss_structure(1); x=0:l_1:6; plot(x,u_1) 
[u_2,l_2,sigma_2]= truss_structure(2); x=0:l_2:6; plot(x,u_2)
[u_4,l_4,sigma_4]= truss_structure(4); x=0:l_4:6; plot(x,u_4)
% Abaqus solution plot, n=4
xa=[0 1.517357111 3.032142878 4.542428493 6.046285629];
ua=[0 0.017357143 0.032142859 0.042428572 0.046285715];
plot(xa,ua,'o')
hold off
grid on
xlabel('Lenth of Truss(m)'); ylabel('displacement(m)');
legend('Exact','1 ele','2 ele','4 ele','abaqus','location','best')
%% stress plot
subplot(122)
grid on
hold on
x=linspace(0,6,10000); n=length(x); 
sigma_exact=(-10*x.^2-10.*x+420)*1000/A; plot(x,sigma_exact) 
y_1(1:n)=sigma_1; plot(x,y_1)
y_2(1:n/2)=sigma_2(1,1); y_2(n/2+1:n)=sigma_2(2,1); plot(x,y_2)
y_4(1:n/4)=sigma_4(1,1); y_4(n/4+1:n/2)=sigma_4(2,1); 
y_4(n/2+1:n*3/4)=sigma_4(3,1); y_4(n*3/4+1:n)=sigma_4(4,1);  plot(x,y_4)
sigma_a=[8.1E+08 7.5E+08 5.85E+08 3.3E+08 1.8E+08 ];
xa= [0 1.517357111 3.032142878 4.542428493 6.046285629]; plot (xa,sigma_a,'x','markersize',10)
x=[0 1.517357111 1.517357111 3.032142878 3.032142878 4.542428493 4.542428493 6.046285629];
u=[810000000 810000000 690000000 690000000 480000000 480000000 180000000 180000000]; % avg=0%
plot(x,u,'o')
hold off
xlabel('Lenth of Truss(m)'); ylabel('Stress(N/m^2)');
legend('Exact','1 ele','2 ele','4 ele','abaqus(avg=75%)','abaqus(avg=0%)','location','best')





