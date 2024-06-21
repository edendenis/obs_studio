#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `obs-studio` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `obs-studio` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings for configuring/installing/using the `obs-studio` on `Linux Ubuntu`._
# 

# ## Revisão(ões)/Versão(ões)

# | Revisão número | Data da revisão | Descrição da revisão                                    | Autor da revisão                                |
# |:--------------:|:---------------:|:--------------------------------------------------------|:------------------------------------------------|
# | 0              | 24/04/2024      | <ul><li>Revisão inicial/criação do documento.</li></ul> | <ul><li>Eden Denis F. da S. L. Santos</li></ul> |
# 

# ## Descrição [2]
# 
# ### `obs-studio`
# 
# O `OBS Studio` é um software de código aberto amplamente utilizado para gravação e transmissão de conteúdo em tempo real. Com recursos avançados de captura de tela, webcam e áudio, permite aos usuários criar transmissões de alta qualidade para plataformas como Twitch, YouTube e Facebook. Além disso, oferece recursos de edição em tempo real, como sobreposições de texto e imagens, e é altamente personalizável por meio de plugins e configurações avançadas. É uma ferramenta popular entre streamers, criadores de conteúdo e profissionais que necessitam de uma solução robusta para produção de vídeo ao vivo.
# 

# ## 1. Como configurar/instalar/usar o `obs-studio` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar/usar o `obs-studio` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.5 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.6 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.7 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.8 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

# Para instalar o `OBS Studio` no `Linux Ubuntu` utilizando o `Terminal Emulator`, você pode seguir os passos abaixo. Essas instruções assumem que você está utilizando uma versão recente do Ubuntu:
# 
# 3. **Adicione o PPA do OBS Studio**: O `OBS Studio` fornece um PPA (Personal Package Archive) oficial que facilita a instalação e atualização. Para adicionar o PPA, execute o seguinte comando: `sudo add-apt-repository ppa:obsproject/obs-studio`
# 
#     Isso adicionará o repositório do OBS ao seu sistema. Você terá que pressionar `Enter` para confirmar.
# 
# 4. **Atualize a lista de pacotes**: Após adicionar o PPA, é uma boa prática atualizar a lista de pacotes do seu sistema para incluir os novos pacotes disponíveis no PPA: `sudo apt update`
# 
# 5. **Instale o OBS Studio**: Com o repositório adicionado e a lista de pacotes atualizada, agora você pode instalar o OBS Studio com o seguinte comando: `sudo apt install obs-studio -y`
# 
# 6. **Execute o OBS Studio**: Após a instalação, você pode iniciar o `OBS Studio` pelo terminal com o comando obs ou encontrá-lo no menu de aplicações.
# 
# 7. **Configurações adicionais**: Após a instalação, você pode querer configurar fontes de áudio e vídeo. `O OBS Studio` geralmente detecta dispositivos de vídeo e áudio automaticamente, mas você pode precisar configurar manualmente dependendo do seu setup.
# Estes passos devem ajudá-lo a instalar o `OBS Studio` no Ubuntu através do terminal. Se houver atualizações disponíveis no futuro, elas devem ser gerenciadas automaticamente pelo gestor de pacotes quando você executar `sudo apt update` e `sudo apt upgrade`.

# ### 1.1 Estilo de letra próxima ao estilo de letra `Book Antiqua`
# 
# ### 1.1.1 Estilo de letra `Noto Serif` 
# 
# Analisando a lista de fontes fornecida, a que se assemelha mais a `"Book Antiqua"` seria `"Noto Serif"`, pois é uma família de fontes serifadas e tem várias variações que podem se aproximar das características da `"Book Antiqua"`. A família `"Noto"` é conhecida por sua ampla cobertura de idiomas e estilos, e as serifas na `"Noto Serif"` têm um estilo que pode lembrar as elegantes serifas da `"Book Antiqua"`.
# 
# Assim, eu sugeriria explorar a `"Noto Serif"` ou alguma de suas variações para algo que possa se aproximar da aparência da `"Book Antiqua"`.
# 
# ### 1.1.2 Estilo de letra `URW Bookman`
# 
# Analisando as novas fontes apresentadas, a que se destaca como mais semelhante à `"Book Antiqua"` seria a `"URW Bookman"`. A `"URW Bookman"` é uma fonte serifada, com um estilo que remete ao design clássico, o que a torna mais próxima visualmente da `"Book Antiqua"` do que outras opções `sans-serif` ou com design moderno.
# 
# A `"Book Antiqua"` é conhecida por suas serifas distintas e a estrutura de suas letras que lembra a tipografia tradicional de livros e impressão clássica. A `"URW Bookman" `compartilha dessas qualidades, fazendo dela uma opção viável se você está buscando uma fonte alternativa no seu sistema que seja semelhante à `"Book Antiqua"`.

# ## 2. Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `obs-studio` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean
#     sudo apt autoclean -y
#     sudo apt autoremove -y
#     sudo apt update -y
#     sudo apt uptoremove -y
#     sudo apt autoclean -y
#     sudo apt install obs-studio -y
#     obs-studio
#     ```
# 

# ## 3. Identificar o caminho do dispotivo `webcam`
# 
# Para ter certeza do caminho do dispositivo de vídeo da sua `webcam` no `Linux`, você pode seguir estes passos no terminal:
# 
# 1. Abra um terminal.
# 
# 2. **Digite o comando a seguir e pressione `Enter`: `ls /dev/video*`
# 
#     Este comando vai listar todos os dispositivos de vídeo reconhecidos pelo sistema, geralmente as webcams são listadas como `/dev/video0`, `/dev/video1` etc.
# 
# 3. **Instalar o `v4l2-utils`**: Faça isso com o comando: `sudo apt-get install v4l-utils`
#     
#     Se estiver usando uma distribuição baseada em `Debian` ou `Ubuntu`.
# 
# 4. Se você tiver mais de um dispositivo listado e não tiver certeza de qual é a sua `webcam`, pode testar uma outra opção é usar o comando:  `v4l2-ctl --list-devices`
# 
#     Este comando que oferece uma listagem mais detalhada dos dispositivos de vídeo e associa cada um aos respectivos caminhos no `/dev`.Você pode precisar instalar a ferramenta `v4l-utils` para usar o `v4l2-ctl`.
# 

# ## Referências
# 
# [1] OPENAI. ***Instale OBS no Ubuntu.*** Disponível em: <https://chat.openai.com/c/8fb38323-56e4-40ba-b1f3-a7d16ceb378d> (texto adaptado). Acessado em: 24/04/2023 17:11.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 24/04/2024 17:10.
# 
