# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 17:08:21 2018

@author: ASUS
"""

import numpy as np
import h5py
import matplotlib.pyplot as plt
import random

def d2bin(t):
    g=bin(t);
    y=[];
    for i in range(len(g)-2):
        y.append( (int)(g[i+2]) );
    ze=9-len(y);
    for i in range(ze):
        y.insert(0,0);
    return y.copy();
def b2dec(H):
    st='';
    for i in range(len(H)):
        st=st+str(H[i]);
    return int(st,2);

def cube(c):
    gb=[];
    for i in range(len(c)):
        gb.append( c[i]**3+5 );
    return gb.copy();



#X=[12,14,16,12,11,10,13,15,18,10,21,23,34,32,14,16,32,56,67,74,52,14,53,23,17,21,81,76,59,37]


tot=50;

def fit(mdata):
    #print(mdata)
    cval=cube(mdata);
    #cval.sort();
    #cval.reverse();
    #print(cval,"\n\n")
    cum=[];
    cum.append(cval[0]);
    sm=cval[0];
    for i in range(len(mdata)-1):
        sm=sm+cval[i+1];
        cum.append(sm);
    #print(cum)
    fitdata=[];
    for i in range(tot):
        rint=random.randrange(0,sm-1,1);
        #print("rando=",rint);
        for j in range( len(cum) ):
            if cum[j]>rint:
                fitdata.append(mdata[j]);
                break;
    #print(fitdata)
    return fitdata.copy();
                
            
        
def cross(g,h):
    bg=d2bin(g);
    bh=d2bin(h);
    ind=np.random.randint(0,9);
    #print(ind)
    #print(bg,"\n",bh,"\n")
    for i in range(ind,9):
        tmp=bg[i];
        bg[i]=bh[i];
        bh[i]=tmp;
    #print(bg,"\n",bh)
    return b2dec(bg),b2dec(bh);

def mutation(H):
    num=(10/100)*50;
    num=round(num);
    mtant=[];
    random.shuffle(H);
    for i in range(num):
        tm=d2bin(H[i]);
        rit=np.random.randint(0,9);
        tm[rit]=1-tm[rit];
        #mtant.append(b2dec(tm))
        H[i]=( b2dec(tm) );
    return H;
        
        
    

X=[];

for i in range(100):
    X.append(random.getrandbits(9) )
    
def genetic(data):
    avgFit=[];
    for itr in range(100):
        fdata=fit(data);
        data=fdata.copy();
        wf=fdata.copy();
        avgFit.append(sum(data)/tot);
        #print(len(data))
        for i in range(0,len(wf),2):
            ff=wf[i];
            ss=wf[i+1];
            cf,cs=cross(ff,ss);
            #data.append(cf)
            #data.append(cs)
            wf[i]=cf;
            wf[i+1]=cs;
        #print(fdata)
        mutdata=mutation(wf);
        data.extend(mutdata.copy());
        #print(len(data))
        #fdata0[0]=mutdata;
    print(data);
    plt.plot(avgFit)
    plt.ylabel('Average Fitness')
    plt.xlabel('iterations' )
    plt.show()
    #print(avgFit);
        
        
    
        
    
