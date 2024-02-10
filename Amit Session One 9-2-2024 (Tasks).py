#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_string ="0123456789"
print(my_string[-2:-6:-2])


# In[2]:


x = 5
x = float(x)
print(x)


# In[3]:


x = 5.5
x = int(x)
print(x)


# In[4]:


x = "Hello world"
print(len(x))


# In[5]:


txt = "Hello World"
x[0]


# In[6]:


txt = "Hello world"
x[2:5]


# In[7]:


txt = "  hello world  "
x = txt.strip()
print(x)


# In[8]:


txt = "Hello world"
print(txt.upper())


# In[9]:


txt = "Hello world"
print(txt.lower())


# In[10]:


txt = "Hello World"
x = txt.replace("H","J")
print(x)


# In[11]:


age = 36
txt = f"my name is Jhon, and I am { age}"
print(txt)


# In[12]:


print(10>9)


# In[13]:


txt = "Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high\n,Like a diamond in the sky.\nTwinkle twinkle little star\nHow I wonder what you are!"


# In[14]:


print(txt)


# In[15]:


name = ["Ahmed","Hamdy"]


# In[16]:


name


# In[17]:


print(name)


# In[18]:


my_list = ['Hamdy', 'Ahmed']
my_string = ','.join(my_list)
print(my_string)


# In[19]:


import math

radius = 1.1
area = math.pi * radius ** 2

print(f"The area of the circle with radius {radius} is **{area:.2f}** square units.")


# In[1]:


filename = "abc.java"
x = filename.split(".")
print(x)
x[1]


# In[2]:


str = "Amit"
str = list(str)
str = tuple(str)
type(str)


# In[3]:


str = list(str)
str


# In[4]:


str[2] = "A"


# In[5]:


str


# In[6]:


x = "".join(str)
print(x)


# In[7]:


color_list = ["Red","Green","White","Black"]


# In[8]:


color_list[0: :3]


# In[9]:


x = print(f"the first color is {color_list[0]}, and the last color is {color_list[-1]}" )


# In[10]:


print("a string that you don't have to escapeThis nis a  ....... multi-lineheredoc string --------> example")


# In[11]:


link = "https://www.google.com/" 
mail = "aimt4536@gmail.com"
link.startswith("http")
mail.endswith(".com")


# In[ ]:




