# Сигнал остановки SIGINT отправляется в *nix системах командой kill -2 PID_процесса
import signal


def register_signals():
    def loop_breaker(*args, **kwargs):
        global STOP
        STOP = True

    signal.signal(signal.SIGTERM, loop_breaker)


# Only signal.SIGINT should be ignored in main process
signal.signal(signal.SIGINT, signal.SIG_IGN)
STOP = False
register_signals()


while not STOP:
    print("a")