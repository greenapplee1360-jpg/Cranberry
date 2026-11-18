% Experiment 9: Implementation of I/D Sampling Rate Converter
 clc; clear all; close all; 
Fs = 8000; t = 0:1/Fs:1-1/Fs; 
x = sin(2*pi*300*t); 
I = 3;    % Interpolation factor
D = 2;    % Decimation factor 
y = resample(x, I, D);   % Rational sampling rate conversion by I/D
subplot(2,1,1); stem(x(1:60)); title('Original Signal');
subplot(2,1,2); stem(y(1:90)); title(['Resampled Signal (I/D = ' num2str(I) '/' num2str(D) ')']);
