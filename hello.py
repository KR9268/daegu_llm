import streamlit as st

st.title("Daegu lecture")

st.write("안녕하세요, Streamlit!")

import pandas as pd
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
st.dataframe(df)

chart_data = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])
st.line_chart(chart_data)

map_data = pd.DataFrame({'lat': [37.7749, 38.7749], 'lon': [-122.4194, -123.4194]})
st.map(map_data)

age = st.slider('나이', 0, 130, 25)
st.write("선택한 나이는", age, "살입니다.")

option = st.sidebar.selectbox('좋아하는 숫자를 선택하세요.', ['1', '2', '3'])
st.write('선택한 숫자:', option)

import time
progress_bar = st.progress(0)
for i in range(100):
    #time.sleep(0.1)
    progress_bar.progress(i + 1)

uploaded_file = st.file_uploader("파일을 선택하세요", type="csv")
if uploaded_file is not None:
     data = pd.read_csv(uploaded_file)
     st.write(data)

if st.button('안녕하세요 버튼'):
    st.write('버튼이 클릭되었습니다.')

color = st.color_picker('색상을 선택하세요')
st.write('선택한 색상:', color)

genre = st.radio(
    "좋아하는 음악 장르는 무엇인가요?",
    ('팝', '록', '재즈'))
st.write('선택한 장르:', genre)

agree = st.checkbox('이용 약관에 동의합니다.')
if agree:
    st.write('동의하셨습니다.')

option = st.selectbox(
    '좋아하는 숫자를 선택하세요:',
    [1, 2, 3, 4, 5])
st.write('선택한 숫자:', option)

options = st.multiselect(
    '좋아하는 색상을 선택하세요:',
    ['녹색', '빨간색', '파란색', '노란색'],
    ['녹색', '빨간색'])
st.write('선택한 색상:', options)

st.download_button(label="Download data as CSV", data="example,csv,data", file_name='data.csv', mime='text/csv')

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

st.balloons()

with st.expander("자세히 보기"):
    st.write("이 안에는 추가 설명이나 상세 데이터가 들어갑니다.")
    st.image("https://picsum.photos/200/300")

st.metric(label="매출", value="1,200만 원", delta="10% 감소")
st.metric(label="방문자 수", value=352, delta="-5명")

with st.popover("옵션 보기"):
    st.write("여기에 팝업 내용이 들어갑니다.")
    st.checkbox("동의합니다")

status = st.empty()

for i in range(101):
    status.text(f"진행률: {i}%")
    time.sleep(0.05)

status.text("완료!")
st.balloons()