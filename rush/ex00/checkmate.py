def checkmate(board):
    
    # Get rows        
    board_rows = [row.strip() for row in board.splitlines() if row.strip()]
    # print(board_rows)
    
    # Check King's position
    K_pos = ()
    for r_idx, row in enumerate(board_rows):
        for c_idx, piece in enumerate(row):
            if piece == "K":
                K_pos = (r_idx, c_idx)
                break
    # print(K_pos)
                
    # Checkmate
    for r_idx, row in enumerate(board_rows):
        for c_idx, piece in enumerate(row):
            # If Pawn
            if piece == "P":
                attack_directions = [
                    (r_idx-1, c_idx-1),
                    (r_idx-1, c_idx+1)
                ]
                
                if K_pos in attack_directions:
                    print("Success")
                    return
            elif piece == "B":
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
                            print("Success")         
                            return
                        current_row += dr
                        current_col += dc
            
            elif piece == "R":
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
                            print("Success") 
                            return        
                        current_row += dr
                        current_col += dc
                    
            elif piece == "Q":
                attack_directions = [
                    (-1, -1),
                    (-1, 1),
                    (1, -1),
                    (1, 1),
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1)
                ]             
                for dr, dc in attack_directions:
                    current_row, current_col = r_idx+dr, c_idx+dc   
                    while 0 <= current_row < len(board_rows) and 0 <= current_col < len(board_rows[0]):
                        if board_rows[current_row][current_col] == "K":
                            print("Success")
                            return
                        current_row += dr
                        current_col += dc
    
    print("Fail")