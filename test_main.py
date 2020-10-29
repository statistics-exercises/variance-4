import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_sample_mean(self):
       var = 1/2 
       for i in range(1,20) : 
       bar = np.sqrt( var / i )*scipy.stats.norm.ppf( (0.99 + 1) / 2 )
       self.assertTrue( np.fabs( sample_mean(i) - 1/2 )<bar, "your function for generating the sample mean appears to be incorrect" )
       
    def test_sample_variance(self):
        samples = 100*[0]
        for i in range(100) : 
           for j in range(10) :
               myvar = (sum( np.random.uniform(0,1, size=5) ) / 5 ) - 0.5
               samples[i] = samples[i] + myvar*myvar 
           samples[i] = samples[i] / 10
    
        samples.sort()
        ss = variance( 10, 5 )
        self.assertTrue( ss>samples[1] and ss<samples[98], "your function for generating the sample variance appears to be incorrect" )
