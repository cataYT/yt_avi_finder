import webbrowser
import csv

def main() -> None:
    # Read the file and open each URL, skipping the header
    with open("results.csv", "r", encoding="utf-8") as f:
        csvFile = csv.reader(f)
        next(csvFile, None)  # Skip the header row
        
        for lines in csvFile:
            # Make sure the row has a URL in the second column
            if len(lines) > 1 and lines[1].strip():
                url: str = lines[1].strip()
                webbrowser.open(url)

    # Clear the file after processing
    with open("results.csv", "w", encoding="utf-8") as f:
        f.write("")

if __name__ == "__main__":
    main()