# class MyCtxManager:
#     def __enter__(self):
#         print('Hello!')  # Star sort
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Bye!')  # Finish
#
#
# lst = [4, 2, 6]
# with MyCtxManager():
#     lst.sort()
#     print(lst)

class MyCtxManager:
    def __enter__(self):
        print('Start')  # Star sort

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Finish')  # Finish


lst = [4, 2, 6]
with MyCtxManager():
    lst.sort()
    print(lst)


