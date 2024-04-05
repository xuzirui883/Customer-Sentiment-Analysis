#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install openai')


# In[2]:


get_ipython().system('pip install gradio')


# In[10]:


from openai import OpenAI
import pandas as pd
client = OpenAI(api_key='invalid')

def time_sensitivity(sentence):
  completion = client.chat.completions.create(
      model='gpt-3.5-turbo',
      messages=[
        {"role": "system",
         "content": "Give me the time sensitivity of the following sentences. Using 1 word like 'High', 'Low' or 'Medium' to cover all the sentences. Using 'High' or 'Low' more."},
        {"role": "user",
         "content": sentence}
      ],
      temperature=0.5,
      top_p=0.5,
  )
  return completion.choices[0].message.content

def importance(sentence):
  completion = client.chat.completions.create(
      model='gpt-3.5-turbo',
      messages=[
        {"role": "system",
         "content": "Give me the urgency of the event of the following sentences. Using 1 word like 'High', 'Low' or 'Medium' to cover all the sentences. Using 'High' or 'Low' more."},
        {"role": "user",
         "content": sentence}
      ],
      temperature=0.5,
      top_p=0.5,
  )
  return completion.choices[0].message.content

def tone(sentence):
  completion = client.chat.completions.create(
      model='gpt-3.5-turbo',
      messages=[
        {"role": "system",
         "content": "Give me the urgency conveys by tone conveys of the following sentences. Using 1 word like 'High', 'Low' or 'Medium' to cover all the sentences. Using 'High' or 'Low' more."},
        {"role": "user",
         "content": sentence}
      ],
      temperature=0.5,
      top_p=0.5,
  )
  return completion.choices[0].message.content

def score(level):

  if level == 'High':
    out = 5
  elif level == 'Medium':
    out = 3
  else:
    out = 1

  return out

def check_all(sentence):

  time_sen = time_sensitivity(sentence)
  # print(time_sen)
  time_sen = score(time_sensitivity(sentence)) * 0.5

  impor = importance(sentence)
  # print(impor)
  impor = score(importance(sentence)) * 0.3

  to = tone(sentence)
  # print(to)
  to = score(tone(sentence)) * 0.2

  return round(time_sen + impor + to)


# In[11]:


import gradio as gr
#from Sentiment_model import time_sensitivity, importance, tone, check_all

def ece1779(sentence):

  tim = time_sensitivity(sentence)
  imp = importance(sentence)
  ton = tone(sentence)
  result = check_all(sentence)

  return tim, imp, ton, result

project = gr.Interface(
    fn=ece1779,
    inputs=[gr.Textbox(lines=50, placeholder="Type here the sentences...")],
    outputs=[gr.Textbox(label='Time Urgency'), gr.Textbox(label='Event Urgency'), gr.Textbox(label='Language Excitement'), gr.Textbox(label='Urgency Rating')]
)


# In[12]:


project.launch()


# In[ ]:




