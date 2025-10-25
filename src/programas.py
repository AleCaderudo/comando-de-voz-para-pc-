import os
import subprocess


def programas(comando: str, falar):
    comando = (comando or "").lower()    

    if "abrir nox" in comando or "nox" in comando or "emulador" in comando:
        falar("Abrindo Nox.")
        caminho_nox = r"C:\Nox\bin\Nox.exe"
        if os.path.exists(caminho_nox):
            subprocess.Popen([caminho_nox])
            falar("Nox aberto.")
        else:
            falar("Nox não encontrado.")
        return True

    elif "abrir whatssap" in comando or "whatssap" in comando or "whats" in comando:
        falar("Abrindo o WhatsApp Web.")
        os.system("start whatsapp://")
        return True
    
    elif "abrir e-mail" in comando or "abrir outlook" in comando or "email" in comando:
        falar("Abrindo o Outlook.")
        os.system("start outlookmail:")
        return True
                   

    elif "abrir câmera" in comando or "câmera" in comando or "câmeras" in comando:
        falar("Abrindo Cameras.")
        caminho_cam = r"C:\Program Files\Intelbras\SIMNext\SIM Next\SIMNext.exe"
        if os.path.exists(caminho_cam):
            subprocess.Popen([caminho_cam])
            falar("Câmeras abertas.")
        else:
            falar("Câmeras não encontradas.")
        return True 
    
    elif "abrir to" in comando or "torre" in comando or "filme" in comando:
        falar("Abrindo torrent.")
        caminho_cam = r"C:\Program Files\qBittorrent\qbittorrent.exe"
        if os.path.exists(caminho_cam):
            subprocess.Popen([caminho_cam])
            falar("torrent aberto.")
        else:
            falar("torrent não encontradas.")
        return True 
          
    elif "abrir bloco de notas" in comando:
        falar("Abrindo bloco de notas.")
        os.system("notepad")
        return True
    
    return False