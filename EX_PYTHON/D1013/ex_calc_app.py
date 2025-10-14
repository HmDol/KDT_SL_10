## ==================================================================
##                          계산기 프로그램 구현
## - 클래스 기반 + CUI 환경
## ==================================================================
## 모듈 로딩
## ==================================================================
from datetime import datetime

## ==================================================================
## 클래스 기능 : 연산 상태 및 히스토리(사칙연산만) 저장/출력 계산기
## 클래스 이름 : Calculator
## 속      성 : value     - 현재까지의 계산결과 저장 
##             history   - 연산 과정 저장 
## ==================================================================
class Calculator:
    ##---------------------------------------------------------------
    ##- 인스턴스 속성 초기화 메서드 
    ##---------------------------------------------------------------
    def __init__(self, value=0):
        self.value   = value
        self.history = []  # [{"op","prev","arg","result","ts"}...]

    ##---------------------------------------------------------------
    ##- 인스턴스 메서드들
    ##---------------------------------------------------------------
    ##- 메서드 기능 : 계산 진행 날짜/시간 저장 메서드
    ##- 메서드 이름 : _stamp    _메서드명 : 클래스 내부에서만 사용/import X
    ##---------------------------------------------------------------
    def _stamp(self):
        return datetime.now().isoformat(timespec="seconds")

    ##---------------------------------------------------------------
    ##- 메서드 기능 : 연산 이력 저장 기능 
    ##- 메서드 이름 : _set_value      클래스 내부에서만 사용/import X
    ##- 매개 변수들 : result   연산결과값
    ##              op        연산자
    ##              arg       피연산자
    ##- 반환  결과 : 인스턴스 
    ##---------------------------------------------------------------
    def _set_value(self, result, op, arg):
        prev = self.value
        self.value = result
        self.history.append({ "op": op, 
                             "prev": prev, 
                             "arg": arg, 
                             "result": self.value,            
                             "ts": self._stamp() })
        return self

    # 상태 제어 명령어 관련 메서드: 결과보기, 값 설정, 결과 지우기 
    def result(self): return self.value
    def set(self, x): return self._set_value(x, "set", x)
    def clear(self):  return self._set_value(0, "clear", None)
    def exit(self ):  print("프로그램 종료합니다.")

    # 사칙연산만
    def add(self, x): return self._set_value(self.value + x, "add", x)
    def sub(self, x): return self._set_value(self.value - x, "sub", x)
    def mul(self, x): return self._set_value(self.value * x, "mul", x)
    def div(self, x): return self._set_value(self.value / x, "div", x)

## ==================================================================
## 전역 변수 및 사용자 정의 함수들
## ==================================================================
# ---------------------------------------------------------
# 터미널 REPL (사칙연산 + 히스토리 + 종료만)
# ---------------------------------------------------------
## 설명 문자열 저장 
FILE_NAME = './calc_help.txt'
with open(FILE_NAME, mode='r', encoding='utf-8') as f:
    HELP = f.read()


## ----------------------------------------------------------------------
## 함수기능 : 입력 값을 float으로 변환 후 반환 
## 함수이름 : parse_float
## 매개변수 : x     - 입력 피연산자 값
## 결과반환 : float 변환 값 
## ----------------------------------------------------------------------
def parse_float(x):
    # 정수도 float 캐스팅 허용
    if x.lower().startswith(("+inf", "-inf", "nan")):
        raise ValueError("NaN/Inf는 허용하지 않습니다.")
    # float 변환 결과 반환
    return float(x)


## ----------------------------------------------------------------------
## 함수기능 : 연산 결과 제거 또는 출력
## 함수이름 : print_result
## 매개변수 : calc      - 계산기 인스턴스
##           isClear   - 연산 결과 삭제 여부 [기 False]
## 결과반환 : X
## ----------------------------------------------------------------------
def print_result(calc, isClear=False):
    if isClear: calc.clear()
    print(f"= {calc.result()}")

## ----------------------------------------------------------------------
## 함수기능 : 연산 이력 출력
## 함수이름 : print_history
## 매개변수 : k          - 출력 이력 수  [기 10개]
##           calc      - 계산기 인스턴스
## 결과반환 : X
## ----------------------------------------------------------------------
def print_history(k, calc):
    #- 연산 이력 추출
    items = calc.history[-k:]

    #- 연산 이력 없는 경우 처리
    if not items:
        print("(기록 없음)")
        return
    
    #- 연산 이력 출력
    for i, h in enumerate(items, 1):
        print(f"{i:>3}. [{h['ts']}] {h['op']:4s} | prev={h['prev']:<7} ", end='')
        print(f"arg={h['arg']:<7} -> result={h['result']:<7}")
        
## ----------------------------------------------------------------------
## 함수이름 : 계산기 프로그램 구동 및 처리 
## ----------------------------------------------------------------------
def check_calc(nums, cmd, func, calc):
    #- 명령어 형식 체크 및 처리 
    if len(nums) != 1:
        raise ValueError(f"사용법: {cmd} <x>")
    
    #- 연산 수행 및 결과 출력
    func(parse_float(nums[0]))
    print_result(calc)


## ----------------------------------------------------------------------
## 함수기능 : 계산기 프로그램 구동 및 처리 
## 함수이름 : run_calc
## 매개변수 : X 
## 결과반환 : X
## ----------------------------------------------------------------------
def run_calc():
    ## 계산기 인스턴스 생성
    calc = Calculator(0)

    ## 사용자 메뉴 및 설명 출력
    print("터미널 계산기 시작!!!\n(help  설명, 'x'/'exit'/'quit' 종료 ):")
    print_result(calc)

    ## 사용자 입력에 따른 계산기 구동 
    while True:
        try:
            line = input("CALC >>> ").strip()
            if not line:      
                print("\n입력이 올바르지 않습니다..")    
                continue
            
            ## 입력에 대한 처리 진행
            cmd, *args = line.split()
            cmd = cmd.lower()

            # 종료
            if cmd in ("x", "exit", "quit"): return calc.exit()
            
            # 명령어에 대한 처리 
            if   cmd == "help":     print(HELP)
            elif cmd == "result":   print_result(calc)
            elif cmd == "clear":    print_result(calc, True)
            elif cmd == "set":      check_calc(args, "set", calc.set, calc)

            # 사칙 연산 명령어 처리
            elif cmd == "add":      check_calc(args, "add", calc.add, calc)
            elif cmd == "sub":      check_calc(args, "sub", calc.sub, calc)
            elif cmd == "mul":      check_calc(args, "mul", calc.mul, calc)
            elif cmd == "div":      check_calc(args, "div", calc.div, calc)

            # 연산 기록 명령어 처리
            elif cmd == "hist":     print_history( int(args[0]) if args else 10, calc)
            # 잘못된 명령어 처리
            else:                   print("알 수 없는 명령입니다. 'help' 입력하세요.")

        except IndexError:
            print("인자가 부족합니다. 'help'를 참고하세요.")
        except ValueError as e: 
            print(f"값 오류: {e}")
        except ZeroDivisionError as e:
            print(f"수학 오류: {e}")
        except (EOFError, KeyboardInterrupt):
            # Ctrl+C 키보드 종료 입력
            print("\n종료합니다.")
            break


## ----------------------------------------------------------------------
## 스크립트 코드 실행 처리 
## ----------------------------------------------------------------------
if __name__ == "__main__":
    ## 계산기 프로그램 실행
    run_calc()