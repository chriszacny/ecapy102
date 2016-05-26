from openpyxl import load_workbook
import csv


INPUT_XLSX_FILE = 'RtrCsatToSf.xlsx'
OUTPUT_CSV_FILE = 'ouput_data.csv'


def main():
    print("Loading data from {}...".format(INPUT_XLSX_FILE))
    workbook = load_workbook(INPUT_XLSX_FILE)
    print('Main worksheet is: {}'.format(workbook.get_sheet_names()[0]))
    main_worksheet = workbook[workbook.get_sheet_names()[0]]

    with open(OUTPUT_CSV_FILE, 'w') as write_handle:
        csv_writer = csv.writer(write_handle, quoting=csv.QUOTE_ALL)
        for row in main_worksheet.rows:
            to_write = []
            for cell in row:
                if cell.value is not None:
                    to_write.append(cell.value)
                else:
                    to_write.append('')
            csv_writer.writerow(to_write)

    print('Data written to: {}'.format(OUTPUT_CSV_FILE))

if __name__ == '__main__':
    main()