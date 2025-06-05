from Game.game_state import GameState
from UI.human_player import HumanPlayer
from Agent.minimax_agent import MinimaxAgent
from UI.display import print_board
from UI.ui_board import BoardGUI  
from Game.utils import generate_all_pieces 
import time
import datetime  # Para incluir fecha y hora en el nombre del archivo PNG

def main():
    print("Bienvenido a Quarto IA")

    # Verificar cuántas piezas se generan y mostrarlas
    piezas = generate_all_pieces()
    print(f"\n[DEBUG] Total de piezas generadas: {len(piezas)}")
    for i, pieza in enumerate(piezas):
        print(f"{i}: {pieza}")

    state = GameState()
    human = HumanPlayer("Jugador Humano")
    ai = MinimaxAgent("Agente IA")

    current_player = human
    next_piece = state.available_pieces[0] 

    gui = BoardGUI(state.board)  

    move_count = 0
    ai_times = []

    while not state.is_game_over():
        print_board(state.board)
        gui.update(state.board)  
        print(f"\nTurno de {current_player.name}")
        print(f"Te ha tocado la pieza: {next_piece}")

        if current_player == human:
            move = human.choose_move(state, next_piece)
            state.play_move(move)
            move_count += 1  # contar movimiento del humano

            next_piece = human.choose_piece(state)
            current_player = ai
        else:
            start_time = time.time()
            move = ai.choose_move(state, next_piece)
            end_time = time.time()

            elapsed = end_time - start_time
            ai_times.append(elapsed)

            print(f"Agente coloca pieza en: {move}")
            state.play_move(move)
            move_count += 1  # contar movimiento del agente

            next_piece = ai.choose_piece(state)
            print(f"Agente entrega pieza: {next_piece}")
            current_player = human

    print_board(state.board)
    gui.update(state.board)

    # Exportar la imagen del tablero final con timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"tablero_final_{timestamp}.png"
    gui.export_to_png(filename)

    print("¡Quarto!")
    winner = state.get_winner()
    if winner:
        print(f"Ganador: {winner}")
    else:
        print("Empate.")
    
    # Mostrar estadísticas
    print(f"\n--- Estadísticas de la partida ---")
    print(f"Total de movimientos realizados: {move_count}")
    if ai_times:
        avg_ai_time = sum(ai_times) / len(ai_times)
        print(f"Tiempo medio de decisión del Agente IA: {avg_ai_time:.4f} segundos")
    else:
        print("El agente no hizo movimientos.")

    gui.show()  

if __name__ == "__main__":
    main()