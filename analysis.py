from Common import *

class Analysis(HasTraits):

    view = View()
                      
    def __init__(self, main, **kwargs):
        HasTraits.__init__(self)
        self.main = main
    