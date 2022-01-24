import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
from scipy.stats import anderson
from scipy.stats import shapiro
import altair as alt
import matplotlib.pyplot as plt

# initial settings
visual_ready, statistical_ready = False, False
variables = ["Feed rate", "Upstream pH", "Pulp level"]
s_normal = pd.DataFrame()
path = "https://openmv.net/file/flotation-cell.csv"

# uploading the file in advance
if "uploading" not in st.session_state:
    df = pd.read_csv(path, usecols = variables)

# st.sidebar.header("Here is a sidebar")
st.title("Normality Visual Test")
col1, col2 = st.columns(2)
with col1:
    st.caption("bryson_je@hotmail.com")
with col2:
    st.write("**Strength Prediction** [link](https://strengthprediction.herokuapp.com)")
    st.write("**Basic Data Visualization** [link](https://basicdatavisualization.herokuapp.com)")
link_openMV = "https://openmv.net"
st.write("Check for **Normality** is an standard procedure of any Exploratory Data Analysis (EDA)")
st.write("**Objective**: Check how normal are your variables")
st.write("**Why**: Most of the statistical techniques assume variables are normal")
st.write("For this we will use 3 variables from **OpenMV.net: flotation-cell.csv**  [link](https://openmv.net)")
st.write("1. Let's start by **uploading** the file from left side panel")

# this is to show the csv file
st.sidebar.header("Use this panel for user input")
upload_csv_file = st.sidebar.checkbox("Click here to upload the csv file")
if upload_csv_file:
    st.subheader("Here below the csv file we will use")
    st.write("File has:", df.shape[1], "columns and:", df.shape[0], "rows")
    col11, col12 = st.columns(2)
    with col11:
        st.write("Flotation-cell.csv")
        st.dataframe(data = df, width = 450, height = 170)
    with col12:
        st.write("CSV file description")
        st.dataframe(data = df.describe(), width = 450, height = 170)
    st.write("2. Select a variable from left side panel")
    variable = st.sidebar.multiselect("Select a variable", df.columns.tolist())
    visual_ready = st.sidebar.checkbox("Click here for visual test")

# select a variable for normality visual test
if visual_ready:
    s_normal["values"] = pd.Series(np.random.normal(0, 1.0, df.shape[0]))
    st.subheader("Here is your visual test")
    st.write("Below is a comparison of your selected variable with a normal profile variable")
    col21, col22 = st.columns(2)
    with col21:
        fig1 = plt.figure(figsize = (7, 4.5))
        sns.histplot(data = df[variable], bins = 40, kde = True)
        st.write("Selected variable")
        st.pyplot(fig1)
        fig3, ax3, = plt.subplots(figsize = (7, 2.5))
        ax3.boxplot(df[variable], vert = False, widths = 0.75)
        st.pyplot(fig3)
    with col22:
        fig2 = plt.figure(figsize = (7, 4.5))
        sns.histplot(data = s_normal, bins = 40, kde = True)
        st.write("Normal profile variable")
        st.pyplot(fig2)
        fig4, ax4, = plt.subplots(figsize = (7, 2.5))
        ax4.boxplot(s_normal, vert = False, widths = 0.75)
        st.pyplot(fig4)
    st.write("Histogram plot for normality visual check")
    fig5, ax5 = plt.subplots(figsize = (10, 6))
    stats.probplot(s_normal["values"], dist = stats.norm, plot = ax5)
    plt.show()
    st.pyplot(fig5)
