
import random

def rock_paper_scissors():
    choices = ['taş', 'kağıt', 'makas']

    while True:
        user_choice = input("Taş, Kağıt veya Makas? (Çıkmak için 'q' tuşuna basın): ").lower()
        if user_choice == 'q':
            print("Oyun sonlandırıldı.")
            break
        if user_choice not in choices:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
            continue

        computer_choice = random.choice(choices)

        print(f"Senin seçimin: {user_choice}")
        print(f"Bilgisayarın seçimi: {computer_choice}")

        if user_choice == computer_choice:
            print("Berabere! Tekrar deneyin.")
        elif (user_choice == 'taş' and computer_choice == 'makas') or \
             (user_choice == 'kağıt' and computer_choice == 'taş') or \
             (user_choice == 'makas' and computer_choice == 'kağıt'):
            print("Tebrikler! Kazandınız.")
        else:
            print("Üzgünüm! Kaybettiniz.")

def minesweeper():
    BOARD_WIDTH = 10
    BOARD_HEIGHT = 10
    NUM_MINES = 10
    board = [[0 for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]
    mines = set()
    while len(mines) < NUM_MINES:
        x = random.randint(0, BOARD_WIDTH - 1)
        y = random.randint(0, BOARD_HEIGHT - 1)
        if board[y][x] == 0:
            board[y][x] = "X"
            mines.add((x, y))

    def get_guess():
        while True:
            try:
                x, y = map(int, input("Tahmin etmek istediğiniz koordinatları girin (örneğin: 2,3): ").split(","))
                if x < 0 or x >= BOARD_WIDTH or y < 0 or y >= BOARD_HEIGHT:
                    print("Girdiğiniz koordinatlar tahtanın dışında kaldı. Lütfen tekrar deneyin.")
                    continue
                return x, y
            except ValueError:
                print("Geçersiz koordinat. Lütfen tekrar deneyin.")

    def print_board(board, show_mines=False):
        print("  " + " ".join(str(x) for x in range(BOARD_WIDTH)))
        for i in range(BOARD_HEIGHT):
            row = ""
            for j in range(BOARD_WIDTH):
                if board[i][j] == "X" and show_mines:
                    row += "X"
                elif board[i][j] == 0:
                    row += "-"
                else:
                    row += str(board[i][j])
            print(str(i) + " " + row)

    def count_adjacent_mines(x, y):
        count = 0
        for i in range(max(0, y - 1), min(BOARD_HEIGHT, y + 2)):
            for j in range(max(0, x - 1), min(BOARD_WIDTH, x + 2)):
                if board[i][j] == "X":
                    count += 1
        return count

    def check_win():
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                if board[i][j] == 0:
                    return False
        return True

    def play_game():
        print("Mayın Tarlası oyununa hoş geldiniz!")
        print_board(board)
        while True:
            x, y = get_guess()
            if board[y][x] == "X":
                print("Oyun bitti! Mayına bastınız.")
                print_board(board, show_mines=True)
                break
            else:
                adjacent_mines = count_adjacent_mines(x, y)
                board[y][x] = adjacent_mines
                print_board(board)
                if check_win():
                    print("Tebrikler, oyunu kazandınız!")
                    break

    play_game()

def hangman():
    try:
        from termcolor import cprint
    except ImportError:
        def cprint(*args, **kwargs):
            print(*args)

    kelimeler = ["vantilatör", "adaptör", "kalem", "fare", "telefon", "kulaklık", "pervane", "merdane", "kestane"]

    def oyun_hazirlik():
        global secilen_kelime, gorunen_kelime, can
        secilen_kelime = random.choice(kelimeler)
        gorunen_kelime = ["-"] * len(secilen_kelime)
        can = 5

    def harf_al():
        devam = True
        while devam:
            harf = input("Bir harf giriniz: ")
            if harf.lower() == "quit":
                cprint("Gidiyor gönlümün efendisi...", color="red", on_color="on_blue")
                exit()
            elif len(harf) == 1 and harf.isalpha() and harf not in gorunen_kelime:
                devam = False
            else:
                cprint("Hatalı Giriş", color="red", on_color="on_grey")
        return harf.lower()

    def oyun_dongusu():
        global gorunen_kelime, can
        while can > 0 and "-" in gorunen_kelime:
            print("Kelime:", " ".join(gorunen_kelime))
            print(f"Kalan Can: {can}")
            tahmin = harf_al()
            if tahmin in secilen_kelime:
                for index, harf in enumerate(secilen_kelime):
                    if harf == tahmin:
                        gorunen_kelime[index] = tahmin
            else:
                can -= 1
                cprint(f"Yanlış tahmin! Kalan can: {can}", color="red", on_color="on_grey")
        if "-" not in gorunen_kelime:
            cprint("Tebrikler! Kelimeyi doğru tahmin ettiniz: " + secilen_kelime, color="green", on_color="on_grey")
        else:
            print("Oyunu kaybettiniz!")
