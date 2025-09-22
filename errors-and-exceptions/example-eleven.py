# def f():
#     excs = [OSError('error 1'), SystemError('error 2')]
#     raise ExceptionGroup('there were problems', excs)

# f()

def f():
    raise ExceptionGroup(
        'group1',
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                'group2',
                [
                    OSError(3),
                    RecursionError(4)
                ]
            )
        ]
    )

try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")