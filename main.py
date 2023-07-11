from utils import operations


def main():
    data = operations.read_json()
    data = operations.filter_data(data)
    data = operations.sort_data(data)


if __name__ == '__main__':
    main()
