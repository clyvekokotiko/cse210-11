class Score:
    """
    Description Coming soon!
    """
    def calculateLevelAndFallFreq(score):
        # Based on the score, return the level the player is on and
        # how many seconds pass until a falling piece falls one space.
        level = int(score / 10) + 1
        fallFreq = 0.27 - (level * 0.02)
        return level, fallFreq
