# Log URL Mapper and Reducer

This MapReduce job consists of two Python scripts: a mapper and a reducer. Together, they process log files to count occurrences of each URL in the logs.

## Mapper: Extract URLs from Logs
### Script: `mapper.py`
The mapper reads log entries line by line from `stdin` and uses a regular expression to extract the URL from each HTTP request. It outputs each URL followed by a count of `1`, tab-separated.

### Key Features:
- Captures HTTP method, URL, and protocol using a regular expression.
- Filters and outputs only the URL and its initial count (`1`).
- Prepares data for aggregation by the reducer.

---

## Reducer: Aggregate URL Counts
### Script: `reducer.py`
The reducer reads the mapper's output (key-value pairs of URLs and counts) from `stdin` and aggregates the counts for each unique URL. It outputs each URL followed by its total count, tab-separated.

### Key Features:
- Groups identical URLs and sums their counts.
- Handles sorted input from the mapper to ensure efficient aggregation.
- Outputs the final count for each unique URL.

---

## How to Run
1. Use the mapper and reducer together in a pipeline.
2. The mapper processes raw logs, and its output is sorted before being passed to the reducer.
