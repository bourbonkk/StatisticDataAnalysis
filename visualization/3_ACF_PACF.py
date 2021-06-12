#!/usr/bin/env python
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from matplotlib import font_manager

df = pd.read_csv('../rawdata/totally_raw_data_delete_expression.csv')
font_path = 'C:\Windows\Fonts\malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font, size=15)

# ACF
plt.figure(figsize=(8, 8))
plt.rcParams['axes.unicode_minus'] = False
sm.graphics.tsa.plot_acf(df['sm_tot_t'], lags=25, ax=plt.subplot(211))
plt.xlim(0, 26)
plt.ylim(-1.1, 1.1)
plt.title("Autocorrelation for 교통량")
plt.xlabel('Lag')
plt.ylabel('ACF')

# PACF
sm.graphics.tsa.plot_pacf(df['sm_tot_t'], lags=25, ax=plt.subplot(212))
plt.xlim(-1, 26)
plt.ylim(-1.1, 1.1)
plt.title("Partial Autocorrelation for 교통량")
plt.xlabel('Lag')
plt.ylabel('PACF')
plt.tight_layout()
# plt.show()
plt.savefig('../image/3_ACF_PACF.png', dpi=300)
# In[ ]:
