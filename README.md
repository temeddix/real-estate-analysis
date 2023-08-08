> As this project is interested in Korean lands, all guides will be written in Korean to fully represent national laws and terminologies.

# 소개

이 프로젝트는 사용자가 다양한 요소를 고려하여 부동산의 관점에서 투자하기 좋은 토지를 찾을 수 있도록 돕는 것을 목표로 합니다. 읽기 쉬운 코드와 다루기 쉬운 화면을 제공하는 것에 중점을 두고 있습니다.

이 프로젝트는 모든 텍스트 데이터에 한국어 인코딩이 적용되어 있다고 간주합니다.

# 시스템 준비

우선, **Python**이 준비되었는지 확인하세요. Python은 가독성이 높고 작성하기 쉬우며, 데이터 분석을 위한 다양한 패키지가 개발되어 있는 프로그래밍 언어입니다. Python은 [공식 다운로드 페이지](https://www.python.org/downloads/)로부터 설치하는 것이 것이 가장 쉽습니다.

또한, **Poetry**가 설치되었는지도 확인하세요. Poetry는 `pip`와 `venv`의 기능을 모두 제공하는 훌륭한 의존성 관리 도구입니다. 자세한 설치 방법은 [공식 문서](https://python-poetry.org/docs/)에 적혀 있습니다.

# 데이터 준비

이 단계부터는 Git clone으로 이 저장소를 컴퓨터에 저장해 놓았다고 간주합니다.

이 프로젝트는 정부에서 제공하는 개방데이터를 활용합니다. Python 코드가 개방데이터를 읽을 수 있어야 하므로, `open_data` 폴더를 생성하고 해당 폴더 내부에 [국토정보 개방데이터](http://openapi.nsdi.go.kr/nsdi/index.do)로부터 다운로드한 파일들을 넣어주세요. `open_data` 폴더에는 수 GB 이상의 큰 데이터가 담겨야 하기 때문에, Git 버전 관리 시스템에서 제외되도록 `.gitignore` 파일에 적혀 있습니다.

`processed_data` 폴더에는 웹 서버에 배포될 수 있도록 가공된, 비교적 작은 크기의 데이터 파일이 담기게 됩니다. 이 폴더는 버전 관리 시스템에 포함됩니다.

개방데이터를 담을 때나 가공 데이터를 생성할 때에는 아래 폴더 구조를 지켜주세요. 모든 Python 코드는 이와 같은 경로로 데이터 파일이 준비되어 있다고 간주합니다.

```json
real-estate-analysis/
├── open_data/
│   └── basic_building_info/ // GIS건물일반집합정보(SHP)
│       ├── AL_11_D162_20230120.shp
│       └── ...
├── processed_data/
│   └── ...
└── ...
```

# 명령어

패키지 설치하기:

```
poetry install
```

가상 환경 활성화하기:

```
poetry shell
```

코드 실행하기:

```
streamlit run home.py
```

# 규칙

- 가능한 한 언제나 함수 매개변수와 전역 변수에 적절한 타입 힌트를 제공해 주세요. 또한 사용 중인 IDE에서 Basic 수준의 타입 검사를 켜 두세요.
- [Black](https://github.com/psf/black) 서식기를 사용하세요.
