import csv

INPUT_CSV_FILE = '/Users/czacny/Development/other_repos/ecapy102/input_output/csv_example/RtrCsatToSf.csv'
OUTPUT_CSV_FILE = '/Users/czacny/Development/other_repos/ecapy102/input_output/csv_example/ouput_data.csv'
TEXT_TO_SEARCH_FOR = 'sad'
INPUT_HAPPY_SAD_FIELD = 'res_q1_as_text'
INPUT_HAPPY_SAD_REASON_FIELD = 'res_q1_as_tags_tagStr'
INPUT_HOTEL_ID='data_hotelId'
OUPUT_HOTEL_ID_FIELD = 'hotel_id'
OUPUT_COMPLAINT_FIELD = 'complaint'


def main():
    print("Loading data from {}...".format(INPUT_CSV_FILE))
    with open(INPUT_CSV_FILE, 'r') as input_csvfile:
        output_field_names = [OUPUT_HOTEL_ID_FIELD, OUPUT_COMPLAINT_FIELD]
        with open(OUTPUT_CSV_FILE, 'w') as output_csvfile:
            reader = csv.DictReader(input_csvfile)
            writer = csv.DictWriter(output_csvfile, output_field_names)
            writer.writeheader()
            for row in reader:
                if row[INPUT_HAPPY_SAD_FIELD].casefold() == TEXT_TO_SEARCH_FOR.casefold():
                    writer.writerow({OUPUT_HOTEL_ID_FIELD: row[INPUT_HOTEL_ID], OUPUT_COMPLAINT_FIELD: row[INPUT_HAPPY_SAD_REASON_FIELD]})
    print("Done ETL-ing data.")


if __name__ == '__main__':
    main()