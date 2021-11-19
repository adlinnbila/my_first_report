# -*- coding: utf-8 -*-
"""My First Streamlit (Training)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PqFbwaQ7K5hrheC--qNtLi46pwUEbx_-

# Overall Procedures to Run Streamlit from Colab

### 1. Install streamlit and pyngrok
"""

!pip install streamlit
!pip install pyngrok

"""### 2. Create our first app"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile myfirstapp.py
# import streamlit as st
# import numpy as np
# import pandas as pd
# 
# st.header("My First Streamlit")
# st.write(pd.DataFrame({
#     'Intplan': ['yes', 'yes', 'yes', 'no'],
#     'Churn Status': [0, 0, 0, 1]
# }))

"""### 3. Start our app!"""

!streamlit run myfirstapp.py --server.port 80 &>/dev/null&

"""### 4.  Create a "tunnel" """

from pyngrok import ngrok
 
ngrok.kill()
 
 
# Setup a tunnel to the streamlit port 80
 
public_url = ngrok.connect(port=80)
public_url

"""### 5. Check which processes are active"""

!streamlit hello --server.port 80 &>/dev/null&

!pgrep streamlit

"""### Kill processes"""

# kill the processes accordingly
!kill 1570

"""### Shut down (Zzz...)"""

! ngrok.kill()

"""# Other demos"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile myfirstapp.py
# import streamlit as st
# 
# import numpy as np
# import pandas as pd
# 
# st.header("My first Streamlit App")
# st.title("This is a title")
# st.write("# This is a first-level heading")
# st.write("## This is a second-level heading")
# st.write(pd.DataFrame({
#     'Intplan': ['yes', 'yes', 'yes', 'no'],
#     'Churn Status': [0, 0, 0, 1]
# }))

"""3. Plot a chart

"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile myfirstapp.py
# import streamlit as st
# import numpy as np
# import pandas as pd
# 
# st.header("My first Streamlit App")
# 
# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])
# 
# st.line_chart(chart_data)
#

"""4. Plot a map"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile myfirstapp.py
# import streamlit as st
# import numpy as np
# import pandas as pd
# 
# st.header("My first Streamlit App")
# 
# 
# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])
# 
# st.map(map_data)

"""# **Add interactivity with widgets**

###1. Checkbox
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile myfirstapp.py
# import streamlit as st
# 
# import numpy as np
# import pandas as pd
# 
# st.header("My first Streamlit App")
# 
# st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
# show = st.checkbox('yeahhh I agree the terms and conditions')
# if show:
#     st.write(pd.DataFrame({
#     'Intplan': ['yes', 'yes', 'yes', 'no'],
#     'Churn Status': [0, 0, 0, 1]
# }))

"""### 2. Select Box"""



# Commented out IPython magic to ensure Python compatibility.
# %%writefile myfirstapp.py
# import streamlit as st
# 
# import numpy as np
# import pandas as pd
# 
# st.header("My first Streamlit App")
# 
# option = st.sidebar.selectbox(
#     'Choose one only ya',
#      ['line chart','map','T n C'])
# 
# 
# if option=='line chart':
#     chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])
# 
#     st.line_chart(chart_data)
# 
# elif option=='map':
#     map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])
# 
#     st.map(map_data)
# 
# else:
# 
#     st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
#     show = st.checkbox('I agree the terms and conditions')
#     if show:
#         st.write(pd.DataFrame({
#         'Intplan': ['yes', 'yes', 'yes', 'no'],
#         'Churn Status': [0, 0, 0, 1]
#         }))

"""### Run Progress

"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile myfirstapp.py
# import streamlit as st
# import numpy as np
# import pandas as pd
# import time
# 
# st.header("My first Streamlit App")
# 
# option = st.sidebar.selectbox(
#     'Select a mini project',
#      ['line chart','map','T n C','Long Process'])
# 
# if option=='line chart':
#     chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])
# 
#     st.line_chart(chart_data)
# 
# elif option=='map':
#     map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])
# 
#     st.map(map_data)
# 
# elif option=='T n C':
#     st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
#     show = st.checkbox('I agree the terms and conditions')
#     if show:
#         st.write(pd.DataFrame({
#         'Intplan': ['yes', 'yes', 'yes', 'no'],
#         'Churn Status': [0, 0, 0, 1]
#         }))
# 
# else:
#     'Starting a long computation...'
#     
#     latest_iteration = st.empty()
#     bar = st.progress(0)
# 
#     for i in range(100):
#    
#         latest_iteration.text(f'Iteration {i+1}')
#         bar.progress(i + 1)
#         time.sleep(0.1)
# 
#     '...and now we\'re done!'

"""# Demo: Classification model"""

# Commented out IPython magic to ensure Python compatibility.
# # Ref: https://github.com/dataprofessor/streamlit_freecodecamp/blob/main/app_7_classification_iris/iris-ml-app.py
# %%writefile myfirstapp.py
# import streamlit as st
# import pandas as pd
# from sklearn import datasets
# from sklearn.ensemble import RandomForestClassifier
# 
# st.write("""
# # Simple Iris Flower Prediction App
# This app predicts the **Iris flower** type!
# """)
# 
# st.sidebar.header('User Input Parameters')
# 
# def user_input_features():
#     sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
#     sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
#     petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
#     petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
#     data = {'sepal_length': sepal_length,
#             'sepal_width': sepal_width,
#             'petal_length': petal_length,
#             'petal_width': petal_width}
#     features = pd.DataFrame(data, index=[0])
#     return features
# 
# df = user_input_features()
# 
# st.subheader('User Input parameters')
# st.write(df)
# 
# iris = datasets.load_iris()
# X = iris.data
# Y = iris.target
# 
# clf = RandomForestClassifier()
# clf.fit(X, Y)
# 
# prediction = clf.predict(df)
# prediction_proba = clf.predict_proba(df)
# 
# st.subheader('Class labels and their corresponding index number')
# st.write(iris.target_names)
# 
# st.subheader('Prediction')
# st.write(iris.target_names[prediction])
# #st.write(prediction)
# 
# st.subheader('Prediction Probability')
# st.write(prediction_proba)

"""# Deployment of the Web App

"""

!pip freeze > requirements.txt
!cat requirements.txt