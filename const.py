from variables import *


fen_starting_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
file_names = ["a","b","c","d","e","f","g","h"]
rank_names = ["1","2","3","4","5","6","7","8"]

""" squares = [
    A1, B1, C1, D1, E1, F1, G1, H1,
    A2, B2, C2, D2, E2, F2, G2, H2,
    A3, B3, C3, D3, E3, F3, G3, H3,
    A4, B4, C4, D4, E4, F4, G4, H4,
    A5, B5, C5, D5, E5, F5, G5, H5,
    A6, B6, C6, D6, E6, F6, G6, H6,
    A7, B7, C7, D7, E7, F7, G7, H7,
    A8, B8, C8, D8, E8, F8, G8, H8,
    ] """

pieces = ["pawn", "rook", "knight", "bishop", "queen", "king"]

top_position = []
bottom_position = []
white = "White"
black = "Black"

#Center text
def text_center(font, text, text_color, y):
    text_surface = font.render(text, True, text_color)
    component_width = text_surface.get_width()
    screen.blit(text_surface, (800 + (400 - component_width) // 2, y))

#Text class
def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

#Mouse position
def mouse_pos():
    mouse_pos = pygame.mouse.get_pos()
    mouse_text = f"Mouse X: {mouse_pos[0]}, Y: {mouse_pos[1]}"
    draw_text(mouse_text, "Black", width // 2, height - 50)

    return mouse_pos[0], mouse_pos[1]

#First windows
def startup_window(width_box, height_box, heading_text, paragraph_text):
    x = (width - width_box) // 2
    y = (height - height_box) // 2
    
    #Background
    for i in range(32):
        tile = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, "Light gray", (0 + (tile * 300), row*125, 150, 125))
        else:
            pygame.draw.rect(screen, "Light gray", (150 + (tile * 300), row*125, 150, 125))


    # Draw box
    pygame.draw.rect(screen, "Light gray", (x, y, width_box, height_box))
    pygame.draw.rect(screen, "Black", (x, y, width_box, height_box), 5) 
    # Draw heading
    heading_surface = big_font.render(heading_text, True, (0, 0, 0))
    heading_rect = heading_surface.get_rect(center=(width // 2, y + 100))
    screen.blit(heading_surface, heading_rect)

    # Draw paragraph
    paragraph_surface = font.render(paragraph_text, True, (0, 0, 0))
    paragraph_rect = paragraph_surface.get_rect(center=(width // 2, y + 200))
    screen.blit(paragraph_surface, paragraph_rect)


    draw_text(white, "Black", width // 2 - 100, y + 300)
    draw_text(black, "Black", width // 2 + 100, y + 300)


    mouse_x, mouse_y = mouse_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if y + 280 < mouse_y < y + 320:
                if x + 250 < mouse_x < x + 350:
                    return "white"
                if x + 450 < mouse_x < x + 550:
                    return "black"

#Chess board                
def draw_board(choice):
    if choice == "black":   
        
         # Draw chessboard squares
        for i in range(32):
            tile = i % 4
            row = i // 4
            if row % 2 == 0:
                pygame.draw.rect(screen, "light gray", [75 + (tile * 200), 100 + row * 100, 100, 100])
            else:
                pygame.draw.rect(screen, "light gray", [175 + (tile * 200), 100 + row * 100, 100, 100])
        
        index = 0
        # Draw file names (columns) in reverse order
        for i in range(len(file_names) -1 ,-1,-1):
            draw_text(file_names[i], "Black", 125 + index * 100, 940)  # Adjust position as needed
            index += 1

        # Draw rank names (rows)
        for i in range(len(rank_names)):
            draw_text(rank_names[i], "Black", 40, 160 + i * 100)  # Adjust position as needed
    
    else:
        # Draw chessboard squares
        for i in range(32):
            tile = i % 4
            row = i // 4
            if row % 2 == 0:
                pygame.draw.rect(screen, "light gray", [175 + (tile * 200), 100 + row * 100, 100, 100])
            else:
                pygame.draw.rect(screen, "light gray", [75 + (tile * 200), 100 + row * 100, 100, 100])

        # Draw file names (columns)
        for i in range(len(file_names)):
            draw_text(file_names[i], "Black", 125 + i * 100, 940)  # Adjust position as needed
        index = 0

        # Draw rank names (rows) in reverse order
        for i in range(len(rank_names) -1, -1, -1):
            draw_text(rank_names[i], "Black", 40, 160 + index * 100)  # Adjust position as needed
            index += 1
    
    pygame.draw.rect(screen, "Black", [75, 100, 800, 800], 3)
    # Sidebar
    opponent = "black" if choice == "white" else "white"
    draw_text(opponent, "black", 400, 50)
    pygame.draw.rect(screen, "white", [925, 0, 400, height], 5)

    piece_text = "QxF5"  # Replace with your piece text
    text_center(big_font, piece_text, "black", 400)

square_size = min(100, 100)
piece_size = square_size // 2

def draw_pieces(choice):
    rows = fen_starting_position.split('/')
    if choice == "white":
        for row_idx, row in enumerate(rows):
            col_idx = 0
            for char in row:
                if char.isdigit():
                    col_idx += int(char)
                else:
                    piece_text = char.upper()  # Use the piece letter
                    piece_font = pygame.font.Font(None, piece_size)  # Use None to use default font
                    piece_surface = piece_font.render(piece_text, True, "Black")  # Render text surface
                    screen.blit(piece_surface, (75 + (col_idx * square_size + square_size // 4), 125 + (row_idx * square_size + square_size // 4)))  # Adjust position for centering
                    col_idx += 1
    else:
        
