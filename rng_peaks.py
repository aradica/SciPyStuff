#!/usr/bin/python3
#Andrija Radica, 26.03.2018.
import os
os.system('clear')
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy import signal
import pickle

def generate_data(parameter): #returns (x,y) where x and y are 1D data sets
    #start value
    x = random.randint(0, parameter)

    #list of 0s and ones, 0 => increase, 1 => decrease
    a = np.random.randint(0, 2, size = (parameter))

    #values to be used with the previous list
    b = np.random.rand(parameter)

    #generated random data will be stored here
    c = []
    #print('List with random zeros and ones: ', a)
    #print('List with random values between zero and 1: ', b)

    #generator
    i = 0
    for k in a:
        if k == 0:
            x += b[i]
        else:
            x -= b[i]
        c.append(x)
        i += 1

    #x axis
    d = list(range(0,len(c)))

    return (d,c)

def main():
    XandY = generate_data(100)
    X = XandY[0]
    Y = XandY[1]

    #find x-coordinate for peaks
    peaks_x = signal.find_peaks_cwt(Y, np.arange(1,10))
    #peaks = signal.find_peaks_cwt(c, np.array([1, 5, 10, 20]))
    #print(peaks_x)
    peaks_y = []

    #find y-coordinate for peaks
    for peak in peaks_x:
        peaks_y.append(Y[peak])
    
    #create graph with marked peaks
    p = plt.plot(X,Y)
    plt.scatter(peaks_x,peaks_y)
    plt.show()
    try:
        pickle.dump(p, open("plot.pickle", "wb"))
    except Exception:
        print("Your file couldn't be saved.")
        pass
    pickle.dump(p, open("last_generated.pickle", "wb"))
main()