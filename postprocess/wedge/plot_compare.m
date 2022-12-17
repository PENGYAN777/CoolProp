% read experiment total cp_euleressure, skip the header
exp = csvread('experiment.csv');
exp_x = exp(:,1);
exp_tp = exp(:,3);



##% read cp_euler model
##cp_euler = dlmread('cp_euler.csv','',2,0);
##cp_euler_x = cp_euler(:,4);
##cp_euler_tp = cp_euler(:,10);
% read coolcp_eulerop_euler
cp_euler = dlmread('coolprop_euler.csv','',1,0);
cp_euler_x = cp_euler(:,4);
cp_euler_tp = cp_euler(:,10);



% read Coolcp_eulerop model
##cp = dlmread('coolcp_eulerop.csv','',1,0);
##cp_x = cp(:,5);
##cp_p = cp(:,2);

% plot comparison
figure(1)
plot(cp_euler_x, cp_euler_tp,'r',"linewidth", 2);
hold on
grid on
##plot(cp_x, cp_p,'r',"linewidth", 2);
##hold on
##grid on
plot(exp_x, exp_tp,'o',"linewidth", 2);
hold on
grid on
xlabel('X/D')
ylabel('P/Pt')
title('Pitot pressure ratio along symmetry axis')
legend boxoff
set(gca, "linewidth", 2, "fontsize", 14);
axis ([0 1.6 0 1])
####errorbar(exp_x,exp_p,exp_up,'ok','MarkerSize',2,'MarkerFaceColor', 'k')
##errorbar(exp_x,exp_p,exp_up,'ok')
legend("CoolProp inviscid","Experiment")
