% Experiment 3: To find DFT / IDFT of given DT signal 
clc; clear all; close all;  
 % Input sequence 
x = input('Enter the input sequence x(n): ');   % e.g. [1 2 3 4]
 N = length(x); 
  % Compute DFT using built-in function
 X = fft(x, N); 
disp('DFT of the sequence X(k):'); 
disp(X); 
  % Magnitude and Phase of DFT
 mag = abs(X);
 phase = angle(X); 
  % Compute IDFT to verify (should return original sequence) x_recovered = ifft(X, N); 
disp('IDFT (reconstructed) sequence:'); 
disp(real(x_recovered));   
% Plotting 
n = 0:N-1;  k = 0:N-1;
 subplot(2,2,1); stem(n, x); title('Input Sequence x(n)'); xlabel('n'); ylabel('Amplitude'); subplot(2,2,2); stem(k, mag); title('Magnitude |X(k)|'); xlabel('k'); ylabel('Magnitude'); subplot(2,2,3); stem(k, phase); title('Phase of X(k)'); xlabel('k'); ylabel('Phase (rad)'); subplot(2,2,4); stem(n, real(x_recovered)); title('IDFT - Reconstructed x(n)'); xlabel('n');
