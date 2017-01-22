# try:
#     print(1/0)
# except:
#     print("예외가 발생했습니다.")

my_list = [1, 2, 3]

# try:
#     print("첨자를 입력하세요:")
#     index = int(input())
#     print(my_list[index] / 0)   # index 오류, 0나누기 오류
# except ZeroDivisionError as err:
#     print("0으로 나눌 수 없습니다. ({0})".format(err))
# except IndexError as err:
#     print("잘못된 첨자입니다. ({0})".format(err))

try:
    print("첨자를 입력하세요:")
    index = int(input())
    print("my_list[{0}]: {1}".format(index, my_list[index]))
except Exception as err:
    print("예외가 발생했습니다. ({0})".format(err))
else:
    print("리스트의 요소 출력에 성공했습니다.")
finally:
    print("어떤 일이 있어도 마무리합니다.")