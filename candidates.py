from Common import *
from numpy.random import random

class Candidates(HasTraits):

    masterpath = Directory
    halopath = Directory

    lowermasscut = Range(7.0,15.0)
    uppermasscut = Range(7.0,15.0)
    normlowermasscut = Float
    normuppermasscut = Float

    snapnum = Range(0,64,63)
    hubble = Float

    writeoutpath = Directory
    writeoutname = Str
    writeoutopt = Bool(False)

    largerthan1 = Range(7.0,15.0)
    distancecut1 = Range(0.0,10.0,1.0)
    moremassivethancand1 = Range(0.0,10.0,1.0)
    useintmult1 = Bool(False)
    normlargerthan1 = Float

    largerthan2 = Range(7.0,15.0)
    distancecut2 = Range(0.0,10.,1.0)
    moremassivethancand2 = Range(0.,10.0,1.0)
    useintmult2 = Bool(False)
    normlargerthan2 = Float

    largerthan3 = Range(7.0,15.0)
    distancecut3 = Range(0.0,10.0,1.0)
    moremassivethancand3 = Range(0.0,10.0,1.0)
    useintmult3 = Bool(False)
    normlargerthan3 = Float

    exclusionstr = Str
    nlargerthanlowermasscut = Int
    nlargerthanuppermasscut = Int
    nbetweenmasscut = Int
    ntotalcandidates = Int
    upper = Float(15.)
 
    candidatearr = Array

    loadpreviouscand = Bool(True)
    
    #candidatearr = random((20, 6))
    haloid = List(Int)
    #haloid = Enum(['190897','208737','140666','28221','147419','28188','147273','78411','131988','19910'])
    #haloid = Enum()
    jobstatus = Str()
    addhalo_button = Button("ADD")
    haloidtoadd = Int()
    getcandidates_button = Button("Get candidates!")
    clear_button = Button("CLEAR")
    view = View(Tabbed(Group(Group(Item(name='halopath',label='Parent Simulation Path'),
                                  HGroup(Item(name='loadpreviouscand',label='Use Existing Candidates'),
                                         Item(name='exclusionstr',show_label=False,style='readonly')),
                            
                            Group(HGroup(Item(name='lowermasscut',label='log[M > Msol]',springy=True,format_str= '%.1f'),
                                         Item(name='normlowermasscut',label='M',width=-70,format_str='%.2e')),
                                  HGroup(Item(name='uppermasscut',label='log[M > Msol]',springy=True,format_str= '%.1f'),
                                         Item(name='normuppermasscut',label='M',width=-70,format_str='%.2e'))
                                  ,label='Mass Range For Base Sample',show_border=True,enabled_when='loadpreviouscand == False'),
                            
                            

                            Group(Group(Group(HGroup(Item(name='largerthan1',label='log[M > Msol]',springy=True),
                                               Item(name='normlargerthan1',label='M',width=-70,format_str='%.2e')),enabled_when='useintmult1==False'),
                                  HGroup(Item(name='useintmult1',label='Use N times candidates mass'),
                                  Group(Item(name='moremassivethancand1',label='N',springy=True),enabled_when='useintmult1==True',springy=True)),

                                  Item(name='distancecut1',label='Within [Mpc]'),label='Exclusion Zone #1',show_border=True),enabled_when='loadpreviouscand == False'),
                            
                            Group(Group(Group(HGroup(Item(name='largerthan2',label='log[M > Msol]',springy=True),
                                               Item(name='normlargerthan2',label='M',width=-70,format_str='%.2e')),enabled_when='useintmult2==False'),
                                  HGroup(Item(name='useintmult2',label='Use N times candidates mass'),
                                         Group(Item(name='moremassivethancand2',label='N',springy=True),enabled_when='useintmult2==True',springy=True)),

                                  Item(name='distancecut2',label='Within [Mpc]'),label='Exclusion Zone #2',show_border=True),enabled_when='loadpreviouscand == False'),
                            
                            Group(Group(Group(HGroup(Item(name='largerthan3',label='log[M > Msol]',springy=True),
                                               Item(name='normlargerthan3',label='M',width=-70,format_str='%.2e')),enabled_when='useintmult3==False'),
                                  HGroup(Item(name='useintmult3',label='Use N times candidates mass'),
                                         Group(Item(name='moremassivethancand3',label='N',springy=True),enabled_when='useintmult3==True',springy=True)),

                                  Item(name='distancecut3',label='Within [Mpc]'),label='Exclusion Zone #3',show_border=True),enabled_when='loadpreviouscand == False'),
                            
                            HGroup(Item(name='writeoutopt',label='W/O?'),
                                         HGroup(Item(name='writeoutpath',label='Directory',springy=True),
                                               Item(name='writeoutname',label='Filename',springy=True),enabled_when='writeoutopt == True',springy=True),
                                          enabled_when='loadpreviouscand == False')),

                            Group(HGroup(Item(name='nbetweenmasscut',label='Base Sample',style='readonly',width=-35),
                                         Item(name='nlargerthanlowermasscut',label='N(M>M[EZ2])',style='readonly',width=-35),
                                         Item(name='nlargerthanuppermasscut',label='N(M>M[EZ3])',style='readonly',width=-35),
                                         Item(name='ntotalcandidates',label='# Candidates',width=-35,style='readonly'))),

                      Item(name='getcandidates_button',show_label=False),label='Collect')),

                      Group(VGroup(Item('candidatearr',show_label = False,
                                       editor= ArrayViewEditor(titles = [ 'Halo ID', 'Mvir [Msol]', 'Rvir [kpc]', 'x [Mpc/h]', 'y [Mpc/h]', 'z [Mpc/h]' ],
                                                                    format = '%.2e',
                                                                    #['%.4f','%.2e','%.4f','%.2f','%.2f','%.2f']
                                                                    show_index = False
                                                                   )),

                      Group(HGroup(Item(name='haloidtoadd',label='Add Halo ID'),
                                   Item(name='addhalo_button',show_label=False),
                                   Item(name='clear_button',show_label=False)),
                            Item(name='jobstatus',label='Job Status',style='readonly'),
                      Group(Item(name='haloid',show_label=False,style='readonly',editor=ListEditor(style='readonly',columns=6,rows=4)),label='Halo Sample',show_border=True))
                      ),label='Tabulate'))

    def _haloid_default(self):
        return [190897,208737]
        #,140666,28221,147419,28188,147273,78411,131988,19910]

    def _addhalo_button_fired(self):
        if len(self.candidatearr[:,0]) != 1:
            if int(self.haloidtoadd) in self.candidatearr[:,0] and int(self.haloidtoadd) not in self.haloid:
                self.haloid.append(int(self.haloidtoadd))
                self.jobstatus = "Candidate added."
            elif int(self.haloidtoadd) in self.haloid:
                self.jobstatus = "Candidate already in list!"
            else:
                self.jobstatus = "Candidate not found!"
        else:
          self.jobstatus = "You need to load some candidates, go back."

        self.main.mergertreetab.haloidlist = self.haloid
        self.main.halofindtab.haloidlist = self.haloid
        self.main.mergertreetab.haloidlist = self.haloid
        self.main.initstab.haloidlist = self.haloid

    def _haloidtoadd_changed(self):
        self.jobstatus = "Waiting for next addition."

    def _clear_button_fired(self):
        self.haloid = []
        self.main.halofindtab.haloidlist = []
        self.main.mergertreetab.haloidlist = []
        self.main.mergertreetab.initstab = []

    def _getcandidates_button_fired(self):
        hubble = 0.6711
        if self.loadpreviouscand == False:
            halodata = RSDataReader.RSDataReader(self.halopath,self.snapnum,digits=2)
            allhalos = halodata.get_hosts()
            
            MWcand = allhalos[np.logical_and(allhalos['mvir']/hubble>self.normlowermasscut, allhalos['mvir']/hubble<self.normuppermasscut)]
            
            halos12 = allhalos[allhalos['mvir']/hubble>self.normlargerthan2] # HALOS LARGER THAN 7E12
            halos13 = allhalos[allhalos['mvir']/hubble>self.normlargerthan3] # HALOS LARGER THAN 7E13
    
            self.nbetweenmasscut = len(MWcand)
            self.nlargerthanlowermasscut = len(halos12)
            self.nlargerthanuppermasscut = len(halos13)
    
            xpos12 = np.array(np.float64(halos12['posX']))
            ypos12 = np.array(np.float64(halos12['posY']))
            zpos12 = np.array(np.float64(halos12['posZ']))
            
            xpos13 = np.array(np.float64(halos13['posX']))
            ypos13 = np.array(np.float64(halos13['posY']))
            zpos13 = np.array(np.float64(halos13['posZ']))
    
            Ncandidates = 0
            if self.writeoutopt == True:
                out = open(self.writeoutpath + self.writeoutname, 'w')
                out.write('# ID M Rvir x y z\n')
            
            #xcand = []
            #ycand = []
            for i in xrange(0,len(MWcand)):
                # CYCLE CANDIDATE i
                xposi = np.array(np.float64(MWcand['posX']))[i]
                yposi = np.array(np.float64(MWcand['posY']))[i]
                zposi = np.array(np.float64(MWcand['posZ']))[i]
                massi = np.array(np.float64(MWcand['mvir']))[i]/hubble
                rviri = np.array(np.float64(MWcand['rvir']))[i]
                idi = np.array(MWcand['id'])[i]
            
                # CALCULATE DISTANCE TO HALOS LARGER THAN 7E12 and 7E13 MSOL
    
                R12 = np.sqrt((xposi-xpos12)**2.+(yposi-ypos12)**2.+(zposi-zpos12)**2.)/hubble
                R13 = np.sqrt((xposi-xpos13)**2.+(yposi-ypos13)**2.+(zposi-zpos13)**2.)/hubble
            
                # SELECT ALL HALOS LARGER THAN HALF THE SIZE OF THE CANDIDATE idi
            
                largerthanMW = allhalos[allhalos['mvir']/hubble >= self.moremassivethancand1*massi]
            
                # SINCE 0.5*massi INCLUDES idi, NEED TO REMOVE IT FROM X,Y,Z POS CALC SO MIN(R) != 0.0
            
                idindex = np.where(largerthanMW['id'] != idi)
                xtmp = np.array(np.float64(largerthanMW['posX']))
                ytmp = np.array(np.float64(largerthanMW['posY']))
                ztmp = np.array(np.float64(largerthanMW['posZ']))
            
                xposMgtMW = xtmp[idindex[0]]
                yposMgtMW = ytmp[idindex[0]]
                zposMgtMW = ztmp[idindex[0]]
            
                RMgtMW = np.sqrt((xposi-xposMgtMW)**2.+(yposi-yposMgtMW)**2.+(zposi-zposMgtMW)**2.)/hubble
                
                # NO HALO LARGER THAN 7e13 CLOSER THAN 4 MPC
                if R13.min() >= self.distancecut3:
                        # NO HALO LARGER THAN 7e12 CLOSER THAN 3 MPC
                    if R12.min() >= self.distancecut2:
                            # NO HALO HALF THE MASS OF CANDIDATE OR LARGER WITHIN 1.4 MPC
                        if RMgtMW.min() >= self.distancecut1:
                            self.candidatearr = np.vstack([self.candidatearr, [idi,massi,rviri,xposi,yposi,zposi]])
                            Ncandidates += 1
                            if self.writeoutopt == True:
                                out.write('%f %e %f %f %f %f \n' % 
                                    (int(idi),massi,rviri,xposi,yposi,zposi)) 
    
                self.ntotalcandidates = Ncandidates
                if Ncandidates > 0:
                    if hasattr(self, 'display_points'):
                        figure = self.main.display
                        figure.clear()
                        ax = figure.add_subplot(111)
        
                    ax = self.main.display.axes[0]
                    
                    self.display_points = ax.plot(self.candidatearr[:,3],self.candidatearr[:,4],marker=self.main.markerstyle,linestyle='none',markersize=self.main.markersize,color=self.main.markercolor,markeredgecolor=self.main.markercolor)
                    ax.set_xlim(0,100)
                    ax.set_ylim(0,100)
                    ax.set_xlabel('posX')
                    ax.set_ylabel('posY')
                    wx.CallAfter(self.main.display.canvas.draw)
    
                if self.writeoutopt == True:
                    out.close()

        elif self.loadpreviouscand == True:
            cand = getcandidatelist(self.writeoutpath + self.writeoutname)
            self.candidatearr = np.zeros(shape=(len(cand[:,0]),6))
            self.candidatearr[:,0] = cand[:,0]
            self.candidatearr[:,1] = cand[:,1]
            self.candidatearr[:,2] = cand[:,2]
            self.candidatearr[:,3] = cand[:,3]
            self.candidatearr[:,4] = cand[:,4]
            self.candidatearr[:,5] = cand[:,5]
            self.ntotalcandidates = len(cand[:,0])
            if hasattr(self, 'display_points'):
                figure = self.main.display
                figure.clear()
                ax = figure.add_subplot(111)
        
            ax = self.main.display.axes[0]
            self.display_points = ax.plot(self.candidatearr[:,3],self.candidatearr[:,4],
                                          marker=self.main.markerstyle,
                                          linestyle='none',
                                          markersize=self.main.markersize,
                                          color=self.main.markercolor,
                                          markeredgecolor=self.main.markercolor)
            ax.set_xlim(0,100)
            ax.set_ylim(0,100)
            ax.set_xlabel('x-pos [Mpc/h]')
            ax.set_ylabel('y-pos [Mpc/h]')
            wx.CallAfter(self.main.display.canvas.draw)

    def _largerthan1_changed(self):
      self.normlargerthan1 = 10**self.largerthan1

    def _largerthan2_changed(self):
      self.normlargerthan2 = 10**self.largerthan2

    def _largerthan3_changed(self):
      self.normlargerthan3 = 10**self.largerthan3  

    def _normlargerthan1_changed(self):
      self.largerthan1  = np.log10(self.normlargerthan1)

    def _normlargerthan2_changed(self):
      self.largerthan2  = np.log10(self.normlargerthan2)

    def _normlargerthan3_changed(self):
      self.largerthan3  = np.log10(self.normlargerthan3)

    def _uppermasscut_changed(self):
      self.normuppermasscut  = 10**self.uppermasscut

    def _normuppermasscut_changed(self):
      self.uppermasscut = np.log10(self.normuppermasscut)
  
    def _lowermasscut_changed(self):
      self.normlowermasscut = 10**self.lowermasscut

    def _normlowermasscut_changed(self):
      self.lowermasscut = np.log10(self.normlowermasscut)
      

    def __init__(self, main, **kwargs):
        HasTraits.__init__(self)
        self.main = main
        self.exclusionstr = 'Exclusion Zones: "no halo with mass M within distance R"'
        self.hubble = 0.6711
        #self.haloid = [190897]

        self.lowermasscut = np.log10(7e11)
        self.uppermasscut = np.log10(7e12)

        self.normlowermasscut = 10**self.lowermasscut
        self.normuppermasscut = 10**self.uppermasscut

        self.candidatearr = np.zeros(shape=(1,6))

        self.distancecut1 = 1.4
        self.distancecut2 = 3.
        self.distancecut3 = 4.

        self.moremassivethancand1 = 0.5

        self.useintmult1 = True

        self.largerthan1 = np.log10(1e12)
        self.largerthan2 = np.log10(7e12)
        self.largerthan3 = np.log10(7e13)

        self.normlargerthan1 = 10**self.largerthan1
        self.normlargerthan2 = 10**self.largerthan2
        self.normlargerthan3 = 10**self.largerthan3
        #self.largerthan3 = np.log10(7e13)
        
        self.writeoutname = 'candidates.dat'
        self.writeoutpath = self.main.headertab.datamasterpath
        self.halopath = self.main.headertab.parentsimpath + 'RockstarData'

        self.masterpath = self.main.headertab.masterpath



