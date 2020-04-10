This is a quick and dirty offline viewer developed by the Bibliotheca Anonoma to display threads from the World4ch databases developed by [ghonsonb3120](https://archive.org/details/@ghonsonb3120) to the Internet Archive.

This specific version uses Python with Flask and the built-in SQLite library to display the text from the database. SQLite is decent enough to run a small archive, but for greater database support, we will use SQLAlchemy.

## Shift JIS Submona Web Font

Note that to properly support Shift JIS art as seen on the /sjis/ board, the following public domain web font is embedded and used for all text:

https://github.com/pera/submona-web-font

![image](https://user-images.githubusercontent.com/614893/79016570-65d68300-7b3d-11ea-8ba7-5159ec4175c3.png)

![image](https://user-images.githubusercontent.com/614893/79016189-59055f80-7b3c-11ea-98a5-fdd9a29c77c4.png)

## Usage

### Download and Install the world4ch Thread Viewer

1. You will need to obtain a copy of the Thread Viewer. If you are reading this, you probably have it here.
2. Install Python. Then, install Flask.
3. Install the dependencies with pip:
    * `pip install -r requirements.txt`

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
