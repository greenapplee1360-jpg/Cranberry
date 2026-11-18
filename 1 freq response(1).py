% Experiment 4: Frequency response of a system given by difference equation
 clc; 
clear all;
 close all;
 % Example: y(n) = 0.5y(n-1) + x(n)  ->  H(z) = 1 / (1 - 0.5 z^-1) 
b = input('Enter numerator coefficients [b0 b1 ...]: ');   % e.g. [1] 
a = input('Enter denominator coefficients [a0 a1 ...]: '); % e.g. [1 -0.5] 

[H, w] = freqz(b, a, 512); 
subplot(2,1,1); plot(w/pi, abs(H));
 title('Magnitude Response'); xlabel('Normalized Frequency (\times\pi rad/sample)'); 
ylabel('|H(e^{j\omega})|'); grid on; 
subplot(2,1,2); plot(w/pi, angle(H));
 title('Phase Response'); xlabel('Normalized Frequency (\times\pi rad/sample)'); 
ylabel('Phase (rad)'); grid on;
