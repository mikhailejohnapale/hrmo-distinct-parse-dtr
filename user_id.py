import sys

def main():
    userid = sys.argv[2]
    log_file = open(sys.argv[1])

    for log in log_file:
        lst = log.split(',')
        user_id = lst[4].replace('\n', '')

        if user_id == userid:
            print(log, end='')

if __name__ == '__main__':
  main()
