import streamlit as st
import pandas as pd
import datetime

import background_work

st.set_page_config(layout="wide")

st.map()

st.sidebar.header("투자 계획")

equity = st.sidebar.slider("자기자본 (억원)", 5, 50, value=12)
loan = st.sidebar.slider("은행 대출 (억원)", 10, 100, value=18)
holding_period = st.sidebar.slider("보유 기간 (년)", 2, 20, value=8)

st.sidebar.header("요인")

construction_cost = st.sidebar.slider("제곱미터당 공사비 (만원)", 200, 400, value=280)
interest_rate = st.sidebar.slider("금리 (%)", 0.0, 10.0, value=3.0)
construction_cost = st.sidebar.slider("공실률 (%)", 0, 40, value=10)


prediction = pd.DataFrame(
    columns=[
        "I/대출신청",
        "I/임대수익/보증금",
        "I/임대수익/월세",
        "I/매각",
        "I/합계",
        "O/대출/이자",
        "O/대출/상환",
        "O/초기비용/필지매입",
        "O/초기비용/공사",
        "O/기타",
        "O/재산세",
        "O/합계",
        "S/현금흐름",
        "S/누계",
        "S/대출",
        "IRR(내부수익률)",
    ],
    index=[datetime.datetime.now().year + i for i in range(holding_period)],
    dtype="int32",
)

st.write(prediction)
st.caption("I는 현금 유입을, O는 현금 지출을 의미합니다. S는 정리된 결과입니다.")
