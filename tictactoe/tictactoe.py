# ***************************
# Já adiantando, 
# esses prints foram gerados com IA, ninguém merece né?
# tamo junto.
# ***************************

import random
import time
import os
from log import GameLogger

# ==========================================
# CONFIGURAÇÕES VISUAIS
# ==========================================
class Cores:
    RESET = '\033[0m'
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AZUL = '\033[94m'
    AMARELO = '\033[93m'
    NEGRITO = '\033[1m'

class TicTacToe:
    def __init__(self):
        self.arr = [["", "", ""] for _ in range(3)]
        self.current_player = "X"

    def show(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"{Cores.AMARELO}{Cores.NEGRITO}")
        print("="*30)
        print("   JOGO DA VELHA - IA MINIMAX")
        print("="*30)
        print(f"{Cores.RESET}\n")

        print("       0   1   2")
        
        for i, linha in enumerate(self.arr):
            row_str = []
            for cell in linha:
                if cell == "X":
                    row_str.append(f"{Cores.AZUL} X {Cores.RESET}")
                elif cell == "O":
                    row_str.append(f"{Cores.VERMELHO} O {Cores.RESET}")
                else:
                    row_str.append("   ")
            
            print(f"  {i}  " + "|".join(row_str))
            
            if i < 2:
                print("     ---+---+---")
        print("\n")

    def append(self, row, col):
        if not (0 <= row < 3 and 0 <= col < 3):
            print(f"{Cores.VERMELHO}❌ Posição inválida! Tente novamente.{Cores.RESET}")
            time.sleep(1) 
            return False
        if self.arr[row][col] != "":
            print(f"{Cores.VERMELHO}❌ Posição ocupada! Tente novamente.{Cores.RESET}")
            time.sleep(1)
            return False
        self.arr[row][col] = self.current_player
        return True

    def check_winner(self):
        lines = []
        lines.extend(self.arr) 
        lines.extend([[self.arr[r][c] for r in range(3)] for c in range(3)]) 
        lines.append([self.arr[i][i] for i in range(3)]) 
        lines.append([self.arr[i][2 - i] for i in range(3)]) 

        for line in lines:
            if line[0] != "" and all(cell == line[0] for cell in line):
                return line[0]
        return None

    def is_draw(self):
        return all(cell != "" for row in self.arr for cell in row)

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

def minimax(current_player, ia_type, depth=0, alpha=float("-inf"), beta=float("inf")):
    winner = game.check_winner()
    if winner:
        if winner == ia_type:
            return 10 - depth
        else:
            return -10 + depth
            
    if game.is_draw():
        return 0
    
    if current_player == ia_type:
        best_score = float("-inf")
        for i in range(3):
            for j in range(3):
                if game.arr[i][j] == "":
                    game.arr[i][j] = current_player
                    other_player = "O" if current_player == "X" else "X"
                    
                    score = minimax(other_player, ia_type, depth + 1, alpha, beta) 
                    game.arr[i][j] = "" 
                    
                    best_score = max(best_score, score)
                    alpha = max(alpha, score)
                    
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if game.arr[i][j] == "":
                    game.arr[i][j] = current_player
                    other_player = "O" if current_player == "X" else "X"
                    
                    score = minimax(other_player, ia_type, depth + 1, alpha, beta)
                    game.arr[i][j] = "" 
                    
                    best_score = min(best_score, score)
                    beta = min(beta, score)
                        
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
                    
    return best_score

# ==========================================
# LOOP PRINCIPAL
# ==========================================
game = TicTacToe()
logger = GameLogger()
options = ["X", "O"]

os.system('cls' if os.name == 'nt' else 'clear')
print(f"{Cores.NEGRITO}Sorteando quem começa...{Cores.RESET}")
time.sleep(1.5)

ia_type = random.choice(options) 
human_type = "O" if ia_type == "X" else "X"

print(f"🤖 A IA jogará com: {Cores.AZUL if ia_type == 'X' else Cores.VERMELHO}{ia_type}{Cores.RESET}")
print(f"👤 Você jogará com: {Cores.AZUL if human_type == 'X' else Cores.VERMELHO}{human_type}{Cores.RESET}")
time.sleep(2)

while True:
    game.show()
    
    if game.current_player == "X":
        cor_jogador = Cores.AZUL
    else:
        cor_jogador = Cores.VERMELHO
        
    print(f"🎮 Vez de: {cor_jogador}{game.current_player}{Cores.RESET}")

    if game.current_player == ia_type:
        melhor_pontuacao = float("-inf")
        melhor_jogada = None
        
        for i in range(3):
            for j in range(3):
                if game.arr[i][j] == "":
                    game.arr[i][j] = ia_type
                    oponente = "O" if ia_type == "X" else "X"
                    score = minimax(oponente, ia_type)
                    game.arr[i][j] = "" 
                    
                    if score > melhor_pontuacao:
                        melhor_pontuacao = score
                        melhor_jogada = (i, j)
        
        if melhor_jogada:
            game.append(melhor_jogada[0], melhor_jogada[1])
            logger.move(game.arr, game.current_player, melhor_jogada) 

    else:
        try:
            print("Digite a posição (Ex: 0 Enter 2 Enter para canto superior direito)")
            row_input = input("Linha (0, 1, 2): ")
            if not row_input.isdigit(): raise ValueError
            
            col_input = input("Coluna (0, 1, 2): ")
            if not col_input.isdigit(): raise ValueError
            
            row = int(row_input)
            col = int(col_input)
            
        except ValueError:
            print(f"{Cores.VERMELHO}❌ Entrada inválida! Digite apenas números.{Cores.RESET}")
            time.sleep(1)
            continue

        if not game.append(row, col):
            continue
            
        logger.move(game.arr, game.current_player, (row, col))

    winner = game.check_winner()
    if winner:
        game.show()
        if winner == ia_type:
            print(f"{Cores.VERMELHO}{Cores.NEGRITO}🤖 A IA (Minimax) VENCEU! Eu sou inevitável.{Cores.RESET}")
        else:
            print(f"{Cores.VERDE}{Cores.NEGRITO}🏆 VOCÊ VENCEU! (Isso não deveria acontecer...){Cores.RESET}")
        
        logger.save_game(winner)
        break

    if game.is_draw():
        game.show()
        print(f"{Cores.AMARELO}{Cores.NEGRITO}🤝 EMPATE! (Como esperado contra o Minimax){Cores.RESET}")
        
        logger.save_game(None)
        break

    game.switch_player()

print("\nFim de jogo. Pressione Enter para sair.")
input()