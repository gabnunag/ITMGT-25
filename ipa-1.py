#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ASSIGNMENT FOR PROGRAMMING:BASIC


# In[7]:


#ITEM NUMBER ONE:
def savings(gross_pay, tax_rate, expenses):
    int(gross_pay)
    float(tax_rate)
    int(expenses)
    
    tax = (gross_pay*tax_rate)
    takehome_pay = (gross_pay-tax) - expenses

    return int(takehome_pay//1) #fixed to round down instead of round up (since previous code used round() which rounds up)

savings(50000, 0.10, 9000)


# In[7]:


#ITEM NUMBER TWO:
def material_waste(total_material, material_units, num_jobs, job_consumption):
    int(total_material)
    int(num_jobs)
    int(job_consumption)
    
    materialsconsumed = num_jobs*job_consumption
    material_waste = total_material - materialsconsumed
    
    return str(material_waste) + material_units

material_waste(2000, "kg", 5, 15)


# In[2]:


#ITEM NUMBER THREE:
def interest(principal, rate, periods):
    
    simpleinterest = (principal*(rate*periods))
    interest = (simpleinterest + principal)
    
    return int(interest//1) #fixed to round down instead of round up (since previous code used round() which rounds up)

interest(9000, 0.05, 12)


# In[15]:


def body_mass_index(weight, height):
    float(weight)
    list(height)
    
    kg = weight / 2.205
    metricheight = (height[0]*12+height[1])*0.0254
    body_mass_index = kg/(metricheight*metricheight)
    
    return body_mass_index

body_mass_index (204, [6,4])

