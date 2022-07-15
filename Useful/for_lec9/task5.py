def fun(x, y):
    def fun1(x, y):
        res = 0

        def fun2(x, y):
            return x / y
        try:
            res = fun2(x, y)
        except ZeroDivisionError:
            print('ZeroDivisionError')
        except TypeError:
            print('TypeError')
        except Exception:
            print('Exception')
        else:
            print('Not Exception')
        finally:
            print('Any case')
        return res

    return fun1(x, y)


print(fun(20, '10'))
print('-----')
