import pyautogui
import keyboard
import subprocess
import os

pyautogui.FAILSAFE = False

def navegacao(comando: str, falar, resource_path):
    comando = (comando or "").lower()

    caminho_firefox = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    if not os.path.exists(caminho_firefox):
        caminho_firefox = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"

    def abrir_firefox(url=None):
        if os.path.exists(caminho_firefox):
            if url:
                subprocess.Popen([caminho_firefox, "-new-tab", url])
            else:
                subprocess.Popen([caminho_firefox])
        else:
            falar("Firefox não encontrado.")

    if "abrir navegador" in comando:
        falar("Abrindo navegador Firefox.")
        abrir_firefox()
        return True

    elif "abrir youtube" in comando or "abrir o youtube" in comando:
        falar("Abrindo YouTube.")
        abrir_firefox("https://www.youtube.com")
        return True

    elif "abrir facebook" in comando or "abrir o facebook" in comando:
        falar("Abrindo Facebook.")
        abrir_firefox("https://www.facebook.com")
        return True

    elif "abrir google" in comando or "abrir o google" in comando:
        falar("Abrindo Google.")
        abrir_firefox("https://www.google.com")
        return True

    elif "abrir cotações" in comando or "cotação" in comando or "cotações" in comando:
        abrir_firefox("https://br.advfn.com/monitor")
        falar("Abrindo Cotações.")
        return True

    elif ("rolar página" in comando or "rolar" in comando or "página" in comando or
          "parar de rolar a página" in comando or "parar" in comando or "rolar a página" in comando):
        try:
            img1 = resource_path('img/scroller.png')
            imagem_rolar = pyautogui.locateOnScreen(img1)
            if imagem_rolar:
                pyautogui.click(imagem_rolar)
                pyautogui.moveRel(0, 50, duration=0.2)
                falar("rolando a página")
            else:
                raise FileNotFoundError("scroller.png não encontrado na tela")
        except Exception:
            try:
                img2 = resource_path('img/scroller_off.png')
                imagem_rolar = pyautogui.locateOnScreen(img2)
                if imagem_rolar:
                    pyautogui.click(imagem_rolar)
                    pyautogui.moveRel(0, 50, duration=0.2)
                    falar("parar de rolar a página")
                else:
                    falar("Botão de rolagem não encontrado na tela.")
            except Exception as e:
                falar("Erro ao tentar localizar o botão de rolagem.")
                print("Erro rolagem:", e)
        return True

    elif "descer" in comando or "baixar" in comando:
        falar("Descendo tela")
        keyboard.press_and_release('down')
        return True

    elif "subir" in comando or "para cima" in comando:
        falar("Subindo tela")
        keyboard.press_and_release('up')
        return True

    return False