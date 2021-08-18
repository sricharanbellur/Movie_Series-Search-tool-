import matplotlib.pyplot as plt
def plotmovie_secondary():
    x = [0,20000,40000,60000,80000,100000]
    y = [0,1000,2000,3000,4000,5000]
    plt.plot(x, y)
    plt.xlabel('no of records') 
    plt.ylabel('time taken in msec')
    plt.title('SECONDARY KEY INDEXING OF MOVIES')
    plt.show()  
# plotmovie