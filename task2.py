from time import time


def read_file_timed(file):
    start_time = time()
    try:
        ff = open(file, mode='rb')
    except FileNotFoundError:
        raise FileNotFoundError
    else:
        return ff
    finally:
        print(f'Time required for {file} = {time() - start_time}')
        ff.close()