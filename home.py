from typing import Tuple
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import pydeck
import geopandas

pd.set_option("display.max_columns", None)

from recipe.common import convert_size
from recipe.common import read_geofile
from recipe.common import insert_custom_css

st.set_page_config(layout="wide")

if "is_session_ready" not in st.session_state.keys():
    st.session_state["is_session_ready"] = True
    st.session_state["equity"] = 12  # 자기자본
    st.session_state["loan"] = 20  # 은행 대출 한도
    st.session_state["construction_cost"] = 280  # 제곱미터당 공사비
    st.session_state["interest_rate"] = 3.0  # 금리
    st.session_state["empty_ratio"] = 10  # 공실률


@st.cache_data
def draw_lands(equity: int, loan: int) -> Tuple[str, pd.DataFrame]:
    raw_land_data = read_geofile("ownership_info/AL_11_D160_20230525")
    # 정부 공공데이터의 SHP 파일에서 사용하는 좌표계는 EPSG:5174입니다.
    # EPSG:4326이 흔히 사용하는 WGS84, 즉 위도/경도 시스템입니다.
    raw_land_data: geopandas.GeoDataFrame = raw_land_data.to_crs(
        epsg=4326
    )  # type:ignore
    rows_to_keep = int(len(raw_land_data) * 0.1)
    land_data: pd.DataFrame = raw_land_data.sample(rows_to_keep)
    land_data = land_data[land_data["A8"] == "개인"]

    # 해당 대지를 그리는 폴리곤 데이터의 평균으로 위도와 경도 행을 추가합니다.
    land_data["lat"] = land_data["geometry"].centroid.y  # type:ignore
    land_data["lon"] = land_data["geometry"].centroid.x  # type:ignore

    deck = pydeck.Deck(
        map_style="dark",
        initial_view_state=pydeck.ViewState(
            latitude=37.5519,
            longitude=126.9918,
            zoom=8,
            controller=True,
        ),
        tooltip={
            "text": "{A2} {A5}\nID: {A0}\n{A16}\n{A18}\n{A22}",
            "style": {
                "color": "white",
                "backgroundColor": "rgb(38,39,48)",
                "borderRadius": "8px",
                "boxShadow": "0px 4px 20px rgba(0,0,0,0.75)",
                "padding": "16px 24px",
            },
        },  # type: ignore
        layers=[
            pydeck.Layer(
                "HeatmapLayer",
                data=land_data,
                opacity=0.1,
                get_position=["lon", "lat"],
                aggregation="MEAN",
                get_weight="A11/1000",
                threshold=0.6,
                color_range=[
                    [0, 63, 0],
                    [63, 255, 0],
                    [191, 255, 0],
                    [255, 255, 191],
                ],
            ),
            pydeck.Layer(
                "GeoJsonLayer",
                data=land_data,
                opacity=0.8,
                filled=True,
                extruded=True,
                get_elevation="A11/10",
                get_fill_color=[255, 40, 40],
                pickable=True,
                auto_highlight=True,
            ),
        ],
    )
    html_content: str = deck.to_html(as_string=True)  # type:ignore
    custom_css = "body { font-family: sans-serif; }"
    html_content = insert_custom_css(html_content, custom_css)
    return html_content, land_data


html_content, land_data = draw_lands(
    st.session_state["equity"],
    st.session_state["loan"],
)
# `st.pyplot_chart`로도 충분히 `pydeck` 지도를 표시할 수 있지만,
# 알 수 없는 이유로 현저한 성능 저하가 발생하여
# 지도 항목 개수가 수 만 개만 넘어가더라도 지나치게 느려집니다.
# https://github.com/streamlit/streamlit/issues/5532
# 이 문제를 피해 가기 위해 일단 `pydeck` 지도를 HTML로 변환한 후
# `streamlit` 라이브러리의 `components.html`로 표시하고 있습니다.
# 이 방법으로는 지도 항목 개수가 수십만 개 이상이 되어도 괜찮으나,
# 그 정도로 항목이 많아지면 필지 용량 조절에 신경써야 합니다.
# 필지 용량 데이터는 대략 200MB 아래로 조절해야 페이지 로딩 속도가 합리적일 것입니다.
components.html(
    html_content,
    height=720,
)
html_size = convert_size(len(html_content.encode("utf-8")))
st.caption(f"내부적으로 생성된 필지 데이터의 용량은 {html_size}입니다.")
with st.expander("필지 데이터 일부"):
    st.dataframe(land_data.head(10).astype(str))

input_column, info_column, guide_column = st.columns((1, 2, 1), gap="medium")

input_column.header("요인 입력")
input_column.subheader("투자 계획")
input_column.slider("자기자본 (억원)", 5, 50, key="equity")
input_column.slider("은행 대출 한도 (억원)", 10, 100, key="loan")
input_column.subheader("변수")
input_column.slider("제곱미터당 공사비 (만원)", 200, 400, key="construction_cost")
input_column.slider("금리 (%)", 0.0, 10.0, key="interest_rate")
input_column.slider("공실률 (%)", 0, 40, key="empty_ratio")
input_column.subheader("필터")
input_column.checkbox("예산 내의 필지만 표시하기")

info_column.header("정보")
info_column.text_input("필지 ID를 입력하세요.", value="")

guide_column.header("안내")
guide_column.markdown(
    r"""
이 시스템은 예상 연면적과 해당 지역의 공공데이터를 기반으로 대략적인 월세를 계산한 후,
현금 지출을 차감하여 내부수익률을 산출한 후 지도에 표시합니다.
"""
)
guide_column.latex(
    r"""
F = A*f*(1-v/100)
\\
R = F - 0.05*F - t(p) - i*l
\\
r = \frac{R}{e}*100
""",
)
guide_column.markdown(
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
