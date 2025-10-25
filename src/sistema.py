import os
import keyboard
import sys


def sistema(comando: str, falar):
    comando = (comando or "").lower()

    if "tela cheia" in comando or "tela" in comando:
        falar("Tela cheia")
        keyboard.press_and_release('f11')
        return True

    elif "fechar" in comando.lower():
        falar("Fechando")
        keyboard.press_and_release('alt+f4')
        return True

    elif "fechar tudo" in comando.lower():
        falar("Fechando todas as janelas e programas")
        os.system("taskkill /f /fi \"status eq running\"")
        return True            

    elif "desligar" in comando:
        falar("Desligando o computador.")
        os.system('shutdown /s /t 5 /c "Deslingando PC"')
        return True

    elif "reiniciar" in comando:
        falar("Reiniciando o computador.")
        os.system('shutdown /r /t 5 /c "Reiniciando o sistema..."')
        return True

    elif "sair" in comando:
        falar("Encerrando o sistema de voz. Até logo!")
        sys.exit()
    else:
        falar("Comando não reconhecido.")
        return True

    return False
