% inlet
x_1 = [0 0 0];
y_1 = [0 1 5];
% upper wall
x_2 = [0 1 11];
y_2 = [5 5 5];
% outlet
x_3 = [11 11 ];
y_3 = [5 2.68];

% lower wall
x_4 = [11 1 0];
y_4 = [2.68 0 0];


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
title('Computational domain of the wedge')
legend boxoff
set(gca, "linewidth", 2, "fontsize", 14);
axis ([0 12 0 8])
legend("inlet","upper wall","outlet","lower wall")

