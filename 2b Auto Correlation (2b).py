% Experiment 2_b: Program for Computing Auto Correlation
 clc; clear all; close all;
 x = input('Enter the sequence x(n): ');   % e.g. [1 2 3 4] 
N = length(x);
 r = xcorr(x, x);    % auto-correlation using built-in function 
disp('Auto-correlation sequence r(n):'); 
disp(r);
 n = -(N-1):(N-1); 
stem(n, r); title('Auto-correlation of x(n)'); 
xlabel('Lag (n)'); ylabel('r(n)'); grid on;
