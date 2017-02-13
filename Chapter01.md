# 밑바닥부터 시작하는 딥러닝
## Chapter 01 헬로 파이썬
### Numpy
- 배열
    - np.array() 메소드 사용
        - 인수: Python List
        - 반환: Numpy 라이브러리의 배열(numpy.ndarray)
       np.array([1.0, 2.0, 3.0])
- 산술 연산
    - np.array()로 생성한 Numpy 배열로 사칙 연산 가능
    - **배열 간의 원소 수가 같아야 함**
    - 각 원소별(Element-Wise) 계산
- N차원 배열
    - .shape: 행렬의 크기
    - .dtype: 행렬에 담긴 원소의 자료형
    - 사칙연산 가능, 스칼라값과 산술 연산도 가능
- 브로드캐스트
    - 행렬 A만큼 스칼라 값이 확대된 뒤 연산되는 기능
- 원소 접근
    - .platten(): 행렬을 1차원 배열로 변환(평탄화)
    - Numpy 배열에 부등호 연산자 사용하면 - Bool 배열로 Return
### matplotlib
- matplotlib: 그래프 그리기용 라이브러리
    - pyplot: 단순한 그래프 그리기
      import matplotlib.pyplot
        - .sin(): Numpy에서 sin 함수로 변환
        - matplotlib.pyplot.plot(x, y): x와 y를 인수로 그래프 그리기
    - imread: 이미지 불러오기
        import matplotlib.pyplot
       from matplotlib.image import imread
       img = imread('이미지 경로)
       plt.imshow(img)
### 정리
- 사용 언어: Python 3
- 사용 라이브러리: Numpy, matplotlib(둘 다 Anaconda에 존재)
- Numpy에서 다차원 배열 사용 방법 알기
- matplotlib에서 그래프 그리는 법 알기