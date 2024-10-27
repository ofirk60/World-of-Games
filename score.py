from utils import SCORES_FILE_NAME

POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5

def add_score(difficulty):
    score = 0
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            score = int(file.read().strip())
    except FileNotFoundError:
        score = 0
    except ValueError:
        score = 0

    new_score = score + POINTS_OF_WINNING(difficulty)

    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(new_score))
