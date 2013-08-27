from Common import *
import getpass
from os.path import expanduser
class Header(HasTraits):

    view = View(Item(name='clusteropt',label='Cluster' ,padding=5),
                Item(name='currentdir'  ,label='CWD',style='readonly',padding=5),
                Item(name='username'  ,label='Username',padding=5),
    	        Item(name='masterpath',label='Home',padding=5),
                Item(name='gadgetpath',label='Gadget',padding=5),
                Item(name='musicpath',label='Music',padding=5),
                Item(name='parentsimpath',label='Parent Sim.',padding=5),
                Item(name='datamasterpath',label='Project Data',padding=5))
    
    clusteropt = Enum(['antares','barrine','odyssey','macbook','spacebase','bigbang','macbook'])
    username = Str
    masterpath = Directory
    homepath = Directory
    gadgetpath = Directory
    musicpath = Directory
    datamasterpath = Directory
    parentsimpath = Directory
    currentdir = Directory

    def _username_changed(self):
        self.masterpath = self.homepath + self.username
        self.gadgetpath = self.masterpath + '/lib/P-Gadget3/'
        self.parentsimpath = self.masterpath + '/AnnaGroup/caterpillar/parent/512Parent/'
        self.datamasterpath = self.masterpath + '/projects/caterpillar/data/'
        self.musicpath = self.homepath + self.username + '/lib/music/'

    def _clusteropt_changed(self):
        self.homepath = expanduser("~")

#        if self.clusteropt == 'Macbook':
#            self.homepath = '/home/'
#
#        if self.clusteropt == 'antares':
#            self.homepath = '/home/'
#
#        if self.clusteropt == 'barrine':
#            self.homepath = '/home/'
#
#        if self.clusteropt == 'odyssey':
#            self.homepath = '/n/home01/'
#
#        if self.clusteropt == 'spacebase':
#            self.homepath = '/spacebase/data/'
#
        self.masterpath = self.homepath + self.username

    def __init__(self, main, **kwargs):
        self.username = getpass.getuser()
        self.homepath = expanduser("~")
        if platform.node() == "csr-dyn-150.mit.edu":
            self.clusteropt = 'macbook'
            self.homepath = '/Users/griffen/Desktop/cme/'
            self.masterpath = self.homepath + self.username
            self.gadgetpath = self.masterpath + '/lib/P-Gadget3'
            self.musicpath = self.masterpath+ '/lib/music'
            self.datamasterpath = self.homepath + 'AnnaGroup/caterpillar/'
            self.parentsimpath = self.homepath + 'AnnaGroup/caterpillar/parent/'
            #self.homepath = '/Users/'
#        
        if platform.node() == "Brendans-MacBook-Pro.local":
            self.homepath = '/Users/'
#            
        if platform.node() == 'antares':
            self.clusteropt = 'antares'

        if platform.node() == 'barrine':
            self.username = 'uqbgriff'

        if platform.node() == 'rclogin13.rc.fas.harvard.edu':
            self.clustopt = 'odyssey'
            self.homepath = '/n/home01/bgriffen/data/'
            self.masterpath = self.homepath + self.username
            self.gadgetpath = self.masterpath + '/lib/P-Gadget3'
            self.musicpath = self.masterpath+ '/lib/music'
            self.datamasterpath = self.homepath + 'caterpillar/'
            self.parentsimpath = self.homepath + 'caterpillar/parent/'

        if platform.node() == 'spacebase':
            self.clusteropt = 'spacebase'
            self.homepath = '/spacebase/data/'
            self.masterpath = self.homepath + self.username
            self.gadgetpath = self.masterpath + '/lib/P-Gadget3'
            self.musicpath = self.masterpath+ '/lib/music'
            self.datamasterpath = self.homepath + 'AnnaGroup/caterpillar/'
            self.parentsimpath = self.homepath + 'AnnaGroup/caterpillar/parent/'

        if platform.node() == 'bigbang.mit.edu':
            self.clusteropt = 'bigbang'
            self.homepath = '/bigbang/data/'
            self.masterpath = self.homepath + self.username
            self.gadgetpath = self.masterpath + '/lib/P-Gadget3'
            self.musicpath = self.masterpath+ '/lib/music'
            self.datamasterpath = self.homepath + 'AnnaGroup/caterpillar/'
            self.parentsimpath = self.homepath + 'AnnaGroup/caterpillar/parent/'

        self.currentdir = os.getcwd()
        self.masterpath = self.homepath + self.username
        

        HasTraits.__init__(self)
        self.main = main
