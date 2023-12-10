
import matplotlib.pyplot as plt
import numpy as np

## 함수 키워드로 넣게 만들자

def plotSinWave(**kwargs): # keyword arguments 약자로 마음대로 정할수있다. 통상적으로 kwargs
    """
    plot sinWave
    y = a sin(2 pi f t + t_0) + b
    """
    
    # kwargs("키워드", 지정안해줄때 디폴트 값)
    startTime = kwargs.get("startTime", 0)
    endTime = kwargs.get("endTime", 1)
    amp = kwargs.get("amp", 1)
    freq = kwargs.get("freq", 1)
    sampleTime = kwargs.get("sampleTime", 0.01)
    bias = kwargs.get("bias", 0)
    figsize = kwargs.get("figsize", (12,6))
    
    time = np.arange(startTime,endTime,sampleTime)
    result = amp * np.sin(2 * np.pi * freq * time + startTime) + bias
    
    plt.figure(figsize=(10,6))
    plt.plot(time, result)
    plt.xlabel("time")
    plt.ylabel("sin")
    plt.title(
        str(amp) + "sin(2*pi" + str(freq) + "*t+" + str(startTime) + ")+" + str(bias))
    plt.show()
    
if __name__ == "__main__":
    print("hello world ~ !!")
    print("this is test graph")
    plotSinWave(amp=1,endTime=2)
    
