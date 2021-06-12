#!/usr/bin/env python
# coding: utf-8

# In[141]:


# 2.요일별 교통량 

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager

df = pd.read_csv('../rawdata/totally_raw_data_delete_expression.csv', index_col='date')
df.index = df.index.astype(str)
df.index = pd.to_datetime(df.index, format='%Y-%m-%d')
df['week'] = df.index.to_series().dt.dayofweek
weekday_names = "월 화 수 목 금 토 일".split(' ')

font_path = 'C:\Windows\Fonts\malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font, size=15)

fig, ax = plt.subplots(figsize=(20, 6))
plt.title('요일별 교통량', loc='center', pad=10)
plt.rcParams['axes.unicode_minus'] = False
plt.ylabel('요일별 교통량(합계)')

ax.set_xticklabels(weekday_names)
ax.set_xticks(range(0, len(weekday_names)))

data_for_week = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
}
for col_name, item in df['week'].iteritems():
    data_for_week[item].append(df['sm_tot_t'].get(col_name))

result_df_for_week = []
for i in range(data_for_week.__len__()):
    result_df_for_week.append(data_for_week[i])
df_for_week = pd.DataFrame(result_df_for_week)

ax.plot(df_for_week, label='요일별 교통량(합계)')

# plt.show()
plt.savefig('../image/2_요일별교통량.png', dpi=300)
