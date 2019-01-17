
# coding: utf-8

# # q1

# In[2]:


my_name='alyssa'
print (my_name)


# # q2

# In[3]:


my_id='1234'
print (my_id)


# # q3

# In[4]:


my_id_str='1234'
print (my_id_str)


# # q4

# In[9]:


print (my_name) + (my_id)


# Doesn't work because trying to combine string and integer

# # q5

# In[6]:


print (my_name + my_id_str)


# It worked because they are both strings

# # q6

# In[13]:


'hello, world. This is my first python string.'.split('.')
    


# # q7

# In[14]:


str_list=['a','b','c','d','e']
str_list.sort()
print (str_list)


# # q8

# In[15]:


str_list.append('f')
print (str_list)


# # q9

# In[16]:


str_list.remove('d')
print (str_list)


# # q10

# In[18]:


print (str_list[2])


# # q11

# In[20]:


num_list=['12','32','43','35']
print (str_list + num_list)


# Yes

# # q12

# In[21]:


my_dict={'name':'alyssa','id':my_id}
print (my_dict)


# # q13

# In[22]:


my_dict['name']='hadfield'
print (my_dict)


# # q14

# In[23]:


print (my_dict['id'])


# # q15

# In[24]:


my_dict['id']='5678'
print (my_dict)


# # q16

# In[26]:


my_dict['num_list']=num_list
print (my_dict)


# We redefined  the key to be the previous list value
