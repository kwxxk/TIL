function [a,b,c,AA]=albegan(xi,yi,xj,yj,xm,ym)
al1=xj*ym-yj*xm;
al2=yi*xm-xi*ym;
al3=xi*yj-yi*xj;

be1=yj-ym;
be2=ym-yi;
be3=yi-yj;

gan1=xm-xj;
gan2=xi-xm;
gan3=xj-xi;

Al_be_gan=[[al1 al2 al3] ; [be1 be2 be3] ; [gan1 gan2 gan3]];
a=Al_be_gan(1,:);
b=Al_be_gan(2,:);
c=Al_be_gan(3,:);
AA=al1+al2+al3;


