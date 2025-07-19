import argparse

# Setup command-line arguments
parser = argparse.ArgumentParser(description="Simple Log Parser")

parser.add_argument("-i", "--input", required=True, help="Input log file name")
parser.add_argument("-o", "--output", required=True, help="Output file name for filtered logs")
parser.add_argument("-k", "--keywords", nargs="+", required=True, help="List of keywords to search for")

args = parser.parse_args()

# Open input and output files
with open(args.input, "r") as infile, open(args.output, "w") as outfile:
    for line in infile:
        if any(keyword in line for keyword in args.keywords):
            print(line.strip())
            outfile.write(line)

