import os, sys, time, subprocess, pyautogui, pyttsx3, speech_recognition as sr
pyautogui.FAILSAFE = False

def geral():
    try:
        from src import navegacao, campainha, audio, programas, sistema, volume
        # Inicializa o mecanismo de voz
        engine = pyttsx3.init()
        engine.setProperty('rate', 180)  # velocidade da fala
        engine.setProperty('volume', 1)  # volume máximo

        def falar(texto):
            print("", texto)
            engine = pyttsx3.init('sapi5')
            engine.setProperty('rate', 180)
            engine.setProperty('volume', 2)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(texto)
            engine.runAndWait()
            engine.stop()

        def ouvir():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Aguardando comando...")
                audio = r.listen(source, phrase_time_limit=5)
            try:
                comando = r.recognize_google(audio, language='pt-BR').lower()
                print("Você disse:", comando)
                return comando
            except sr.UnknownValueError:
                return ""
            except sr.RequestError:
                falar("Erro na conexão com o reconhecimento de voz.")
                return ""

        def resource_path(relative_path):
            try:
                base_path = sys._MEIPASS  # quando rodando o .exe
            except Exception:
                base_path = os.path.abspath(".")  # quando rodando como script
            return os.path.join(base_path, relative_path)


        def executar_comando(comando):
            # Navegação em paginas em geral
            if navegacao(comando, falar, resource_path):
                return

            # Campainha
            if campainha(comando, falar, resource_path):
                return   

            # Volume do sistema
            if volume(comando, falar):
                return

            #Audio
            if audio(comando, falar):
                return

            # Programas
            if programas(comando, falar):
                return

            # Sistema
            if sistema(comando, falar):
                return


        # --- Loop principal ---
        falar("Sistema de comando por voz iniciado.")
        time.sleep(1)
        falar("Diga 'computador' para ativar.")

        while True:
            ativador = ouvir()
            if "computador" in ativador:
                falar("Sim.")
                comando = ouvir()
                executar_comando(comando)

    except Exception as e:
        print(f"Erro detectado: {e}")
        print("Reiniciando em 10 segundos...")
        time.sleep(10)
        subprocess.Popen([sys.executable, os.path.abspath(__file__)])
        sys.exit()
         
geral()