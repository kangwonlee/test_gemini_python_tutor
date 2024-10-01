# Basic Arithmetic Operations using Functions<br>함수를 이용한 기본적인 사칙 연산

**Please edit and commit the `exercise.py` file to your web repository.**<br>
**`exercise.py` 파일을 수정하여 학생의 웹 저장소에 저장 바랍니다.**

## Objective 목표

Complete the following functions in `exercise.py`:<br>
`exercise.py` 파일에서 다음 함수들을 완성하세요:

* `add(a, b)`: <br>Adds two numbers and returns the result.<br>두 숫자를 더하고 결과를 반환합니다.
* `sub(a, b)`: <br>Subtracts two numbers and returns the result.<br>두 숫자를 빼고 결과를 반환합니다.
* `mul(a, b)`: <br>Multiplies two numbers and returns the result.<br>두 숫자를 곱하고 결과를 반환합니다.
* `div(a, b)`: <br>Divides two numbers and returns the result. If division by zero, return a string `'Cannot divide by zero'` instead.<br>두 숫자를 나누고 결과를 반환합니다. 0으로 나누는 경우 `'Cannot divide by zero'` 라는 문자열을 대신 반환합니다.

## Files 제공된 파일

* **exercise.py**: Includes the skeleton code for the four functions. Edit this file to complete the assignment.<br>위 네 함수의 뼈대 코드가 포함되어 있습니다. 이 파일을 수정하여 과제를 완성하세요.
* **sample.py**: Sample code to test the completed functions.<br>완성된 함수를 테스트하는 예제 코드입니다.

## Function descriptions 함수 설명

```python
def add(a, b):
    # TODO:
    # Write code to add two numbers
    # 두 숫자를 더하는 코드를 작성하세요.
    # return the result.
    # 결과값을 return하세요.

def sub(a, b):
    # TODO:
    # Write code to subtract two numbers
    # 두 숫자를 빼는 코드를 작성하세요.
    # return the result.
    # 결과값을 return하세요.

def mul(a, b):
    # TODO:
    # Write code to multiply two numbers
    # 두 숫자를 곱하는 코드를 작성하세요.
    # return the result.
    # 결과값을 return하세요.

def div(a, b):
    # TODO:
    # Write code to divide two numbers
    # 두 숫자를 나누는 코드를 작성하세요.
    # return the result.
    # 결과값을 return하세요.
    # if divide by zero, please return string `'Cannot divide by zero'` instead.
    # 0으로 나누는 경우 `'Cannot divide by zero'` 라는 문자열을 반환합니다.
```

* **Input arguments 입력 매개변수:**
    * `a`: The first number.<br>첫번쨰 숫자
    * `b`: The second number.<br>두번쨰 숫자
* **Output result 출력 결과:**
    * The result of the corresponding arithmetic operation.<br>각 연산의 결과

## How to run .py file on a shell 쉘에서 실행해 보는 방법

1. Complete the functions in the `exercise.py` file.<br>`exercise.py` 파일의 함수들을 완성합니다.
1. On a shell, run `python sample.py` to see the results.<br>쉘에서 `python sample.py` 명령을 실행하여 결과를 확인합니다.

## How to run the function on Google Colab<br>함수를 구글 코랩에서 실행해보는 방법 예

1. Ensure that you have completed the functions in `exercise.py` before proceeding.<br>실행하기 전에 `exercise.py` 파일의 함수들을 모두 완성했는지 확인하세요.
1. Open Google Colab: Go to https://colab.research.google.com/ and create a new notebook.<br>Google Colab 열기: https://colab.research.google.com/ 에 접속하여 새 노트북을 만듭니다.
1. Upload the .py files:<br>.py 파일 업로드:
    1. Click on the "Files" icon on the left sidebar.<br>왼쪽 사이드바에서 "파일" 아이콘을 클릭합니다.
    1. Click on the "Upload" button and select your exercise.py and sample.py files.<br>"업로드" 버튼을 클릭하고 exercise.py 와 sample.py 파일을 선택합니다.
1. Run the code:<br>코드 실행:
    1. In a new code cell, type `!python sample.py` and press <kbd>Shift</kbd>+<kbd>Enter</kbd> to execute it.<br>새로운 코드 셀에 `!python sample.py`를 입력하고 <kbd>Shift</kbd>+<kbd>Enter</kbd> 를 눌러 실행합니다.

## Notice 참고

* Edit `exercise.py` file only.<br>`exercise.py` 파일만 수정하세요.

* In the `exercise.py`, all code lines must belong to one of functions.<br>`exercise.py` 파일의 모든 코드 행은 함수 중 하나에 속해야 합니다.
* The `random` module will be used to generate pseudo-random numbers.<br>`random` 모듈은 무작위 숫자를 생성하는 데 사용됩니다.
* To complete the assignment, understand how Python functions work and add the necessary logic.<brr>파이썬 함수의 작동 방식을 이해하고 필요한 로직을 추가해야 합니다.
* For more information on Python functions, please refer to [4.7 Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)<br>파이썬 함수에 대한 참고문헌 : [파이썬 함수의 구조](https://wikidocs.net/24#_3)

## Submit 제출

Please commit the completed `exercise.py` file to the web repository.<br>완성된 `exercise.py` 파일을 웹 저장소에 저장 바랍니다.

## Grading Criteria<br>채점 기준

| Criteria<br>기준 | Points<br>배점 |
|:-----:|:-----:|
| Is the code written according to Python syntax?<br>Python 문법대로 작성되었는가? | 2 |
| Are all code lines belong to one of functions?<br>모든 코드가 함수 내에 작성되었는가? | 1 |
| Is the output as expected?<br>출력 결과가 예상과 같은가? | 2 |

## How to Use the GitHub Online Editor (If Needed)<br>Github 온라인 편집기 필요한 경우 사용법

* Press the <kbd>.</kbd> key while viewing the files in your repository on GitHub. This will launch a web version of VS Code.<br><kbd>.</kbd> 키를 누르면 MS VS Code 의 Web version 이 시작됨
* Make your changes to the exercise file.<br>실습 파일을 수정
* To commit your changes:<br>수정 사항을 commit 등록 하려면:
    * Click the branch icon on the left sidebar (the third icon below the magnifying glass).<br>왼쪽에서 줄 셋 아래 (확대경 다음) 세번째 가지치기 아이콘 선택
    * Click the `+` sign next to the filename to stage your changes.<br>파일 이름의 오른쪽 `+` 기호 선택 (staging)
    * In the text box above, summarize your changes in a clear and concise message.<br>위 빈칸에 변경 사항을 간결 명료하게 요약
       * Here are some examples:<br>예:
       * "Add function to calculate average grade"<br>"평균값을 계산하기 위해 함수 추가"
       * "Fix bug causing incorrect calculations"<br>"계산 오류를 일으키는 버그 수정"
       * "Refactor code for better readability"<br>"가독성 향상을 위해 코드 재구성"
    * Click "Commit & Push."<br>[커밋 및 푸시] 선택
* Click "Back to Repository" on the branch icon to return to your repository.<br>줄 셋 의 [리포지토리로 이동] 선택하여 저장소로 복귀

## NOTICE REGARDING STUDENT SUBMISSIONS<br>제출 결과물에 대한 알림

* Your submissions for this assignment may be used for various educational purposes. These purposes may include developing and improving educational tools, research, creating test cases, and training datasets.<br>제출 결과물은 다양한 교육 목적으로 사용될 수 있을 밝혀둡니다. (교육 도구 개발 및 개선, 연구, 테스트 케이스 및 교육용 데이터셋 생성 등).

* The submissions will be anonymized and used solely for educational or research purposes. No personally identifiable information will be shared.<br>제출된 결과물은 익명화되어 교육 및 연구 목적으로만 사용되며, 개인 식별 정보는 공유되지 않을 것입니다.

* If you do not wish to have your submission used for any of these purposes, please inform the instructor before the assignment deadline.<br>위와 같은 목적으로 사용되기 원하지 않는 경우, 과제 마감일 전에 강사에게 알려주기 바랍니다.
