import sys
import six

#버전 확인을 통한 구분으로 마이그레이션

print(sys.version_info.major)       #version_info을 통해서 major의 값이 3 or 2로 버전 구분이 가능합니다.

if sys.version_info.major == 3:
    print("버전 확인, python 3")
elif sys.version_info.major == 2:
    #print "버전 확인, python 2"  
    print("python 3 에서 print "" 로 실행 시 에러로 잡히므로 우선 주석 처리해놓았습니다.")


print(six.PY3)
print(six.PY2)       #six.PY2, six.PY3을 통해서 True or False로 해당 버전에 대한 구분이 가능합니다. 

if six.PY3:
    print("버전 확인, python 3")
elif six.PY2:
    #print "버전 확인, python 2"  
    print("python 3 에서 print "" 로 실행 시 에러로 잡히므로 우선 주석 처리해놓았습니다.")
    


#1. print, python 2는 print ""으로 처리, python 3은 print()로 처리하는 차이가 있습니다.
if sys.version_info.major == 3:
    print("print 확인, python 3")
elif sys.version_info.major == 2:
    #print "print 확인, python 2"  
    print("python 3 에서 print "" 로 실행 시 에러로 잡히므로 우선 주석 처리해놓았습니다.")
    

#2. 계산 식, python 2는 정수/정수 = 정수로 표현하고, python 3는 정수/정수 = 실수로 표현이 가능해졌습니다.
if sys.version_info.major == 3:
    print("타입 확인", 1/2)
    print(type(1/2), "python 3")
elif sys.version_info.major == 2:
    #print("타입 확인", 1/2)
    #print(type(1/2), "python 2")  
    print("python 3 에서 print "" 로 실행 시 에러로 잡히므로 우선 주석 처리해놓았습니다.")
    

#3. xrange or range, python 2는 xrange를 사용하지만 phtyon 3는 range를 사용합니다.
if sys.version_info.major == 3:
    for x in range(5):
        print(x)
elif sys.version_info.major == 2:
    # for x in xrange(5):
    #     print "x"
    print("python 3 에서 xrange 실행 시 에러로 잡히므로 우선 주석 처리해놓았습니다.")


#4. unicode and binary, python 2의 경우 문자열이 binary로 표현되고 python 3의 경우 unicode로 표현되는 차이가 있습니다.
#결론적으로 기존에 python 2에서 binary 타입을 사용하던 함수 혹은 모듈이 있었다면 python 3에서는 바꿔줄 필요가 있습니다.
if sys.version_info.major == 3:
    s = b"string"
    print(type(s))
elif sys.version_info.major == 2:
    s = "그대로"
    print(type(s))


#5. class에 대한 사용
#python 3에서는 super()에 인자를 넣지 않아도 됩니다(인자를 넣어도 실행됩니다).
class A:
   def __init__(self):
      print("Class A __init__()")
      super(A, self).__init__()

class B(A):
   def __init__(self):
      print("Class B __init__()")
      super().__init__()

b = B()

#python 2에서는 super()에 인자를 넣어야 됩니다. python 3에서도 실행되므로 이렇게 작성하는 것이 좋을것 같습니다.
class C:
   def __init__(self):
      print("Class C __init__()")
      super(C, self).__init__()

class D(C):
   def __init__(self):
      print("Class D __init__()")
      super(D, self).__init__()

d = D()