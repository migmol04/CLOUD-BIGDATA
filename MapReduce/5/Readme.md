# Meteorite Class Mass Analysis: Mapper and Reducer

This MapReduce pipeline analyzes meteorite data to calculate the average mass and total count for each meteorite classification.

---

## Step 1: Extract Classification and Mass
### Mapper: `mapper.py`

The mapper reads a CSV file with meteorite data and emits the meteorite class (`recclass`), its mass, and a count of `1`, tab-separated.

### Key Features:
- **Input**: CSV data with `;` as the delimiter.
- **Processing**:
  - Skips the header row (if present).
  - Extracts the `recclass` (classification) from the fourth column and the `mass` from the fifth column.
  - Emits the meteorite class, its mass, and a count of `1`.
- **Output**: `recclass`, `mass`, and `1`.

---

## Step 2: Calculate Average Mass
### Reducer: `reducer.py`

The reducer aggregates the mass and count for each meteorite class and calculates the average mass.

### Key Features:
- **Input**: Tab-separated output from the mapper: `recclass`, `mass`, and `count`.
- **Processing**:
  - Groups data by `recclass`.
  - Accumulates the total mass and count for each class.
  - Calculates the average mass for each meteorite class.
  - Outputs the `recclass`, average mass (formatted to two decimal places), and total count.
- **Output**: `recclass`, `average_mass`, and `count`.

---

## How to Run
1. Ensure the input data is a CSV file with the following structure:
   - Column 4: `recclass` (classification)
   - Column 5: `mass` (in numeric format)
2. Use the mapper and reducer in a pipeline.
