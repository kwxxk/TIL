%-----------------------------------------------------------------------------------------%
% 2022 유한요소법 Project1
% 2018100722 윤인수
% Problem 1
%-----------------------------------------------------------------------------------------%
function [u_d, u_r, sigma] = Prob2_func(ne,E,I,L)
    l = L/ne;                                                             % lenght of a beam(for 1 element)
    nn = ne + 1;                                                          % number of nodes
    d_full = 1:nn;                                                        % displacement
    r_full = 1:nn;                                                        % rotation

    %% Stiffness matrix K
    K = zeros(nn*2,nn*2);               
    k_local = zeros(nn*2,nn*2);
    k = E*I/ l^3 * [12 6*l -12 6*l
                    6*l 4*l^2 -6*l 2*l^2
                    -12 -6*l 12 -6*l
                    6*l 2*l^2 -6*l 4*l^2];

    for i = 1:ne
        k_local(2*i-1:2*i+2,2*i-1:2*i+2) = k;
        K = K + k_local;
        k_local = zeros(nn*2,nn*2);
    end

    %% Force F (for uniformly distributed load)
    w = -10e3;                                                            
    f = zeros(1,nn);                                                        
    m = zeros(1,nn);                                                        

    f_local = zeros(1,nn);
    m_local = zeros(1,nn);

    for i = 1:ne
        f_local(i:i+1) = w * l/2;
        m_local(i:i+1) = [-w*l^2/12 w*l^2/12];

        f = f + f_local;
        m = m + m_local;

        f_local = zeros(1,nn);
        m_local = zeros(1,nn);
    end

    F(2*[1:nn]-1) = f;
    F(2*[1:nn]) = m;

    %% B.Cs
    Bc_d = [1, ne/2+1];
    Bc_r = [1];

    d_full(Bc_d) = [];
    r_full(Bc_r) = [];

    Bc_index = sort([2*d_full-1 2*r_full]);

    %% Displacement
    u = zeros(1,2*nn);
    u(Bc_index) = K(Bc_index,Bc_index)\F(Bc_index)';

    u_d = u(2*[1:nn]-1);
    u_r = u(2*[1:nn]);

    %% Stresses
    x = [0; l];
    B = [(12*x - 6*l)/l^3 (6*x*l - 4*l^2)/l^3 (-12*x + 6*l)/l^3 (6*x*l - 2*l^2)/l^3];
    sigma = zeros(nn,1);
    for i = 1:ne
        sigma(i) = 0.1*E*B(1,:)*u(2*i-1:2*i+2)';
    end
    sigma(nn) = -0.1*E*B(2,:)*u(2*i-1:2*i+2)';
end