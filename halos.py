from Common import *

class HaloFind(HasTraits):

    halopath = Directory

    x_scale = Enum(['linear','log'])
    y_scale = Enum(['linear','log'])
    #haloid = Enum([])
    #haloid = List(Int)
    haloid = Int()
    #Enum(['190897','208737','140666','28221','147419','28188','147273','78411','131988','19910'])
    snapshot = Range(0,255,255)

    deltar = Range(0.0,10.0,5.0)
    id_select = Int(0)
    haloidlist = List(Int)
    datastatus = Str
    halo_varx  = Enum(['id','posX','posY','posZ','corevelx','corevely','corevelz', \
          'pecVX','pecVY','pecVZ', 'bulkvelX','bulkvelY','bulkvelZ','mvir',\
          'rvir','child_r','mgrav','vmax','rvmax','rs','rs_klypin',\
          'vrms','Jx','Jy','Jz','Epot','spin','m200c','m500c','m2500c', \
          'Xoff','Voff','b_to_a','c_to_a','A[x]','A[y]','A[z]','spin_bullock','T/|U|','npart',\
          'num_cp','numstart','desc','flags','n_core','min_pos_err','min_vel_err','min_bulkvel_err' \
          'hostID','offset','particle_offset'])

    halo_vary = Enum(['id','posX','posY','posZ','corevelx','corevely','corevelz', \
          'pecVX','pecVY','pecVZ', 'bulkvelX','bulkvelY','bulkvelZ','mvir',\
          'rvir','child_r','mgrav','vmax','rvmax','rs','rs_klypin',\
          'vrms','Jx','Jy','Jz','Epot','spin','m200c','m500c','m2500c', \
          'Xoff','Voff','b_to_a','c_to_a','A[x]','A[y]','A[z]','spin_bullock','T/|U|','npart',\
          'num_cp','numstart','desc','flags','n_core','min_pos_err','min_vel_err','min_bulkvel_err' \
          'hostID','offset','particle_offset'])
    
    quiver_mode = Enum(['2darrow','2dcircle','2dcross','2ddash','2ddiamond','2dhooked_arrow','2dsquare','2dthick_arrow','2dthick_cross','2dtriangle','2dvertex','arrow','axes','cone','cube','cylinder','point','sphere'])
    enable_haloglyps = Bool(False)
    plot_button = Button('Plot')
    plotxyzrvir_button = Button('Plot 3D Halo Distribution')
    quiver_button = Button('Plot 3D Halo Velocity Field')

    opacity_select = Range(low=0.00,high=1.00,value=1.00,auto_set=False)
    vmin_select = Range(low=0.00,high=10.00,value=0.00,auto_set=False)
    vmax_select = Range(low=0.00,high=10.00,value=10.00,auto_set=False)
    quiver_width = Range(low=0,high=10,value=2,auto_set=False)

    min_vmag = Float
    max_vmax = Float

    padding = Range(5,10,7,auto_set=False)
    lmin = Range(7,14,7,auto_set=False)
    lmax = Range(7,14,11,auto_set=False)
    overlap = Range(1,6,4,auto_set=False)
    nrvir =Range(1,9,3,auto_set=False)
    boxtype = Enum(['ellipsoid','box'])
    boxtype = Enum(['box','ellipsoid'])
    parentorzoom = Enum(['zoom','parent'])
    halo_type = Enum(['all halos','hosts only','subhalos only'])
    fullboxopt = Enum(['full box','specific halo'])

    hostmvir = Float
    hostrvir = Float
    hostrvmax = Float
    hostposx = Float
    hostposy = Float
    hostposz = Float
    zoomid = Int
    nhosts = Int
    nsubs = Int
    sinhost = Int
    enableplot = Bool(False)

    view = View(VGroup(Item(name='halopath',style='readonly',label='Reading'),
                       HGroup(Item(name='snapshot',label='Snapshot'),Item(name='datastatus',label='Status',style='readonly')),
                 HGroup(Item(name='halo_type',style='custom',show_label=False),enabled_when='fullboxopt=="full box"'),
                        Item(name='parentorzoom',label='Which Type?',style='custom'),
                        Group(Item(name='fullboxopt',style='custom',label='Which object?'),enabled_when='parentorzoom=="parent"'),
                        Group(Item(name='haloid',label='Rockstar Halo ID'),
                            #Item(name='halopath',label='Reading',style='readonly')
                              enabled_when='fullboxopt=="specific halo" or parentorzoom=="zoom"'),
                            Group(HGroup(Item(name='deltar',label='Box Width [Mpc/h]',springy=True),springy=True)
                                ,enabled_when='fullboxopt=="specific halo" or parentorzoom=="zoom"'),
                            
                        Group(Item(name='boxtype',label='Which Volume?',style='custom'),enabled_when='parentorzoom=="zoom"'),
                        HGroup(Group(HGroup(Group(Item(name='nrvir',label='n*rvir(z=0)'),
                                     Item(name='lmin',label='Level Min'),
                                     Item(name='lmax',label='Level Max'),
                                     Item(name='padding',label='Padding'),
                                     Item(name='overlap',label='Overlap'),
                                     HGroup(Group(Item(name='zoomid',label='ID',style='readonly'),
                                      Item(name='nhosts',label='# hosts',style='readonly'),
                                     Item(name='nsubs',label='# subs',style='readonly'),
                                     Item(name='sinhost',label='# subs in host',style='readonly'),
                                     Item(name='hostmvir',label='mvir',style='readonly',format_str='%.2e'),
                                     Item(name='hostrvir',format_str= '%.2f',label='rvir',style='readonly'),
                                     Item(name='hostrvmax',format_str= '%.2f',label='rvmax',style='readonly')),
                                     Group(Item(name='hostposx',format_str= '%.2f',label='pos-X',style='readonly'),
                                     Item(name='hostposy',format_str= '%.2f',label='pos-Y',style='readonly'),
                                     Item(name='hostposz',format_str= '%.2f',label='pos-Z',style='readonly'))))),enabled_when='parentorzoom=="zoom"'),
                    Group(Item(name='haloidlist',show_label=False,style='readonly',editor=ListEditor(style='readonly',columns=4,rows=3)),label='Halo Sample',show_border=True)),
                       HGroup(HGroup(HGroup(Group(HGroup(VGroup(Group(Item(name='halo_varx',label='x-axis',springy=True),
                                           Item(name='halo_vary',label='y-axis',springy=True))),label='Set Quantities',show_border=True)),enabled_when='use_common == True')),

                              HGroup(Group(HGroup(VGroup(Group(Item(name='x_scale',label='x-scale',springy=True),
                                     Item(name='y_scale',label='y-scale',springy=True))),label='Set Scale',show_border=True)),enabled_when='use_common == True')),

                       Group(Item(name='plot_button',show_label=False,springy=True),enabled_when='enableplot == True'),
                       Group(HGroup(Item(name='enable_haloglyps',label='+halos'),
                                Item(name='quiver_button',show_label=False,springy=True),
                                Item(name='plotxyzrvir_button',show_label=False,springy=True))),
                       Group(VGroup(Item(name='quiver_mode',label='Mode',padding=5),
                             HGroup(Item(name='vmin_select',label='vmin',padding=5,springy=True),Item(name='vmax_select',label='vmax',padding=5,springy=True)),
                             HGroup(Item(name='opacity_select',label='opacity',padding=5,springy=True),Item(name='quiver_width',label='width',padding=5,springy=True))))
                        ))
    def _haloid_changed(self):
        if self.haloid in self.haloidlist:
            self.enableplot = True
        else:
            self.enableplot = False

    def _parentorzoom_changed(self):
        if self.parentorzoom == 'parent':
            self.snapshot = 63
            self.enableplot = True
        elif self.haloid == 0 and self.parentorzoom == 'zoom':
            self.enableplot = False

        if self.parentorzoom == 'zoom':
            self.snapshot = 255

    def gethostid(self):
        path = "/bigbang/data/AnnaGroup/caterpillar/halos"
        with open(path + "/halosummary.txt") as f:
            for line in f:
                if line[0] != '#':
                    linecomp = line.split()
                    if 'H'+str(self.haloid) == linecomp[0] and 'B'+str(self.boxtype.upper())[0] == linecomp[1] \
                       and str(self.lmax) == linecomp[2] and str(self.nrvir) == linecomp[3]:
                       haloid = linecomp[17]

        return haloid

    def gethalos_xy(self):
        if self.parentorzoom == 'parent':
            self.halopath = self.main.headertab.parentsimpath + 'RockstarData'
            if os.path.exists(self.halopath):
                halodata = RSDataReader.RSDataReader(self.halopath,self.snapshot,digits=2)
                self.datastatus = 'Parent found.'
                dataexists = True
            else:
                dataexists = False
                self.datastatus = 'Parent not found.'
            
        elif self.parentorzoom == 'zoom':
            self.foldername = 'H' + str(self.haloid) + \
                     '_B' + str(self.boxtype.upper())[0] + \
                     '_Z127' + \
                     '_P' + str(self.padding) + \
                     '_LN' + str(self.lmin) + \
                     '_LX' + str(self.lmax) + \
                     '_O' + str(self.overlap) + \
                     '_NV' + str(self.nrvir)

            self.halopath = self.gadpath + 'halos/H' + str(self.haloid) + '/' + self.foldername + "/rockstardata"
            
            if os.path.exists(self.halopath):
                halodata = RSDataReader.RSDataReader(self.halopath,self.snapshot,digits=2)
                self.datastatus = 'Zoom found.'
                dataexists = True
            else:
                dataexists = False
                self.datastatus = 'Zoom not found.'
        
        if dataexists:
            if self.halo_type == 'all halos':
                tmphalos = halodata.data
            if self.halo_type == 'hosts only':
                tmphalos = halodata.get_hosts()
            if self.halo_type == 'subhalos only':
                tmphalos = halodata.get_subs()
            if self.halo_type == 'subs of ID':
                tmphalos = halodata.get_subhalos_from_halo(self.haloid)

            
            if self.fullboxopt == 'full box' and self.parentorzoom == 'parent':
                x = np.array(tmphalos[self.halo_varx])
                y = np.array(tmphalos[self.halo_vary])
            elif self.parentorzoom == 'zoom':
                idhost = self.gethostid()
                if idhost:
                    hosts = halodata.get_hosts()
                    subs = halodata.get_subs()
                    host = hosts.ix[int(idhost)]
                    subsinhost  = halodata.get_subhalos_from_halo(self.haloid)
                    xposhost = float(host['posX'])
                    yposhost = float(host['posY'])
                    zposhost = float(host['posZ'])
                    self.zoomid = int(idhost)
                    self.hostmvir = host['mvir']/halodata.h0
                    self.hostrvir = host['rvir']
                    self.hostrvmax = host['rvmax']
                    self.hostposx = host['posZ']
                    self.hostposy = host['posY']
                    self.hostposz = host['posZ']
                    self.nhosts = len(hosts['posX'])
                    self.nsubs = len(subs['posX'])
                    self.sinhost = len(subsinhost['posX'])
                    cond1h = (np.array(tmphalos['posX']) >= xposhost - self.deltar/2.) & (np.array(tmphalos['posX']) <= xposhost + self.deltar/2.)
                    cond2h = (np.array(tmphalos['posY']) >= yposhost - self.deltar/2.) & (np.array(tmphalos['posY']) <= yposhost + self.deltar/2.)
                    cond3h = (np.array(tmphalos['posZ']) >= zposhost - self.deltar/2.) & (np.array(tmphalos['posZ']) <= zposhost + self.deltar/2.)
                    condh = cond1h & cond2h & cond3h 

                    x = np.array(tmphalos[self.halo_varx][condh])
                    y = np.array(tmphalos[self.halo_vary][condh])
                    self.datastatus = 'Host found.'
                elif not idhost:
                    self.datastatus = "No host found, plotting all."
                    x = np.array(tmphalos[self.halo_varx])
                    y = np.array(tmphalos[self.halo_vary])

            if 'pos' in self.halo_varx and 'pos' in self.halo_vary:
                if idhost:
                    rvir =  np.array(tmphalos['rvir'][condh])
                elif not idhost:
                    rvir =  np.array(tmphalos['rvir'])
                
                x,y = drawcircle(x,y,rvir/1000)
            
        else:
            self.datastatus = 'Data not found or plotted.'

        return x,y
        

    def _plot_button_fired(self):
        if self.parentorzoom == 'parent':
            self.halopath = self.main.headertab.parentsimpath + 'RockstarData'
            if os.path.exists(self.halopath):
                dataexists = True
            else:
                dataexists = False
    
        elif self.parentorzoom == 'zoom':
            self.foldername = 'H' + str(self.haloid) + \
                     '_B' + str(self.boxtype.upper())[0] + \
                     '_Z127' + \
                     '_P' + str(self.padding) + \
                     '_LN' + str(self.lmin) + \
                     '_LX' + str(self.lmax) + \
                     '_O' + str(self.overlap) + \
                     '_NV' + str(self.nrvir)

            self.halopath = self.gadpath + 'halos/H' + str(self.haloid) + '/' + self.foldername + "/rockstardata"
            
            if os.path.exists(self.halopath):
                dataexists = True
            else:
                dataexists = False

        
            if hasattr(self, 'display_points'):
                figure = self.main.display
                figure.clear()
                ax = figure.add_subplot(111)
    
            if dataexists:
                ax = self.main.display.axes[0]
                x,y = self.gethalos_xy()
                xmin_use = x.min()
                xmax_use = x.max()
                ymin_use = y.min()
                ymax_use = y.max()
        
                if 'pos' in self.halo_varx and 'pos' in self.halo_vary and self.fullboxopt == 'specific halo':
                    self.display_points = ax.plot(x,y,linestyle='-',linewidth=self.main.markersize,color=self.main.markercolor)
                else:
                    self.display_points = ax.plot(x,y,marker=self.main.markerstyle,linestyle='none',markersize=self.main.markersize,color=self.main.markercolor,markeredgecolor=self.main.markercolor)
        
                ax.set_xlim(xmin_use,xmax_use)
                ax.set_ylim(ymin_use,ymax_use)
                ax.set_xlabel(self.halo_varx)
                ax.set_ylabel(self.halo_vary)
                ax.set_xscale(self.x_scale)
                ax.set_yscale(self.y_scale)
                #self.datastatus = 'X-Y plotted.'
                wx.CallAfter(self.main.display.canvas.draw)

        

    def _quiver_button_fired(self):
        self.main.scene.mlab.clf(figure=self.main.scene.mayavi_scene)
        halodata = RSDataReader.RSDataReader(self.halopath,self.snapshot,digits=2)

        if self.fullboxopt == 'full box':
            if self.halo_type == 'all halos':
                tmphalos = halodata.data
            if self.halo_type == 'hosts only':
                tmphalos = halodata.get_hosts()
            if self.halo_type == 'subhalos only':
                tmphalos = halodata.get_subs()
            if self.halo_type == 'subs of ID':
                tmphalos = halodata.get_subhalos_from_halo(self.haloid)
            
            x = np.array(tmphalos['posX'])
            y = np.array(tmphalos['posY'])
            z = np.array(tmphalos['posZ'])
            vx = np.array(tmphalos['pecVX'])
            vy = np.array(tmphalos['pecVY'])
            vz = np.array(tmphalos['pecVZ'])
            #vmag = np.sqrt(vx**2+vy**2+vz**2)

        else:
            allhalos = halodata.get_hosts()
            halotmp = allhalos.ix[int(self.haloid)]

            xposhost = float(halotmp['posX'])
            yposhost = float(halotmp['posY'])
            zposhost = float(halotmp['posZ'])

            cond1h = (np.array(halodata.data['posX']) >= xposhost - self.deltar/2.) & (np.array(halodata.data['posX']) <= xposhost + self.deltar/2.)
            cond2h = (np.array(halodata.data['posY']) >= yposhost - self.deltar/2.) & (np.array(halodata.data['posY']) <= yposhost + self.deltar/2.)
            cond3h = (np.array(halodata.data['posZ']) >= zposhost - self.deltar/2.) & (np.array(halodata.data['posZ']) <= zposhost + self.deltar/2.)

            condh = cond1h & cond2h & cond3h 

            x = np.array(halodata.data['posX'][condh])
            y = np.array(halodata.data['posY'][condh])
            z = np.array(halodata.data['posZ'][condh])
            vx = np.array(halodata.data['pecVX'][condh])
            vy = np.array(halodata.data['pecVY'][condh])
            vz = np.array(halodata.data['pecVZ'][condh])
            rvir = np.array(halodata.data['rvir'][condh])

            

        vmag = np.sqrt(vx**2+vy**2+vz**2)
        self.main.scene.mlab.quiver3d(x,y,z,vx,vy,vz,line_width=self.quiver_width,opacity=self.opacity_select,mode=self.quiver_mode,scalars=vmag)
        
        if self.enable_haloglyps and self.fullboxopt == 'specific halo':
                self.main.scene.mlab.points3d(x, y, z, rvir/1000)

        self.main.scene.mlab.xlabel('x-pos')
        self.main.scene.mlab.ylabel('y-pos')
        self.main.scene.mlab.zlabel('z-pos')
        self.main.scene.mlab.colorbar(orientation='horizontal',title='velocity [km/s]')
        self.main.scene.mlab.show()
        self.main.scene.mlab.outline()

        return x,y,z,vx,vy,vz



    def _plotxyzrvir_button_changed(self):
        self.main.scene.mlab.clf(figure=self.main.scene.mayavi_scene)
        halodata = RSDataReader.RSDataReader(self.halopath,self.snapshot,digits=2)
        boxwidth = self.deltar/2

        if self.fullboxopt == 'full box':
            if self.halo_type == 'all halos':
                tmphalos = halodata.data
            if self.halo_type == 'hosts only':
                tmphalos = halodata.get_hosts()
            if self.halo_type == 'subhalos only':
                tmphalos = halodata.get_subs()
            if self.halo_type == 'subs of ID':
                tmphalos = halodata.get_subhalos_from_halo(self.haloid)
            
            x = tmphalos['posX']
            y = tmphalos['posY']
            z = tmphalos['posY']
            rvir =  tmphalos['rvir']
            self.main.scene.mlab.points3d(x, y, z, rvir/1000,colormap="copper")
        
        else:
            allhalos = halodata.get_hosts()
            halotmp = allhalos.ix[int(self.haloid)]

            xposhost = float(halotmp['posX'])
            yposhost = float(halotmp['posY'])
            zposhost = float(halotmp['posZ'])

            cond1h = (np.array(halodata.data['posX']) >= xposhost - self.deltar/2.) & (np.array(halodata.data['posX']) <= xposhost + self.deltar/2.)
            cond2h = (np.array(halodata.data['posY']) >= yposhost - self.deltar/2.) & (np.array(halodata.data['posY']) <= yposhost + self.deltar/2.)
            cond3h = (np.array(halodata.data['posZ']) >= zposhost - self.deltar/2.) & (np.array(halodata.data['posZ']) <= zposhost + self.deltar/2.)

            condh = cond1h & cond2h & cond3h

            condid =  (np.array(halodata.data['id']) == self.haloid)

            condnew = condh & condid

            x = np.array(halodata.data['posX'][condh])
            y = np.array(halodata.data['posY'][condh])
            z = np.array(halodata.data['posZ'][condh])
            rvir =  np.array(halodata.data['rvir'][condh])
            rvirn =  np.array(halodata.data['rvir'][condnew])
            mvir =  np.array(halodata.data['mvir'][condnew])
            rvmax =  np.array(halodata.data['rvmax'][condnew])
            vmax =  np.array(halodata.data['vmax'][condnew])

            print mvir,mvir/0.6711,rvirn,rvmax,vmax,xposhost,yposhost,zposhost

            extent = [xposhost-boxwidth,xposhost+boxwidth,yposhost-boxwidth,yposhost+boxwidth,zposhost-boxwidth,zposhost+boxwidth]
            self.main.scene.mlab.points3d(x, y, z, rvir/1000,colormap="copper")
            self.main.scene.mlab.colorbar(orientation='vertical',title='rvir')
            #self.main.scene.mlab.outline(extent = extent)
            #self.main.scene.mlab.axes(extent = extent) 
        
        self.main.scene.mlab.orientation_axes(xlabel='x-pos',ylabel='x-pos',zlabel='z-pos')
        self.main.scene.mlab.show()
        self.main.scene.mlab.axes()
        self.main.scene.mlab.outline()

    def _x_scale_changed(self):
        if hasattr(self, 'display_points'): 
               # self.display_points[0].remove()
                self.main.display.axes[0].set_xscale(self.x_scale)
                wx.CallAfter(self.main.display.canvas.draw)

    def _y_scale_changed(self):
        if hasattr(self, 'display_points'): 
                #self.display_points[0].remove()
                self.main.display.axes[0].set_yscale(self.y_scale)
                wx.CallAfter(self.main.display.canvas.draw)

#    def _haloid_default(self):
#         dirs = [d for d in os.listdir(self.main.headertab.datamasterpath+"halos/") if os.path.isdir(os.path.join(self.main.headertab.datamasterpath+"halos/", d))]
#         haloidvals = dirs
#         idlist = []
#         for idi in haloidvals:
#             idlist.append(idi[1:])
#         return idlist

    def __init__(self, main, **kwargs):
        HasTraits.__init__(self)
        self.main = main
        self.quiver_mode = 'arrow'
        self.haloidlist = self.main.candidatestab.haloid
        self.halo_varx = 'posX'
        self.halo_vary = 'posY'
        self.gadpath = self.main.headertab.datamasterpath
        self.halopath = self.main.headertab.parentsimpath + 'RockstarData'