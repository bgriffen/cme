from Common import *
import mergertrees.MTCatalogue as MT

class MergerTree(HasTraits):

    halopath = Directory

    x_scale = Enum(['linear','log'])
    y_scale = Enum(['linear','log'])
    haloid = List( editor = CheckListEditor(values = ['190897','208737','140666','28221','147419','28188','147273','78411','131988','19910'],cols   = 5) )
    specificid = Int(0)
    #haloid = Enum(['190897','208737','140666','28221','147419','28188','147273','78411','131988','19910'])
    snapshot = Range(0,64,63)
    id_select = Int(0)
    haloidlist = List(Int)

    halo_varx  = Enum(['scale','rvir','posX','posY','posZ','mvir','m200c_all','m200b',\
                       'vmax','vrms','rs','xoff','voff','T/|U|','b_to_a','c_to_a','spin','spin_bullock',\
                       'pecVX','pecVY','pecVZ','Jx','Jy','Jz','A[x]','A[y]','A[z]'])

    halo_vary = Enum(['scale','rvir','posX','posY','posZ','mvir','m200c_all','m200b',\
                      'vmax','vrms','rs','xoff','voff','T/|U|','b_to_a','c_to_a','spin','spin_bullock',\
                      'pecVX','pecVY','pecVZ','Jx','Jy','Jz','A[x]','A[y]','A[z]'])

    plot_button = Button('Plot')
    plotxyzrvir_button = Button('Plot 3D Halo Distribution (scaled by rvir)')
    quiver_button = Button('Plot 3D Halo Velocity Field')

    min_vmag = Float
    max_vmax = Float

    jobstatus = Str

    view = View(VGroup(Item(name='halopath',style='readonly'),
                       Item(name='snapshot',label='Snapshot'),
 
                 Group(HGroup(Item(name='haloid',label='Halo ID',style='custom'),springy=True),enabled_when='len(specificid) != 0'),
                 Group(Item(name='specificid',label='Specific ID',width=-80),enabled_when='len(haloid) == 0'),

                 Group(HGroup(HGroup(Group(HGroup(VGroup(Group(Item(name='halo_varx',label='x-axis',springy=True),
                                           Item(name='halo_vary',label='y-axis',springy=True)))
                       ,label='Set Quantities',show_border=True)),enabled_when='use_common == True'),

                 

                       HGroup(Group(HGroup(VGroup(Group(Item(name='x_scale',label='x-scale',springy=True),
                              Item(name='y_scale',label='y-scale',springy=True))),label='Set Scale',show_border=True)),enabled_when='use_common == True')),

                      Item(name='jobstatus',style='readonly',label='Status'),

                       Group(Item(name='plot_button',show_label=False,springy=True),enabled_when='len(halo_type) > 0'),enabled_when='len(haloid) >= 1 or specificid != 0'),
                    Group(Item(name='haloidlist',show_label=False,style='readonly',editor=ListEditor(style='readonly',columns=6,rows=4)),label='Halo Sample',show_border=True)))
    
    def _plot_button_fired(self):
        if hasattr(self, 'display_points'):
            figure = self.main.display
            figure.clear()
            ax = figure.add_subplot(111)

        ax = self.main.display.axes[0]
        if self.specificid != 0 or len(self.haloid) >= 1:
            if len(self.haloid) >= 1:
                idlist = np.array(self.haloid)
                for halo in idlist:
                    cat = MT.MTCatalogue(self.halopath + '/trees',indexbyrsid=False,haloids=[int(halo)])
                    tree = cat[0]
                    mainbranch = tree.getMainBranch()
                    self.display_points = ax.plot(mainbranch[self.halo_varx],mainbranch[self.halo_vary],markersize=self.main.markersize,linestyle='-')

            if self.specificid != 0:
                cat = MT.MTCatalogue(self.halopath + '/trees',indexbyrsid=False,haloids=[int(self.specificid)])
                tree = cat[0]
                mainbranch = tree.getMainBranch()
                self.display_points = ax.plot(mainbranch[self.halo_varx],mainbranch[self.halo_vary],markersize=self.main.markersize,linestyle='-')
                
            ax.set_xlabel(self.halo_varx)
            ax.set_ylabel(self.halo_vary)
            ax.set_xscale(self.x_scale)
            ax.set_yscale(self.y_scale)
            ax.autoscale_view(True,True,True)
            wx.CallAfter(self.main.display.canvas.draw)
            self.jobstatus= "Quantities plotted."

    def _halo_varx_changed(self):
       self.jobstatus = "Nothing plotted."
       if hasattr(self, 'display_points'):
            figure = self.main.display
            figure.clear()
            ax = figure.add_subplot(111)

       ax = self.main.display.axes[0]
       wx.CallAfter(self.main.display.canvas.draw)

    def _halo_vary_changed(self):
       self.jobstatus = "Nothing plotted."
       if hasattr(self, 'display_points'):
            figure = self.main.display
            figure.clear()
            ax = figure.add_subplot(111)

       ax = self.main.display.axes[0]
       wx.CallAfter(self.main.display.canvas.draw)

    def _haloid_changed(self):
      self.jobstatus = "Nothing plotted."
      if hasattr(self, 'display_points'):
            figure = self.main.display
            figure.clear()
            ax = figure.add_subplot(111)

      ax = self.main.display.axes[0]
      wx.CallAfter(self.main.display.canvas.draw)

    def _specificid_changed(self):
      self.jobstatus = "Nothing plotted."
      if hasattr(self, 'display_points'):
            figure = self.main.display
            figure.clear()
            ax = figure.add_subplot(111)

      ax = self.main.display.axes[0]
      wx.CallAfter(self.main.display.canvas.draw)

    def _x_scale_changed(self):
        self.jobstatus = "Scale (x) changed."
        if hasattr(self, 'display_points'): 
               # self.display_points[0].remove()
                self.main.display.axes[0].set_xscale(self.x_scale)
                wx.CallAfter(self.main.display.canvas.draw)

    def _y_scale_changed(self):
        self.jobstatus = "Scale (y) changed."
        if hasattr(self, 'display_points'): 
                #self.display_points[0].remove()
                self.main.display.axes[0].set_yscale(self.y_scale)
                wx.CallAfter(self.main.display.canvas.draw)
                
    def __init__(self, main, **kwargs):
        HasTraits.__init__(self)
        self.main = main
        self.halo_vary = 'mvir'
        self.halo_varx = 'scale'
        self.haloidlist = self.main.candidatestab.haloid
        self.halopath = self.main.headertab.parentsimpath + 'RockstarData'


    