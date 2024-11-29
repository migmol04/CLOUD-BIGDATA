# Movie Ratings Analysis: Mapper and Reducer

This MapReduce pipeline analyzes movie ratings to calculate average ratings, group movies by average rating ranges, and list movies within each range.

---

## Step 1: Extract Ratings and Counts
### Mapper: `mapper.py`
The first mapper reads a CSV file containing user ratings and emits the movie ID, rating, and a count of `1`, tab-separated.

### Key Features:
- **Input**: CSV lines with the format `[userId, movieId, rating, ...]`.
- **Processing**:
  - Skips the header row and empty lines.
  - Reads the `movieId` and `rating` columns.
  - Emits the movie ID, rating, and a count of `1` for aggregation.
- **Output**: `movie_id`, `rating`, and `1`.

---

## Step 2: Calculate Average Ratings
### Reducer: `reducer.py`
The first reducer aggregates ratings for each movie and calculates the average rating and total count of ratings.

### Key Features:
- **Input**: `movie_id`, `rating`, and `count` from the mapper.
- **Processing**:
  - Groups by `movie_id`.
  - Computes the sum of ratings and the count of ratings for each movie.
  - Outputs the `movie_id`, average rating, and total count.
- **Output**: `movie_id`, `average_rating`, and `count`.

---

## Step 3: Categorize Movies by Rating Range
### Mapper: `range_mapper.py`
The second mapper reads the output of the first reducer, assigns each movie to a rating range, and emits the range ID, movie ID, and average rating.

### Key Features:
- **Input**: `movie_id`, `average_rating`, and `count` from the first reducer.
- **Processing**:
  - Assigns movies to predefined rating ranges:
    - `Range 1: [0, 1]`
    - `Range 2: (1, 2]`
    - `Range 3: (2, 3]`
    - `Range 4: (3, 4]`
    - `Range 5: (4, 5]`
  - Emits the range ID, `movie_id`, and `average_rating`.
- **Output**: `range_id`, `movie_id`, and `average_rating`.

---

## Step 4: Group Movies by Range
### Reducer: `range_reducer.py`
The second reducer groups movies by rating range and lists their IDs and average ratings.

### Key Features:
- **Input**: `range_id`, `movie_id`, and `average_rating` from the second mapper.
- **Processing**:
  - Groups movies by `range_id`.
  - Aggregates movies in each range with their average ratings.
- **Output**: `range_id` and a semicolon-separated list of movies with their average ratings.

---
