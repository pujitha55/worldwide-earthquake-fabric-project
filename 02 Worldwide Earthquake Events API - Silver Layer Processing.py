#!/usr/bin/env python
# coding: utf-8

# ## 02 Worldwide Earthquake Events API - Silver Layer Processing
# 
# New notebook

# # Worldwide Earthquake Events API - Silver Layer Processing

# In[ ]:


from pyspark.sql.functions import col
from pyspark.sql.types import TimestampType


# In[18]:


# df now is a Spark DataFrame containing JSON data
df = spark.read.option("multiline", "true").json(f"Files/{start_date}_earthquake_data.json")


# In[20]:


# Reshape earthquake data by extracting and renaming key attributes for further analysis.
df = \
df.\
    select(
        'id',
        col('geometry.coordinates').getItem(0).alias('longitude'),
        col('geometry.coordinates').getItem(1).alias('latitude'),
        col('geometry.coordinates').getItem(2).alias('elevation'),
        col('properties.title').alias('title'),
        col('properties.place').alias('place_description'),
        col('properties.sig').alias('sig'),
        col('properties.mag').alias('mag'),
        col('properties.magType').alias('magType'),
        col('properties.time').alias('time'),
        col('properties.updated').alias('updated')
        )


# In[23]:


# Convert 'time' and 'updated' columns from milliseconds to timestamp format for clearer datetime representation.
from pyspark.sql.functions import col, from_unixtime
from pyspark.sql.types import TimestampType
df = df.\
    withColumn('time', col('time')/1000).\
    withColumn('updated', col('updated')/1000).\
    withColumn('time', col('time').cast(TimestampType())).\
    withColumn('updated', col('updated').cast(TimestampType()))


# In[26]:


# appending the data to the gold table
df.write.mode('append').saveAsTable('earthquake_events_silver')

