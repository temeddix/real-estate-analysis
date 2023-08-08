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


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def read_geofile(path: str):
    processed_filepath = f"./processed_data/{path}.parquet"

    if os.path.isfile(processed_filepath):
        geo_data = geopandas.read_parquet(processed_filepath)
    else:
        geo_data = geopandas.read_file(
            f"./open_data/{path}.shp",
            encoding="euc-kr",
        )
        processed_directory = os.path.dirname(processed_filepath)
        os.makedirs(processed_directory, exist_ok=True)
        geo_data.to_parquet(processed_filepath)

    return geo_data
