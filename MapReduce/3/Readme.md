# Yearly Average Closing Price Mapper and Reducer

This MapReduce job calculates the yearly average of closing prices from financial data. It consists of a mapper and a reducer script that work together to process CSV data.

## Mapper: Extract Year and Closing Price
### Script: `mapper.py`
The mapper reads financial data from `stdin` in CSV format and extracts the year and closing price. It outputs the year, the closing price, and a count (`1`), tab-separated.

### Key Features:
- **Data Parsing**: Reads rows from a CSV file and handles potential formatting issues.
- **Date Formatting**: Converts the date from the first column into a `datetime` object to extract the year.
- **Output**: Emits the year, closing price, and a count of `1` for aggregation by the reducer.

---

## Reducer: Calculate Yearly Average
### Script: `reducer.py`
The reducer reads the mapper's output (year, closing price, and count) from `stdin` and calculates the average closing price for each year. It outputs the year, average closing price, and total count of records, tab-separated.

### Key Features:
- **Aggregation**: Groups data by year and calculates the total sum and count for each year.
- **Average Calculation**: Divides the total sum of closing prices by the total count of records to compute the average.
- **Error Handling**: Handles potential issues with invalid numerical values.

---
