import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
from PyQt5 import QtWidgets, QtGui, QtCore

# credenciais spotify for dev
CLIENT_ID = '57202c8ae7024c3aac399499bfb026b1'
CLIENT_SECRET = '4c543f7bde714b68a681d03ebea209ad'
REDIRECT_URI = 'https://github.com/adajamile/MeMO.git'
scope = 'playlist-read-private user-modify-playback-state user-read-playback-state'

# autenticação do oauth
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

        # cor de fundo e a imagem
        self.setStyleSheet("background-color: #7c44bd;")
        self.setWindowIcon(QtGui.QIcon(r'C:\Users\adaja\Desktop\project memo\memo logo.png'))  # Ícone do aplicativo, coloque a imagem no diretório do script

        layout = QtWidgets.QVBoxLayout()

        # estilo da fonte do título
        font = QtGui.QFont("Roboto", 20, QtGui.QFont.Bold)

        self.label = QtWidgets.QLabel("Insira o link da playlist do Spotify:")
        self.label.setFont(font)
        self.label.setStyleSheet("color: #ffffff;")  # cor do texto
        layout.addWidget(self.label)

        # campo de entrada de texto
        self.playlist_input = QtWidgets.QLineEdit(self)
        self.playlist_input.setStyleSheet("background-color: #e2d3eb; color: white; padding: 5px; border-radius: 5px;")
        layout.addWidget(self.playlist_input)

        # botão de reprodução com fonte personalizada
        self.play_button = QtWidgets.QPushButton("Reproduzir Playlist", self)
        play_button_font = QtGui.QFont("Arial", 14, QtGui.QFont.Bold)  # fonte e tamanho da fonte do botão
        self.play_button.setFont(play_button_font)
        self.play_button.setStyleSheet("background-color: #cca6e0; color: white; padding: 8px; border-radius: 5px;")
        self.play_button.clicked.connect(self.play_playlist)
        layout.addWidget(self.play_button)

        # botão de sair com fonte personalizada
        self.exit_button = QtWidgets.QPushButton("Sair", self)
        exit_button_font = QtGui.QFont("Arial", 14, QtGui.QFont.Bold)  # fonte e tamanho da fonte do botão
        self.exit_button.setFont(exit_button_font)
        self.exit_button.setStyleSheet("background-color: #77afd1; color: white; padding: 8px; border-radius: 5px;")
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
