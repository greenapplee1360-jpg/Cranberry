% Experiment 7b: Implementation of High Pass IIR filter

 clc; clear all; close all;
 N = 4; 
Fc = 0.4;
 [b, a] = butter(N, Fc, 'high'); 
[H, w] = freqz(b, a, 512);
 figure;
 subplot(2,1,1); plot(w/pi, abs(H)); 
title('Magnitude Response of HP IIR Filter'); xlabel('Normalized Frequency'); 
ylabel('Magnitude'); grid on;
 Fs = 1000; t = 0:1/Fs:1-1/Fs; 
x = sin(2*pi*50*t) + sin(2*pi*300*t);
 y = filter(b, a, x); subplot(2,1,2); plot(t, x); hold on; plot(t, y, 'r'); 
legend('Input','Filtered Output'); 
title('Filtering Result'); xlabel('Time (s)'); ylabel('Amplitude');
