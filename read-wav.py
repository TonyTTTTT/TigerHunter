# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 00:32:29 2021

@author: Tony Tsou
"""
from scipy.io import wavfile
import scipy.io

samplerate, data = wavfile.read('sound.wav')
print(f"number of channels = {data.shape[1]}")
length = data.shape[0] / samplerate
print(f"length = {length}s")
import matplotlib.pyplot as plt
import numpy as np
time = np.linspace(0., length, data.shape[0])
plt.plot(time, data[:, 0], label="Left channel")
plt.plot(time, data[:, 1], label="Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

f = open('sound.txt', 'w')
f.write(str(samplerate)+'\n')
f.write('[')
for i in range(data.shape[0]):
    f.write('[{}, {}],\n'.format(data[i][0], data[i][1]))
    
f.close()