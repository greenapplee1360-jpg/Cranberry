% Experiment 5c: Generation of DTMF signals
 clc; clear all; close all; 
key = '5';    % example key to generate ('0'-'9','*','#') 
lowFreq  = [697 697 697 770 770 770 852 852 852 941 941 941];
 highFreq = [1209 1336 1477 1209 1336 1477 1209 1336 1477 1209 1336 1477]; 
keys = '123456789*0#'; 
idx = strfind(keys, key);
 f1 = lowFreq(idx); 
f2 = highFreq(idx); 
Fs = 8000; t = 0:1/Fs:0.25;
 y = sin(2*pi*f1*t) + sin(2*pi*f2*t); 
plot(t, y); title(['DTMF Signal for Key: ' key]);
 xlabel('Time (s)'); ylabel('Amplitude'); xlim([0 0.02]);
 sound(y, Fs);   % play the generated tone
