% Experiment 4: Implementation of FFT of given sequence 
clc; clear all; close all;
   x = input('Enter the input sequence: ');   % e.g. [1 2 3 4 5 6 7 8]
 N = length(x);

   X = fft(x, N); 
disp('FFT of the sequence:'); 
disp(X);  

 k = 0:N-1;
 subplot(2,1,1); stem(k, abs(X)); title('Magnitude of FFT'); xlabel('k'); ylabel('|X(k)|');
 subplot(2,1,2); stem(k, angle(X)); title('Phase of FFT'); xlabel('k'); ylabel('Phase (rad)');  
 % Time comparison (demonstration)
 tic; X1 = fft(x); t_fft = toc;
 fprintf('Time taken by FFT: %f sec\n', t_fft);
