import asyncio

import csv
import datetime

FILE_NAME_READ = "Before Eod.csv"
FILE_NAME_WRITE_THREAD1 = "After Eod_1.csv"
FILE_NAME_WRITE_THREAD2 = "After Eod_2.csv"
FILE_NAME_WRITE_THREAD3 = "After Eod_3.csv"
FILE_NAME_WRITE_THREAD4 = "After Eod_4.csv"
FIELDS_NAME = [
        'id',
        'Nama',
        'Age',
        'Balanced',
        'No 2b Thread-No',
        'No 3 Thread-No',
        'Previous Balanced',
        'Average Balanced',
        'No 1 Thread-No',
        'Free Transfer',
        'No 2a Thread-No',
    ]


def calculate_average_balance(current_balance, previous_balance):
    return (current_balance + previous_balance) / 2


def assign_additional_balance_top_100(users):
    for user in users[:100]:
        current_balance = user[FIELDS_NAME[3]]
        user[FIELDS_NAME[3]] = current_balance + 10


def get_data_from_csv(filename):
    print(f"Start Read Data from `{FILE_NAME_READ}` at {datetime.datetime.now()}")
    users = []
    with open(filename, 'r') as csv_file:
        data_from_csv = csv.DictReader(csv_file)
        for row in data_from_csv:
            balance = int(row['Balanced'])
            prev_balance = int(row['Previous Balanced'])
            free_transfer = int(row['Free Transfer'])
            users.append(
                {
                    FIELDS_NAME[0]: row[FIELDS_NAME[0]],
                    FIELDS_NAME[1]: row[FIELDS_NAME[1]],
                    FIELDS_NAME[2]: row[FIELDS_NAME[2]],
                    FIELDS_NAME[3]: 25 + balance if balance > 150 else balance,
                    FIELDS_NAME[4]: '',
                    FIELDS_NAME[5]: '',
                    FIELDS_NAME[6]: prev_balance,
                    FIELDS_NAME[7]: calculate_average_balance(
                        balance, prev_balance),
                    FIELDS_NAME[8]: '',
                    FIELDS_NAME[9]: 5 + free_transfer if 100 <= balance <= 150 else free_transfer,
                    FIELDS_NAME[10]: '',
                }
            )
        assign_additional_balance_top_100(users)
    print(f"Finish Read Data from `{FILE_NAME_READ}` at {datetime.datetime.now()}")
    return users


async def write_data_to_csv(filename, users, thread_number):
    print(f"Start write file `{filename}` at {datetime.datetime.now()}")
    for user in users:
        user[FIELDS_NAME[8]] = thread_number
        user[FIELDS_NAME[4]] = thread_number
        user[FIELDS_NAME[10]] = thread_number
    await asyncio.sleep(0.005)

    with open(filename, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDS_NAME)
        writer.writeheader()
        writer.writerows(users)
    print(f"Finish write file `{filename}` at {datetime.datetime.now()}")


async def main():
    users = get_data_from_csv(FILE_NAME_READ)
    thread1 = loop.create_task(write_data_to_csv(FILE_NAME_WRITE_THREAD1, users[:50], 1))
    thread2 = loop.create_task(write_data_to_csv(FILE_NAME_WRITE_THREAD2, users[50:100], 2))
    thread3 = loop.create_task(write_data_to_csv(FILE_NAME_WRITE_THREAD3, users[100:150], 3))
    thread4 = loop.create_task(write_data_to_csv(FILE_NAME_WRITE_THREAD4, users[150:200], 4))
    await asyncio.wait([thread1, thread2, thread3, thread4])


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
