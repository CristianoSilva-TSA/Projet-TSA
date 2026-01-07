# 🌐 Bash Multi-Player Rock-Paper-Scissors

Um sistema Cliente-Servidor escrito em **Bash** que permite que dois jogadores em computadores diferentes joguem Pedra, Papel ou Tesoura através de uma rede local.

## 🛠️ Requisitos
* Sistema Operativo: Linux / macOS / WSL (Windows)
* Dependência: `netcat` (instalado por padrão na maioria das distros)

## 🚀 Como Jogar

### 1. Preparar o Servidor (O Árbitro)
No computador que servirá de servidor, execute:
```bash
chmod +x server.sh
./server.sh
