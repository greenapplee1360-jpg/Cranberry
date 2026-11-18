% Experiment 6b: Implementation of High Pass FIR filter 
clc; clear all; close all;
 N = 31; 
Fc = 0.4; 

b = fir1(N-1, Fc, 'high', hamming(N)); 
[H, w] = freqz(b, 1, 512); 
figure;
 subplot(2,1,1); plot(w/pi, abs(H));
 title('Magnitude Response of HP FIR Filter'); xlabel('Normalized Frequency'); 
ylabel('Magnitude'); grid on; 
Fs = 1000; t = 0:1/Fs:1-1/Fs; 
x = sin(2*pi*50*t) + sin(2*pi*300*t); 
y = filter(b, 1, x); subplot(2,1,2); plot(t, x); hold on; plot(t, y, 'r'); legend('Input','Filtered Output'); 
title('Filtering Result'); xlabel('Time (s)'); ylabel('Amplitude');
