#EXERCISE 1:

lst = [i for i in range(51) if i >=1]
print(lst)

#EXERCISE 2:

lst2 = [i for i in range(1,201) if i%2==0]
print(lst2)

#EXERCISE 3:

import numpy as np

a = np.array([ [0.84062117, 0.48006452, 0.7876326 , 0.77109654],
               [0.44409793, 0.09014516, 0.81835917, 0.87645456],
               [0.7066597 , 0.09610873, 0.41247947, 0.57433389],
               [0.29960807, 0.42315023, 0.34452557, 0.4751035 ],
               [0.17003563, 0.46843998, 0.92796258, 0.69814654],
               [0.41290051, 0.19561071, 0.16284783, 0.97016248],
               [0.71725408, 0.87702738, 0.31244595, 0.76615487],
               [0.20754036, 0.57871812, 0.07214068, 0.40356048],
               [0.12149553, 0.53222417, 0.9976855 , 0.12536346],
               [0.80930099, 0.50962849, 0.94555126, 0.33364763]])
lst3 = [x for i in a for x in i]
print(lst3)

#EXERCISE 4:

lst4= [x for i in a for x in i if x >= 0.5]
print(lst4)

#EXERCISE 5:

lst5 = [x for i in a for x in i]
print(lst5)

#EXERCISE 6:

import os

file_list = [f for f in os.listdir('/Users/MIGUEL/Desktop/CLAB1/dataptmad1019/module-1/lab-list-comprehensions/data') if f.endswith('.csv')]
print(file_list)

#EXERCISE 7:

import pandas as pd

file_list = [f for f in os.listdir('/Users/MIGUEL/Desktop/CLAB1/dataptmad1019/module-1/lab-list-comprehensions/data') if f.endswith('.csv')]
data_sets = [pd.read_csv(os.path.join('/Users/MIGUEL/Desktop/CLAB1/dataptmad1019/module-1/lab-list-comprehensions/data', f)) for f in file_list]
data = pd.concat(data_sets, axis=0)

print(data[:10])

#EXERCISE 8:

import pandas as pd

file_list = [f for f in os.listdir('/Users/MIGUEL/Desktop/CLAB1/dataptmad1019/module-1/lab-list-comprehensions/data') if f.endswith('.csv')]
data_sets = [pd.read_csv(os.path.join('/Users/MIGUEL/Desktop/CLAB1/dataptmad1019/module-1/lab-list-comprehensions/data', f)) for f in file_list]
data = pd.concat(data_sets, axis=0)

selected_columns = [col for col in data._get_numeric_data() if data[col].median() < 0.48]

print(selected_columns)

#EXERCISE 9:

import pandas as pd

file_list = [f for f in os.listdir('/Users/MIGUEL/Desktop/CLAB1/dataptmad1019/module-1/lab-list-comprehensions/data') if f.endswith('.csv')]
data_sets = [pd.read_csv(os.path.join('/Users/MIGUEL/Desktop/CLAB1/dataptmad1019/module-1/lab-list-comprehensions/data', f)) for f in file_list]
data = pd.concat(data_sets, axis=0)

df = data
df['20'] =  df['19'] - 0.1

print(df[:10])

#EXERCISE 10:

import pandas as pd

file_list = [f for f in os.listdir('/Users/MIGUEL/Desktop/CLAB1/dataptmad1019/module-1/lab-list-comprehensions/data') if f.endswith('.csv')]
data_sets = [pd.read_csv(os.path.join('/Users/MIGUEL/Desktop/CLAB1/dataptmad1019/module-1/lab-list-comprehensions/data', f)) for f in file_list]
data = pd.concat(data_sets, axis=0)

df = data
df['20'] =  df['19'] - 0.1

final_data = [(df > 0.7) & (df < 0.75)]

print(final_data)




