# ============================================================
# SPOTIFY TRACKS DATASET - COMPLETE DATA ANALYSIS
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt


# 1. LOAD DATASET

df = pd.read_csv(
   r"C:\Users\dilip\OneDrive\文件\ML PROJECT DATASETS\Spotify Tracks Dataset\dataset.csv"
)

print("==============================================")
print("       SPOTIFY TRACKS DATASET")
print("==============================================")


# 2. DISPLAY COMPLETE DATASET

print("\n1. COMPLETE DATASET:")
print(df.to_string())


# 3. DISPLAY FIRST 10 RECORDS

print("\n\n2. FIRST 10 RECORDS:")
print(df.head(10))


# 4. DISPLAY LAST 10 RECORDS

print("\n\n3. LAST 10 RECORDS:")
print(df.tail(10))


# 5. DISPLAY NUMBER OF ROWS AND COLUMNS

print("\n\n4. DATASET SHAPE:")
print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])


# 6. DISPLAY COLUMN NAMES

print("\n\n5. COLUMN NAMES:")

for i, column in enumerate(df.columns, start=1):
    print(i, ".", column)


# 7. DISPLAY DATA TYPES

print("\n\n6. DATA TYPES:")
print(df.dtypes)


# 8. DATASET INFORMATION

print("\n\n7. DATASET INFORMATION:")
df.info()


# 9. CHECK MISSING VALUES

print("\n\n8. MISSING VALUES:")

print(df.isnull().sum())


# 10. TOTAL MISSING VALUES

print("\n\n9. TOTAL MISSING VALUES:")

print(df.isnull().sum().sum())


# 11. CHECK DUPLICATE VALUES

print("\n\n10. DUPLICATE ROWS:")

print(df.duplicated().sum())


# 12. REMOVE DUPLICATES

df = df.drop_duplicates()

print("\nDataset after removing duplicates:")
print(df.shape)


# 13. STATISTICAL INFORMATION

print("\n\n11. STATISTICAL INFORMATION:")

print(df.describe())


# 14. UNIQUE VALUES IN EACH COLUMN

print("\n\n12. UNIQUE VALUES:")

for column in df.columns:
    print(
        column,
        "=", 
        df[column].nunique()
    )


# 15. POPULARITY INFORMATION

print("\n\n13. POPULARITY INFORMATION:")

print("Minimum Popularity:",
      df["popularity"].min())

print("Maximum Popularity:",
      df["popularity"].max())

print("Average Popularity:",
      df["popularity"].mean())


# 16. MOST POPULAR SONGS

print("\n\n14. TOP 10 MOST POPULAR SONGS:")

top_songs = df.sort_values(
    by="popularity",
    ascending=False
)

print(
    top_songs[
        ["track_name", "artists", "popularity"]
    ].head(10)
)


# 17. LEAST POPULAR SONGS

print("\n\n15. TOP 10 LEAST POPULAR SONGS:")

least_songs = df.sort_values(
    by="popularity",
    ascending=True
)

print(
    least_songs[
        ["track_name", "artists", "popularity"]
    ].head(10)
)


# 18. MOST COMMON ARTISTS

print("\n\n16. TOP 10 ARTISTS:")

print(
    df["artists"]
    .value_counts()
    .head(10)
)


# 19. MOST COMMON GENRES

print("\n\n17. TOP 20 TRACK GENRES:")

print(
    df["track_genre"]
    .value_counts()
    .head(20)
)


# 20. EXPLICIT SONG COUNT

print("\n\n18. EXPLICIT SONGS:")

print(
    df["explicit"].value_counts()
)


# 21. AVERAGE AUDIO FEATURES

print("\n\n19. AVERAGE AUDIO FEATURES:")

audio_features = [
    "danceability",
    "energy",
    "loudness",
    "speechiness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "valence",
    "tempo"
]

print(
    df[audio_features].mean()
)


# 22. MOST DANCEABLE SONGS

print("\n\n20. TOP 10 MOST DANCEABLE SONGS:")

dance = df.sort_values(
    by="danceability",
    ascending=False
)

print(
    dance[
        ["track_name", "artists", "danceability"]
    ].head(10)
)


# 23. HIGHEST ENERGY SONGS

print("\n\n21. TOP 10 HIGHEST ENERGY SONGS:")

energy = df.sort_values(
    by="energy",
    ascending=False
)

print(
    energy[
        ["track_name", "artists", "energy"]
    ].head(10)
)


# 24. MOST POSITIVE / HAPPY SONGS

print("\n\n22. TOP 10 SONGS BY VALENCE:")

valence = df.sort_values(
    by="valence",
    ascending=False
)

print(
    valence[
        ["track_name", "artists", "valence"]
    ].head(10)
)


# ============================================================
# GRAPHS
# ============================================================


# 25. POPULARITY DISTRIBUTION

plt.figure(figsize=(8, 5))

plt.hist(
    df["popularity"],
    bins=20
)

plt.title("Spotify Song Popularity Distribution")

plt.xlabel("Popularity")

plt.ylabel("Number of Songs")

plt.show()


# 26. TOP 10 GENRES

genre_count = (
    df["track_genre"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10, 5))

genre_count.plot(
    kind="bar"
)

plt.title("Top 10 Spotify Genres")

plt.xlabel("Genre")

plt.ylabel("Number of Tracks")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# 27. AUDIO FEATURES

df[audio_features].mean().plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Average Spotify Audio Features")

plt.xlabel("Audio Features")

plt.ylabel("Average Value")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# 28. POPULARITY VS DANCEABILITY

plt.figure(figsize=(8, 5))

plt.scatter(
    df["danceability"],
    df["popularity"],
    alpha=0.3
)

plt.title("Popularity vs Danceability")

plt.xlabel("Danceability")

plt.ylabel("Popularity")

plt.show()


# 29. POPULARITY VS ENERGY

plt.figure(figsize=(8, 5))

plt.scatter(
    df["energy"],
    df["popularity"],
    alpha=0.3
)

plt.title("Popularity vs Energy")

plt.xlabel("Energy")

plt.ylabel("Popularity")

plt.show()


# 30. POPULARITY VS VALENCE

plt.figure(figsize=(8, 5))

plt.scatter(
    df["valence"],
    df["popularity"],
    alpha=0.3
)

plt.title("Popularity vs Valence")

plt.xlabel("Valence")

plt.ylabel("Popularity")

plt.show()


# ============================================================
# FINAL OUTPUT
# ============================================================

print("\n==============================================")
print("       DATA ANALYSIS COMPLETED")
print("==============================================")

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nAnalysis completed successfully!")