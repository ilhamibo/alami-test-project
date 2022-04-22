import csv
import datetime


FILE_NAME_READ = "Before Eod.csv"
FILE_NAME_WRITE = "After Eod.csv"
FIELDS_NAME = [
        'id',
        'Nama',
        'Age',
        'Balanced',
        'No 2b Thread-No',
        'No 3 Thread-No',
        'Previous Balanced',
        'Average Balanced',
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
    print(f"Start Read Data from {FILE_NAME_READ} at {datetime.datetime.now()}")
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
                    FIELDS_NAME[8]: 5 + free_transfer if 100 <= balance <= 150 else free_transfer,
                    FIELDS_NAME[9]: '',
                }
            )

        assign_additional_balance_top_100(users)

    print(f"Finish Read Data from {FILE_NAME_READ} at {datetime.datetime.now()}")
    return users


def write_data_to_csv(filename, users):
    print(f"Start Write Data to {FILE_NAME_WRITE} at {datetime.datetime.now()}")
    with open(filename, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDS_NAME)
        writer.writeheader()
        writer.writerows(users)
    print(f"Finish Write Data to {FILE_NAME_WRITE} at {datetime.datetime.now()}")


if __name__ == '__main__':
    users = get_data_from_csv(FILE_NAME_READ)
    write_data_to_csv(FILE_NAME_WRITE, users)
