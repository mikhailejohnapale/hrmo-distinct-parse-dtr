import sys

def main():

    uniques = []
    dirty = []

    log_file = open(sys.argv[1])

    for log in log_file:
        fields = log.split(',')

        num = fields[0]
        date_time = fields[1]
        user_id = fields[2]
        username = fields[3]
        position = fields[4]
        terminal_id = fields[5]
        terminal_name = fields[6]
        auth_type = fields[7]
        auth_result = fields[8]
        function_key_no = fields[9]

        date_time = date_time.split(' ')
        date = date_time[0]
        time = date_time[1]
        merediem = date_time[2]

        date = date.split('/')

        year = date[2]
        month = date[1]
        day = date[0]

        date = month + "/" + day + "/" + year

        record = []

        record.append(num)
        record.append(date)
        record.append(time)
        record.append(merediem)
        record.append(user_id)
        record.append(username)
        record.append(position)
        record.append(terminal_id)
        record.append(terminal_name)
        record.append(auth_type)
        record.append(auth_result)
        record.append(function_key_no)

        dirty.append(record)

        if not uniques:
            uniques.append(record)
            # print(num + "," + date + " " + time + " " + merediem + "," + user_id + "," + username + "," + position + "," + terminal_id + "," + terminal_name + "," + auth_type + "," + auth_result + "," + function_key_no, end='')
            print('{0:7} {1:13} {2:8} {3:5} {4}'.format(
                num, date, time, merediem, user_id))
            print(num, end='')
        else:
            for unique in uniques:
                found = 1
                # date
                if unique[1] == record[1]:
                    # time
                    if unique[2] == record[2]:
                        # merediem
                            if unique[3] == record[3]:
                                # user id
                                if unique[4] == record[4]:
                                    found = 0

            if found == 1:
                uniques.append(record)
                # print record
                # print(num + "," + date + " " + time + " " + merediem + "," + user_id + "," + username + "," + position + "," + terminal_id + "," + terminal_name + "," + auth_type + "," + auth_result + "," + function_key_no, end='')
                print('{0:7} {1:13} {2:8} {3:5} {4}'.format(
                    num, date, time, merediem, user_id))

    # total clean
    print('Dirty : ', len(dirty))
    print('Clean : ', len(uniques))

    user_id = input('User id : ')
    clean = 0
    for e in uniques:
        if e[4] == user_id:
            num = e[0]
            date = e[1]
            time = e[2]
            merediem = e[3]
            # print('{0:7} {1:13} {2:8} {3:5}'.format(
                # num, date, time, merediem))
            clean += 1
            print(num)

    print('Count : ', clean)

    user_dirty = []
    # dirty user
    for r in dirty:
        if r[4] == user_id:
            user_dirty.append(r)

    print('Dirty user id : ', len(user_dirty))

if __name__ == '__main__':
  main()
