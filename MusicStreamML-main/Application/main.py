from flask import Flask, render_template
from pyspark.sql import SparkSession
from annoy import AnnoyIndex
import os

app = Flask(__name__)

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Nearest Neighbor Search") \
    .getOrCreate()

VECTOR_DIMENSION = 10000
annoy_index = AnnoyIndex(VECTOR_DIMENSION)

# Define nearest neighbor search function
def nearest_neighbor_search(annoy_index, query_feature_vector, spark_df, k=5):
    nearest_indices = annoy_index.get_nns_by_vector(query_feature_vector, k)
    nearest_labels = [spark_df.select('Label').collect()[i][0] for i in nearest_indices]
    return nearest_indices, nearest_labels

# Read the Parquet file into a PySpark DataFrame
df = spark.read.parquet("dataFrame")

# Read the annoy index file
annoy_index.load("music.ann")

@app.route('/')
def index():
    # List all the audio files in the songs folder
    songs = os.listdir("static/songs")
    return render_template('index.html', songs=songs)
import os

@app.route('/play/<song>')
def play(song):
    song_label = os.path.splitext(song)[0]  # Extract song label without file extension
    print("Song Label:", song_label)  # Debugging statement
    row = df.filter(df['Label'] == song_label).select('feature').first()
    if row:
        label_vector = row[0]
        nearest_indices, nearest_labels = nearest_neighbor_search(annoy_index, label_vector, df)
        recommended_songs = [df.filter(df['Label'] == label).select('Label').first()[0] for label in nearest_labels]
        return render_template('player.html', song=song, recommended_songs=recommended_songs)
    else:
        return "Song not found in the dataset. Please make sure the song label is correct."
@app.route('/play/recommendation/<song>')
def play_recommendation(song):
    # Check if the song label includes ".mp3", and remove it if present
    if song.endswith(".mp3"):
        song = song[:-4]  # Remove the last 4 characters (".mp3")

    row = df.filter(df['Label'] == song).select('feature').first()
    if row:
        label_vector = row[0]
        nearest_indices, nearest_labels = nearest_neighbor_search(annoy_index, label_vector, df)
        recommended_songs = [label + ".mp3" for label in nearest_labels]  # Append ".mp3" to recommended song labels
        return render_template('player.html', song=song + ".mp3", recommended_songs=recommended_songs)  # Append ".mp3" to the main song label
    else:
        return "Song not found in the dataset."

if __name__ == '__main__':
    app.run(debug=True)

