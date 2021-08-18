import matplotlib.pyplot as plt
def plotmovie_primary():
    x = [0,20000,40000,60000,80000,100000]
    y = [0,500,1000,1500,2000,2500]
    plt.plot(x, y)
    plt.xlabel('no of records') 
    plt.ylabel('time taken in msec')
    plt.title('PRIMARY KEY INDEXING OF MOVIES')
    plt.show()  
# plotmovie