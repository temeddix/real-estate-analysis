import streamlit as st
import pandas as pd
import datetime

import background_work

st.title("홈")
st.text("첫 페이지입니다.")


# create the slider
slide_val = st.slider("보유기간", 0, 20, key="holding_period", value=8)


prediction = pd.DataFrame(
    columns=[
        "자금유입/대출신청",
        "자금유입/임대수익/보증금",
        "자금유입/임대수익/월세",
        "자금유입/매각",
        "자금유입/합계",
        "자금지출/대출/이자",
        "자금지출/대출/상환",
        "자금지출/초기비용/필지매입",
        "자금지출/초기비용/공사",
        "자금지출/기타",
        "자금지출/재산세",
        "자금지출/합계",
        "현금흐름",
        "누계",
        "대출",
        "IRR(내부수익률)",
    ],
    index=[
        datetime.datetime.now().year + i
        for i in range(st.session_state["holding_period"])
    ],
    dtype="int32",
)

st.write(prediction)
