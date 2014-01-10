###############################################################
#figure plotting fuctions
###############################################################

from helper import *
import cStringIO
from pylab import *
import numpy
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

def setPlot(ax, title='Title', xlab='Vuosi', ylab='Pisteet', dataX=[], dataY=[]):
    if title: ax.set_title(title)
    if xlab: ax.set_xlabel(xlab)
    if ylab: ax.set_ylabel(ylab)
    ax.plot(dataX, dataY)

def plot(title0='Title', title1='Title', title2='Title', title3='Title', 
         xlab='Vuosi', ylab='Pisteet', dataX=[],
         dataY0=[], dataY1=[], dataY2=[], dataY3=[]): 
    fig=Figure()
    fig.set_facecolor('white')
    fig.subplots_adjust(wspace=0.5, hspace=0.75)
    ax0=fig.add_subplot(2, 2, 1)
    ax1=fig.add_subplot(2, 2, 2)
    ax2=fig.add_subplot(2, 2, 3)
    ax3=fig.add_subplot(2, 2, 4)
    setPlot(ax0, title0, xlab, ylab, dataX, dataY0)
    setPlot(ax1, title1, xlab, ylab, dataX, dataY1)
    setPlot(ax2, title2, xlab, ylab, dataX, dataY2) 
    setPlot(ax3, title3, xlab, ylab, dataX, dataY3) 
    canvas=FigureCanvas(fig)
    stream=cStringIO.StringIO()
    canvas.print_png(stream)
    return stream.getvalue()    
    
def myplot():
    if session.logged_in_user:
        return plot('Yhteistulos', 'AAM', '110m-aidat', 'Pituus', X_LAB, Y_LAB, session.xData, session.scoreResult, session.aamResult, session.aidatResult, session.pituusResult)
    else:
        redirect(URL('default', 'login'))
            
def myplot2():
    if session.logged_in_user:
        return plot('satanen', 'Kuula', 'Seivas', '400m', X_LAB, Y_LAB, session.xData, session.satanenResult, session.kuulaResult, session.seivasResult, session.neljasataaResult)
    else:
        redirect(URL('default', 'login'))
        
def myplot3():
    if session.logged_in_user:        
        return plot('Korkeus', 'Kiekko', 'Keihas', '1500m', X_LAB, Y_LAB, session.xData, session.korkeusResult, session.kiekkoResult, session.keihasResult, session.tuhatviisisataaResult)
    else:
        redirect(URL('default', 'login'))

