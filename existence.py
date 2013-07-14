from Common import *

class Existence(HasTraits):

    haloid = Enum(['190897','140666','208737'])
    halomasterdir = Directory

    view = View(Item(name='halomasterdir',springy=True,label='Directory'),
                Item(name='haloid',label='Cluster',padding=5))
                      
    def __init__(self, main, **kwargs):
        HasTraits.__init__(self)
        self.main = main
        self.halomasterdir = self.main.headertab.basepath
