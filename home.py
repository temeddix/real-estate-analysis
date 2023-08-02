import streamlit as st
import pandas as pd
import numpy as np

import background_work


st.sidebar.header("투자 계획")

equity = st.sidebar.slider("자기자본 (만원)", 50000, 500000, value=120000, step=5000)
loan = st.sidebar.slider("은행 대출 한도 (만원)", 100000, 1000000, value=180000, step=5000)

st.sidebar.header("요인")

construction_cost = st.sidebar.slider("제곱미터당 공사비 (만원)", 200, 400, value=280)
interest_rate = st.sidebar.slider("금리 (%)", 0.0, 10.0, value=3.0)
construction_cost = st.sidebar.slider("공실률 (%)", 0, 40, value=10)

st.checkbox("예산 내의 필지만 표시하기")

df = pd.DataFrame(
    {
        "lat": np.random.randn(1000) / 50 + 37.5519,
        "long": np.random.randn(1000) / 50 + 126.9918,
        "col": np.random.rand(1000, 4).tolist(),
    }
)

st.map(df, latitude="latitude", longitude="long", size=3, color="col")

st.markdown(
    r"""
이 시스템은 예상 연면적과 해당 지역 데이터를 기반으로 대략적인 월세를 계산한 후, 여러 요인을 계산에 포함하여 내부수익률을 산출한 후 지도에 표시합니다.
"""
)
st.latex(
    r"""
F = A*f*(1-v/100)
\\
R = F - 0.05*F - t(p) - i*l
\\
r = \frac{R}{e}*100
""",
)
st.markdown(
    r"""
계산 과정에서 도출되는 변수들은 다음과 같습니다.

- F: 건물 전체 월세
- R: 연간 순수익 (만원)
- r: IRR, 내부수익률 (%)

외부 데이터 또는 입력값으로 생성되는 변수는 다음과 같습니다.

- A: 연면적 (제곱미터) - 공공데이터 용도지역으로 추정
- f: 제곱미터당 월세 (만원) - 공공데이터 자료
- t(): 세율 구간을 고려한 재산세
- p: 공시지가
- e: 자기자본금 (만원)
- i: 금리
- l: 은행 대출
- v: 공실률 (%)

이 시스템은 공공데이터와 입력값만을 사용하여 해당 지역의 상가 부동산 수익성을 분석합니다. 일조권 사선, 개발 정보, 치안, 문화 등의 세부적인 요소들은 반영되지 않습니다. 각각의 필지의 특성을 파악하기 위해선 사설 서비스 이용, 답사 등 별도의 조사가 필요합니다.
"""
)
