import matplotlib.pyplot as plt
def plotseries_secondary():
    x = [0,40000,80000,120000,160000,200000]
    y = [0,1500,3000,4500,6000,7500]
    plt.plot(x, y)
    plt.xlabel('no of records') 
    plt.ylabel('time taken in msec')
    plt.title('SECONDARY KEY INDEXING OF SERIES')
    plt.show()  
# plotmovie