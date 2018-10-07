import matplotlib.pyplot as plt

class LoadingDiagram:
    def __init__(self,normalisedValue):
        self.NormalisedValue = normalisedValue        
  
    def DrawBoundingBox(self,axes, beamLength):
        leftBoundLim = -1*beamLength*0.2
        rightBoundLim = beamLength*1.2
        axes.set_xlim(leftBoundLim,rightBoundLim)
        axes.set_ylim(-12,12)
        axes.set_xticks([])
        axes.set_yticks([])
        axes.set_xlabel("Loading on this Beam",fontsize=24)
    
    def DrawSpan(self,axes,beamLength):
        lineWidth = 1
        axes.hlines(y=0, xmin=0, xmax=beamLength, linewidth=lineWidth, color='black')
        axes.text(0.4*beamLength,-1.2*lineWidth,"Length = "+str(beamLength))

    def DrawLoadsAndReactions(self,axes, load, dist, isReaction):
        arrowHeadLength = 9*self.NormalisedValue
        for loadIndex in range(0,len(load)):
            color = 'm'
            x = dist[loadIndex]
            dx = 0
            y = load[loadIndex]*self.NormalisedValue
            dy = -load[loadIndex]*self.NormalisedValue + arrowHeadLength
            text_y = y+arrowHeadLength
            text_x = x-arrowHeadLength
            if isReaction:
                color = 'b'
                x = dist[loadIndex]
                dx = 0
                y = -1*load[loadIndex]*self.NormalisedValue
                dy = load[loadIndex]*self.NormalisedValue - arrowHeadLength
                text_y = y-arrowHeadLength*2
            
            axes.arrow(x, y, dx, dy, head_width=1.0, head_length=arrowHeadLength, fc=color, ec=color)
            axes.text(text_x,text_y,str(load[loadIndex]))