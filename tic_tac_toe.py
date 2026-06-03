def print_board(board):
    print()
    for row in range(3):
        cells = board[row * 3:(row + 1) * 3]
        print(" " + " | ".join(cells))
        if row < 2:
            print("---+---+---")
    print()


def winner(board):
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    ]

    for a, b, c in lines:
        if board[a] == board[b] == board[c] and board[a] in ("X", "O"):
            return board[a]

    if all(cell in ("X", "O") for cell in board):
        return "draw"

    return None


def ask_move(board, player):
    while True:
        move = input(f"Spieler {player}, waehle ein Feld (1-9): ").strip()

        if move.lower() in ("q", "quit", "exit"):
            return None

        if not move.isdigit():
            print("Bitte gib eine Zahl von 1 bis 9 ein.")
            continue

        index = int(move) - 1
        if index < 0 or index > 8:
            print("Die Zahl muss zwischen 1 und 9 liegen.")
            continue

        if board[index] in ("X", "O"):
            print("Dieses Feld ist schon belegt.")
            continue

        return index


def main():
    board = [str(i) for i in range(1, 10)]
    player = "X"

    print("Tic Tac Toe")
    print("Tippe q zum Beenden.")

    while True:
        print_board(board)
        move = ask_move(board, player)

        if move is None:
            print("Spiel beendet.")
            break

        board[move] = player
        result = winner(board)

        if result == "draw":
            print_board(board)
            print("Unentschieden!")
            break

        if result:
            print_board(board)
            print(f"Spieler {result} gewinnt!")
            break

        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    main()
