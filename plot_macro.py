from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt

def upload_and_plot():
    # 파일 업로드
    uploaded = files.upload()

    # 업로드한 파일명 확인
    file_name = list(uploaded.keys())[0]

    # 데이터 파일 읽기
    data = pd.read_csv(file_name, sep='\t', encoding='cp949')

    # 데이터의 열 이름 확인
    print(data.columns)

    def plot_graph_from_excel(x_col, y_col, graph_type, color):
        plt.figure(figsize=(10, 6))  # 그래프 크기 설정

        if graph_type.lower() == 'scatter':
            plt.scatter(data[x_col], data[y_col], color=color)  # 산포도 그래프
            plt.title('산점도 그래프')
        elif graph_type.lower() == 'line':
            plt.plot(data[x_col], data[y_col], color=color)  # 선 그래프
            plt.title('선 그래프')
        else:
            print("지원하지 않는 그래프 형태입니다.")
            return

        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.show()

    # 파일 경로와 그래프를 그릴 컬럼, 그래프 종류, 색상 입력 받기
    x_column = input('X 축으로 사용할 열을 입력하세요: ')
    y_column = input('Y 축으로 사용할 열을 입력하세요: ')
    plot_type = input("그래프 종류를 입력하세요 (scatter 또는 line): ")
    plot_color = input("그래프 색상을 입력하세요 (예: 'red', 'blue', 'green' 등): ")

    # 함수 호출하여 그래프 그리기
    plot_graph_from_excel(x_column, y_column, plot_type, plot_color)

def upload_and_plot_combined():
    # 첫 번째 파일 업로드
    uploaded_1 = files.upload()
    file_name_1 = list(uploaded_1.keys())[0]
    data_1 = pd.read_csv(file_name_1, encoding='cp949', delimiter='\t')  # 탭을 구분자로 사용하여 데이터 파일 읽기

    # 데이터의 열 이름 확인
    print(data_1.columns)

    # 데이터의 행 이름 확인
    print(data_1.index)

    # 두 번째 파일 업로드
    uploaded_2 = files.upload()
    file_name_2 = list(uploaded_2.keys())[0]
    data_2 = pd.read_csv(file_name_2, encoding='cp949', delimiter='\t')  # 탭을 구분자로 사용하여 데이터 파일 읽기

    # 데이터의 열 이름 확인
    print(data_2.columns)

    # 데이터의 행 이름 확인
    print(data_2.index)

    def plot_graph_from_excel(ax, x_col, y_col, graph_type, color, data, label):
        if graph_type.lower() == 'scatter':
            ax.scatter(data[x_col], data[y_col], color=color, label=label)  # 산점도 그래프
        elif graph_type.lower() == 'line':
            ax.plot(data[x_col], data[y_col], color=color, label=label)  # 선 그래프
        else:
            print("지원하지 않는 그래프 형태입니다.")
            return

        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.legend()

    fig, ax = plt.subplots(figsize=(10, 6))  # 서브플롯 하나 생성

    x_column_1 = input('첫 번째 파일의 X 축으로 사용할 열을 입력하세요: ')
    y_column_1 = input('첫 번째 파일의 Y 축으로 사용할 열을 입력하세요: ')
    plot_type_1 = input("첫 번째 파일의 그래프 종류를 입력하세요 (scatter 또는 line): ")
    plot_color_1 = input("첫 번째 파일의 그래프 색상을 입력하세요 (예: 'red', 'blue', 'green' 등): ")

    plot_graph_from_excel(ax, x_column_1, y_column_1, plot_type_1, plot_color_1, data_1, 'File 1')

    x_column_2 = input('두 번째 파일의 X 축으로 사용할 열을 입력하세요: ')
    y_column_2 = input('두 번째 파일의 Y 축으로 사용할 열을 입력하세요: ')
    plot_type_2 = input("두 번째 파일의 그래프 종류를 입력하세요 (scatter 또는 line): ")
    plot_color_2 = input("두 번째 파일의 그래프 색상을 입력하세요 (예: 'red', 'blue', 'green' 등): ")

    plot_graph_from_excel(ax, x_column_2, y_column_2, plot_type_2, plot_color_2, data_2, 'File 2')

    plt.tight_layout()  # 그래프 간 간격 조정
    plt.show()  # 두 개의 그래프 한 번에 표시
