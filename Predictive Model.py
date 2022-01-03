### Ensemble

###### Check Collinearity in MLR??? #####

# Importing Packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime
print(1)

os.getcwd()

os.chdir('P:\Departments\Analytics\_USER_FILES\cokura\Python\Predictive Model')

a = os.getcwd()
print("cur dir = " + a)


order_hist = pd.read_csv('PMA last 12 months.csv')
order_hist.head()x`