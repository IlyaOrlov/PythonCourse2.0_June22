import sys


def my_program(*args):
    print(f'Program started with arguments: {args}')


if __name__ == '__main__':
    print('This is main program')
    my_program(*sys.argv)
