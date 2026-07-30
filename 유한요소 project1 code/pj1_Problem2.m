%-----------------------------------------------------------------------------------------%
% 2022 유한요소법 Project1
% 2018100722 윤인수
% Problem 1
%-----------------------------------------------------------------------------------------%
clear
clc

%% Initial conditions
L = 8;                                                                % lenght of a beam
E = 210e9;                                                            % elastic modulus
I = 4*10^-4;                                                          % moment of inertia

%% Stresses & Displacements at each elements
[ud2, ur2, sigma2] = Prob2_func(2,E,I,L);
[ud4, ur4, sigma4] = Prob2_func(4,E,I,L);
[ud8, ur8, sigma8] = Prob2_func(8,E,I,L);
[ud16, ur16, sigma16] = Prob2_func(16,E,I,L);

%% Plot
figure()
plot(linspace(0,L,3),ud2, linspace(0,L,5),ud4, linspace(0,L,9),ud8)
xlabel('Length(m)')
ylabel('Displacement(m)')
title('Deflection')
legend('2 elements', '4 elements', '8 elements')
grid on
 
figure()
plot(linspace(0,L,3),sigma2, linspace(0,L,5),sigma4, linspace(0,L,9),sigma8)
xlabel('Length (m)')
ylabel('Stress (N/m^2)')
title('Bending stress')
legend('2 elements', '4 elements', '8 elements')
grid on