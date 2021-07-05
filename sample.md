## Python2 -> 3 마이그레이션 기술 조사 및 샘플링
<br>
<br>

**1. 마이그레이션 방법**<br><br>
기존 python 2 코드와 python 3 코드를 호환하기 위한 방법으로<br>
**import sys** 혹은<br>
**import six** 를 하여<br><br>
**if sys.version_info.major == 3:** <br>
처럼 sys.version_info.major으로 버전을 확인하는 if문을 열거나(위 코드의 경우 버전 3일 경우를 의미합니다)<br><br>
**if six.PY3:** <br>
과 같이 six.PY3를 통해 버전을 확인하는 if문을 엽니다.
<br><br>
그 후 각 버전에 맞는 코드를 작성하여 실행합니다.
<br><br>

**2. 샘플 코드 설명**<br><br>
**2-1. print문 차이**<br>
python 2는 print ''로 실행하지만, python 3은 print()로 실행됩니다.<br><br>
**2-2. 계산식 차이**<br>
python 2는 '정수 / 정수 = 정수'로 표현되지만, python 3은 '정수 / 정수 = 실수'로 표현이 가능합니다.<br><br>
**2-3. xrange와 range**<br>
python 2는 xrange를 사용했지만 python 3은 range로 사용합니다.<br><br>
**2-4. unicode and binary**<br>
python 2는 문자열이 binary로 표현되고 python 3은 unicode로 사용합니다. 즉, 기존에 python 2에서 binary로 사용하던 모듈 혹은 함수가 존재한다면 python 3에서 문자열을 binary로 바꿔주는 과정이 필요합니다.<br><br>
**2-5. class에 대한 사용**<br>
python 2는 super()에 인자를 넣어야 합니다. python 3에서는 super()에 인자를 넣지 않아도 됩니다(인자를 넣어도 실행됩니다). 즉, 두 버전을 호환하려면 python 2의 문법을 사용해야 합니다.




