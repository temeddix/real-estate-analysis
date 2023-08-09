import json
import math
import os
import geopandas


def format_json(input: str, item_limit: int = 5) -> str:
    structure = json.loads(input)
    if isinstance(structure, list):
        structure = structure[:item_limit]
    if isinstance(structure, dict):
        for item_key, item_value in structure.items():
            if isinstance(item_value, list):
                structure[item_key] = item_value[:item_limit]
    return json.dumps(
        structure,
        indent=2,
        ensure_ascii=False,
    )


def convert_size(size_bytes: int) -> str:
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def read_geofile(path: str) -> geopandas.GeoDataFrame:
    downloaded_filepath = f"./downloaded_data/{path}.shp"
    processed_filepath = f"./processed_data/{path}.parquet"
    online_url = f"sftp://kdhns.synology.me:5022/KDHPF/real-estate-analysis/processed_data/{path}.parquet"

    if os.path.isfile(processed_filepath):
        geo_data = geopandas.read_parquet(processed_filepath)
    else:
        # 공공데이터가 준비되어 있다면 그걸 읽습니다.
        if os.path.isfile(downloaded_filepath):
            geo_data = geopandas.read_file(
                downloaded_filepath,
                encoding="euc-kr",
            )
        # 공공데이터가 다운로드되지 않았다면 NAS 파일을 받습니다.
        # 배포된 클라우드에서는 파일 준비에 이 절차가 필요합니다.
        else:
            geo_data = geopandas.read_parquet(
                online_url,
                storage_options={"username": "anonymous", "password": ""},
            )
        processed_directory = os.path.dirname(processed_filepath)
        os.makedirs(processed_directory, exist_ok=True)
        geo_data.to_parquet(processed_filepath)

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
