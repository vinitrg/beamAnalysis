from .PointLoad import PointLoads

class BeamAnalysis:
    def calcReactions(loadIntensity, a, length):
        rightReactions = 0
        leftReactions = 0.2
        for index in range(0,len(loadIntensity)):
            rightReaction = loadIntensity[index]*a[index] / length
            leftReaction = loadIntensity[index] - rightReaction
            rightReactions += rightReaction
            leftReactions += leftReaction
        return(leftReactions,rightReactions)