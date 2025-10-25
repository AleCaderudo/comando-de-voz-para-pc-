# 🎙️ Voice Command PC

Um assistente de **comandos por voz para Windows**, desenvolvido em **Python**, que permite controlar programas, volume, navegador, músicas e até sistemas de câmeras e campainha inteligente — tudo apenas com a voz.

---

## 🚀 Funcionalidades

O sistema reconhece o comando de ativação **“computador”** e aguarda a próxima instrução.  
Abaixo estão os principais comandos suportados:

### 🧭 Navegação (arquivo `navegacoes.py`)
- `abrir navegador` → Abre o Firefox  
- `abrir youtube`, `abrir facebook`, `abrir google`, `abrir cotações`  
- `rolar página`, `subir`, `descer`

### 🔔 Campainha (arquivo `campainha.py`)
- `abrir campainha`, `atender` → Abre o site das câmeras no Chrome  
- `falar`, `silenciar` → Alterna o microfone na interface das câmeras (via PyAutoGUI)

### 🎵 Áudio e Músicas (arquivo `audio.py`)
- `abrir áudio` ou `abrir winamp` → Abre o Winamp  
- `abrir playlist` ou `abrir legais` → Reproduz playlist `.m3u`  
- `tocar`, `parar`, `próxima`, `anterior` → Controla reprodução via atalhos de teclado

### 🔊 Volume do Sistema (arquivo `volume.py`)
- `aumentar volume`, `diminuir volume`  
- `volume máximo`, `volume mínimo`, `mutar`

### 🖥️ Programas (arquivo `programas.py`)
- `abrir nox` → Abre o emulador Nox  
- `abrir whatsapp` → Abre WhatsApp Desktop  
- `abrir e-mail` → Abre Outlook  
- `abrir câmeras`, `abrir torrent`, `abrir bloco de notas`

### ⚙️ Sistema (arquivo `sistema.py`)
- `tela cheia`  
- `fechar`, `fechar tudo`  
- `desligar`, `reiniciar`, `sair`

---

## 🧩 Estrutura do Projeto

```
src/
├── __init__.py
├── audio.py
├── campainha.py
├── navegacoes.py
├── programas.py
├── sistema.py
└── volume.py
main.py
```

O arquivo `main.py` é o ponto de entrada principal. Ele:
- Inicializa o reconhecimento de voz (`speech_recognition`);
- Reproduz respostas por voz (`pyttsx3`);
- Detecta o comando de ativação “computador”;
- Chama as funções correspondentes de cada módulo.

---

## 🛠️ Requisitos

Antes de executar o projeto, instale as dependências:

```bash
pip install pyttsx3 speechrecognition pyautogui keyboard pycaw comtypes
```

> ⚠️ Para usar o reconhecimento de voz, é necessário um microfone funcional e conexão com a internet.

---

## ▶️ Como Executar

Execute diretamente o arquivo principal:

```bash
python main.py
```

Ou, para compilar como executável (via PyInstaller):

```bash
pyinstaller --onefile --windowed --add-data "img/scroller.png;img" --add-data "img/scroller_off.png;img" --add-data "img/falar.png;img" --add-data "img/silenciar.png;img" --icon=icon.ico main.py
```

---

## 💡 Dicas de Uso

- Diga **“computador”** para ativar o assistente.  
- Em seguida, diga o comando desejado (ex: “abrir YouTube”, “aumentar volume”, “abrir WhatsApp”).  
- O programa responderá por voz e executará a ação.

---

## 🧰 Tecnologias Utilizadas

- 🐍 Python 3  
- 🎤 SpeechRecognition  
- 🔊 Pyttsx3 (síntese de voz)  
- 🎚️ Pycaw (controle de volume do sistema)  
- 🖱️ PyAutoGUI e Keyboard (interação com interface e atalhos)

---

## 🧑‍💻 Autor

**Ale Motta**  
Projeto pessoal para automação de PC com comandos de voz.  
💬 _"Diga 'computador' e o controle é todo seu!"_

---

## 📝 Licença

Este projeto é de uso pessoal e educacional.  
Sinta-se à vontade para adaptar ou expandir conforme sua necessidade.

## 👨‍💻 Desenvolvido por

[MHPS](https://www.mhps.com.br) – Soluções em automação e sistemas inteligentes.
