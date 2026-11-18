% Experiment 6a: Implementation of Low Pass FIR filter
 clc; clear all; close all; 
N = 31;            % Filter order (odd length for Type I linear phase) 
Fc = 0.3;          % Normalized cutoff frequency (0 to 1, 1 = Nyquist) 

b = fir1(N-1, Fc, 'low', hamming(N));   % LPF using Hamming window 
[H, w] = freqz(b, 1, 512); 
figure; 
subplot(2,1,1); plot(w/pi, abs(H));
 title('Magnitude Response of LP FIR Filter'); xlabel('Normalized Frequency'); 
ylabel('Magnitude'); grid on;
 % Applying filter to a test signal
 Fs = 1000; t = 0:1/Fs:1-1/Fs; 
x = sin(2*pi*50*t) + sin(2*pi*300*t); 
y = filter(b, 1, x); 
subplot(2,1,2); plot(t, x); hold on; plot(t, y, 'r');
 legend('Input','Filtered Output'); 
title('Filtering Result'); xlabel('Time (s)'); ylabel('Amplitude');
