
import numpy as np
arr=np.array([46,34,78,92,19])
print(arr)
sort=np.sort(arr)
print(sort)
arr1=np.array([23,47,89,20,31])
sort2=np.sort(arr1)
print(sort2)
print(np.flip(sort2))

import numpy as np
arr=np.array([2,3,5,6,1,7,9,3])
print(arr)
print(arr[1:6])
print(np.max(arr))
print(np.min(arr))
print(np.sum(arr))
print(np.sort(arr))
print(np.average(arr))
print(np.std(arr))
print(np.var(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.flip(arr))

import numpy as np
x=np.arange(10)
print("Elements are:",x)
x[[4,7,2]]=26
print(x)

import numpy as np
a=np.array([('JAIN1',2,21.0),('JAIN3',7,39.0),('JAIN2',7,29.0)], dtype=[('name',(np.str_,10)),('age',np.int32),('weight',np.float64)])
b=np.sort(a,order='name')
print("sorted:",b)

import pandas as pd
data={"Name":["A","B","C","D"], "Marks":[80,90,85,70],"Age":[19,20,14,15],"Course":["BCA","BSc","Bcom","BMS"],"State":["E","F","G","H"]}
df=pd.DataFrame(data)
print(df)
print("Head:\n",df.head())
print("\nTail:\n",df.tail())
print("\nInfo:")
df.info()
print("\nDescribe:\n",df.describe())
print("\nSorted:\n",df.sort_values("Marks"))
