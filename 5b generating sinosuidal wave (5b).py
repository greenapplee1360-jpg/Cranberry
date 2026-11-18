% Experiment 5b: Generation of Sinusoidal signal through filtering 
clc; clear all; close all;
 Fs = 1000; t = 0:1/Fs:1-1/Fs; 
% Composite input signal containing multiple frequencies 
x = sin(2*pi*50*t) + sin(2*pi*150*t) + sin(2*pi*300*t); 
% Design bandpass filter to extract 150 Hz component 
Fc1 = 100/(Fs/2);   % Normalized lower cutoff 
Fc2 = 200/(Fs/2);   % Normalized upper cutoff 
[b, a] = butter(4, [Fc1 Fc2], 'bandpass'); 

y = filter(b, a, x);   % filtered output ~ pure sinusoid at 150 Hz 
subplot(2,1,1); plot(t, x); title('Composite Input Signal'); xlabel('Time (s)'); 
subplot(2,1,2); plot(t, y); title('Extracted Sinusoidal Signal (150 Hz) via Filtering'); xlabel('Time (s)');
