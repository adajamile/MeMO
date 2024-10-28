import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
from PyQt5 import QtWidgets, QtGui, QtCore

# Credenciais do Spotify
CLIENT_ID = '57202c8ae7024c3aac399499bfb026b1'
CLIENT_SECRET = '4c543f7bde714b68a681d03ebea209ad'
REDIRECT_URI = 'https://github.com/adajamile/MeMO.git'
scope = 'playlist-read-private user-modify-playback-state user-read-playback-state'

# Autenticação com OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope))

class SpotifyYouTubeApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Projeto MeMO')
        self.setGeometry(100, 100, 400, 200)

        layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel("Insira o link da playlist do Spotify:")
        layout.addWidget(self.label)

        self.playlist_input = QtWidgets.QLineEdit(self)
        layout.addWidget(self.playlist_input)

        self.play_button = QtWidgets.QPushButton("Reproduzir Playlist", self)
        self.play_button.clicked.connect(self.play_playlist)
        layout.addWidget(self.play_button)

        self.exit_button = QtWidgets.QPushButton("Sair", self)
        self.exit_button.clicked.connect(self.close)
        layout.addWidget(self.exit_button)

        self.setLayout(layout)

    def play_playlist(self):
        playlist_link = self.playlist_input.text()
        if playlist_link.lower() == 'sair':
            self.close()
        
        try:
            playlist_id = playlist_link.split("/")[-1].split("?")[0]
            playlist = sp.playlist(playlist_id)

            devices = sp.devices()
            if devices['devices']:
                active_device = devices['devices'][0]
                device_id = active_device['id']
                # especificar o volume
                sp.volume(30, device_id=device_id)

                sp.start_playback(context_uri=playlist['uri'], device_id=device_id)

                # abrir o youtube
                webbrowser.open("https://youtu.be/A2_YmvHxVmA?si=YUWvgC_PObf21zui")

                QtWidgets.QMessageBox.information(self, "Sucesso", f"Reproduzindo a playlist: {playlist['name']}")
            else:
                QtWidgets.QMessageBox.warning(self, "Erro", "Nenhum dispositivo ativo encontrado.")
        
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", str(e))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SpotifyYouTubeApp()
    window.show()
    sys.exit(app.exec_())
