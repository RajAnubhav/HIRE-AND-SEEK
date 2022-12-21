
#// #!/usr/bin/env python
# coding: utf-8

# In[103]:


import pandas as pd
import numpy as np
import ast
from joblib import dump

# In[104]:


import mysql.connector
my_conn = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="jobship"
    )
####### end of connection ####
job_comp = pd.read_sql("SELECT * FROM job ",my_conn)
job_comp.head(50)


# In[105]:


import mysql.connector
my_conn = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="jobship"
    )
####### end of connection ####
profile = pd.read_sql("SELECT * FROM stud_profile ",my_conn)
profile.head(50)


# In[106]:


cmp = job_comp
job = profile


# In[107]:


job.head(100)


# In[108]:


cmp.head()


# In[109]:


cmp = cmp.loc[:,['job_id','domain', 'company','jobtitle','skills','joblocation_address']]
cmp.head()


# In[110]:


cmp.isnull().sum()


# In[111]:


cmp.dropna(inplace = True)
j = len(cmp.shape)


# In[112]:


cmp.duplicated().sum()


# In[113]:


cmp.shape


# In[114]:


def convert_skills():
    data = []
    for i in range(len(cmp)):
        data.append(cmp.iloc[i].skills.split(","))
    return data
    


# In[115]:


data = convert_skills()
cmp['skills'] = data
cmp['skills'].head()


# In[116]:


cmp.head()


# In[117]:


def convert_jobtitle():
    data2 = []
    for i in range(len(cmp)):
        data2.append(cmp.iloc[i].jobtitle.split(","))
    return data2

cmp['jobtitle'] = convert_jobtitle()
cmp.head()


# In[118]:


#def convert_Company():
  #  data3 = []
   # for i in range(len(cmp)):
    #    data3.append(cmp.iloc[i].company.split(","))
    #return data3
#data3 = convert_Company()
#cmp['company'] = data3

def convert_joblocation_address():
    data4 = []
    for i in range(len(cmp)):
        data4.append(cmp.iloc[i].joblocation_address.split(" "))
    return data4
data4 = convert_joblocation_address()
cmp['joblocation_address'] = data4

cmp.head()


# In[119]:


#cmp['jobdescription']=cmp['jobdescription'].apply(lambda x:x.split())


# In[120]:


cmp.head()


# In[121]:


cmp['jobtitle'] = cmp['jobtitle'].apply(lambda x:[i.replace(" ","")for i in x])


# In[122]:


# cmp['jobdescription']=cmp['jobdescription'].apply(lambda x:[i.replace(" ","")for i in x])
cmp['skills']=cmp['skills'].apply(lambda x:[i.replace(" ","")for i in x])
cmp['joblocation_address']=cmp['joblocation_address'].apply(lambda x:[i.replace(" ","")for i in x])


# In[123]:


cmp.head()


# In[124]:


cmp['tags'] = cmp['jobtitle'] + cmp['skills'] + cmp['joblocation_address']


# In[125]:


cmp.head()


# In[126]:


comp =  cmp[['job_id','domain','company','tags']]


# In[127]:


comp.head()


# In[128]:


comp['tags']=comp['tags'].apply(lambda x:" ".join(x))


# In[129]:


comp.head()


# In[130]:


comp['tags'] = comp['tags'].apply(lambda x:x.lower())


# In[131]:


comp.head()


# In[132]:


comp.shape


# In[133]:


comp.head()


# In[134]:


comp['tags'][0]


# In[135]:


job.head()


# In[136]:


job = job[['id','name','place','database_worked_with','language_worked_with','collab_tools','opsys','plateform_worked_with','degree',]]


# In[137]:


job.head()


# In[138]:


job.isnull().sum()


# In[139]:


job.shape


# In[140]:


job.dropna(inplace = True)


# In[141]:


#def c_MB():
 #   data5 = []
  #  for i in range(len(job)):
   #     data5.append(job.iloc[i].summary.split(","))
    #return data5
#job['summary'] = c_MB()


# In[142]:


def c_C():
    data6 = []
    for i in range(len(job)):
        data6.append(job.iloc[i].place.split(","))
    return data6
job['place'] = c_C()


# In[143]:


def c_DW():
    data7 = []
    for i in range(len(job)):
        data7.append(job.iloc[i].database_worked_with.split(","))
    return data7
job['database_worked_with'] = c_DW()


# In[144]:


# def c_DT():
#    data8 = []
#    for i in range(len(job)):
#        data8.append(job.iloc[i].DevType.split(","))
#    return data8
# job['DevType'] = c_DT()


# In[145]:


def c_LWW():
    data9 = []
    for i in range(len(job)):
        data9.append(job.iloc[i].language_worked_with.split(","))
    return data9
job['language_worked_with'] = c_LWW()

def c_NCTWW():
    data10 = []
    for i in range(len(job)):
        data10.append(job.iloc[i].collab_tools.split(","))
    return data10
job['collab_tools'] = c_NCTWW()

def c_OS():
    data11 = []
    for i in range(len(job)):
        data11.append(job.iloc[i].opsys.split(","))
    return data11
job['opsys'] = c_OS()


def c_PlatformWorkedWith():
    data12 = []
    for i in range(len(job)):
        data12.append(job.iloc[i].plateform_worked_with.split(","))
    return data12
job['plateform_worked_with'] = c_PlatformWorkedWith()

def c_UndergradMajor():
    data13 = []
    for i in range(len(job)):
        data13.append(job.iloc[i].degree.split(","))
    return data13
job['degree'] = c_UndergradMajor()
    


# In[146]:


job.head()


# In[147]:


job['place'] = job['place'].apply(lambda x:[i.replace(" ","")for i in x])
job.head()


# In[148]:


job['database_worked_with'] = job['database_worked_with'].apply(lambda x:[i.replace(" ","")for i in x])
job['language_worked_with'] = job['language_worked_with'].apply(lambda x:[i.replace(" ","")for i in x])
job['collab_tools'] = job['collab_tools'].apply(lambda x:[i.replace(" ","")for i in x])
job['plateform_worked_with'] = job['plateform_worked_with'].apply(lambda x:[i.replace(" ","")for i in x])
job['degree'] = job['degree'].apply(lambda x:[i.replace(" ","")for i in x])
#job['MainBranch'] = job['MainBranch'].apply(lambda x:[i.replace(" ","")for i in x])


# In[149]:


job.head()


# In[150]:


job['tags'] =job['place'] + job["database_worked_with"] + job['language_worked_with'] + job['collab_tools'] + job['opsys'] + job['plateform_worked_with'] + job['degree']  


# In[151]:


job.head()


# In[152]:


job_seekr = job[['id','name', 'tags']]


# In[153]:


job_seekr.head()


# In[154]:


job_seekr['tags']=job_seekr['tags'].apply(lambda x:" ".join(x))


# In[155]:


job_seekr['tags'] = job_seekr['tags'].apply(lambda x:x.lower())


# In[156]:


job_seekr['tags'][7]


# In[157]:

from sklearn.feature_extraction.text import CountVectorizer 

cv = CountVectorizer(max_features=117,stop_words='english')


# In[158]:


vector2 = cv.fit_transform(comp['tags']).toarray()


# In[159]:


vector2.shape


# In[160]:


# cv.get_feature_names()


# In[161]:


vector1 = cv.fit_transform(job_seekr['tags']).toarray()
vector1.shape


# In[162]:


# cv.get_feature_names()


# In[163]:


import nltk


# In[164]:


from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()


# In[165]:


def stem(text):
    y = []
    
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)


# In[166]:


job_seekr['tags'] = job_seekr['tags'].apply(stem)


# In[167]:


comp['tags'] = comp['tags'].apply(stem)


# In[168]:



# In[169]:

from sklearn.metrics.pairwise import cosine_similarity

simalarity = cosine_similarity(vector1, vector2)


# In[170]:


simalarity[0]


# In[171]:


sorted(list(enumerate(simalarity[0])), reverse = False,key = lambda x:x[1])[0:5]


# In[172]:


def recommend(int):
    job_index=job_seekr[job_seekr['id'] == int].index[0]
    distances = simalarity[job_index]
    company_list = sorted(list(enumerate(distances)), reverse = True,key = lambda x:x[1])[0:5]
    id = []
    
    for i in company_list:
        id.append(comp.iloc[i[0]].job_id)
    print(id)
        
    return id
    
    


# In[173]:


    
    


# In[ ]:





# In[174]:


comp.head(12)


# In[175]:


job_seekr.head()


# In[176]:


job_seekr['id'].values


# In[177]:


job_seekr.to_dict()


# In[178]:


comp.to_dict()

