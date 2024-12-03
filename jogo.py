import tkinter as tk
import random
import math
from typing import Tuple, Optional

# Configurações globais do jogo
LARGURA = 700  # Largura da janela (canvas) principal
ALTURA = 800  # Altura da janela (canvas) principal
COLUNAS = 14  # Número de colunas horizontais no grid
LINHAS = 8  # Número de linhas verticais no grid
TAMANHO_BOLA = LARGURA // COLUNAS  # Tamanho de cada célula para ajustar dinamicamente ao grid

# Paleta de cores associada às figuras geométricas
FORMAS = {
    "Círculo": "blue",       # Cor azul para círculos
    "Quadrado": "yellow",    # Cor amarela para quadrados
    "Triângulo": "red",      # Cor vermelha para triângulos
    "Hexágono": "orange",    # Cor laranja para hexágonos
    "Pentágono": "purple",   # Cor roxa para pentágonos
    "Retângulo": "green",    # Cor verde para retângulos
}


class MenuInicial:
    """Classe responsável por criar o menu inicial do jogo."""
    def __init__(self, master: tk.Tk, iniciar_jogo_callback):
        """
        Inicializa o menu inicial com título, botões e explicação.
        """
        self.master = master
        self.iniciar_jogo_callback = iniciar_jogo_callback

        # Cria o frame principal para o menu inicial
        self.frame_menu = tk.Frame(master, bg="#f0f8ff", width=LARGURA, height=ALTURA)
        self.frame_menu.pack_propagate(False)  # Impede que o frame redimensione automaticamente
        self.frame_menu.pack(fill=tk.BOTH, expand=True)

        # Adiciona o título ao menu inicial
        self.titulo = tk.Label(
            self.frame_menu,
            text="Lança Figuras",  # Nome do jogo
            font=("Helvetica", 40, "bold"),
            bg="#f0f8ff",
            fg="#333"
        )
        self.titulo.pack(pady=30)  # Adiciona espaçamento

        # Adiciona o subtítulo para explicar o objetivo do jogo
        self.subtitulo = tk.Label(
            self.frame_menu,
            text="Aprende Geometria a brincar!",
            font=("Helvetica", 16, "italic"),
            bg="#f0f8ff",
            fg="#555"
        )
        self.subtitulo.pack(pady=10)

        # Canvas para desenhar as figuras geométricas no menu
        self.canvas_figuras = tk.Canvas(self.frame_menu, bg="#f0f8ff", width=LARGURA, height=100, highlightthickness=0)
        self.canvas_figuras.pack()
        self.desenhar_figuras()  # Método que desenha figuras de exemplo no canvas

        # Criação de botões para seleção de níveis
        self.botoes_frame = tk.Frame(self.frame_menu, bg="#f0f8ff")  # Container para os botões
        self.botoes_frame.pack(pady=20)

        # Loop para criar os botões dos níveis (Nível 1, Nível 2 e Nível 3)
        for nivel in range(1, 4):  # Três níveis disponíveis
            botao = tk.Button(
                self.botoes_frame,
                text=f"Nível {nivel}",
                font=("Helvetica", 16, "bold"),
                bg="#4caf50",  # Verde
                fg="white",  # Texto branco
                activebackground="#45a049",  # Verde mais claro no hover
                activeforeground="white",
                width=12,
                height=2,
                command=lambda n=nivel: self.selecionar_nivel(n),  # Callback ao clicar no botão
            )
            botao.grid(row=0, column=nivel - 1, padx=10)  # Adiciona os botões horizontalmente com espaçamento

        # Botão adicional para exibir "Como Jogar"
        self.botao_como_jogar = tk.Button(
            self.frame_menu,
            text="Como jogar",
            font=("Helvetica", 16, "bold"),
            bg="#2196f3",  # Azul
            fg="white",  # Texto branco
            activebackground="#1e88e5",  # Azul mais claro no hover
            activeforeground="white",
            width=12,
            height=2,
            command=self.mostrar_como_jogar,  # Callback ao clicar no botão
        )
        self.botao_como_jogar.pack(pady=10)  # Adiciona espaçamento

    def desenhar_figuras(self):
        """Desenha exemplos de figuras geométricas no canvas do menu."""
        TAMANHO = 50  # Tamanho padrão das figuras no canvas
        total_figuras = 6  # Número de figuras a desenhar
        espacamento = 20  # Espaço fixo entre as figuras
        largura_total = total_figuras * TAMANHO + (total_figuras - 1) * espacamento  # Calcula largura ocupada
        x_inicial = (LARGURA - largura_total) // 2  # Calcula posição inicial centralizada
        y_centro = 50  # Posição vertical fixa para todas as figuras

        # Desenho das figuras uma por uma:
        # Círculo
        self.canvas_figuras.create_oval(
            x_inicial, y_centro - TAMANHO // 2, x_inicial + TAMANHO, y_centro + TAMANHO // 2,
            fill="blue", outline="black"
        )
        x_inicial += TAMANHO + espacamento

        # Quadrado
        self.canvas_figuras.create_rectangle(
            x_inicial, y_centro - TAMANHO // 2,
            x_inicial + TAMANHO, y_centro + TAMANHO // 2,
            fill="yellow", outline="black"
        )
        x_inicial += TAMANHO + espacamento

        # Triângulo
        self.canvas_figuras.create_polygon(
            x_inicial, y_centro + TAMANHO // 2,
            x_inicial + TAMANHO // 2, y_centro - TAMANHO // 2,
            x_inicial + TAMANHO, y_centro + TAMANHO // 2,
            fill="red", outline="black"
        )
        x_inicial += TAMANHO + espacamento

        # Hexágono
        x_centro_hexagono = x_inicial + TAMANHO // 2
        y_centro_hexagono = y_centro
        raio_hexagono = TAMANHO // 2
        pontos_hexagono = [
            (x_centro_hexagono + raio_hexagono * math.cos(math.radians(60 * i)),
             y_centro_hexagono + raio_hexagono * math.sin(math.radians(60 * i)))
            for i in range(6)
        ]
        self.canvas_figuras.create_polygon(
            pontos_hexagono, fill="orange", outline="black"
        )
        x_inicial += TAMANHO + espacamento

        # Pentágono
        x_centro_pentagono = x_inicial + TAMANHO // 2
        y_centro_pentagono = y_centro
        raio_pentagono = TAMANHO // 2
        pontos_pentagono = [
            (x_centro_pentagono + raio_pentagono * math.cos(math.radians(72 * i)),
             y_centro_pentagono + raio_pentagono * math.sin(math.radians(72 * i)))
            for i in range(5)
        ]
        self.canvas_figuras.create_polygon(
            pontos_pentagono, fill="purple", outline="black"
        )
        x_inicial += TAMANHO + espacamento

        # Retângulo
        largura = TAMANHO  # Largura do retângulo
        altura = TAMANHO // 2  # Altura do retângulo
        x_inicial += 25  # Ajusta a posição
        self.canvas_figuras.create_rectangle(
            x_inicial - largura // 2, y_centro - altura // 2,
            x_inicial + largura // 2, y_centro + altura // 2,
            fill="green", outline="black"
        )
        
    def selecionar_nivel(self, nivel: int):
        """
        Chama o callback para iniciar o jogo no nível selecionado.
        """
        self.frame_menu.destroy()  # Remove o menu inicial
        self.iniciar_jogo_callback(nivel)  # Chama a função para iniciar o jogo

    def mostrar_como_jogar(self):
        """
        Exibe a explicação de como jogar o jogo.
        Substitui o menu inicial por um ecrã com instruções.
        """
        self.frame_menu.destroy()  # Remove o menu inicial
        self.frame_como_jogar = tk.Frame(self.master, bg="lightyellow", width=LARGURA, height=ALTURA)
        self.frame_como_jogar.pack_propagate(False)  # Desativa redimensionamento automático
        self.frame_como_jogar.pack(fill=tk.BOTH, expand=True)  # Preenche todo o espaço disponível

        # Título "Como Jogar"
        self.titulo = tk.Label(
            self.frame_como_jogar,
            text="Como Jogar",
            font=("Helvetica", 36, "bold"),
            bg="lightyellow",
        )
        self.titulo.pack(pady=20)  # Adiciona espaçamento

        # Texto explicativo com instruções do jogo
        texto_explicativo = (
            "1. Junta as figuras geométricas da mesma cor.\n"
            "2. Pressiona no local onde queres lançar a figura.\n"
            "3. Ao juntares duas figuras da mesma cor, verás o nome da figura na tela.\n"
            "4. Completa todos os níveis para ganhares o jogo e aprenderes!"
        )

        self.texto_explicativo = tk.Label(
            self.frame_como_jogar,
            text=texto_explicativo,
            font=("Helvetica", 16),
            bg="lightyellow",
            justify="left",  # Alinha o texto à esquerda
            wraplength=LARGURA - 40,  # Limita a largura do texto para evitar que ultrapasse o ecrã
        )
        self.texto_explicativo.pack(pady=20)  # Adiciona espaçamento

        # Botão para voltar ao menu inicial
        self.botao_voltar = tk.Button(
            self.frame_como_jogar,
            text="Voltar",
            font=("Helvetica", 16),
            bg="red",
            fg="white",
            width=10,
            height=2,
            command=self.voltar_menu,  # Callback para retornar ao menu
        )
        self.botao_voltar.pack(pady=20)  # Adiciona espaçamento

    def voltar_menu(self):
        """
        Volta ao menu inicial.
        Destroi o ecrã atual e recria o menu inicial.
        """
        self.frame_como_jogar.destroy()  # Remove o ecrã atual
        self.__init__(self.master, self.iniciar_jogo_callback)  # Recria o menu inicial


class JogoBubbleShooter:
    """Classe principal que gere a lógica do jogo e as interações."""
    def __init__(self, master: tk.Tk, nivel: int, voltar_menu_callback):
        """
        Inicializa o jogo para o nível selecionado.
        """
        self.master = master
        self.nivel = nivel
        self.voltar_menu_callback = voltar_menu_callback

        # Cria o canvas para desenhar o jogo
        self.canvas = tk.Canvas(master, width=LARGURA, height=ALTURA, bg="white")
        self.canvas.pack()  # Posiciona o canvas na janela principal

        # Configurações de cada nível (formas, colunas e linhas)
        self.formas_por_nivel = {
            1: {"formas": ["Círculo", "Quadrado", "Triângulo"], "colunas": 10, "linhas": 6},
            2: {"formas": ["Círculo", "Quadrado", "Triângulo", "Retângulo"], "colunas": 12, "linhas": 7},
            3: {"formas": list(FORMAS.keys()), "colunas": 14, "linhas": 8},
        }

        # Configuração de cores de fundo por nível
        self.fundos_por_nivel = {
            1: {"cor": "lightblue"},  # Fundo azul claro para o nível 1
            2: {"cor": "lightgreen"},  # Fundo verde claro para o nível 2
            3: {"cor": "lightpink"},  # Fundo rosa claro para o nível 3
        }

        # Descrições associadas a cada figura geométrica
        self.descricoes_figuras = {
            "Círculo": "O círculo não tem lados!",
            "Quadrado": "O quadrado tem 4 lados!",
            "Triângulo": "O triângulo tem 3 lados!",
            "Hexágono": "O hexágono tem 6 lados!",
            "Pentágono": "O pentágono tem 5 lados!",
            "Retângulo": "O retângulo tem 4 lados!",
        }

        # Configuração inicial do jogo
        self.atualizar_dificuldade()  # Ajusta as configurações com base no nível

        # Variáveis de estado do jogo
        self.figura_jogador = None  # Figura controlada pelo jogador
        self.linha_direcao = None  # Linha que mostra a direção do disparo
        self.movendo = False  # Indica se a figura está em movimento
        self.texto_figura = None  # Texto descritivo exibido no canvas

        # Inicializa o tabuleiro e a figura do jogador
        self.preencher_grade()  # Preenche o topo do canvas com figuras aleatórias
        self.criar_figura_jogador()  # Cria a figura controlada pelo jogador

        # Adiciona botões de controlo (Voltar ao menu e Reiniciar)
        self.adicionar_botao_voltar_menu()
        self.adicionar_botao_reiniciar()

        # Eventos de interação do rato
        self.canvas.bind("<Motion>", self.atualizar_linha_direcao)  # Atualiza a linha de direção ao mover o rato
        self.canvas.bind("<Button-1>", self.disparar_figura)  # Dispara a figura ao clicar com o rato

    def atualizar_dificuldade(self):
        """
        Atualiza as configurações do jogo de acordo com o nível selecionado.
        Define o número de colunas, linhas e formas disponíveis no nível.
        """
        if self.nivel in self.formas_por_nivel:
            config = self.formas_por_nivel[self.nivel]  # Configurações específicas do nível
            global COLUNAS, LINHAS, TAMANHO_BOLA, FORMAS
            COLUNAS = config["colunas"]  # Atualiza o número de colunas
            LINHAS = config["linhas"]  # Atualiza o número de linhas
            TAMANHO_BOLA = LARGURA // COLUNAS  # Calcula o tamanho das bolas dinamicamente

            # Filtra apenas as formas disponíveis neste nível
            self.formas_nivel = {forma: FORMAS[forma] for forma in config["formas"]}

        # Ajusta a cor de fundo do nível
        fundo = self.fundos_por_nivel[self.nivel]
        self.canvas.config(bg=fundo["cor"])  # Define a cor de fundo do canvas


    def adicionar_botao_voltar_menu(self):
        """
        Adiciona o botão no canvas para voltar ao menu inicial.
        """
        # Botão "Menu" representado como um retângulo no canvas
        self.botao_voltar = self.canvas.create_rectangle(
            130, ALTURA - 50, 240, ALTURA - 10, fill="blue", outline="black"
        )
        # Texto "Menu" dentro do retângulo
        self.texto_voltar = self.canvas.create_text(
            185, ALTURA - 30, text="Menu", font=("Helvetica", 12, "bold"), fill="white"
        )
        # Vincula a ação de clique ao botão e ao texto
        self.canvas.tag_bind(self.botao_voltar, "<Button-1>", self.voltar_menu)
        self.canvas.tag_bind(self.texto_voltar, "<Button-1>", self.voltar_menu)

    def adicionar_botao_reiniciar(self):
        """
        Adiciona o botão no canvas para reiniciar o jogo.
        """
        # Botão "Reiniciar" representado como um retângulo no canvas
        self.botao_reiniciar = self.canvas.create_rectangle(
            10, ALTURA - 50, 120, ALTURA - 10, fill="red", outline="black"
        )
        # Texto "Reiniciar" dentro do retângulo
        self.texto_reiniciar = self.canvas.create_text(
            65, ALTURA - 30, text="Reiniciar", font=("Helvetica", 12, "bold"), fill="white"
        )
        # Vincula a ação de clique ao botão e ao texto
        self.canvas.tag_bind(self.botao_reiniciar, "<Button-1>", self.reiniciar_jogo)
        self.canvas.tag_bind(self.texto_reiniciar, "<Button-1>", self.reiniciar_jogo)

    def voltar_menu(self, event=None):
        """
        Volta ao menu inicial, limpando o canvas atual.
        """
        self.canvas.destroy()  # Remove o canvas do jogo
        self.voltar_menu_callback()  # Chama a função para recriar o menu inicial

    def reiniciar_jogo(self, event=None):
        """
        Reinicia o estado do jogo atual.
        """
        self.canvas.delete("all")  # Remove todos os elementos do canvas
        self.figura_jogador = None  # Reseta a figura controlada pelo jogador
        self.linha_direcao = None  # Remove a linha de direção
        self.movendo = False  # Indica que não há movimento
        self.texto_figura = None  # Reseta o texto exibido
        self.preencher_grade()  # Recria a grade inicial
        self.criar_figura_jogador()  # Recria a figura do jogador
        self.adicionar_botao_reiniciar()  # Recria o botão "Reiniciar"
        self.adicionar_botao_voltar_menu()  # Recria o botão "Menu"
        self.texto_descricao = None  # Reseta a descrição da figura
        

    def preencher_grade(self):
        """
        Preenche o topo do canvas com bolas contendo figuras geométricas.
        """
        # Inicializa a grade como uma matriz vazia
        self.grade = [[None for _ in range(COLUNAS)] for _ in range(LINHAS)]
        # Adiciona figuras geométricas nas primeiras linhas da grade
        for linha in range(LINHAS // 2):  # Apenas metade das linhas são preenchidas
            for coluna in range(COLUNAS):
                # Seleciona aleatoriamente uma figura e a sua cor
                tipo_figura = random.choice(list(self.formas_nivel.keys()))
                cor = FORMAS[tipo_figura]
                # Calcula as coordenadas da célula
                x, y = self.calcular_posicao_celula(linha, coluna)
                # Desenha a bola com a figura e adiciona à grade
                figura = self.desenhar_bola_com_figura(x, y, tipo_figura, cor)
                self.grade[linha][coluna] = figura

    def criar_figura_jogador(self):
        """
        Cria a figura controlada pelo jogador no centro inferior do canvas.
        """
        if self.figura_jogador is not None:  # Se já existir, não cria outra
            return
        # Seleciona aleatoriamente o tipo de figura e a sua cor
        tipo_figura = random.choice(list(self.formas_nivel.keys()))
        cor = self.formas_nivel[tipo_figura]
        # Calcula a posição inicial no centro inferior
        x = (LARGURA // 2) - (TAMANHO_BOLA // 2)
        y = ALTURA - (TAMANHO_BOLA * 1.5)
        # Desenha a bola controlada pelo jogador
        self.figura_jogador = self.desenhar_bola_com_figura(x, y, tipo_figura, cor)
        self.atualizar_texto_figura(tipo_figura)  # Atualiza o texto com o tipo de figura
        self.atualizar_texto_descricao(tipo_figura)  # Mostra a descrição da figura

    def atualizar_texto_figura(self, tipo_figura: str):
        """
        Atualiza o texto exibido no canto inferior direito com o tipo da figura atual.
        """
        if self.texto_figura:
            self.canvas.delete(self.texto_figura)  # Remove o texto anterior
        # Cria o texto no canto inferior direito do canvas
        self.texto_figura = self.canvas.create_text(
            LARGURA - 10, ALTURA - 20,
            text=f"Figura Atual: {tipo_figura}",
            font=("Helvetica", 14, "bold"),
            fill="black",
            anchor="se"  # Alinha o texto à direita
        )

    def calcular_posicao_celula(self, linha: int, coluna: int) -> Tuple[int, int]:
        """
        Calcula as coordenadas (x, y) do canto superior esquerdo de uma célula na grelha.
        """
        x = coluna * TAMANHO_BOLA  # Posição x com base na coluna
        y = linha * TAMANHO_BOLA  # Posição y com base na linha
        return x, y

    def desenhar_bola_com_figura(self, x: int, y: int, tipo_figura: str, cor: str):
        """
        Desenha uma bola no canvas com uma figura geométrica centralizada dentro.
        """
        margem = 3  # Margem para separar as bordas
        # Desenha a bola (um círculo cinzento)
        bola = self.canvas.create_oval(
            x + margem, y + margem,
            x + TAMANHO_BOLA - margem, y + TAMANHO_BOLA - margem,
            fill="lightgray", outline="black"
        )
        # Desenha a figura geométrica centralizada dentro da bola
        figura = self.desenhar_figura_centralizada(x, y, tipo_figura, cor)
        return bola, figura, tipo_figura  # Retorna os elementos criados

    def desenhar_figura_centralizada(self, x: int, y: int, tipo_figura: str, cor: str):
        """
        Desenha a figura geométrica centralizada dentro de uma célula.
        """
        centro_x = x + TAMANHO_BOLA // 2  # Calcula o centro da célula em x
        centro_y = y + TAMANHO_BOLA // 2  # Calcula o centro da célula em y

        # Desenha a figura com base no tipo
        if tipo_figura == "Círculo":
            raio = TAMANHO_BOLA // 3  # Raio proporcional ao tamanho da célula
            return self.canvas.create_oval(
                centro_x - raio, centro_y - raio, centro_x + raio, centro_y + raio, fill=cor
            )
        elif tipo_figura == "Quadrado":
            lado = TAMANHO_BOLA // 2  # Lado proporcional ao tamanho da célula
            return self.canvas.create_rectangle(
                centro_x - lado // 2, centro_y - lado // 2,
                centro_x + lado // 2, centro_y + lado // 2, fill=cor
            )
        elif tipo_figura == "Triângulo":
            return self.desenhar_poligono(centro_x, centro_y, 3, TAMANHO_BOLA // 3, cor)
        elif tipo_figura == "Hexágono":
            return self.desenhar_poligono(centro_x, centro_y, 6, TAMANHO_BOLA // 3, cor)
        elif tipo_figura == "Pentágono":
            return self.desenhar_poligono(centro_x, centro_y, 5, TAMANHO_BOLA // 3, cor)
        elif tipo_figura == "Retângulo":
            largura = TAMANHO_BOLA // 2
            altura = TAMANHO_BOLA // 3
            return self.canvas.create_rectangle(
                centro_x - largura // 2, centro_y - altura // 2,
                centro_x + largura // 2, centro_y + altura // 2, fill=cor
            )

    def desenhar_poligono(self, x: int, y: int, lados: int, raio: int, cor: str):
        """
        Desenha um polígono regular no canvas.
        """
        # Calcula os pontos (vértices) do polígono
        pontos = [
            (x + raio * math.cos(2 * math.pi * i / lados),
             y + raio * math.sin(2 * math.pi * i / lados))
            for i in range(lados)
        ]
        # Desenha o polígono no canvas
        return self.canvas.create_polygon(pontos, fill=cor, outline="black")

    def tratar_colisao(self, linha: int, coluna: int) -> None:
        """
        Trata das colisões entre a figura do jogador e uma figura da grelha.
        """
        # Obtém as cores da figura do jogador e da grade
        cor_jogador = self.canvas.itemcget(self.figura_jogador[1], "fill")
        cor_grade = self.canvas.itemcget(self.grade[linha][coluna][1], "fill")

        if cor_jogador == cor_grade:  # Se as cores forem iguais
            tipo_figura = self.figura_jogador[2]  # Tipo da figura do jogador
            self.exibir_nome_figura(tipo_figura)  # Exibe o nome da figura combinada

            # Remove ambas as figuras (do jogador e da grade)
            self.canvas.delete(self.grade[linha][coluna][0])  # Remove a bola
            self.canvas.delete(self.grade[linha][coluna][1])  # Remove a figura
            self.canvas.delete(self.figura_jogador[0])  # Remove a bola do jogador
            self.canvas.delete(self.figura_jogador[1])  # Remove a figura do jogador
            self.grade[linha][coluna] = None  # Liberta a célula na grade
        else:
            # Se as cores não forem iguais, tenta reposicionar a figura do jogador
            nova_linha, nova_coluna = self.encontrar_posicao_disponivel(linha, coluna)
            if nova_linha is not None:
                # Calcula a nova posição da célula disponível
                x, y = self.calcular_posicao_celula(nova_linha, nova_coluna)
                # Move a bola para a nova posição
                self.canvas.coords(
                    self.figura_jogador[0], x + 3, y + 3, x + TAMANHO_BOLA - 3, y + TAMANHO_BOLA - 3
                )
                # Remove a figura antiga e cria uma nova centralizada
                self.canvas.delete(self.figura_jogador[1])
                nova_figura = self.desenhar_figura_centralizada(x, y, self.figura_jogador[2], cor_jogador)
                # Atualiza a figura do jogador na nova posição
                self.figura_jogador = (self.figura_jogador[0], nova_figura, self.figura_jogador[2])
                self.grade[nova_linha][nova_coluna] = self.figura_jogador

        # Reseta o estado de movimento e cria uma nova figura para o jogador
        self.movendo = False
        self.figura_jogador = None
        self.criar_figura_jogador()

    def encontrar_posicao_disponivel(self, linha: int, coluna: int) -> Tuple[Optional[int], Optional[int]]:
        """
        Encontra a posição disponível mais próxima na grelha.
        """
        # Procura na mesma coluna para as linhas seguintes
        for l in range(linha + 1, LINHAS):
            if not self.grade[l][coluna]:  # Se a célula estiver vazia
                return l, coluna

        # Procura em colunas adjacentes
        for c in [coluna - 1, coluna + 1]:
            if 0 <= c < COLUNAS:  # Garante que a coluna está dentro dos limites
                for l in range(LINHAS):
                    if not self.grade[l][c]:  # Se a célula estiver vazia
                        return l, c

        return None, None  # Retorna (None, None) se não encontrar posição disponível
    
    def atualizar_linha_direcao(self, event: tk.Event) -> None:
        """
        Atualiza a linha de direção da figura do jogador com base na posição do rato.
        """
        if self.movendo:  # Se a figura está em movimento, não atualiza a linha
            return

        if self.linha_direcao:  # Remove a linha de direção anterior, se existir
            self.canvas.delete(self.linha_direcao)

        if self.figura_jogador is not None:
            # Obtém as coordenadas do centro da bola do jogador
            bola_coords = self.canvas.coords(self.figura_jogador[0])
            jogador_centro_x = (bola_coords[0] + bola_coords[2]) / 2
            jogador_centro_y = (bola_coords[1] + bola_coords[3]) / 2

            # A linha só é desenhada se o rato estiver acima da bola do jogador
            if event.y > jogador_centro_y:
                return

            # Cria uma linha de direção entre o centro da bola e a posição do rato
            self.linha_direcao = self.canvas.create_line(
                jogador_centro_x, jogador_centro_y, event.x, event.y, fill="gray", dash=(4, 2)
            )

    def exibir_nome_figura(self, nome_figura: str):
        """
        Exibe o nome da figura combinada no centro do canvas por 1 segundo.
        """
        # Cria o texto no centro do canvas
        texto = self.canvas.create_text(
            LARGURA // 2, ALTURA // 2,  # Coordenadas do centro
            text=nome_figura,
            font=("Helvetica", 24, "bold"),
            fill="black"  # Cor preta para o texto
        )
        # Remove o texto após 1 segundo
        self.canvas.after(1000, lambda: self.canvas.delete(texto))

    def disparar_figura(self, event: tk.Event) -> None:
        """
        Inicia o movimento da figura do jogador na direção do clique do rato.
        """
        if self.movendo or self.figura_jogador is None:  # Ignora se já está em movimento
            return

        # Obtém o centro da bola do jogador
        bola_coords = self.canvas.coords(self.figura_jogador[0])
        jogador_centro_x = (bola_coords[0] + bola_coords[2]) / 2
        jogador_centro_y = (bola_coords[1] + bola_coords[3]) / 2

        # O clique deve estar acima da bola do jogador para iniciar o movimento
        if event.y > jogador_centro_y:
            return

        # Calcula as componentes x e y da direção do disparo
        dx = (event.x - jogador_centro_x) / 30  # Divisão para suavizar a velocidade
        dy = (event.y - jogador_centro_y) / 30

        self.movendo = True  # Marca que a figura está em movimento
        self.mover_figura(dx, dy)  # Inicia o movimento

    def mover_figura(self, dx: float, dy: float) -> None:
        """
        Move a figura do jogador e verifica colisões ou limites do canvas.
        """
        if not self.movendo:  # Se não está em movimento, sai da função
            return

        for _ in range(5):  # Move a figura em pequenos incrementos para suavizar o movimento
            self.canvas.move(self.figura_jogador[0], dx / 5, dy / 5)  # Move a bola
            self.canvas.move(self.figura_jogador[1], dx / 5, dy / 5)  # Move a figura
            bola_coords = self.canvas.coords(self.figura_jogador[0])

            # Verifica colisões com as bordas do canvas
            if bola_coords[0] <= 0 or bola_coords[2] >= LARGURA:  # Borda esquerda/direita
                dx = -dx  # Inverte a direção horizontal

            # Verifica colisões com outras figuras na grade
            for linha in range(LINHAS):
                for coluna in range(COLUNAS):
                    if self.grade[linha][coluna]:  # Se a célula contém uma figura
                        figura, tipo = self.grade[linha][coluna][0:2]
                        figura_coords = self.canvas.coords(figura)
                        if self.colisao(bola_coords, figura_coords):  # Se houve colisão
                            self.tratar_colisao(linha, coluna)
                            return

            # Verifica se a bola atinge o topo do canvas
            if bola_coords[1] <= 0:
                self.movendo = False
                self.reposicionar_figura_jogador()
                return

        # Continua o movimento após um pequeno intervalo
        self.canvas.after(20, lambda: self.mover_figura(dx, dy))

    def colisao(self, bola_coords, figura_coords) -> bool:
        """
        Verifica se há colisão entre duas bolas.
        """
        # Calcula os centros das duas bolas
        bola_centro_x = (bola_coords[0] + bola_coords[2]) / 2
        bola_centro_y = (bola_coords[1] + bola_coords[3]) / 2

        figura_centro_x = (figura_coords[0] + figura_coords[2]) / 2
        figura_centro_y = (figura_coords[1] + figura_coords[3]) / 2

        # Calcula a distância entre os dois centros
        distancia = math.sqrt((bola_centro_x - figura_centro_x) ** 2 +
                              (bola_centro_y - figura_centro_y) ** 2)

        # Verifica se a distância é menor que o diâmetro da bola
        return distancia < TAMANHO_BOLA

    def reposicionar_figura_jogador(self) -> None:
        """
        Reposiciona a figura do jogador após atingir o topo ou terminar o movimento.
        """
        if self.figura_jogador:
            # Remove a figura antiga do canvas
            self.canvas.delete(self.figura_jogador[0])
            self.canvas.delete(self.figura_jogador[1])
        self.figura_jogador = None  # Reseta a referência da figura do jogador
        self.criar_figura_jogador()  # Cria uma nova figura
    
    def atualizar_texto_descricao(self, tipo_figura: str):
        """
        Atualiza o texto mostrado no canvas com a descrição da figura atual.
        """
        descricao = self.descricoes_figuras.get(tipo_figura, "")  # Obtém a descrição da figura
        if hasattr(self, "texto_descricao"):  # Se o texto já existir no canvas
            self.canvas.itemconfig(self.texto_descricao, text=descricao)  # Atualiza o texto
        else:  # Caso contrário, cria um novo texto no canvas
            self.texto_descricao = self.canvas.create_text(
                LARGURA - 115, ALTURA - 60,  # Coordenadas no canto inferior direito
                text=descricao,
                font=("Helvetica", 14, "italic"),
                fill="black",
            )


if __name__ == "__main__":
    """
    Código principal que inicializa o jogo e o menu inicial.
    """
    root = tk.Tk()  # Cria a janela principal do jogo

    def iniciar_jogo(nivel: int):
        """
        Callback para iniciar o jogo com o nível selecionado.
        """
        JogoBubbleShooter(root, nivel, voltar_menu)  # Cria a instância do jogo

    def voltar_menu():
        """
        Callback para retornar ao menu inicial.
        """
        MenuInicial(root, iniciar_jogo)  # Cria a instância do menu inicial

    voltar_menu()  # Inicializa o menu inicial
    root.mainloop()  # Inicia o loop principal da aplicação