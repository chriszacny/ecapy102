import os

OUTPUT_FILE_NAME = 'output.txt'


def get_input_file_path():
    input_file_found = False
    input_file_path = None
    while not input_file_found:
        input_file_path = input("Please enter a valid path to a file to import: ")
        if not os.path.exists(input_file_path):
            print("I'm sorry, that is not a valid file path.")
        else:
            input_file_found = True
    return input_file_path


def main():
    print("Welcome to the data importer. I will import lines of data from a file and rewrite them to a new file in your current working directory called {}".format(OUTPUT_FILE_NAME))

    input_file_path = get_input_file_path()

    with open(input_file_path, 'r') as input_file_handle:
        with open(OUTPUT_FILE_NAME, 'w') as output_file_handle:
            for line in input_file_handle:
                output_file_handle.write(line)

    print("Write complete. Please verify {}".format(OUTPUT_FILE_NAME))


if __name__ == '__main__':
    main()