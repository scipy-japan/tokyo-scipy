# -*- coding: utf-8 -*-
import numpy as np

class MCMC(object):
    def __init__(self, x0, target, propose_next, burn_in):
        self._x0 = x0        
        self._x  = x0        
        self._target = target
        self._propose_next = propose_next
        self._burn_in = burn_in
        #Burn in
        for i in range(self._burn_in):
            self._x = self.next()
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, val):
        self._x = val
    
    def next(self):
        """
        Calculate next position by Metropolis algorithm
        """    
        x_proposed = self._propose_next(self._x)
        ratio = self._target(x_proposed)/self._target(self._x)    
        if(np.random.uniform(size=1) < ratio):
            self._x = x_proposed
            return x_proposed
        else:
            return self._x

class REMC(object):
    def __init__(self, x0, targets, propose_next, burn_in, replica_size, exchange_frequency):
        self._counter = 0
        self._replica_size = replica_size
        self._exchange_frequency = exchange_frequency
        self._mcmcs = [MCMC(x0, target, propose_next, burn_in) for target in targets]
    def next(self):
        """
        """
        self._counter+=1
        #Usual MCMC simulation for all replicas
        for index_replica in range(self._replica_size):
            self._mcmcs[index_replica].next()
        #Exchange replicas at specified frequency.
        if(self._counter % self._exchange_frequency == 0):
            index_exchange = int(np.random.uniform(0, self._replica_size-1))
            x1 = self._mcmcs[index_exchange  ].x                
            x2 = self._mcmcs[index_exchange+1].x
            target1 = self._mcmcs[index_exchange  ]._target          
            target2 = self._mcmcs[index_exchange+1]._target
            #Exchange the current states by metropolis algorithm
            if(np.random.uniform(size=1) < (target1(x2)*target2(x1))/(target1(x1)*target2(x2))):
                self._mcmcs[index_exchange].x, self._mcmcs[index_exchange+1].x = np.copy(x2),np.copy(x1)
        #Create return value
        return self._mcmcs[self._replica_size-1].x        
    