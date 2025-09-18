def checkmate(board):  
    # Get rows        
    board_rows = [row.strip() for row in board.splitlines() if row.strip()]
                
    # Checkmate
    is_checkmate = False
    for r_idx, row in enumerate(board_rows):
        for c_idx, piece in enumerate(row):
            if check_pawn(board_rows, piece, r_idx, c_idx) or \
                check_bishop(board_rows, piece, r_idx, c_idx) or \
                check_rook(board_rows, piece, r_idx, c_idx) or \
                check_queen(board_rows, piece, r_idx, c_idx):
                    print("Success")
                    is_checkmate = True
                    break
        if is_checkmate:
            break      
    if not is_checkmate:
        print("Fail")
 
def check_pawn(board_rows, piece, r_idx, c_idx):
    if piece == "P":
        attack_directions = [
            (-1, -1),
            (-1, 1)
        ]
        for dr, dc in attack_directions:
            current_row, current_col = r_idx+dr, c_idx+dc
            if 0 <= current_row < len(board_rows) and 0 <= current_col < len(board_rows[0]):
                if board_rows[current_row][current_col] == "K":
                    return True
    return False
        
def check_bishop(board_rows, piece, r_idx, c_idx):
    if piece == "B":
        attack_directions = [
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)
        ]             
        for dr, dc in attack_directions:
            current_row, current_col = r_idx+dr, c_idx+dc   
            while 0 <= current_row < len(board_rows) and 0 <= current_col < len(board_rows[0]):
                if board_rows[current_row][current_col] == "K":         
                    return True
                current_row += dr
                current_col += dc
    return False
                
def check_rook(board_rows, piece, r_idx, c_idx):
    if piece == "R":
        attack_directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]             
        for dr, dc in attack_directions:
            current_row, current_col = r_idx+dr, c_idx+dc   
            while 0 <= current_row < len(board_rows) and 0 <= current_col < len(board_rows[0]):
                if board_rows[current_row][current_col] == "K":        
                    return True
                current_row += dr
                current_col += dc
    return False
                
def check_queen(board_rows, piece, r_idx, c_idx):
    if piece == "Q":
        attack_directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)
        ]             
        for dr, dc in attack_directions:
            current_row, current_col = r_idx+dr, c_idx+dc   
            while 0 <= current_row < len(board_rows) and 0 <= current_col < len(board_rows[0]):
                if board_rows[current_row][current_col] == "K":        
                    return True
                current_row += dr
                current_col += dc
    return False 