This is a quick and dirty offline viewer developed by the Bibliotheca Anonoma to display threads from the World4ch databases developed by [ghonsonb3120](https://archive.org/details/@ghonsonb3120) to the Internet Archive.

This specific version uses Python 2.x with Flask and the built-in SQLite library to display the text from the database, This is only reliable enough for one person to use (SQLite does not scale to multiple users well), so for future development, we will use SQLAlchemy.

## Usage

### Download and Install the world4ch Thread Viewer

1. You will need to obtain a copy of the Thread Viewer. If you are reading this, you probably have it here.
2. Install Python 2.x. Then, install Flask.

### Installing the database

> **Note:** This thread viewer is tuned to the schema found in a specifically generated thread archiver. It will not work on Kusaba or other textboard systems (though we certainly will attempt to archive them that way).

1. Download the desired world4ch database from the [Internet Archive](https://archive.org/details/@ghonsonb3120).
2. Put it in the same folder as `run.py`, and rename it to `db.sqlite`.

For testing. the world4ch /sjis/ board has been included.

### Running the Thread Viewer

The thread viewer runs a little active server to allow you to read the threads. You just need to run the following command:

    python run.py

This will launch the server at `http://127.0.0.1:5000/`. Press Ctrl-C to stop the server.

### Thread Index Page

The homepage at the server will show you a large list of all the threads ever made on the board, without pagination (may take a few seconds to load). Just click on a title to view it.

You can search all thread titles using Ctrl-F. Another method is to sort the tables by a column, by double-clicking a column title.

The Threads themselves are set to use MSPGothic or Osaka font to display the Shift_JIS art the way it was intended. If you don't, we provide our own Monafont, so don't worry.