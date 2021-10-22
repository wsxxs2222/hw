import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
# Q1

st.title("some app")
# Q2
st.markdown("[Qizhou Fang](https://github.com/wsxxs2222/hw.git) is a link to **GitHub repository**")
# Q3
uploaded_file = st.file_uploader(label = "Upload a CSV file, please", type = "CSV")
# Q4
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # Q5
    df = df.applymap(lambda x: np.nan if x == " " else x)
# Q6
    def can_be_numeric(c):
        try:
            pd.to_numeric(df[c])
            return True
        except:
            return False

good_cols = [c for c in df.columns if can_be_numeric(c)]
# Q7
df[good_cols] = df[good_cols].apply(pd.to_numeric, axis=0)
# Q8
x_axis = st.selectbox("choose an x-value", good_cols)
y_axis = st.selectbox("choose a y-value", good_cols)
# Q9

num_range = st.slider("Please select the rows you want to plot", 0 ,df.shape[0], (0, df.shape[0]))
num_range = list(num_range)
# Q10
st.write(f"the datas you will plot are {x_axis} and {y_axis} and row {num_range} will be included")
# Q11
row_min = num_range[0]
row_max = num_range[1]
df1 = df.iloc[row_min:(row_max-1),:]
# Q12 make a button that can turn the points to be red
color1 = "blues"
if st.button("press this to turn the points in the plot redpurple"):
    color1 = "redpurple"
chart1 = alt.Chart(df1).mark_circle().encode(x=x_axis,y=y_axis,color=alt.Color(x_axis,scale=alt.Scale(scheme=color1)))
st.altair_chart(chart1, use_container_width=True)