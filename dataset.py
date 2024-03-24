import csv


def createCsv(filename, data):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data[0].keys())  # Write header
        for row in data:
            writer.writerow(row.values())


if __name__ == "__main__":
    # Data to be written to the CSV file
    data = [
        {"Age": 25, "Gender": "Male", "Income": 35000, "Purchase": "No"},
        {"Age": 30, "Gender": "Female", "Income": 30000, "Purchase": "Yes"},
        {"Age": 35, "Gender": "Female", "Income": 32000, "Purchase": "Yes"},
        {"Age": 20, "Gender": "Male", "Income": 40000, "Purchase": "Yes"},
        {"Age": 40, "Gender": "Male", "Income": 45000, "Purchase": "Yes"},
        {"Age": 45, "Gender": "Female", "Income": 28000, "Purchase": "No"},
        {"Age": 55, "Gender": "Male", "Income": 55000, "Purchase": "Yes"},
        {"Age": 50, "Gender": "Female", "Income": 26000, "Purchase": "No"},
        {"Age": 22, "Gender": "Male", "Income": 42000, "Purchase": "Yes"},
        {"Age": 38, "Gender": "Female", "Income": 58000, "Purchase": "Yes"},
    ]

    # Call the function to create the CSV file
    createCsv("./data/data.csv", data)
