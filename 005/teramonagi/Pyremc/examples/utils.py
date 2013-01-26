# -*- coding: utf-8 -*-
import numpy as np
def standard_multivariate_normal_pdf(x):
    """
    Calculate the probability density function of standard multivariate gaussian distribution.

    Parameters
    ----------
    x : 1-d array of positions which you want to calculate.

    Returns
    -------
    out : float
        probability distribution function
        
    Examples
    --------
    """
    x = np.asarray(x)    
    return 1.0/(2.0*np.pi)**(len(x)/2.0)*np.exp(-0.5*np.dot(x,x))
