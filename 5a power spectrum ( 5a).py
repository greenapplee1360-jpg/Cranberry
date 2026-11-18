% Experiment 5a: Determination of Power Spectrum of a given signal 
clc; clear all; close all; 
Fs = 1000;              % Sampling frequency
 t = 0:1/Fs:1-1/Fs;      % Time vector 
x = sin(2*pi*50*t) + sin(2*pi*120*t) + 0.5*randn(size(t)); % noisy signal 

N = length(x);
 X = fft(x, N); 
Pxx = (abs(X).^2) / N;   
f = (0:N-1)*(Fs/N);  
plot(f(1:N/2), Pxx(1:N/2)); 
title('Power Spectrum of the Signal');
 xlabel('Frequency (Hz)'); ylabel('Power'); grid on;
