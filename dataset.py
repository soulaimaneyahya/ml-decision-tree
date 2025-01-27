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
        {"Age": 20, "Gender": "Male", "Income": 40000, "Purchase": "No"},
        {"Age": 22, "Gender": "Male", "Income": 42000, "Purchase": "No"},
        {"Age": 25, "Gender": "Male", "Income": 90000, "Purchase": "Yes"},
        {"Age": 30, "Gender": "Male", "Income": 55000, "Purchase": "Yes"},
        {"Age": 40, "Gender": "Male", "Income": 60000, "Purchase": "Yes"},
        {"Age": 55, "Gender": "Male", "Income": 70000, "Purchase": "Yes"},
        {"Age": 60, "Gender": "Male", "Income": 75000, "Purchase": "Yes"},
        {"Age": 28, "Gender": "Male", "Income": 50000, "Purchase": "Yes"},
        {"Age": 35, "Gender": "Male", "Income": 57000, "Purchase": "Yes"},
        {"Age": 24, "Gender": "Male", "Income": 46000, "Purchase": "No"},
        {"Age": 27, "Gender": "Male", "Income": 49000, "Purchase": "No"},
        {"Age": 32, "Gender": "Male", "Income": 60000, "Purchase": "No"},
        {"Age": 40, "Gender": "Male", "Income": 65000, "Purchase": "Yes"},
        {"Age": 45, "Gender": "Male", "Income": 70000, "Purchase": "Yes"},
        {"Age": 52, "Gender": "Male", "Income": 75000, "Purchase": "Yes"},
        {"Age": 30, "Gender": "Female", "Income": 45000, "Purchase": "No"},
        {"Age": 32, "Gender": "Female", "Income": 48000, "Purchase": "No"},
        {"Age": 35, "Gender": "Female", "Income": 47000, "Purchase": "No"},
        {"Age": 38, "Gender": "Female", "Income": 60000, "Purchase": "Yes"},
        {"Age": 40, "Gender": "Female", "Income": 55000, "Purchase": "Yes"},
        {"Age": 45, "Gender": "Female", "Income": 50000, "Purchase": "Yes"},
        {"Age": 50, "Gender": "Female", "Income": 48000, "Purchase": "No"},
        {"Age": 60, "Gender": "Female", "Income": 65000, "Purchase": "Yes"},
        {"Age": 65, "Gender": "Female", "Income": 60000, "Purchase": "Yes"},
        {"Age": 33, "Gender": "Female", "Income": 49000, "Purchase": "No"},
        {"Age": 29, "Gender": "Female", "Income": 52000, "Purchase": "Yes"},
        {"Age": 34, "Gender": "Female", "Income": 54000, "Purchase": "Yes"},
        {"Age": 42, "Gender": "Female", "Income": 56000, "Purchase": "No"},
        {"Age": 47, "Gender": "Female", "Income": 58000, "Purchase": "No"},
        {"Age": 56, "Gender": "Female", "Income": 63000, "Purchase": "Yes"},
        {"Age": 62, "Gender": "Female", "Income": 65000, "Purchase": "Yes"},
    ]

    # Call the function to create the CSV file
    createCsv("./data/data.csv", data)
