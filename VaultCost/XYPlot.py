#from math import *

import matplotlib.pyplot as plt
import numpy as np
from pylab import figure,show,setp

#import pydot
#import pycallgraph

class plot:
    '''usage--->PLOTNAME=plot(seq1,seq2)
    '''
    def __init__(self,obj1,obj2):
        self.obj1=obj1
        self.obj2=obj2
        self.plot()
        
    def plot(self):
        fig=plt.figure()
        plt.ion()
        plt.plot(self.obj1,self.obj2)
        plt.grid(b='on', which='both')
        plt.autoscale(enable=True, axis='both', tight=None)
        
        def onclick(event):
            print(('button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(
            event.button, event.x, event.y, event.xdata, event.ydata)))
            
        cid = fig.canvas.mpl_connect('button_press_event', onclick)
        show()

def multilineplot():
    time = np.arange(0.0, 2.0, 0.01)
    s1 = [sin(2*pi*t) for t in time]
    s2 = [exp(-t) for t in time]
    s3 = [sin(2*pi*t)*exp(-t) for t in time]
    s4 = [sin(2*pi*t)*cos(4*pi*t) for t in time]
    fig = figure()
    t = np.arange(0.0, 2.0, 0.01)
    yprops = dict(rotation=0,horizontalalignment='right',
                  verticalalignment='center',x=-0.01)
    axprops = dict(yticks=[])
    ax1 =fig.add_axes([0.1, 0.7, 0.8, 0.2], **axprops)
    ax1.plot(t, s1)
    ax1.set_ylabel('S1', **yprops)
    axprops['sharex'] = ax1
    axprops['sharey'] = ax1
    #force x axes to remain in register, even with toolbar navigation
    ax2 = fig.add_axes([0.1, 0.5, 0.8, 0.2], **axprops)
    ax2.plot(t, s2)
    ax2.set_ylabel('S2', **yprops)
    ax3 = fig.add_axes([0.1, 0.3, 0.8, 0.2], **axprops)
    ax3.plot(t, s4)
    ax3.set_ylabel('S3', **yprops)
    ax4 = fig.add_axes([0.1, 0.1, 0.8, 0.2], **axprops)
    ax4.plot(t, s4)
    ax4.set_ylabel('S4', **yprops)
    # turn off x ticklabels for all but the lower axes
    for ax in ax1, ax2, ax3:
        setp(ax.get_xticklabels(), visible=False)
    show()
    
def iplot(seq1,seq2):
    '''plots seq1 vs seq2; usage--->iplot(seq1,seq2)'''
    plt.plot(seq1,seq2)
    plt.grid(b='on', which='both')
    plt.autoscale(enable=True, axis='both', tight=None)
    plt.show()
        
    def onclick(event):
        print(('button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(
        event.button, event.x, event.y, event.xdata, event.ydata)))

if __name__=='__main__':
    #pycallgraph.start_trace()
    #graph=pydot.Dot(graph_type='graph')
    #multilineplot()
    
    xaxis=np.linspace(0, 175,20)
    y=[80*(x**-.02) for x in xaxis]
    y2=[x for x in xaxis]
    #print xaxis
    xaxis=[0,4]
    y=[0,4800]

    iplot(xaxis,y)
    #plot(xaxis,y2)
    show()
   # pycallgraph.stop_trace()    
    #pycallgraph.make_dot_graph('test.png')
    