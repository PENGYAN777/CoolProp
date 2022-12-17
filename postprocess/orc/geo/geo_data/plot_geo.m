clear all;
clc;
% inlet
x_1 = [-4 -4];
y_1 = [0 5.0005];
%  wall
wall = dlmread('wall.csv','', 1, 0);
x_2 = wall(:,1);
y_2 = wall(:,2);
% outlet
x_3 = [6.1618 6.1618];
y_3 = [1.8254 0];

% sys
x_4 = [6.1618 -4];
y_4 = [0 0];


##% read coolprop inviscid model
##cp = dlmread('coolprop.csv','',1,0);
##cp_x = cp(:,5);
##cp_p = cp(:,2);
##cp_m = cp(:,1);

% plot comparison
figure(1)
plot(x_1, y_1,'r',"linewidth", 3);
hold on
grid on
plot(x_2, y_2,'g',"linewidth", 3);
hold on
grid on
plot(x_3, y_3,'b',"linewidth", 3);
hold on
grid on
plot(x_4, y_4,'k',"linewidth", 3);
hold on
grid on

xlabel('X[mm]')
ylabel('Y[mm]')
title('Computational domain of the nozzle for R1233zd(E)')
legend boxoff
set(gca, "linewidth", 2, "fontsize", 14);
##axis ([0 12 0 8])
legend("inlet","upper wall","outlet","symmetry")

