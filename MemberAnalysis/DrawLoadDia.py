import matplotlib.pyplot as plt

class LoadingDiagram:
    def __init__(self,normalisedValue):
        self.NormalisedValue = normalisedValue
        
  
    def DrawBoundingBox(self,ax, beamLength,load):
        leftBoundLim = -1*beamLength*0.2
        rightBoundLim = beamLength*1.2
        bottomBoundLim = -1.2*load*self.NormalisedValue
        topBoundLim = load*self.NormalisedValue*1.2
        ax.set_xlim(leftBoundLim,rightBoundLim)
        ax.set_ylim(bottomBoundLim,topBoundLim)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlabel("Loading on this Beam",fontsize=24)
    
    def DrawSpan(self,ax,beamLength):
        lineWidth = 1
        ax.hlines(y=0, xmin=0, xmax=beamLength, linewidth=lineWidth, color='black')
        ax.text(0.4*beamLength,-1.2*lineWidth,"Length = "+str(beamLength))

    def DrawLoadsAndReactions(self,ax, dist, load, isReaction):
        arrowHeadLength = 9*self.NormalisedValue
        for loadIndex in range(0,len(dist)):
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
            
            ax.arrow(x, y, dx, dy, head_width=1.0, head_length=arrowHeadLength, fc=color, ec=color)
            ax.text(text_x,text_y,str(load[loadIndex]))
        
