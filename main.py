from utils import operations


def main():
    data = operations.read_json()
    data = operations.filter_data(data)
    data = operations.sort_data(data)

    for row in range(5):
        print(operations.right_format(data[row]))

if __name__ == '__main__':
    main()
