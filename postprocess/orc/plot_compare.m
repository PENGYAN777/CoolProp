clear all;
clc;
% read experiment pressure, skip the header
exp = dlmread('ex.csv');
##exp_x = (exp(:,1)-70)/10;
exp_x = exp(:,1)/10-7.1;
exp_p = exp(:,3)*10^5;



% read coolprop inviscid model
cp_euler = dlmread('ccolprop_euler.csv','',1,0);
##cp_euler = dlmread('pr.csv','',1,0);
cp_euler_x = cp_euler(:,5);
cp_euler_p = cp_euler(:,2);
cp_euler_m = cp_euler(:,1);
##
% read coolprop viscous model
##cp_rans = dlmread('pr_rans.csv','',1,0);
cp_rans = dlmread('coolprop_rans.csv','',1,0);
cp_rans_x = cp_rans(:,5);
cp_rans_p = cp_rans(:,2);
cp_rans_m = cp_rans(:,1);

% plot comparison
figure(1)
##plot(PR_x, PR_p,'k',"linewidth", 2);
##hold on
##grid on
plot(cp_euler_x, cp_euler_p,'k',"linewidth", 2);
hold on
grid on
plot(cp_rans_x, cp_rans_p,'r',"linewidth", 2);
hold on
grid on
plot(exp_x, exp_p,'o',"linewidth", 2);
hold on
grid on
xlabel('X[mm]')
ylabel('P[Pa]')
title('Pressure along symmetry axis')
legend boxoff
set(gca, "linewidth", 2, "fontsize", 12);
##axis ([0 0.13 2e5 9e5])
legend("CoolProp inviscid","CoolProp viscous","Experiment")
