import psutil


def count_running_processes():
    return len(psutil.pids())


if __name__ == '__main__':
    print(count_running_processes())
