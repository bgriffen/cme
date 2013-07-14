from Common import *

class Header(HasTraits):

    view = View(Item(name='clusteropt',label='Cluster' ,padding=5),
                Item(name='username'  ,label='Username',padding=5),
    	        Item(name='basepath'  ,label='Home'    ,padding=5))
    
    clusteropt = Enum(['Antares','Barrine','Odyssey','Macbook'])
    username = Str
    basepath = Directory
    homepath = Directory

    def _username_changed(self):
        self.basepath = self.homepath + self.username

    def _clusteropt_changed(self):
        if self.clusteropt == 'Macbook':
            self.username = 'griffen'
            self.homepath = '/home/'

        if self.clusteropt == 'Antares':
            self.username = 'griffen'
            self.homepath = '/home/'

        if self.clusteropt == 'Barrine':
            self.username = 'uqbgriff'
            self.homepath = '/home/'

        if self.clusteropt == 'Odyssey':
            self.username = 'bgriffen'
            self.homepath = '/n/home01/'

        if self.clusteropt == 'Spacebase':
            self.username = 'bgriffen'
            self.homepath = '/spacebase/data/'

        self.basepath = self.homepath + self.username

    def __init__(self, main, **kwargs):
        if platform.node() == "csr-dyn-150.mit.edu":
            self.username = 'griffen'
            self.homepath = '/Users/'
        
        if platform.node() == "Brendans-MacBook-Pro.local":
            self.username = 'griffen'
            self.homepath = '/Users/'
            
        if platform.node() == 'Antares':
            self.clusteropt = 'Antares'
            self.username = 'griffen'
            self.homepath = '/home/'

        if platform.node() == 'Barrine':
            self.username = 'uqbgriff'
            self.homepath = '/home/'

        if platform.node() == 'Odyssey':
            self.clusteropt = 'Odyssey'
            self.username = 'bgriffen'
            self.homepath = '/n/home01/'

        if platform.node() == 'Spacebase':
            self.clusteropt = 'Spacebase'
            self.username = 'bgriffen'
            self.homepath = '/spacebase/data/'

        self.basepath = self.homepath + self.username

        HasTraits.__init__(self)
        self.main = main