<p align="center">
  <b>👤 Gustavo Marques de Almeida</b><br>
  <a href="https://www.linkedin.com/in/gustavo-marques-de-almeida-5755202a6/">🔗 LinkedIn</a> |
  <a href="https://github.com/Gustah-Py">💻 GitHub</a>
</p>

---

# 🎥 CFTV Python Automation
---

Sistema de **monitoramento e automação CFTV** usando Python para câmeras IP (RTSP/ONVIF).
 código limpo, README completo,
licença, changelog e estrutura 

---

## 🚀 Objetivo
Automatizar tarefas comuns em CFTV:
- Monitorar status (watchdog) e capturar snapshots periódicos.
- Gerar timelapse diário com FFmpeg.
- Enviar alertas (opcional) via Telegram.
- Configuração simples com `config.yaml` e `.env`.

> Este repo inclui um **script de demonstração** que usa apenas FFmpeg para capturar um frame de um RTSP público,
> ideal para rodar em qualquer máquina sem dependências pesadas.

---

## 🧩 Tecnologias
Python 3 • OpenCV (opcional) • FFmpeg • YAML • systemd (Linux, opcional)

---

## 🧰 Estrutura
```
.
├── src/
│   └── RTSP-Snapshots.py       # Demo: snapshot via FFmpeg
├── config.yaml                 # Configuração de câmeras (já vem com RTSP público)
├── requirements.txt            # Dependências
├── .gitignore                  # Ignora venv e pastas temporárias
├── LICENSE                     # MIT
├── CHANGELOG.md                # Histórico
└── demo/
    ├── README.txt              # Onde colocar saídas de exemplo
    └── sample-log.txt          # Log fictício para vitrine
```

---

## 🔧 Como rodar a demo (Windows)
```bat
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src\RTSP-Snapshots.py
```
Os snapshots serão salvos em `data/snapshots/Teste_Publico/<data>/`.

> Se sua rede bloquear RTSP, teste no VLC ou troque a URL por uma câmera da sua rede (RTSP do DVR/NVR).

---

## ⚙️ Configuração rápida
Edite `config.yaml` quando quiser usar sua própria câmera:
```yaml
cameras:
  - name: Entrada
    rtsp: "rtsp://usuario:senha@192.168.1.50:554/Streaming/Channels/101"
```

---

## 🖼️ Demonstração
Coloque prints de execução (terminal, pastas criadas, snapshot) na pasta `demo/`.  
Exemplos prontos: `demo/sample-log.txt`.

---

## 🔒 Boas práticas
- Troque senhas padrão das câmeras, desligue UPnP, use VLAN.
- Respeite LGPD (sinalização e retenção de mídia).
- Não exponha RTSP diretamente na internet.

---

## 👤 Autor
**Gustavo Marques de Almeida** • São Paulo-SP, Brasil  
GitHub e LinkedIn aqui (edite este README após publicar).

---

## 📄 Licença
MIT — livre para uso e adaptação.
