import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import pydeck as pdk


st.sidebar.header("투자 계획")

equity = st.sidebar.slider("자기자본 (억원)", 5, 50, value=12) * 10000
loan = st.sidebar.slider("은행 대출 한도 (억원)", 10, 100, value=18) * 10000

st.sidebar.header("요인")

construction_cost = st.sidebar.slider("제곱미터당 공사비 (만원)", 200, 400, value=280)
interest_rate = st.sidebar.slider("금리 (%)", 0.0, 10.0, value=3.0)
construction_cost = st.sidebar.slider("공실률 (%)", 0, 40, value=10)

st.checkbox("예산 내의 필지만 표시하기")

map_data = pd.DataFrame(
    {
        "lat": np.random.randn(50000) / 50 + 37.5519,
        "lon": np.random.randn(50000) / 50 + 126.9918,
        "id": np.arange(50000),
        "text": "필지 정보...",
    }
)


def on_point_click(widget_instance, payload):
    print("YAHOO")


deck = pdk.Deck(
    map_style="dark",
    initial_view_state=pdk.ViewState(
        latitude=37.5519, longitude=126.9918, zoom=8, controller=True
    ),
    tooltip={
        "text": "{text}\n임시 ID: {id}",
        "style": {
            "color": "white",
            "backgroundColor": "rgb(38,39,48)",
            "borderRadius": "8px",
            "boxShadow": "0px 4px 20px rgba(0,0,0,0.75)",
            "padding": "16px 24px",
        },
    },  # type: ignore
    layers=[
        pdk.Layer(
            "HeatmapLayer",
            data=map_data,
            opacity=0.2,
            get_position=["lon", "lat"],
            aggregation="MEAN",
            get_weight="id / 1000",
            threshold=0.6,
        ),
        pdk.Layer(
            "ScatterplotLayer",
            data=map_data,
            get_position=["lon", "lat"],
            point_size=3,
            get_color=[255, 255, 255, "id/30"],
            pickable=True,
            auto_highlight=True,
        ),
    ],
)
deck.deck_widget.on_click(on_point_click)
html_content: str = deck.to_html(as_string=True)  # type:ignore
components.html(html_content, height=800)

st.markdown(
    r"""
이 시스템은 예상 연면적과 해당 지역의 공공데이터를 기반으로 대략적인 월세를 계산한 후,
현금 지출을 차감하여 내부수익률을 산출한 후 지도에 표시합니다.
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

이 시스템은 공공데이터와 입력값만을 사용하여 해당 지역의 상가 부동산 수익성을 분석합니다.
일조권 사선, 개발 정보, 치안, 문화 등의 세부적인 요소들은 반영되지 않습니다.
각각의 필지의 특성을 파악하기 위해선 사설 서비스 이용, 답사 등 별도의 조사가 필요합니다.
"""
)
