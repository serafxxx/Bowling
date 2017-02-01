
class BowlingException(Exception):
    """Exception class to raise exceptions in our bowling function"""
    pass


def safe_list_get(l, i, default=0):
    """Return default and do not throw in case of IndexError"""
    try:
        return l[i]
    except IndexError:
        return default


def count_bowling_score(rolls):
    """
    Count total for the bowling game.
    Function accepts list of scores. No frames separation and
    no strike/spare designation needed. Just bowled pins amount
    with each roll.
    Will proceed not finished game (not enough scores passed)
    in regular way. Will ignore redundant rolls.
    Will trow BowlingException in case of inconsistent data.
    :param rolls: List of scores (integers)
    :return: Final score
    """
    score = 0
    frame_index = 0
    next_frame_start = 0
    for i in range(len(rolls)):
        if i != next_frame_start:
            # Skip rolls up to the next frame
            continue

        # Increase frame index.
        frame_index += 1
        # Current score
        roll = rolls[i]

        if frame_index > 10:
            # Game finished. Ignoring the rest of the passed rolls
            return score

        if roll < 0 or roll > 10:
            # Impossible score per one roll
            raise BowlingException('Wrong roll score')

        if roll == 10:
            # Strike!
            score += 10 + safe_list_get(rolls, i+1) + safe_list_get(rolls, i+2)
            # No second roll in the frame. So next frame will start on the next roll
            next_frame_start = i+1

        else:
            if roll + rolls[i+1] < 0 or roll + rolls[i+1] > 10:
                raise BowlingException('Wrong roll score')
            elif roll + safe_list_get(rolls, i+1) == 10:
                # Spare!
                score += 10 + safe_list_get(rolls, i+2)
            else:
                score += roll + safe_list_get(rolls, i+1)

            next_frame_start = i + 2

    return score
