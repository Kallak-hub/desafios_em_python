import yt_dlp

def baixar_video(url):
    opcoes = {
        'format': 'bestvideo+bestaudio/best',  #melhor qualidade de vídeo e audio.
        'merge_output_format': 'mp4', #baixar o vídeo em mp4.
        'outtmpl': '%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        print("Baixando vídeo com áudio compatível...")
        ydl.download([url])
        print("Download concluído!")


url = input("URL: ")
baixar_video(url)
#observação: pode não estar funcionando devidamente na sua maquina, pois o yt sempre atualiza e é necessário a instalação do ffmpeg.