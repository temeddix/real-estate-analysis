> As this project is interested in Korean lands, all guides will be written in Korean to fully represent national laws and terminologies.

# 소개

이 프로젝트는 사용자가 다양한 요소를 고려하여 부동산의 관점에서 투자하기 좋은 토지를 찾을 수 있도록 돕는 것을 목표로 합니다. 읽기 쉬운 코드와 다루기 쉬운 화면을 제공하는 것에 중점을 두고 있습니다.

# 시스템 준비

우선, **Python**이 준비되었는지 확인하세요. Python은 가독성이 높고 작성하기 쉬우며, 데이터 분석을 위한 다양한 패키지가 개발되어 있는 프로그래밍 언어입니다. Python은 [공식 다운로드 페이지](https://www.python.org/downloads/)로부터 설치하는 것이 것이 가장 쉽습니다.

또한, **Poetry**가 설치되었는지도 확인하세요. Poetry는 `pip`와 `venv`의 기능을 모두 제공하는 훌륭한 의존성 관리 도구입니다. 자세한 설치 방법은 [공식 문서](https://python-poetry.org/docs/)에 적혀 있습니다.

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
