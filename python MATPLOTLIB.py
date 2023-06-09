#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install matplotlib


# In[2]:


pip install pandas


# In[5]:


import pandas as pd

data=pd.read_csv("Data_Bank.csv")

display(data.head(20))


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data_Bank.csv")

plt.scatter(data['job'], data['age'])

plt.title("Scatter Plot")

plt.xlabel('education')
plt.ylabel('age')

plt.show()


# In[8]:


import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("Data_Bank.csv")

plt.scatter(data['education'], data['age'], c=data['day'], 
            s=data['previous'])

plt.title("Scatter Plot")

plt.xlabel('education')
plt.ylabel('age')

plt.colorbar()

plt.show()


# In[15]:


import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("Data_Bank.csv")

plt.plot(data['marital']) 
plt.plot(data['previous'])

plt.title("Lin Chart")
 
plt.xlabel('marital')
plt.ylabel('previous')

plt.show()


# In[17]:


import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("Data_Bank.csv")

plt.bar(data['job'], data['campaign'])

plt.title("Bar Chart")

plt.xlabel('job') 
plt.ylabel('campaign')

plt.show()


# In[20]:


import pandas as pd 
import matplotlib.pyplot as plt
 
data = pd.read_csv("Data_Bank.csv")

plt.hist(data['day'])

plt.title("Histogram")

plt.show()


# In[27]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data_Bank.csv")

education = ['secondary', 'tertiary', 'primary']

data = [15, 11, 20]

plt.pie(data, labels=education)

plt.title("Pie Chart")

plt.show()


# In[30]:


#Foto Scatter Plot#1

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data_Bank.csv")

plt.scatter(data['job'], data['age'])

plt.title("Scatter Plot")

plt.xlabel('education')
plt.ylabel('age')

plt.savefig("ScatterPlot[1].jpg")


# In[31]:


#Foto Scatter Plot#2

import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("Data_Bank.csv")

plt.scatter(data['education'], data['age'], c=data['day'], 
            s=data['previous'])

plt.title("Scatter Plot")

plt.xlabel('education')
plt.ylabel('age')

plt.colorbar()

plt.savefig("ScatterPlot[2].jpg")


# In[32]:


#Foto Line Chart#

import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("Data_Bank.csv")

plt.plot(data['marital']) 
plt.plot(data['previous'])

plt.title("Lin Chart")
 
plt.xlabel('marital')
plt.ylabel('previous')

plt.savefig("LineChart.jpg")


# In[33]:


#Foto Bar Chart#

import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("Data_Bank.csv")

plt.bar(data['job'], data['campaign'])

plt.title("Bar Chart")

plt.xlabel('job') 
plt.ylabel('campaign')

plt.savefig("BarChart.jpg")


# In[34]:


#Foto Histogram#

import pandas as pd 
import matplotlib.pyplot as plt
 
data = pd.read_csv("Data_Bank.csv")

plt.hist(data['day'])

plt.title("Histogram")

plt.savefig("Histogram.jpg")


# In[36]:


#Foto Pie Chart#

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data_Bank.csv")

education = ['secondary', 'tertiary', 'primary']

data = [15, 11, 20]

plt.pie(data, labels=education)

plt.title("Pie Chart")

plt.savefig("PieChart", facecolor='y', bbox_inches="tight",
           pad_inches=0.3, transparent=True)


# In[ ]:




