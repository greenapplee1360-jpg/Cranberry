% Experiment 8a: Implementation of Decimation Process
 clc; clear all; close all; 
Fs = 8000; t = 0:1/Fs:1-1/Fs;
 x = sin(2*pi*200*t) + 0.5*sin(2*pi*400*t); 

M = 4;                
y = decimate(x, M);     
subplot(2,1,1); stem(x(1:100)); title('Original Signal (first 100 samples)');
subplot(2,1,2); stem(y(1:25)); title(['Decimated Signal by factor ' num2str(M)]);
