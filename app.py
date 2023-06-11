from flask import *
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_playlist', methods=['POST'])
def create_playlist():
    files = request.files.getlist('mp3_files')
    playlist_name = request.form['playlist_name']

    playlist_dir = os.path.join(app.root_path, 'playlists')
    os.makedirs(playlist_dir, exist_ok=True)

    playlist_path = os.path.join(playlist_dir, playlist_name + '.txt')
    with open(playlist_path, 'w') as playlist_file:
        for file in files:
            if file.filename.endswith('.mp3'):
                file.save(os.path.join(playlist_dir, file.filename))
                playlist_file.write(file.filename + '\n')

    playlist_name = request.form['playlist_name']
    playlist_path = url_for('playlist', playlist_name=playlist_name)

    return redirect(playlist_path)


@app.route('/playlist/<playlist_name>')
def playlist(playlist_name):
    playlist_dir = os.path.join(app.root_path, 'playlists')
    playlist_file = f"{playlist_name}.txt"
    playlist_path = os.path.join(playlist_dir, playlist_file)

    if not os.path.exists(playlist_path):
        return render_template('index.html')

    with open(playlist_path, 'r') as file:
        songs = file.read().splitlines()

    return render_template('playlists.html', playlist_name=playlist_name, songs=songs)


# @app.route('/view_playlists/<playlists>')
# def view_playlists(playlists):


if __name__ == '__main__':
    app.run()
