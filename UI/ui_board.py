import tkinter as tk
from PIL import ImageGrab  # Necesario para capturar imagen de la ventana

class BoardGUI:
    def __init__(self, board):
        self.board = board
        self.root = tk.Tk()
        self.root.title("Quarto - Visualizador del Tablero")
        self.cell_size = 90

        # Canvas del tablero
        self.canvas = tk.Canvas(self.root, width=4*self.cell_size, height=4*self.cell_size)
        self.canvas.pack()

        # Leyenda debajo del tablero
        leyendas = [
            ("▼", "▲", "Bajo / Alto"),
            ("⚪", "⚫", "Claro / Oscuro"),
            ("■", "⭗", "Sólido / Hueco"),
            ("◼", "🔵", "Cuadrado / Redondo")
        ]

        legend_frame = tk.Frame(self.root)
        legend_frame.pack(pady=10)

        for simbolo1, simbolo2, texto in leyendas:
            fila = tk.Frame(legend_frame)
            fila.pack(anchor="w")
            etiqueta = tk.Label(fila, text=f"{simbolo1}  {simbolo2}  →  {texto}", font=("Arial", 12))
            etiqueta.pack()

        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        for i in range(4):
            for j in range(4):
                x0 = j * self.cell_size
                y0 = i * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="black")

                piece = self.board.grid[i][j]
                if piece:
                    self.canvas.create_text(
                        (x0 + x1) // 2,
                        (y0 + y1) // 2,
                        text=str(piece),
                        font=("Courier", 20),
                        anchor="center"
                    )

        self.root.update()

    def update(self, board):
        self.board = board
        self.draw_board()

    def export_to_png(self, filename):
        # Asegura que la ventana esté completamente actualizada
        self.root.update_idletasks()
        self.root.update()

        # Captura toda la ventana (canvas + leyendas)
        x = self.root.winfo_rootx()
        y = self.root.winfo_rooty()
        x1 = x + self.root.winfo_width()
        y1 = y + self.root.winfo_height()

        # Guarda la imagen como PNG
        ImageGrab.grab(bbox=(x, y, x1, y1)).save(filename)
        print(f"[INFO] Tablero completo exportado como imagen: {filename}")

    def show(self):
        self.root.mainloop()