# dev 브랜치 테스트 수정
import requests
from tabulate import tabulate
import pyfiglet
from tqdm import tqdm
import emoji
import tqdm as tqdm_module  # 버전확인용

def main():
def main():
    print(pyfiglet.figlet_format("MASTER VERSION"))
    print(pyfiglet.figlet_format("DEV VERSION"))

    print("\n[1] HTTP 요청 테스트")
    r = requests.get("https://httpbin.org/get")
    print("Status:", r.status_code)

    print("\n[2] 패키지 표 출력")
    rows = [
        ["패키지", "버전"],
        ["requests", requests.__version__],
        ["emoji", emoji.__version__],
        ["tqdm", tqdm.__version__],
    ]
    print(tabulate(rows, headers="firstrow", tablefmt="github"))

    print("\n[3] tqdm 진행바")
    for _ in tqdm(range(30)):
        pass

    print(emoji.emojize("\n완료! :sparkles:"))

if __name__ == "__main__":
    main()