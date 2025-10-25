import subprocess
import os
import keyboard

def audio(comando: str, falar):
    comando = (comando or "").lower()

    # Sim meu player de audio é o jurassico winamp desde 97
    if "abrir áudio" in comando or "abrir música" in comando or "abrir winamp" in comando:
        falar("Abrindo Winamp.")
        caminho_winamp = r"C:\Program Files (x86)\Winamp\Winamp.exe"
        if os.path.exists(caminho_winamp):
            subprocess.Popen([caminho_winamp])
            falar("Winamp aberto.")
        else:
            falar("Winamp não encontrado.")
        return True    

    elif "abrir legais" in comando or "legais" in comando or "abrir playlist" in comando or "playlist" in comando:
        falar("Abrindo playlist de músicas.")
        caminho_playlist = r"C:\Users\aleca\OneDrive\Área de Trabalho\legais.m3u"
        if os.path.exists(caminho_playlist):
            os.startfile(caminho_playlist)  
            falar("Tocando músicas.")
        else:
            falar("Arquivo de playlist não encontrado.")
        return True

    elif "parar música" in comando or "parar audio" in comando or "parar som" in comando or "música" in comando or "continuar" in comando:
        falar("Ok, Pausando Música.")
        keyboard.press_and_release('c')
        return True

    elif "tocar música" in comando or "tocar" in comando:
        falar("Tocando a música.")
        keyboard.press_and_release('x')
        return True

    elif "próxima música" in comando or "próxima" in comando:
        # Proxima com 2 ss caso contrario ele le o x
        falar("Prossíma música.")
        keyboard.press_and_release('b')
        return True

    elif "música anterior" in comando or "anterior" in comando:
        falar("Música Anterior.")
        keyboard.press_and_release('z')
        return True

    return False