% Experiment 2: Linear Convolution of two finite length sequences
 clc; clear all; close all;
 x = input('Enter first sequence x(n): ');    % e.g. [1 2 3] 
h = input('Enter second sequence h(n): ');   % e.g. [1 1 1] 

y = conv(x, h);   % built-in linear convolution
 disp('Linear Convolution output y(n):'); 
disp(y);

 n1 = 0:length(x)-1; 
n2 = 0:length(h)-1; 
n3 = 0:length(y)-1; 

subplot(3,1,1); stem(n1, x); title('x(n)'); xlabel('n');
 subplot(3,1,2); stem(n2, h); title('h(n)'); xlabel('n');
 subplot(3,1,3); stem(n3, y); title('y(n) = x(n) * h(n)'); xlabel('n');
