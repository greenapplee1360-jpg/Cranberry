% Experiment 10: Impulse Response of First Order and Second Order Systems 
clc; clear all; close all; 
% First order system: y(n) = x(n) + 0.5y(n-1)
 b1 = 1; a1 = [1 -0.5]; 
[h1, n1] = impz(b1, a1, 30); 
% Second order system: y(n) = x(n) + 0.6y(n-1) - 0.3y(n-2) 
b2 = 1; a2 = [1 -0.6 0.3]; 
[h2, n2] = impz(b2, a2, 30); 
subplot(2,1,1); stem(n1, h1);
 title('Impulse Response - First Order System'); xlabel('n'); ylabel('h(n)');

 subplot(2,1,2); stem(n2, h2);
 title('Impulse Response - Second Order System'); xlabel('n'); ylabel('h(n)');
