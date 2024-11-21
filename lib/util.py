
# PLEASE TRY USING THIS FORMAT FOR THE CALCULATION FUNCTIONS SO ITS EASY TO READ IM TALKING TO YOU TATSUMI AND ONLY CALCULATION FUNCTIONS ALLOWED HERE OR ELSE GET OUT !
# nah fuck that 


def calculate_winrate(win_count, total_games):
    """
    Calculates the win rate based on the number of wins and total games played.

    Parameters:
    win_count (int): Number of games won
    total_games (int): Total number of games played

    Returns:
    int: Win rate percentage rounded to an integer
    """
    if total_games > 0:
        win_rate = (win_count / total_games) * 100
        return int(win_rate)
    else:
        raise ValueError("Total games must be greater than zero")
