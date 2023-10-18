import random

create_board = lambda width, height: [['-' for _ in range(width)] for _ in range(height)]

display_board = lambda board: [print(' '.join(row)) for row in board]

def generate_positions(width, height):
    for _ in range(3):
        yield (random.randint(0, height - 1), random.randint(0, width - 1))

def setup_board(width, height, create_board, generate_positions):
    board = create_board(width, height)
    player_pos, goal_pos = generate_positions(width, height), generate_positions(width, height)

    try:
        player_y, player_x = next(player_pos)
        goal_y, goal_x = next(goal_pos)

        board[player_y][player_x] = 'A'
        board[goal_y][goal_x] = 'O'

        return board, player_y, player_x, goal_y, goal_x

    except StopIteration:
        return None

def check_game_result(player_y, player_x, goal_y, goal_x):
    return player_y == goal_y and player_x == goal_x

def play_game(width, height, setup_board, display_board, check_game_result, create_board, generate_positions):
    while True:
        max_attempts = 3
        for _ in range(max_attempts):
            board, player_y, player_x, goal_y, goal_x = setup_board(width, height, create_board, generate_positions)

            if board is not None:
                print("\nNew board generated")
                display_board(board)

                generate_again = input("Generate new positions? (Y/N): ").lower()
                if generate_again == 'n':
                    break
            else:
                print("Failed to generate positions. Please try again.")
        
        if max_attempts <= 0:
            print("Failed to generate positions three times. Exiting the game.")
            break

        while True:
            moves = input("Enter your moves (WASD): ").lower()

            for move in moves:
                if move == 'w':
                    if player_y > 0:
                        board[player_y][player_x] = '-'
                        player_y -= 1
                elif move == 'a':
                    if player_x > 0:
                        board[player_y][player_x] = '-'
                        player_x -= 1
                elif move == 's':
                    if player_y < height - 1:
                        board[player_y][player_x] = '-'
                        player_y += 1
                elif move == 'd':
                    if player_x < width - 1:
                        board[player_y][player_x] = '-'
                        player_x += 1
                else:
                    print("Invalid move! Use WASD to move.")
                    continue

                board[player_y][player_x] = 'A'
                print("\n")
                display_board(board)

                if check_game_result(player_y, player_x, goal_y, goal_x):
                    print("You win!")
                    break

            if not check_game_result(player_y, player_x, goal_y, goal_x):
                print("You lose!")

            generate_again = input("Continue the game? (Y/N): ").lower()
            if generate_again != 'y':
                return

def main(play_game, setup_board, display_board, check_game_result, create_board, generate_positions):
    print("~~ Selamat datang di permainan board game pemrograman fungsional ~~")
    print("Anda (A) dapat berjalan secara horizontal dan vertikal untuk menuju target (O)")
    print("Gunakan keyboard WASD untuk bergerak")
    print("-------------------------------")
    print("~~Selamat bermain ~~")

    width = int(input("Enter the board width: "))
    height = int(input("Enter the board height: "))

    while True:
        play_game(width, height, setup_board, display_board, check_game_result, create_board, generate_positions)
        menu = input("Leave the game? (Y/N): ").lower()
        if menu == 'y':
            print("See you!")
            break

if __name__ == "__main__":
    main(play_game, setup_board, display_board, check_game_result, create_board, generate_positions)