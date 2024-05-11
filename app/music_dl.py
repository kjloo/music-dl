import csv

def extract_first_column(input_file, output_file):
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        first_column = [row['Song'] for row in reader]
    
    with open(output_file, 'w', newline='') as output:
        for value in first_column:
            output.write(value + '\n')

if __name__ == "__main__":
    input_file = 'input/source.csv'  # Update with the name of your CSV file
    output_file = 'output/output.txt'  # Output file name

    extract_first_column(input_file, output_file)
