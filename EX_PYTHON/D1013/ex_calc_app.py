## ==================================================================
##                          계산기 프로그램 구현
## - 클래스 기반
## - CUI 환경
## ==================================================================
## 모듈 로딩
## ==================================================================
import math
from datetime import datetime

## ==================================================================
## 클래스 기능 : 연산 상태 및 히스토리(사칙연산만) 저장/출력 계산기
## 클래스 이름 : Calculator
## 속      성 : value   - 현재까지의 계산결과 저장
##             history - 연산 과정 저장 
## ==================================================================
class Calculator:
    ##---------------------------------------------------------------
    ##- 인스턴스 속성 초기화 메서드 
    ##---------------------------------------------------------------
    def __init__(self, value=0):
        self.value = value
        self.history = []  # [{"op","prev","arg","result","ts"}...]

    ##---------------------------------------------------------------
    ##- 인스턴스 메서드 : _메서드명() 내부 호출용
    ##---------------------------------------------------------------

    ## 메서드 기능 : 게산 진행 날짜/시간 저장
    ## 메서드 이름 : _stamp    / _메서드명: 클래스 내부에서만 사용되는 함수를 의미, import 안됨
    def _stamp(self):
        return datetime.now().isoformat(timespec="seconds")

    ## 메서드 기능 : 연산 이력 저장 기능
    ## 메서드 이름 : _set_value    / _메서드명: 클래스 내부에서만 사용되는 함수를 의미, import 안됨
    ## 메개 변수들 : result-결과, op-연산자, arg-값
    def _set_value(self, result, op, arg):
        prev = self.value
        self.value = result
        self.history.append({
            "op": op,
            "prev": prev,
            "arg": arg,
            "result": self.value,
            "ts": self._stamp(),
        })
        return self

    # 상태 제어 명령어 관련 메서드 : 결과보기, 값 설정, 결과 지우기
    def result(self): return self.value
    def set(self, x): return self._set_value(x, "set", x)
    def clear(self):  return self._set_value(0, "clear", None)

    # 사칙연산만
    def add(self, x): return self._set_value(self.value + x, "add", x)
    def sub(self, x): return self._set_value(self.value - x, "sub", x)
    def mul(self, x): return self._set_value(self.value * x, "mul", x)
    def div(self, x):
        if x == 0:
            raise ZeroDivisionError("0으로는 나눌 수 없습니다.")
        return self._set_value(self.value / x, "div", x)

    def __repr__(self):
        return f"Calculator(value={self.value}, history={len(self.history)} ops)"

# ---------------------------------------------------------
# 터미널 REPL (사칙연산 + 히스토리 + 종료만)
# ---------------------------------------------------------
FILE_NAME ='./calc_help.txt'
with open(FILE_NAME, mode = 'r', encoding='utf-8') as f :
    Help = f.read()


def parse_float(x):
    # 정수도 float 캐스팅 허용
    if x.lower().startswith(("+inf", "-inf", "nan")):
        raise ValueError("NaN/Inf는 허용하지 않습니다.")
    return float(x)

def print_result(calc):
    print(f"= {calc.result()}")

def print_history(items):
    if not items:
        print("(기록 없음)")
        return
    for i, h in enumerate(items, 1):
        op = h["op"]; prev = h["prev"]; arg = h["arg"]
        res = h["result"]; ts = h["ts"]
        print(f"{i:>3}. [{ts}] {op:4s} | prev={prev} arg={arg} -> result={res}")

def check_calc(nums, cmd, calc):
    if len(nums) != 1 :
        raise ValueError(f'사용법 : {cmd} <x>')
    calc.set(parse_float(nums[0]))

def run_calc():
    calc = Calculator(0)
    print("터미널 계산기 시작!  (help 입력 시 설명)")
    print_result(calc)

    while True:
        try:
            line = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n종료합니다.")
            break

        if not line:
            continue

        cmd, *args = line.split()
        cmd = cmd.lower()

        # 종료
        if cmd in ("x", "exit", "quit"):
            print("안녕히 가세요!")
            break

        try:
            if cmd == "help":
                print(HELP)

            # 값/상태
            elif cmd == "result":
                print_result(calc)

            elif cmd == "set":
                check_calc(args, "set", calc)
                # if len(args) != 1:
                #     raise ValueError("사용법: set <x>")
                # calc.set(parse_float(args[0]))
                print_result(calc)

            elif cmd == "clear":
                calc.clear()
                print_result(calc)

            # 사칙연산
            elif cmd == "add":
                check_calc(args, "add", calc)
                # if len(args) != 1:
                #     raise ValueError("사용법: add <x>")
                # calc.add(parse_float(args[0]))
                print_result(calc)

            elif cmd == "sub":
                check_calc(args, "sub", calc)
                # if len(args) != 1:
                #     raise ValueError("사용법: sub <x>")
                # calc.sub(parse_float(args[0]))
                print_result(calc)

            elif cmd == "mul":
                check_calc(args, "mul", calc)
                # if len(args) != 1:
                #     raise ValueError("사용법: mul <x>")
                # calc.mul(parse_float(args[0]))
                print_result(calc)

            elif cmd == "div":
                if len(args) != 1:
                    raise ValueError("사용법: div <x>")
                calc.div(parse_float(args[0]))
                print_result(calc)

            # 기록
            elif cmd == "hist":
                k = int(args[0]) if args else 10
                print_history(calc.history[-k:])

            else:
                print("알 수 없는 명령입니다. 'help'를 입력하세요.")

        except IndexError:
            print("인자가 부족합니다. 'help'를 참고하세요.")
        except ValueError as e:
            print(f"값 오류: {e}")
        except ZeroDivisionError as e:
            print(f"수학 오류: {e}")

if __name__ == "__main__":
    run_calc()
