from Common import *
import modules.mergertrees.MTCatalogue as MT

class Contamination(HasTraits):

    gadpath = Directory
    checkexistence_button = Button("Check Existence")
    createconfig_button = Button("Make and distribute gadget!")
    checkcontam_button = Button("Plot Radial Distribution")

    plothalodist_button = Button("Plot Heatmap")
    plotmayavi_button = Button("3D Visualisation")
    padding = Range(5,10,7,auto_set=False)
    lmin = Range(7,14,7,auto_set=False)
    lmax = Range(7,14,11,auto_set=False)
    overlap = Range(1,6,4,auto_set=False)
    nrvir =Range(1,9,3,auto_set=False)
    boxtype = Enum(['ellipsoid','box'])
    haloid = Int(190897)
    haloidlist = List(Int)
    snapnum = Range(0,64,63,auto_set=False)
    foldername = Str()
    lowermassrange = Float(1e12)
    uppermassrange = Float(1.3e12)
    deltar =  Range(0.0,10.0,5.0,auto_set=False)
    zinit = Range(0,127,127)
    datastatus = Str()
    hostposx = Float()
    hostposy = Float()
    hostposz = Float()
    hostmass = Float()
    vizexpz_button = Button("Inspect/Update List")
    subscript_button = Button("Create Submission Script")
    includegroupsopt = Bool(False)
    xvar = Enum(['X-POS','Y-POS','Z-POS'])
    yvar = Enum(['X-POS','Y-POS','Z-POS'])
    weightopt = Enum(['count','mass'])
    makeactive = Bool()
    lowerlogmassbound = Float(11)
    nbins = Int(64)
    xymatch = Bool(False)
    xref = Float(50.)
    yref = Float(50.)
    zref = Float(50.)

    

    view = View(Item('gadpath',label='Base Path'),
                Item(name='haloid',label='Halo ID'),
                Item(name='boxtype',label='Box Type',style='custom'),
                Item(name='nrvir',label='n*rvir(z=0)'),
                Item(name='lmin',label='Level Min'),
                Item(name='lmax',label='Level Max'),
                Item(name='padding',label='Padding'),
                Item(name='overlap',label='Overlap'),
                Item(name='snapnum',label='Snapnum'),
                Item(name='deltar',label='Delta R',springy=True),
                HGroup(Item(name='xref',label='x-ref',springy=True),
                       Item(name='yref',label='y-ref',springy=True),
                       Item(name='zref',label='z-ref',springy=True),springy=True),
                HGroup(Item(name='lowermassrange',label='Lower Mass Cut'),
                       Item(name='uppermassrange',label='Upper Mass Cut')),
                Item(name='datastatus',label='Data Status',style='readonly'),
                Item(name='foldername',label='Examining',style='readonly'),
                Group(Item(name='checkcontam_button',show_label=False),enabled_when='makeactive == True'),
                Item('_'),
                HGroup(Item(name='xvar',label='X-AXIS'),
                       Item(name='yvar',label='Y-AXIS')),
                HGroup(Item(name='includegroupsopt',label='include halos?'),
                Group(Item(name='lowerlogmassbound',label='above log(M):'),enabled_when='includegroupsopt == True'),
                      Item(name='weightopt',label='weight by?'),
                      Item(name='nbins',label='Bins'),enabled_when='makeactive == True'),
                HGroup(Item(name='plotmayavi_button',show_label=False,springy=True),
                       Item(name='plothalodist_button',show_label=False,springy=True),enabled_when='makeactive == True and xymatch == False',springy=True),
                Item(name='hostmass',label='FOF Mass',style='readonly'),
                HGroup(Item(name='hostposx',label='FOF X-POS',style='readonly',springy=True),
                       Item(name='hostposy',label='FOF Y-POS',style='readonly',springy=True),
                       Item(name='hostposz',label='FOF Z-POS',style='readonly',springy=True),springy=True),
                Group(Item(name='haloidlist',show_label=False,style='readonly',editor=ListEditor(style='readonly',columns=6,rows=4)),label='Halo Sample',show_border=True))

    def _checkcontam_button_fired(self):
        self.foldername = 'H' + str(self.haloid) + \
                 '_B' + str(self.boxtype.upper())[0] + \
                 '_Z127' + \
                 '_P' + str(self.padding) + \
                 '_LN' + str(self.lmin) + \
                 '_LX' + str(self.lmax) + \
                 '_O' + str(self.overlap) + \
                 '_NV' + str(self.nrvir)

        dircheck = self.gadpath + 'halos/H' + str(self.haloid) + '/' + self.foldername + "/outputs" \
                    + "/groups_0" + str(self.snapnum)
        hubble = 0.6711
        if os.path.exists(dircheck):
            
            tmppath = self.gadpath + 'halos/H' + str(self.haloid) + '/' + self.foldername + "/outputs"
            filepath = tmppath + "/snapdir_0" + str(self.snapnum) + "/snap_0" + str(self.snapnum)
            s = readsubf.subfind_catalog(tmppath, self.snapnum)
            #ids = readsubf.subf_ids(tmppath, self.snapnum, 0, 0, read_all=1)
            mgroup = s.group_m_mean200*10**10/hubble
            rvirgroup = s.group_r_mean200
            xposgroup = s.group_pos[:,0]
            yposgroup = s.group_pos[:,1]
            zposgroup = s.group_pos[:,2]

            encloseminx = self.xref - self.deltar
            enclosemaxx = self.xref + self.deltar
            encloseminy = self.yref - self.deltar
            enclosemaxy = self.yref + self.deltar
            encloseminz = self.zref - self.deltar
            enclosemaxz = self.zref + self.deltar

            cond1 = (xposgroup >= encloseminx) & (xposgroup <= enclosemaxx)
            cond2 = (yposgroup >= encloseminy) & (yposgroup <= enclosemaxy)
            cond3 = (zposgroup >= encloseminz) & (zposgroup <= enclosemaxz)
            cond4 = (mgroup > self.lowermassrange) & (mgroup < self.uppermassrange)
            cond = cond1 & cond2 & cond3 & cond4

            xposhost = xposgroup[cond]
            yposhost = yposgroup[cond]
            zposhost = zposgroup[cond]
            mvir = mgroup[cond]

            rvirsub = s.sub_halfmassrad
            xpossub = s.sub_pos[:,0]
            ypossub = s.sub_pos[:,1]
            zpossub = s.sub_pos[:,2]
            mhalfsub = s.sub_mass*10**10/hubble

            #print s.sub_grnr
            titlestr = "Type:  " + str(self.boxtype[0]) + "\n" +  \
                       "padding:  " + str(self.padding) + "\n" +  \
                       "n*rvir(z=0):  " + str(self.nrvir) + "\n" + \
                       "level max: " + str(self.lmax) + "\n"

            
            R = np.sqrt((self.xref-xpossub)**2+(self.yref-ypossub)**2+(self.zref-zpossub)**2)
            sortindex = np.argsort(R)
            Rsorted = R[sortindex]
            Msorted = mhalfsub[sortindex]
            Groupsorted = s.sub_grnr[sortindex]

            masscon = (Msorted > self.lowermassrange) & (Msorted < self.uppermassrange) & (Rsorted < self.deltar)
            #print Groupsorted[masscon]
            #print Rsorted[masscon]
            #print Msorted[masscon]

            if len(xposhost) > 1:
                self.datastatus = "Too many possible hosts found, be more strict."
                self.hostposx = 0.
                self.hostposy = 0.
                self.hostposz = 0.
                self.hostmass = 0.
            elif len(xposhost) == 0:
                self.datastatus = "No hosts found, relax constraints."
                self.hostposx = 0.
                self.hostposy = 0.
                self.hostposz = 0.
                self.hostmass = 0.
            elif len(xposhost) == 1:
                self.datastatus = "Data exists, 1 host found, plotted."
                self.hostposx = float(xposhost)
                self.hostposy = float(yposhost)
                self.hostposz = float(zposhost)
                self.hostmass = float(mvir)
    
                R = np.sqrt((xposhost-xposgroup)**2+(yposhost-yposgroup)**2+(zposhost-zposgroup)**2)
                sortindex = np.argsort(R)
                Rsorted = R[sortindex]
                contamNR = np.cumsum(s.group_contamination_count[sortindex])
                contamMR = np.cumsum(s.group_contamination_mass[sortindex]*10**10)
    
                figure = self.main.display
                figure.clear()
                ax = figure.add_subplot(111)
                ax = self.main.display.axes[0]
                addsubtitle(ax,titlestr)

                ax.plot(Rsorted,np.log10(np.array(contamNR)),linestyle='-',color='b',linewidth=2)
                ax.set_xlim([0,7])
                ax.set_ylim([0,5])
    
                ax.set_ylabel(r'$\mathrm{\Sigma\ log_{10}\ N_{CP}}$', color='b',fontsize=14)
    
                for tl in ax.get_yticklabels():
                        tl.set_color('b')
                    
                axb = ax.twinx()
                axb.tick_params(axis='both', which='major', labelsize=12)
                axb.set_ylim([8,14])
                axb.plot(Rsorted,np.log10(contamMR),linestyle='-',color='r',linewidth=2)
                axb.set_ylim([8,14])
                for tl in axb.get_yticklabels():
                    tl.set_color('r')
    
                axb.set_ylabel(r'$\mathrm{log_{10}\ \Sigma\ M_{CP}\ [M_\odot/h]}$', color='r',fontsize=14)
                ax.set_xlabel(r'$\mathrm{R_{FOF}\ [Mpc/h]}$',fontsize=14)
                #ax.set_ylabel(r'$\mathrm{y-pos\ [Mpc/h]}$')
                #ax.set_xlabel(r'$\mathrm{y-pos\ [Mpc/h]}$')
    
                wx.CallAfter(self.main.display.canvas.draw)

        else:
            self.datastatus = "Data not found, not plotted."

    def _haloid_changed(self):
        #self.checkcontam_button_fired()
        self.foldername = 'H' + str(self.haloid) + '_B' + str(self.boxtype.upper())[0] + '_Z127' + '_P' + str(self.padding) + '_LN' + str(self.lmin) + '_LX' + str(self.lmax) + '_O' + str(self.overlap) + '_NV' + str(self.nrvir)
        dircheck = self.gadpath + 'halos/H' + str(self.haloid) + '/' + self.foldername + "/outputs/groups_0" + str(self.snapnum)
        if os.path.exists(dircheck):
            self.makeactive = True
        else:
            self.makeactive = False
    
    def _boxtype_changed(self):
        self.foldername = 'H' + str(self.haloid) + '_B' + str(self.boxtype.upper())[0] + '_Z127' + '_P' + str(self.padding) + '_LN' + str(self.lmin) + '_LX' + str(self.lmax) + '_O' + str(self.overlap) + '_NV' + str(self.nrvir)
        dircheck = self.gadpath + 'halos/H' + str(self.haloid) + '/' + self.foldername + "/outputs/groups_0" + str(self.snapnum)
        if os.path.exists(dircheck):
            self.makeactive = True
        else:
            self.makeactive = False
    
    def _nrvir_changed(self):
        self.foldername = 'H' + str(self.haloid) + '_B' + str(self.boxtype.upper())[0] + '_Z127' + '_P' + str(self.padding) + '_LN' + str(self.lmin) + '_LX' + str(self.lmax) + '_O' + str(self.overlap) + '_NV' + str(self.nrvir)
        dircheck = self.gadpath + 'halos/H' + str(self.haloid) + '/' + self.foldername + "/outputs/groups_0" + str(self.snapnum)
        if os.path.exists(dircheck):
            self._checkcontam_button_fired()
            self.makeactive = True
        else:
            self.makeactive = False
    
    def _deltar_changed(self):
        self.foldername = 'H' + str(self.haloid) + '_B' + str(self.boxtype.upper())[0] + '_Z127' + '_P' + str(self.padding) + '_LN' + str(self.lmin) + '_LX' + str(self.lmax) + '_O' + str(self.overlap) + '_NV' + str(self.nrvir)
        dircheck = self.gadpath + 'halos/H' + str(self.haloid) + '/' + self.foldername + "/outputs/groups_0" + str(self.snapnum)
        if os.path.exists(dircheck):
            self.makeactive = True
            self._checkcontam_button_fired()
        else:
            self.makeactive = False

    def _lmin_changed(self):
        self.foldername = 'H' + str(self.haloid) + '_B' + str(self.boxtype.upper())[0] + '_Z127' + '_P' + str(self.padding) + '_LN' + str(self.lmin) + '_LX' + str(self.lmax) + '_O' + str(self.overlap) + '_NV' + str(self.nrvir)
        dircheck = self.gadpath + 'halos/H' + str(self.haloid) + '/' + self.foldername + "/outputs/groups_0" + str(self.snapnum)
        if os.path.exists(dircheck):
            self.makeactive = True
            self._checkcontam_button_fired()
        else:
            self.makeactive = False
    
    def _lmax_changed(self):
        self.foldername = 'H' + str(self.haloid) + '_B' + str(self.boxtype.upper())[0] + '_Z127' + '_P' + str(self.padding) + '_LN' + str(self.lmin) + '_LX' + str(self.lmax) + '_O' + str(self.overlap) + '_NV' + str(self.nrvir)
        dircheck = self.gadpath + 'halos/H' + str(self.haloid) + '/' + self.foldername + "/outputs/groups_0" + str(self.snapnum)
        if os.path.exists(dircheck):
            self.makeactive = True
            self._checkcontam_button_fired()
        else:
            self.makeactive = False
    
    def _padding_changed(self):
        self.foldername = 'H' + str(self.haloid) + '_B' + str(self.boxtype.upper())[0] + '_Z127' + '_P' + str(self.padding) + '_LN' + str(self.lmin) + '_LX' + str(self.lmax) + '_O' + str(self.overlap) + '_NV' + str(self.nrvir)
        dircheck = self.gadpath + 'halos/H' + str(self.haloid) + '/' + self.foldername + "/outputs/groups_0" + str(self.snapnum)
        if os.path.exists(dircheck):
            self.makeactive = True
            self._checkcontam_button_fired()
        else:
            self.makeactive = False
    
    def _overlap_changed(self):
        self.foldername = 'H' + str(self.haloid) + '_B' + str(self.boxtype.upper())[0] + '_Z127' + '_P' + str(self.padding) + '_LN' + str(self.lmin) + '_LX' + str(self.lmax) + '_O' + str(self.overlap) + '_NV' + str(self.nrvir)
        dircheck = self.gadpath + 'halos/H' + str(self.haloid) + '/' + self.foldername + "/outputs/groups_0" + str(self.snapnum)
        if os.path.exists(dircheck):
            self.makeactive == True
            self._checkcontam_button_fired()
        else:
            self.makeactive == False
    
    def _snapnum_changed(self):
        self.foldername = 'H' + str(self.haloid) + '_B' + str(self.boxtype.upper())[0] + '_Z127' + '_P' + str(self.padding) + '_LN' + str(self.lmin) + '_LX' + str(self.lmax) + '_O' + str(self.overlap) + '_NV' + str(self.nrvir)
        dircheck = self.gadpath + 'halos/H' + str(self.haloid) + '/' + self.foldername + "/outputs/groups_0" + str(self.snapnum)
        if os.path.exists(dircheck):
            self.makeactive == True
            self._checkcontam_button_fired()
        else:
            self.makeactive == False

    def _xvar_changed(self):
        if self.xvar == self.yvar:
            self.xymatch = True
        else:
            self.xymatch = False

    def _yvar_changed(self):
        if self.xvar == self.yvar:
            self.xymatch = True
        else:
            self.xymatch = False

    def _plothalodist_button_fired(self):
        self.foldername = 'H' + str(self.haloid) + \
                     '_B' + str(self.boxtype.upper())[0] + \
                     '_Z127' + \
                     '_P' + str(self.padding) + \
                     '_LN' + str(self.lmin) + \
                     '_LX' + str(self.lmax) + \
                     '_O' + str(self.overlap) + \
                     '_NV' + str(self.nrvir)
    
        figure = self.main.display
        figure.clear()
        ax = figure.add_subplot(111)
        ax = self.main.display.axes[0]
    
        dircheck = self.gadpath + 'halos/H' + str(self.haloid) + '/' + self.foldername + "/outputs" \
                        + "/groups_0" + str(self.snapnum)
        
        hubble = 0.6711
    
        if os.path.exists(dircheck):
            self.datastatus = "Data exists, plotted."
            tmppath = self.gadpath + 'halos/H' + str(self.haloid) + '/' + self.foldername + "/outputs"
            filepath = tmppath + "/snapdir_0" + str(self.snapnum) + "/snap_0" + str(self.snapnum)
            s = readsubf.subfind_catalog(tmppath, self.snapnum)
            #ids = readsubf.subf_ids(tmppath, self.snapnum, 0, 0, read_all=1)
            mgroup = s.group_m_mean200*10**10/hubble
            rvirmgroup = s.group_r_mean200
            xposmgroup = s.group_pos[:,0]
            yposmgroup = s.group_pos[:,1]
            zposmgroup = s.group_pos[:,2]
            

            if self.weightopt == 'count':
                weights = s.group_contamination_count

            if self.weightopt == 'mass':
                weights = s.group_contamination_mass

            if self.xvar == 'X-POS':
                xvar = xposmgroup
                ax.set_xlabel(r'$\mathrm{x-pos\ [Mpc/h]}$')

            if self.xvar == 'Y-POS':
                xvar = yposmgroup
                ax.set_xlabel(r'$\mathrm{y-pos\ [Mpc/h]}$')

            if self.xvar == 'Z-POS':
                xvar = zposmgroup
                ax.set_xlabel(r'$\mathrm{z-pos\ [Mpc/h]}$')

            if self.yvar == 'X-POS':
                yvar = xposmgroup
                ax.set_ylabel(r'$\mathrm{x-pos\ [Mpc/h]}$')

            if self.yvar == 'Y-POS':
                yvar = yposmgroup
                ax.set_ylabel(r'$\mathrm{y-pos\ [Mpc/h]}$')

            if self.yvar == 'Z-POS':
                yvar = zposmgroup
                ax.set_ylabel(r'$\mathrm{z-pos\ [Mpc/h]}$')


            heatmap, xedges, yedges = np.histogram2d(xvar, yvar, bins=self.nbins,weights=weights)
            extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
                
            if self.includegroupsopt == True:
                xcirc,ycirc = drawcircle(xvar[mgroup > 10**self.lowerlogmassbound],yvar[mgroup > 10**self.lowerlogmassbound],rvirmgroup[mgroup > 10**self.lowerlogmassbound])        
                ax.plot(xcirc,ycirc,'k-',linewidth=2,alpha=0.3)    

            heatmap = np.flipud(np.rot90(heatmap))
            sc1 = ax.imshow(np.log10(heatmap),extent = extent,cmap = 'jet', origin='lower')
            cbar1 = figure.colorbar(sc1)

            if self.weightopt == 'mass':
                cbar1.set_label(r'$\mathrm{log_{10}\ mass\ [M_\odot/h]}$')

            if self.weightopt == 'count':
                cbar1.set_label(r'$\mathrm{log_{10}\ contamination\ count}$')

            wx.CallAfter(self.main.display.canvas.draw)

    def _plotmayavi_button_fired(self):
        self.main.scene.mlab.clf(figure=self.main.scene.mayavi_scene)
        self.foldername = 'H' + str(self.haloid) + '_B' + str(self.boxtype.upper())[0] + '_Z127' + '_P' + str(self.padding) + '_LN' + str(self.lmin) + '_LX' + str(self.lmax) + '_O' + str(self.overlap) + '_NV' + str(self.nrvir)
        dircheck = self.gadpath + 'halos/H' + str(self.haloid) + '/' + self.foldername + "/outputs/groups_0" + str(self.snapnum)
        hubble = 0.6711
        if os.path.exists(dircheck):
            self.datastatus = "Data exists, plotted."
            tmppath = self.gadpath + 'halos/H' + str(self.haloid) + '/' + self.foldername + "/outputs"
            filepath = tmppath + "/snapdir_0" + str(self.snapnum) + "/snap_0" + str(self.snapnum)
            s = readsubf.subfind_catalog(tmppath, self.snapnum)
            mgroup = s.group_m_mean200*10**10/hubble

            #contamN = s.group_contamination_count[mgroup > 10**self.lowerlogmassbound]
            #contamM = s.group_contamination_mass[mgroup > 10**self.lowerlogmassbound]
            #contamN = contamN.astype(float)
            #contamM = contamM.astype(float)
            #normcontamN = contamN/contamN.max()
            #normcontamM = contamM/contamM.max()

            rvir = s.group_r_mean200[mgroup > 10**self.lowerlogmassbound]
            x = s.group_pos[:,0][mgroup > 10**self.lowerlogmassbound]
            y = s.group_pos[:,1][mgroup > 10**self.lowerlogmassbound]
            z = s.group_pos[:,2][mgroup > 10**self.lowerlogmassbound]

            #,color=normcontamN

            self.main.scene.mlab.points3d(x, y, z, rvir*1000)
            self.main.scene.mlab.xlabel('x-pos')
            self.main.scene.mlab.ylabel('y-pos')
            self.main.scene.mlab.zlabel('z-pos')
            self.main.scene.mlab.colorbar(orientation='horizontal',title='r_mean200 [kpc]')
            self.main.scene.mlab.show()
            self.main.scene.mlab.outline()

    def __init__(self, main, **kwargs):
        HasTraits.__init__(self)
        self.main = main
        self.xvar = 'X-POS'
        self.yvar = 'Y-POS'
        self.boxtype = 'box'

        self.haloidlist = self.main.candidatestab.haloid
        self.gadpath = self.main.headertab.datamasterpath
              
        self.foldername = 'H' + str(self.haloid) + '_B' + str(self.boxtype.upper())[0] + '_Z127' + '_P' + str(self.padding) + '_LN' + str(self.lmin) + '_LX' + str(self.lmax) + '_O' + str(self.overlap) + '_NV' + str(self.nrvir)
        dircheck = self.gadpath + 'halos/H' + str(self.haloid) + '/' + self.foldername + "/outputs/groups_0" + str(self.snapnum)
        if os.path.exists(dircheck):
            self.makeactive = True
        else:
            self.makeactive = False


   
