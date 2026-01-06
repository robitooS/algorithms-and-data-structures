import json
import os

class GameLogger:
    def __init__(self, log_name="game_data.json"):
        # Define o nome da pasta
        folder_name = "tictactoe"
        
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            
        self.filename = os.path.join(folder_name, log_name)
        
        self.reset()
    
    def reset(self) -> None:
        self.history = []
    
    def convert_board(self, board_2d, player) -> list:
        """
        Converte o tabuleiro 2D para 1D
        1 -> PLAYER (Eu)
        0 -> NONE (Vazio)
        -1 -> ENEMY (Oponente)
        """
        board_1d = []
        
        for row in board_2d:
            for cell in row:
                if cell == "":
                    board_1d.append(0)
                elif cell == player:
                    board_1d.append(1)
                else:
                    board_1d.append(-1)
        return board_1d
                
    def move(self, board, player, move) -> None:
        num_board = self.convert_board(board, player)
        
        self.history.append({
            "player": player,
            "board": num_board,
            "move": move
        })
        
    def save_game(self, winner):
        data_to_save = []

        for entry in self.history:
            result = 0 # Default: Draw
            
            if winner is not None:
                if entry["player"] == winner:
                    result = 1
                else:
                    result = -1 
            
            record = {
                "features": entry["board"], 
                "label": entry["move"],     
                "reward": result            
            }
            data_to_save.append(record)

        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                try:
                    existing_data = json.load(f)
                except json.JSONDecodeError:
                    existing_data = []
        else:
            existing_data = []

        existing_data.extend(data_to_save)

        with open(self.filename, "w") as f:
            json.dump(existing_data, f, indent=4) 
        
        full_path = os.path.abspath(self.filename)
        print(f"💾 Jogo salvo em:\n   -> {full_path}")
        print(f"   -> {len(data_to_save)} jogadas registradas.")