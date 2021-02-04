import streamlit as st
import plotly_express as px
import pandas as pd

# configuration
st.set_option('deprecation.showfileUploaderEncoding', False)

# title of the app
st.title("データ可視化アプリ")

# Add a sidebar
st.sidebar.subheader("設定")

# Setup file upload
uploaded_file = st.sidebar.file_uploader(
                        label="Upload your CSV or Excel file.",
                         type=['csv', 'xlsx'])

global df
if uploaded_file is not None:
    print(uploaded_file)
    print("hello")

    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)

global numeric_columns
global non_numeric_columns
try:
    st.write(df)
    numeric_columns = list(df.select_dtypes(['float', 'int64']).columns)
    non_numeric_columns = list(df.select_dtypes(['object']).columns)
    non_numeric_columns.append(None)
    print(non_numeric_columns)
except Exception as e:
    print(e)
    st.write("Please upload file to the application.")

# add a select widget to the side bar
chart_select = st.sidebar.selectbox(
    label="Select the chart type",
    options=['散布図', '折れ線グラフ', 'ヒストグラム','棒グラフ']
)

if chart_select == '散布図':
    st.sidebar.subheader("散布図設定")
    try:
        x_values = st.sidebar.selectbox('X軸', options=non_numeric_columns)
        y_values = st.sidebar.selectbox('Y軸', options=numeric_columns)
        color_value = st.sidebar.selectbox("色", options=non_numeric_columns)
        plot = px.scatter(data_frame=df, x=x_values, y=y_values, color=color_value)
        # display the chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == '折れ線グラフ':
    st.sidebar.subheader("折れ線グラフ設定")
    try:
        x_values = st.sidebar.selectbox('X axis', options=non_numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.line(data_frame=df, x=x_values, y=y_values, color=color_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'ヒストグラム':
    st.sidebar.subheader("ヒストグラム設定")
    try:
        x = st.sidebar.selectbox('特徴', options=numeric_columns)
        bin_size = st.sidebar.slider("ビン数", min_value=10,
                                     max_value=100, value=40)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.histogram(x=x, data_frame=df, color=color_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == '棒グラフ':
    st.sidebar.subheader("棒グラフ設定")
    try:
        x_values = st.sidebar.selectbox('X軸', options=non_numeric_columns)
        y_values = st.sidebar.selectbox('Y軸', options=numeric_columns)
        color_value = st.sidebar.selectbox("色", options=non_numeric_columns)
        plot = px.bar(data_frame=df, x=x_values, y=y_values, color=color_value)
        # display the chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)