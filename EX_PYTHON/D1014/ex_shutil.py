## -----------------------------------------------------------------
##                      내장 패키지 shutil활용  
##
## - shutil 모듈  → 파일/디렉토리 복사, 이동, 압축 같은 작업
##               → os 모듈과 함께 쓰이며, 파일 관리 자동화할 때 아주 유용
## -----------------------------------------------------------------
## 모듈 로딩
## -----------------------------------------------------------------
import shutil
import os

## =================================================================
##  전역 변수들     
## =================================================================
FILE1 = './test.txt'
FILE2 = './copy_test.txt'
FILE3 = './copy_with_meta.txt'
FILE4 = './moved_test.txt'

DIR1 = './myfolder'
DIR2 = './myfolder_backup'

## =================================================================
##  사용자 정의 함수들
## =================================================================
## -----------------------------------------------------------------
## 함수기능 : 파일 존재 체크 후 없으면 생성 함수
## 함수이름 : create_file
## 매개변수 : filepath 
## 반환결과 : 없음
## -----------------------------------------------------------------
def check_file(filepath):
    if not os.path.exists(filepath):
        with open(FILE1, mode='w', encoding='utf-8') as F:
            ret = F.write("Good Luck\n좋은 날~^^")
            if ret: print(f"{filepath} 생성되었습니다.")
    else:
        print(f"{filepath} 존재합니다.")

## -----------------------------------------------------------------
## 함수기능 : 2개 파일 정보 비교 출력 함수
## 함수이름 : compare_info
## 매개변수 : src_file 
##           des_file 
## 반환결과 : 없음
## -----------------------------------------------------------------
def compare_info(src_file, des_file):
    # os.stat() : 파일의 통계 정보 
    #             => 상태 정보 포함하는 os.stat_result 객체 반환
    src_stats = os.stat(src_file)
    des_stats = os.stat(des_file) 

    # 권한 추출 => 모드(권한, 파일 타입 등 포함) 정보 담고 있음
    MASK = 0o777
    print(src_stats.st_mode, oct(src_stats.st_mode)) # 0o100644
    src_permissions = oct(src_stats.st_mode & MASK)
    des_permissions = oct(des_stats.st_mode & MASK)

    # 메타데이터 비교
    print("-" * 30)
    print("파일 크기 (st_size):")
    print(f"원  본: {src_stats.st_size} bytes")
    print(f"복사본: {des_stats.st_size} bytes")
    print("-" * 30)

    print("파일 권한:")
    print(f"원  본: {src_permissions} ")
    print(f"복사본: {des_permissions} ")
    print("-" * 30)

    print("수정 시간 (st_mtime):")
    print(f"원  본: {src_stats.st_mtime}")
    print(f"복사본: {des_stats.st_mtime}")
    print("-" * 30)

    print("접근 시간 (st_atime):")
    print(f"원  본: {src_stats.st_atime}")
    print(f"복사본: {des_stats.st_atime}")
    print("-" * 30)

    print("생성 시간 (st_ctime):")
    print(f"원  본: {src_stats.st_ctime}")
    print(f"복사본: {des_stats.st_ctime}")
    print("-" * 30)
    print()


## -----------------------------------------------------------------
## [1] 파일 복사 / 이동 / 삭제
## -----------------------------------------------------------------
print('\n[1] 복사/이동/삭제 +++++++++++++++')

##=> 원본 파일 생성
check_file(FILE1)

##=> 파일 복사 : copyfile(원본, 복사본)
shutil.copyfile(FILE1, FILE2)

##=> 파일 복사 : 파일 복사 + 권한
##=>            copy(원본, 복사본)
shutil.copy(FILE1, FILE2)
compare_info(FILE1, FILE2)

##=> 파일 복사 : 파일 복사 + 권한 + 수정시간 등 메타데이터까지 포함
##=>            copy2(원본, 복사본)
shutil.copy2(FILE1, FILE3)
compare_info(FILE1,  FILE3)

## ---------------------------------------------------
## [2] 폴더 복사 / 이동 / 삭제
## ---------------------------------------------------
if not os.path.exists(DIR1):
    os.makedirs(DIR1, exist_ok=True)

##=> 폴더 전체 복사 : copytree(원본폴더, 복사폴더)
shutil.copytree(DIR1, DIR2)
print( os.path.exists(DIR2))

##=> 폴더 전체 삭제 : rmtree(원본폴더)
##=>                폴더와 그 안의 모든 파일 삭제
shutil.rmtree(DIR2)

##=> 파일 이동 : move(원본, 이동파일명)
##=>           같은 경로면 이름 변경
shutil.move(FILE2, FILE4)

## ---------------------------------------------------
## [2] 압축
## ---------------------------------------------------
print('\n[2] 압축 +++++++++++++++')

##=> 폴더 압축 : make_archive(압축폴더명, 압축형식, 원본폴더)
##=>           "zip", "tar", "gztar", "bztar", or "xztar"...
shutil.make_archive("myarchive", "zip", "myfolder")


##=> 폴더 압축 해제 : unpack_archive(압축폴더명, 해제폴더명)
shutil.unpack_archive("myarchive.zip", "extracted_dir")

## ---------------------------------------------------
## [3] 디스크 용량
## ---------------------------------------------------
print('\n[3] 디스크 용량 +++++++++++++++')

total, used, free = shutil.disk_usage(".")
print(f"총  용  량: {total / (1024**3):.2f} GB" )
print("사  용  중: %.2f GB" % (used / (1024**3)))
print("남은  용량: %.2f GB" % (free / (1024**3)))
