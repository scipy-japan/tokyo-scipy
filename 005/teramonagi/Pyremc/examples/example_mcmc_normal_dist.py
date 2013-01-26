# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from utils import standard_multivariate_normal_pdf
import pyremc

#サンプルの散布図　＆　真の確率密度の等高線
def plot_result(x, mu):    
    target = generate_target(mu)
    axis_range = mu+3.0
    #散布図
    #plt.scatter(x[:,0],x[:,1],c="black",s=10,edgecolors="None",alpha=0.5)    
    #等高線（真の確率密度から計算）
    mesh = np.arange(-axis_range,axis_range,0.1)
    X,Y = np.meshgrid(mesh, mesh)
    Z = np.zeros(np.shape(X))
    for i in xrange(np.size(X,0)):
        for j in xrange(np.size(X,1)):
            Z[i,j] = target((X[i,j],Y[i,j]))
    CS = plt.contour(X,Y,Z,linewidths=5)
    plt.clabel(CS,fontsize=15)
    #各ガウシアンの平均値が見やすいように適用に線を入れる    
    plt.axvline(x= mu,c='r',ls='--')
    plt.axhline(y= mu,c='r',ls='--')
    #plt.axis([-axis_range, axis_range,-axis_range, axis_range])
    plt.axis([0, axis_range,0, axis_range])
    plt.show()

if __name__ == "__main__":
    from scipy.stats import norm
    np.random.seed(100)
    #generator of target distribution
    def generate_target(mu):
        def _target(x):    
            x = np.asarray(x)
            return standard_multivariate_normal_pdf(x-np.array(( mu,  mu)))
        return _target

    #target mean parameter of Gaussian mixture
    MU = 3.0
    #params    
    SIZE_SIMULATION = 10000
    X0 = np.array([0,0])
    propose_next = lambda x:x+0.5*np.random.normal(size=len(x))
    #(Usual) Markov Chain MonteCarlo 
    target = generate_target(MU)
    mcmc = pyremc.MCMC(X0, target, propose_next, 10)    
    x = X0
    for i in range(SIZE_SIMULATION):
        x = np.vstack((x, mcmc.next()))   
    plot_result(x, MU)    

    #
    x_range = np.linspace(MU-3, MU+3 ,100)
    plt.plot(x_range, norm.pdf(x_range-MU), 'r', linewidth=3) # distribution function
    plt.hist(x[:,0], SIZE_SIMULATION**0.5, normed=True)
    plt.show()
    #
    plt.plot(x_range, norm.pdf(x_range-MU), 'r', linewidth=3) # distribution function
    plt.hist(x[:,1], SIZE_SIMULATION**0.5, normed=True)
    plt.show()
    print np.mean(x, axis=0)
    print np.std(x, axis=0)