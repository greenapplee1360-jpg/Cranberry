% Experiment 8b: Implementation of Interpolation Process
 clc; clear all; close all; 
Fs = 2000; t = 0:1/Fs:1-1/Fs;
 x = sin(2*pi*100*t); 
L = 4;                 
y = interp(x, L);         
subplot(2,1,1); stem(x(1:50)); title('Original Signal (first 50 samples)');
 subplot(2,1,2); stem(y(1:200)); title(['Interpolated Signal by factor ' num2str(L)]);
