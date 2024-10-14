import tkinter as tk
import webbrowser
from tkinter import messagebox

class AudioMixerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MeMO Prototype")
        self.root.geometry("400x200")

        # URL fixa do áudio do YouTube
        self.youtube_url = "https://youtu.be/A2_YmvHxVmA?si=zCLZCPg-NNowZ0cM"

        # exibir URL do YouTube
        self.youtube_label = tk.Label(root, text="YouTube Audio URL:")
        self.youtube_label.pack()
        self.youtube_entry = tk.Entry(root, width=50)
        self.youtube_entry.insert(0, self.youtube_url)  # Preencher com a URL fixa
        self.youtube_entry.pack()

        # entrada da URL da Playlist do Spotify
        self.spotify_label = tk.Label(root, text="Spotify Playlist URL:")
        self.spotify_label.pack()
        self.spotify_entry = tk.Entry(root, width=50)
        self.spotify_entry.insert(0, "https://open.spotify.com/playlist/5ipnXoByzxbTqD5o1o25zR?si=U6onMjxcQeCgTnB1BkmrTQ")
        self.spotify_entry.pack()

        # botão para tocar os áudios
        self.play_button = tk.Button(root, text="Play Both Audios", command=self.open_links)
        self.play_button.pack(pady=20)

    def open_links(self):
        youtube_url = self.youtube_entry.get()
        spotify_url = self.spotify_entry.get()

        if not youtube_url or not spotify_url:
            messagebox.showerror("Input Error", "Please enter both YouTube audio URL and Spotify Playlist URL.")
            return
        
        # abrir URLs do YouTube e Spotify no navegador padrão
        webbrowser.open_new_tab(youtube_url + "&volume=100")  # definir volume para 100%
        webbrowser.open_new_tab(spotify_url + "?volume=25")   # definir volume para 20%

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioMixerApp(root)
    root.mainloop()