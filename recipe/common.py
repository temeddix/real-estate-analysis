import math
import os

import geopandas
import streamlit as st


def convert_size(size_bytes: int) -> str:
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


@st.cache_resource
def read_geofile(path: str) -> geopandas.GeoDataFrame:
    # 가능하다면 원본이 아닌 가공된 데이터를 사용합니다.
    # 내용물은 같지만, 읽고 쓰는 속도가 훨씬 빠르고 크기도 작기 때문입니다.
    downloaded_filepath = f"./downloaded_data/{path}.shp"
    processed_filepath = f"./processed_data/{path}.parquet"
    online_url = f"sftp://kdhns.synology.me:5022/KDHPF/real-estate-analysis/processed_data/{path}.parquet"

    if os.path.isfile(processed_filepath):
        # 가공된 데이터가 준비되어 있다면 그걸 읽습니다.
        geo_data = geopandas.read_parquet(processed_filepath)  # type:ignore
    else:
        # 가공된 데이터가 없다면 만들거나 다운로드해야 합니다.
        if os.path.isfile(downloaded_filepath):
            # 원본 공공데이터가 준비되어 있다면 그걸 읽습니다.
            geo_data = geopandas.read_file(  # type:ignore
                downloaded_filepath,
                encoding="euc-kr",
            )
        else:
            # 공공데이터가 다운로드되지 않았다면 가공된 파일을 NAS로부터 받습니다.
            # 배포된 클라우드 서버에서는 파일 준비에 이 절차가 필요합니다.
            geo_data = geopandas.read_parquet(  # type:ignore
                online_url,
                storage_options={"username": "anonymous", "password": ""},
            )
        # 가공된 데이터를 저장해 놓습니다.
        processed_directory = os.path.dirname(processed_filepath)
        os.makedirs(processed_directory, exist_ok=True)
        geo_data.to_parquet(processed_filepath)  # type:ignore

    return geo_data


def insert_custom_css(html_string: str, custom_css: str) -> str:
    # Find the position to insert the custom CSS
    head_position = html_string.find("<head>")
    if head_position == -1:
        # If <head> is not found, insert the <style> tag at the beginning of the HTML
        head_position = 0
    else:
        head_position += len("<head>")

    # Insert the custom CSS inside the <head> section
    modified_html = (
        html_string[:head_position]
        + "<style>"
        + custom_css
        + "</style>"
        + html_string[head_position:]
    )

    return modified_html
