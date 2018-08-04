
import numpy as np
import matplotlib.pyplot as plt



def draw(WT):
    m=WT.shape[0]
    n=WT.shape[1]
    i=0
    while(i<m):
        j=0;
        while(j<n):
            plt.scatter(i,j,s=300,c=WT[i][j]);
            j=j+1;
        i=i+1;
    plt.show()


def dist(X,Y):
    return np.sqrt( np.sum( (X-Y)*(X-Y),axis=2 ) );
           
def bmu(dst):
    r,c=dst.shape
    mb=dst[0][0];
    ir,ic=0,0;
    for i in range(r):
        for j in range(c):
            if dst[i][j]<mb:
                mb=dst[i][j];
                ir,ic=i,j;
    return ir,ic

print("Random initialization of GRID-")
WT=np.random.random(size=(10,10,3))
draw(WT)



x=np.random.random(size=(5,1,3))
print("Sample values-")
for fv in range(5):
    plt.scatter(0,fv,s=300,c=x[fv]);
plt.show();

for row in range(5):
    
    n_itr=500
    dst=dist(WT,x[row])
    rr,cc=bmu(dst)
    ini_rad=6;
    ini_lr=.01
    tc=650;
    WT_0=WT
    for i in range(1,n_itr):
        rad_i=ini_rad*np.exp(-i/tc);
        lr_i=ini_lr*np.exp(-i/tc)
        for j in range(10):
            for k in range(10):
                disc=np.sqrt( ((rr-j)**2 )+( (cc-k)**2) );
                if disc<=rad_i:
                    inf_r=np.exp((-disc**2)/(2*rad_i*rad_i));
                    tmp=WT[j][k];
                    WT[j][k]=tmp+(x[row]-tmp)*lr_i*inf_r;
        
        
    print("GRID values after update for ",row+1,"th sample")
    draw(WT);

print("Final values of GRID")
draw(WT)


    
    