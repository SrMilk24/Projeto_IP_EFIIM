# Projeto_IP_EFIIM

Estrutura proposta

my_game/
│
├── assets/                # Recursos do jogo, como imagens, sons e músicas
│   ├── images/            # Imagens do jogo (sprites, backgrounds, etc)
│   ├── sounds/            # Arquivos de áudio (efeitos sonoros, músicas)
│   └── fonts/             # Fontes utilizadas no jogo
│
├── core/                  # Lógica central do jogo (domínio do jogo)
│   ├── __init__.py        # Arquivo para tornar o diretório um pacote Python
│   ├── entities/          # Entidades do jogo, como Jogador, Inimigos, etc
│   │   ├── player.py      # Lógica do jogador
│   │   ├── enemy.py       # Lógica do inimigo
│   │   └── bullet.py      # Lógica das balas do jogador, por exemplo
│   ├── use_cases/         # Casos de uso, como movimentação, colisões, etc
│   │   ├── movement.py    # Lógica de movimentação dos personagens
│   │   ├── collision.py   # Lógica de colisões
│   │   └── game_logic.py  # Regras do jogo (por exemplo, pontuação, vitória, derrota)
│   └── interfaces/        # Interface para abstrair a interação com o Pygame
│       ├── display.py     # Lógica para renderizar objetos na tela
│       └── input.py       # Lógica de captura de entrada (teclado, mouse)
│
├── game/                  # Lógica do jogo em si, que orquestra a execução
│   ├── __init__.py        # Arquivo para tornar o diretório um pacote Python
│   └── game_manager.py    # Controla o fluxo do jogo (início, fim, pause)
│
├── config/                # Arquivos de configuração (parâmetros do jogo, como tamanho da tela, FPS)
│   └── settings.py        # Configurações principais do jogo
│
├── tests/                 # Testes automatizados
│   ├── __init__.py
│   ├── test_entities.py   # Testes das entidades (jogador, inimigo, etc)
│   ├── test_use_cases.py  # Testes dos casos de uso
│   └── test_game_manager.py # Testes do gerenciamento do jogo
│
└── main.py                # Ponto de entrada do jogo (onde o Pygame é inicializado)
