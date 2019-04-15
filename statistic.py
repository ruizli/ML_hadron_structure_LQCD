import pandas as pd
import matplotlib.pyplot as mplot
import seaborn as sbn

class Dataframe:
    def __init__(self, data, xl='X', yl='Y'):
        self.nx = int(len(data[xl])/len(data[yl]))
        self.ndata = len(data[yl])
        self.data = pd.DataFrame(data['X'].reshape(self.ndata, self.nx), 
                                 columns=list(['X-'+str(i) for i in range(self.nx)]))
#        self.data.assign(Y=data[yl])
        self.data.insert(self.nx, 'Y', data[yl])
#        print(self.data)
        self.block = 1
        
    def autocorr(self, tol):
        assert(1.>tol>0.)
        at = 1.0
        block = 0
        while at > tol:
            if block > 0:
                block += int((at-tol)*5+1)
            else:
                block = 1
            at = 0.
            for i in range(self.nx):
                atn = pd.Series(self.data['X-'+str(i)].to_dict()).autocorr(self.block)
                if atn > at: 
                    at = atn
        return block, at    
                                 
    def blockdata(self, blk):
        if blk > 1:
            self.data = pd.DataFrame(np.ndarray([self.data.iloc[i:i+blk,:].mean().to_dict('list') 
                                             for i in range(0, self.ndata, blk)]).reshape(int(self.ndata/blk), self.nx+1), 
                                columns=list(['X-'+str(i) for i in range(self.nx)]).append('Y'))
        self.block = blk
        return
    
    def hist(self, out = None):
        fig, axis = mplot.subplots()
        axis.hist(self.data, subplots=True, title='Data(X Y) histgram')
        mplot.show()
        #self.data.plot.hist(subplots=True, title='Data(X Y) histgram')
        if out != None:
            #self.data.get_figure().savefig(out)
            mplot.savefig(out)
        self.data.plot.density()
     #   mplot.show()
        return
    
    def covplot(self, out = None):
        corrl = self.data.corr()
   #     corrl.plot.hexbin(x=corrl[0], y=corrl[1])
        sbn.heatmap(corrl, xticklabels=corrl.columns, yticklabels=corrl.columns, cmap=sbn.diverging_palette(220, self.nx+1, as_cmap=True))
        mplot.show()
        if out != None:
            corrl.get_figure().savefig(out)
        return
    
