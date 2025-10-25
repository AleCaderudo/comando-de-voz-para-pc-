from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import os, sys, time

# inicializa controle de volume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
audio_volume = cast(interface, POINTER(IAudioEndpointVolume))


def set_volume(level):
    # Define volume entre 0.0 (mudo) e 1.0 (máximo)
    audio_volume.SetMasterVolumeLevelScalar(level, None)

def get_volume():
    # Retorna o volume atual entre 0.0 e 1.0
    return audio_volume.GetMasterVolumeLevelScalar()

def change_volume(delta):
    # Aumenta ou diminui volume
    current = get_volume()
    new = min(1.0, max(0.0, current + delta))
    set_volume(new)
    return new

def volume(comando: str, falar):
    comando = (comando or "").lower()

    if "aumentar volume" in comando or "up" in comando or "aumentar" in comando:
        novo = change_volume(0.1)
        falar(f"Volume aumentado para {int(novo*100)} por cento.")
        return True

    elif "diminuir volume" in comando or "reduzir" in comando or "diminuir" in comando:
        novo = change_volume(-0.1)
        falar(f"Volume diminuído para {int(novo*100)} por cento.")
        return True

    elif "volume máximo" in comando or "volume alto" in comando:
        set_volume(1.0)
        falar("Volume no máximo.")
        return True

    elif "volume mínimo" in comando or "volume baixo" in comando:
        set_volume(0.05)
        falar("Volume no mínimo.")
        return True

    elif "mutar" in comando or "mudo" in comando:
        set_volume(0.0)
        falar("Som mutado.")
        return True

    return False
