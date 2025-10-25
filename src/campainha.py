import pyautogui
import subprocess
import os


def campainha(comando: str, falar, resource_path):
    comando = (comando or "").lower()

    if "abrir campainha" in comando or "campainha" in comando or "atender" in comando:
        falar("Abrindo câmeras no Google Chrome.")
        caminho_chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        if not os.path.exists(caminho_chrome):
            caminho_chrome = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

        if os.path.exists(caminho_chrome):
            subprocess.Popen([caminho_chrome, "https://ipc-us.ismartlife.me/"])
        else:
            falar("Google Chrome não encontrado.")
        return True
    
    elif "falar" in comando or "silenciar" in comando:
        try:
            imagem_on = pyautogui.locateOnScreen(resource_path('img/falar.png'))
            pyautogui.click(imagem_on)
            falar("Abrindo microfone")
        except:
            imagem_on = pyautogui.locateOnScreen(resource_path('img/silenciar.png'))
            pyautogui.click(imagem_on)
            falar("Fechando microfone")
        return True
        
    return False  # nenhum comando reconhecido