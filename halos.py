from Common import *

class HaloFind(HasTraits):

    halopath = Directory

    x_scale = Enum(['linear','log'])
    y_scale = Enum(['linear','log'])
    haloid = Enum(['190897','208737','140666','28221','147419','28188','147273','78411','131988','19910'])
    snapshot = Range(0,64,63)
    halo_type = Enum(['all halos','hosts only','subhalos only'])
    fullboxopt = Enum(['full box','specific halo'])
    deltar = Range(0,10,5)
    id_select = Int(0)

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
    
    plot_button = Button('Plot')
    plotxyzrvir_button = Button('Plot 3D Halo Distribution (scaled by rvir)')
    quiver_button = Button('Plot 3D Halo Velocity Field')

    opacity_select = Range(low=0.00,high=1.00,value=1.00,auto_set=False)
    vmin_select = Range(low=0.00,high=10.00,value=0.00,auto_set=False)
    vmax_select = Range(low=0.00,high=10.00,value=10.00,auto_set=False)
    quiver_width = Range(low=0,high=10,value=2,auto_set=False)

    min_vmag = Float
    max_vmax = Float

    view = View(VGroup(Item(name='halopath',style='readonly'),
                       Item(name='snapshot',label='Snapshot'),
                 HGroup(Item(name='halo_type',style='custom',show_label=False)),
                        Item(name='fullboxopt',style='custom',show_label=False),
                            Group(HGroup(Item(name='haloid',label='Rockstar Halo ID'),
                                         Item(name='deltar',label='Box Width [Mpc/h]',springy=True),springy=True)
                                ,enabled_when='fullboxopt=="specific halo"'),

                       HGroup(HGroup(HGroup(Group(HGroup(VGroup(Group(Item(name='halo_varx',label='x-axis',springy=True),
                                           Item(name='halo_vary',label='y-axis',springy=True))),label='Set Quantities',show_border=True)),enabled_when='use_common == True')),

                              HGroup(Group(HGroup(VGroup(Group(Item(name='x_scale',label='x-scale',springy=True),
                                     Item(name='y_scale',label='y-scale',springy=True))),label='Set Scale',show_border=True)),enabled_when='use_common == True')),

                       Group(Item(name='plot_button',show_label=False,springy=True),enabled_when='len(halo_type) > 0'),
                       Group(HGroup(Item(name='quiver_button',show_label=False,springy=True),Item(name='plotxyzrvir_button',show_label=False,springy=True))),
                       Group(VGroup(Item(name='quiver_mode',label='Mode',padding=5),
                             HGroup(Item(name='vmin_select',label='vmin',padding=5,springy=True),Item(name='vmax_select',label='vmax',padding=5,springy=True)),
                             HGroup(Item(name='opacity_select',label='opacity',padding=5,springy=True),Item(name='quiver_width',label='width',padding=5,springy=True))))))
    
    def _plot_button_fired(self):
        if hasattr(self, 'display_points'):
            figure = self.main.display
            figure.clear()
            ax = figure.add_subplot(111)

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

        wx.CallAfter(self.main.display.canvas.draw)

    def _quiver_button_fired(self):
        x,y,z,vx,vy,vz = self.gethalos_xyzvzvyvz()
        
        self.main.scene.mlab.clf(figure=self.main.scene.mayavi_scene) 
        self.min_vmag = 0
        self.max_vmag = 10000
        self.main.scene.mlab.quiver3d(np.array(x), np.array(y), np.array(z), np.array(vx), np.array(vy), np.array(vz),line_width=self.quiver_width,opacity=self.opacity_select,mode=self.quiver_mode)
        self.main.scene.mlab.xlabel('x-pos')
        self.main.scene.mlab.ylabel('y-pos')
        self.main.scene.mlab.zlabel('z-pos')
        self.main.scene.mlab.colorbar(orientation='horizontal',title='velocity [km/s]')
        self.main.scene.mlab.show()
        self.main.scene.mlab.outline()

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

        self.main.scene.mlab.clf(figure=self.main.scene.mayavi_scene) 
        self.main.scene.mlab.quiver3d(x,y,z,vx,vy,vz,line_width=self.quiver_width,opacity=self.opacity_select,mode=self.quiver_mode)
        self.main.scene.mlab.xlabel('x-pos')
        self.main.scene.mlab.ylabel('y-pos')
        self.main.scene.mlab.zlabel('z-pos')
        self.main.scene.mlab.colorbar(orientation='horizontal',title='velocity [km/s]')
        self.main.scene.mlab.show()
        self.main.scene.mlab.outline()

        return x,y,z,vx,vy,vz

    def gethalos_xy(self):
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
            
            x = tmphalos[self.halo_varx]
            y = tmphalos[self.halo_vary]

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

            x = np.array(halodata.data[self.halo_varx][condh])
            y = np.array(halodata.data[self.halo_vary][condh])

            if 'pos' in self.halo_varx and 'pos' in self.halo_vary:
                rvir =  np.array(halodata.data['rvir'][condh])
                x,y = drawcircle(x,y,rvir/1000)

        return x,y

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

            x = np.array(halodata.data['posX'][condh])
            y = np.array(halodata.data['posY'][condh])
            z = np.array(halodata.data['posZ'][condh])
            rvir =  np.array(halodata.data['rvir'][condh])

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

    def __init__(self, main, **kwargs):
        HasTraits.__init__(self)
        self.main = main
        self.halo_varx = 'posX'
        self.halo_vary = 'posY'
        self.halopath = self.main.headertab.parentsimpath + 'RockstarData'