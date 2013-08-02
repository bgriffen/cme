from Common import *
from glob import glob

import random
import modules.convertfiles.reWriteIC as re

class InitialConditions(HasTraits):

    masterpath = Directory
    resimlagrdir = Directory
    resimlagrfile = Directory
    candidatefiledir = Directory
    candidatefilename = Str
    parentsimconf = Str
    parentsimpath = Directory
    lagroutputdir = Directory
    musicpath = Directory
    confstatus = Str
    parentseednum = Int
    parentseedlevel = Int

    parentconfstatus = Str

    lagroutputname = Str
    toplagr = Str

    cosmologylist = List( editor = CheckListEditor(values = ['WMAP1','WMAP3','WMAP5','WMAP7','WMAP9','PLANCK'],cols   = 6) )

    boxlength = List(editor = CheckListEditor(values = ['5','10','25','50','75','100','250','500'],cols= 4))
    
    zinit = Range(0,127,127)
    
    padding = List(editor = CheckListEditor(values = ['5','6','7','8','9','10'],cols=6) )
    lmin = Enum(['7','8','9','10','11','12','13','14','15'])
    #lmin = List(editor = CheckListEditor(values = ['7','8','9','10','11','12','13','14','15'],cols=9))
    lmax = List(editor = CheckListEditor(values = ['7','8','9','10','11','12','13','14'],cols=9))
    overlap = List(editor = CheckListEditor(values = ['1','2','3','4','5','6'],cols=6) )
    nrvir = List(editor = CheckListEditor(values = ['1','2','3','4','5','6','7','8','9'],cols=11))

    projopt = Enum(['xy','xz','yz'])

    baryons = Bool(False)
    use2LPT = Bool(False)
    useLLA = Bool(False)
    periodicTF = Bool(True)

    parentbox = Bool(False)
    resimbox = Bool(False)

    refx = Float
    refy = Float
    refz = Float
    extentx = Float
    extenty = Float
    extentz = Float

    boxtype = List( editor = CheckListEditor(values = ['ellipsoid','box'],cols=2))
    tranfunc = List( editor = CheckListEditor(values = ['eisenstein','bbks','camb'],cols=1))

    haloidselect = Int()
    #Enum(['190897','208737','140666','28221','147419','28188','147273','78411','131988','19910'])
    haloid = List(Int)

    #OUTPUT
    outformat = Enum(['gadget','enzo','grafic2','generic','tipsy'])
    outfilename = Str
    outpath = Str

    noutput = Int

    #POISSON
    fftfine = Bool(False)
    accuracy = Float
    presmooth = 3
    postsmooth = 3
    smoother = Str
    laplaceorder = Int
    gradorder = Int
    align = Bool(True)
    writelagrfile = Bool(False)

    centx = Float
    centy = Float
    centz = Float
    extx = Float
    exty = Float
    extz = Float
    lagrvol = Float
    lagrnpart = Int

    filestatus = Str

    xpos = Array
    ypos = Array
    zpos = Array

    rockstarhaloid = Int
    haloposx = Str
    haloposy = Str
    haloposz = Str
    halomvir = Str
    halorvir = Str

    lTF = Int(9)
    boxlevel = Int(9)
    seedinit = Int(34567)
    makeic_button = Button("Generate/Plot Lagrangian Region(s)")
    generate_button = Button("Make directories, populate with config files and run MUSIC")
    existencebutton = Button()

    view = View(Item(name='masterpath',label='Home'),
                 Tabbed(
                    Group(Item(name='toplagr' ,label='Top Dir.'),
                          Item(name='candidatefiledir' ,label='Candidate Dir.',style='readonly'),
                          Item(name='candidatefilename' ,label='Candidate List'),
                          Item(name='lagroutputdir' ,label='Output Dir.',style='readonly'),
                          Item(name='lagroutputname' ,label='Output Filename',style='readonly'),

                          Item(name='haloidselect',label='Halo ID'),
                          Item(name='nrvir',label='N*Rvir(z=0)',style='custom'),
                          Group(HGroup(Item(name='writelagrfile',label='Write File'),
                                       Item(name='makeic_button',show_label=False,springy=True),
                                       Item(name='projopt',show_label=False)),enabled_when='haloidselect in haloid'),
                          Group(Item(name='filestatus',label='Status',style='readonly')),

                          Group(HGroup(Item(name='rockstarhaloid',label='Halo ID',style='readonly',springy=True),
                                       Item(name='halomvir',label='mvir [Msol/h]',style='readonly',springy=True),
                                       Item(name='halorvir',label='rvir [kpc]',style='readonly',springy=True)),
                                HGroup(Item(name='haloposx',label='x [Mpc]',style='readonly',springy=True),
                                       Item(name='haloposy',label='y [Mpc]',style='readonly',springy=True),
                                       Item(name='haloposz',label='z [Mpc]',style='readonly',springy=True)),label='Halo Information From Parent Simulation'),

                          Group(Item(name='lagrnpart',label='# particles',style='readonly'),
                                Item(name='lagrvol',label='Minimum Cuboid Volume',style='readonly'),
                          HGroup(Item(name='centx',label='Lagrangian Center X',style='readonly',springy=True),
                                 Item(name='extx',label='Lagrangian Extent X',style='readonly',springy=True)),
                          HGroup(Item(name='centy',label='Lagrangian Center Y',style='readonly',springy=True),
                                 Item(name='exty',label='Lagrangian Extent Y',style='readonly',springy=True)),
                          HGroup(Item(name='centz',label='Lagrangian Center Z',style='readonly',springy=True),
                                 Item(name='extz',label='Lagrangian Extent Z',style='readonly',springy=True)),label='Lagrangian Information'),
                          Group(Item(name='haloid',show_label=False,style='readonly',editor=ListEditor(style='readonly',columns=6,rows=4)),label='Halo Sample',show_border=True),
                          label='Caterpillar'),

                      Group(HGroup(Item(name='parentbox',show_label=False),
                                Group(Group(Group(HGroup(Item(name='refx',label='ref_centerx',width=-60),
                                                         Item(name='refy',label='ref_centery',width=-60),
                                                         Item(name='refz',label='ref_centerz',width=-60)),

                                                  HGroup(Item(name='extentx',label='ref_extentx',width=-60),
                                                         Item(name='extenty',label='ref_extenty',width=-60),
                                                         Item(name='extentz',label='ref_extentz',width=-60)),
                                                  HGroup(HGroup(Item(name='boxlength',label='Box Length',style='custom'),                                                         ),
                                                                VGroup(Item(name='boxlevel',label='Level',width=-30),
                                                                       Item(name='seedinit',label='Seed',width=-80)))
                                                  ,enabled_when='parentbox==True')
                                                  ,enabled_when='resimbox==False')
                                                  ,show_border=True,label='parent Box')),
                            HGroup(Item(name='resimbox',show_label=False),

                              Group(Group(HGroup(Group(Item(name='parentsimpath',label='PP'),
                                                      HGroup(Item(name='parentsimconf',label='Parent Conf. File',style='readonly',width=-130),
                                                      Item(name='parentconfstatus',label='Conf. Status',style='readonly')),
                                                      HGroup(Item(name='parentseedlevel',label='Seed Level',style='readonly'),
                                                             Item(name='parentseednum',label='Seed Value',style='readonly')),
                                                      Item(name='resimlagrdir',label='Pointer Directory'),
                                                      HGroup(Item(name='haloidselect',label='HaloID'),
                                                        Item(name='resimlagrfile',label='Pointer File',springy=True)),
                                                      Item(name='nrvir',label='N*Rvir(z=0)',style='custom'))
                                       ,enabled_when='resimbox==True'),enabled_when='parentbox==False')
                                       ,show_border=True,label='Re-simulation')),

                            Group(HGroup(Group(Item(name='boxtype',label='Box Type',style='custom'),enabled_when='resimbox==True'),
                                         Group(HGroup(Item(name='zinit',label='zinit'),
                                               Item(name='lmin',label='Level Min')),enabled_when='resimbox==True or parentbox==True')),
                                  Group(Item(name='cosmologylist',label='Cosmology',style='custom'),enabled_when='resimbox==True or parentbox==True'),

                                  Group(Item(name='lmax',label='Level Max',style='custom'),
                                        Item(name='padding',label='Padding',style='custom',springy=False),
                                        Item(name='overlap',label='Overlap',style='custom'),enabled_when='resimbox==True'),show_border=True,label='Iterative Components')                            
                                  ,label='Setup'),

                            Group(Item(name='fftfine' ,label='fft_fine'),
                                  Item(name='accuracy'       ,label='accuracy',width=-80),
                                  Item(name='presmooth'      ,label='pre_smooth',width=-60),
                                  Item(name='postsmooth'     ,label='post_smooth',width=-60),
                                  Item(name='smoother',label='smoother',width=-60),
                                  Item(name='laplaceorder'   ,label='laplace_order',width=-60),
                                  Item(name='gradorder'      ,label='grad_order',width=-60),
                                  
                                  HGroup(Item(name='baryons'        ,label='Baryons'),
                                                      Item(name='use2LPT'        ,label='use_2LPT'),
                                                      Item(name='useLLA'         ,label='use_LLA'),
                                                      Item(name='tranfunc'       ,label='Trans. Func.')),
                                                HGroup(Item(name='periodicTF'     ,label='periodicTF'),
                                                       Item(name='align',label='align_top'),
                                                       Item(name='lTF',label='levelmin_TF'))
                                                ,label='Options'),

                            Group(Group(Item(name='outformat',show_label=False,style='custom')),
                                  HGroup(Item(name='noutput',label='# outputs',width=-30),
                                         Item(name='outpath',label='File Dir.',springy=True)),
                                  Group(Item(name='outfilename',label='IC File Name')),
                                  Item(name='confstatus',label='Status',style='readonly'),
                                  Group(Item(name='generate_button',show_label=False),enabled_when='haloidselect in haloid'),label='Output')))

    def _parentbox_changed(self):
        if self.parentbox == True:
            self.resimbox = False

    def _resimbox_changed(self):
        if self.resimbox == True:
            self.parentbox = False

    def _generate_button_fired(self):
      if self.haloidselect in self.haloid:
          if self.parentbox == True:
              for cosmi in self.cosmologylist:
                  for boxlengthi in self.boxlength:
                      foldername = cosmi + \
                                  '_L' + str(boxlengthi) + \
                                  '_Z' + str(self.zinit) + \
                                  '_LMIN' + str(self.boxlevel)
  
                      #filepath = self.outpath + 'halos/H' + str(self.haloid) + '/' + foldername
  
                      if not os.path.exists(self.outpath + 'parent/'):
                          os.makedirs(self.outpath + 'parent/')
  
                      if not os.path.exists(self.outpath + 'parent/' + foldername):
                          os.makedirs(self.outpath + 'parent/' + foldername)
  
                      writepath = self.outpath + 'parent/' + foldername
                      confname = self.outpath + 'parent/' + foldername + '/' + foldername + '.conf'
  
  
                      omegam,omegal,omegab,hubble,sigma8,nspec = cosmoconstant(cosmi)
  
                      baryonsstr = determineboolstr(self.baryons)
                      use2LPTstr = determineboolstr(self.use2LPT)
                      useLLAstr = determineboolstr(self.useLLA)
                      periodicTFstr = determineboolstr(self.periodicTF)
                      fftfinestr = determineboolstr(self.fftfine)
                      alignstr = determineboolstr(self.align)
                      padding = 8
                      overlap = 4
  
                      constructparentconf(confname,boxlengthi,self.zinit,self.lTF,padding,overlap,self.refx,self.refy,self.refz, \
                                         self.extentx,self.extenty,self.extentz,alignstr,baryonsstr,use2LPTstr,useLLAstr,omegam,omegal,omegab,hubble, \
                                         sigma8,nspec,self.tranfunc[0],self.seedinit,self.outformat,'./' + self.outfilename,fftfinestr,self.accuracy,self.presmooth,self.postsmooth, \
                                         self.smoother,self.laplaceorder,self.gradorder,self.boxlevel,periodicTFstr,self.noutput)
  
                      self.confstatus = 'Generated halo configuration files.'
                      runmusic = self.musicpath + '/MUSIC ' + confname
                      cding = "cd " + writepath
                      print "EXECUTING..."
                      print runmusic
                      subprocess.call(';'.join([cding, runmusic]), shell=True)
                      re.getBlocks(writepath)
  
          else:
              for cosmi in self.cosmologylist:
                  for boxtypei in self.boxtype:
                      for nrviri in self.nrvir:
                          for paddingi in self.padding:
                              for lmini in self.lmin:
                                  for lmaxi in self.lmax:
                                    for overlapi in self.overlap:
                                        foldername = 'H' + str(self.haloidselect) + \
                                                    '_B' + str(boxtypei.upper())[0] + \
                                                    '_Z' + str(self.zinit) + \
                                                    '_P' + str(paddingi) + \
                                                    '_LN' + str(lmini) + \
                                                    '_LX' + str(lmaxi) + \
                                                    '_O' + str(overlapi) + \
                                                    '_NV' + str(nrviri)
                                        
                                        filepath = self.outpath + 'halos/H' + str(self.haloidselect) + '/' + foldername
  
                                        if os.path.exists(filepath):
                                            self.confstatus = 'DIR EXIST!'
  
                                        elif not os.path.exists(filepath):
                                            os.makedirs(filepath)
  
                                            pointfile = self.outpath  + 'ics/lagr/H' + str(self.haloidselect) + 'NRVIR' + str(int(nrviri))
                                            writepath = filepath 
                                            #self.outpath + 'halos/' + foldername
                                            confname = filepath + '/' + foldername + '.conf'
                                            #self.outpath + 'halos/' + foldername + '/' + foldername + '.conf'
          
                                            self.centx,self.centy,self.centz,self.extx,self.exty,self.extz = getcentext(pointfile + '.head')
          
                                            omegam,omegal,omegab,hubble,sigma8,nspec = cosmoconstant(cosmi)
      
                                            baryonsstr = determineboolstr(self.baryons)
                                            use2LPTstr = determineboolstr(self.use2LPT)
                                            useLLAstr = determineboolstr(self.useLLA)
                                            periodicTFstr = determineboolstr(self.periodicTF)
                                            fftfinestr = determineboolstr(self.fftfine)
                                            alignstr = determineboolstr(self.align)
                                            boxlength = 100
              
                                            constructresimconf(confname,boxlength,self.zinit,lmini,self.lTF,lmaxi,paddingi,overlapi,self.refx,self.refy,self.refz, \
                                                                   self.extentx,self.extenty,self.extentz,alignstr,baryonsstr,use2LPTstr,useLLAstr,omegam,omegal,omegab,hubble, \
                                                                   sigma8,nspec,self.tranfunc[0],self.parentseednum,self.parentseedlevel,self.outformat,'./' + self.outfilename,fftfinestr,self.accuracy,self.presmooth,self.postsmooth, \
                                                                   self.smoother,self.laplaceorder,self.gradorder,self.boxlevel,periodicTFstr,pointfile,boxtypei,self.noutput)
                                            
                                            self.confstatus = 'Generated halo configuration files.'
                                            runmusic = self.musicpath + '/MUSIC ' + confname
                                            cding = "cd " + writepath
                                            print "EXECUTING..."
                                            print runmusic
                                            subprocess.call(';'.join([cding, runmusic]), shell=True)
                                            #cpconvert = "cp ./lib/reWriteIC.py ./lib/convertics.py " + writepath
                                            #runconvert = "python convertics.py"
                                            #rmconvert = "rm reWriteIC.py convertics.py"
                                            re.getBlocks(writepath)
                                            #subprocess.call(';'.join([cpconvert,cding,runconvert,rmconvert]), shell=True)
      else:
        self.confstatus = "Please select only IDs from list."

    def _masterpath_changed(self):
      self.candidatefiledir = self.main.headertab.datamasterpath
      self.main.headertab.masterpath = self.masterpath
      #self.main.existencetab.masterpath = self.masterpath
      #self.lagroutputdir = self.main.headertab.masterpath + '/' + self.toplagr

    def _haloidselect_changed(self):
      self.lagroutputname = 'HALO' + str(self.haloidselect) + 'NRVIR' + str(self.nrvir)
      self.resimlagrfile = 'halos' + str(self.toplagr) + '/H' + str(self.haloidselect) + 'NRVIR' + str(self.nrvir)

      self._existencebutton_fired()

    def _nrvir_changed(self):
      self.lagroutputname = 'HALO' + str(self.haloidselect) + 'NRVIR' + str(self.nrvir)
      self.resimlagrfile = str(self.toplagr) + '/H' + str(self.haloidselect) + 'NRVIR' + str(self.nrvir)
      self._existencebutton_fired()

    def _toplagr_changed(self):
      self.lagroutputdir = str(self.main.headertab.datamasterpath) + str(self.toplagr)
      self.lagroutputname = 'H' + str(self.haloidselect) + 'NRVIR' + str(self.nrvir)
      self.resimlagrfile = str(self.toplagr) + '/H' + str(self.haloidselect) + 'NRVIR' + str(self.nrvir)
      self._existencebutton_fired()

    def _resimlagrdir_changed(self):
      self.resimlagrdir = str(self.main.headertab.datamasterpath)
      self.resimlagrfile = str(self.toplagr) + '/H' + str(self.haloidselect) + 'NRVIR' + str(self.nrvir)

    def _resimlagrfile_changed(self):
      self.resimlagrdir = str(self.main.headertab.datamasterpath)
      self.resimlagrfile = str(self.toplagr) + '/H' + str(self.haloidselect) + 'NRVIR' + str(self.nrvir)

    def _parentsimpath_changed(self):
      if len(os.path.basename(glob(self.parentsimpath + "*.conf")[0])) == 1:
         self.parentsimconf = os.path.basename(glob(self.parentsimpath + "*.conf")[0])
         self.parentconfstatus = "Proceed."
      else:
         self.parentconfstatus = "Cannot locate file."

    def _existencebutton_fired(self):
        if len(self.nrvir) == 1:
            filename = self.lagroutputdir + '/H' + str(self.haloidselect) + 'NRVIR' + str(int(self.nrvir[0]))
            try:
                with open(filename):
                    self.filestatus = 'Lagrangian file exists.'
            except IOError:
                self.filestatus = 'Does not exist.'

        elif len(self.nrvir) == 0:
            self.filestatus = 'Select one nrvir value.'

        elif len(self.nrvir) > 1:
            self.filestatus = 'Select only one nrvir value if you want a plot.'

    def _projopt_changed(self):
        if len(self.xpos) > 0 and len(self.nrvir) == 1:
            figure = self.main.display
            figure.clear()
            ax = figure.add_subplot(111)
            if self.projopt == 'xy':
                xbox = self.centx - 0.5*self.extx
                ybox = self.centy - 0.5*self.exty
                xext = self.extx
                yext = self.exty
                xtmp = self.xpos
                ytmp = self.ypos
                xlabel = 'x-pos'
                ylabel = 'y-pos'
             
            if self.projopt == 'xz':
                xbox = self.centx - 0.5*self.extx
                ybox = self.centz - 0.5*self.extz
                xext = self.extx
                yext = self.extz
                xtmp = self.xpos
                ytmp = self.zpos
                xlabel = 'x-pos'
                ylabel = 'z-pos'
    
            if self.projopt == 'yz':
                xbox = self.centy - 0.5*self.exty
                ybox = self.centz - 0.5*self.extz
                xext = self.exty
                yext = self.extz
                xtmp = self.ypos
                ytmp = self.zpos
                xlabel = 'y-pos'
                ylabel = 'z-pos'
    
            ax = self.main.display.axes[0]
            ax.add_patch(patches.Rectangle((xbox,ybox),xext,yext,facecolor='none',
                                                                edgecolor=self.main.markercolor,
                                                                linestyle='dashed'))
            ax.plot(xtmp,ytmp,color=self.main.markercolor,
                             marker=self.main.markerstyle,
                             markersize=self.main.markersize,
                             markeredgewidth=0.0,
                             linestyle='None')
            ax.set_xlim(xtmp.min()*0.9,xtmp.max()*1.1)
            ax.set_ylim(ytmp.min()*0.9,ytmp.max()*1.1)
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            wx.CallAfter(self.main.display.canvas.draw)
        else:
            if len(self.xpos) == 0:
                self.filestatus = 'No data to manipulate.'

            if len(self.nrvir) > 1:
                self.filestatus = 'Too many nrvir values selected.'

            if len(self.nrvir) == 0:
                self.filestatus = 'No nrvir values selected.'

            pass

    def _makeic_button_fired(self):
        for Nrvir in self.nrvir:
            filename = self.lagroutputdir + '/H' + str(self.haloidselect) + 'NRVIR' + str(int(Nrvir))
            try:
                with open(filename):
                    if len(self.nrvir) == 1:
                        print "Visualising:", 'HALO' + str(self.haloidselect) + 'NRVIR' + str(int(self.nrvir[0]))
                        figure = self.main.display
                        figure.clear()
                        ax = figure.add_subplot(111)
        
                        self.xpos,self.ypos,self.zpos = getlagrxyz(filename)

                        self.centx,self.centy,self.centz,self.extx,self.exty,self.extz = getcentext(filename + '.head')
        
                        if self.projopt == 'xy':
                            xbox = self.centx - 0.5*self.extx
                            ybox = self.centy - 0.5*self.exty
                            xext = self.extx
                            yext = self.exty
                            xtmp = self.xpos
                            ytmp = self.ypos
                            xlabel = 'x-pos'
                            ylabel = 'y-pos'
                            
                        if self.projopt == 'xz':
                            xbox = self.centx - 0.5*self.extx
                            ybox = self.centz - 0.5*self.extz
                            xext = self.extx
                            yext = self.extz
                            xtmp = self.xpos
                            ytmp = self.zpos
                            xlabel = 'x-pos'
                            ylabel = 'z-pos'
                
                        if self.projopt == 'yz':
                            xbox = self.centy - 0.5*self.exty
                            ybox = self.centz - 0.5*self.extz
                            xext = self.exty
                            yext = self.extz
                            xtmp = self.ypos
                            ytmp = self.zpos
                            xlabel = 'y-pos'
                            ylabel = 'z-pos'
                
                        ax = self.main.display.axes[0]
                        self.lagrnpart = len(xtmp)
                        self.lagrvol = self.extx*self.exty*self.extz
                        ax.add_patch(patches.Rectangle((xbox,ybox),xext,yext,facecolor='none',
                                                                            edgecolor=self.main.markercolor,
                                                                            linestyle='dashed'))
                        ax.plot(xtmp,ytmp,color=self.main.markercolor,
                                         marker=self.main.markerstyle,
                                         markersize=self.main.markersize,
                                         markeredgewidth=0.0,
                                         linestyle='None')
                        ax.set_xlim(xtmp.min()*0.9,xtmp.max()*1.1)
                        ax.set_ylim(ytmp.min()*0.9,ytmp.max()*1.1)
                        ax.set_xlabel(xlabel)
                        ax.set_ylabel(ylabel)
                        wx.CallAfter(self.main.display.canvas.draw)
    
                    else:
                        self.filestatus = 'Not plotting more than one region, select only one nrvir value!'
                        figure = self.main.display
                        figure.clf()
                        ax = figure.add_subplot(111)

            except IOError:
                try:
                    with open(self.candidatefiledir + self.candidatefilename): pass
                except IOError:
                    print 'CANT FIND CANDIDATE LIST - CHECK DIRECTORIES!'
                    return

                if self.writelagrfile == False and len(self.nrvir) != 1:
                    self.filestatus = 'Cant plot, wont write! I do nothing then!'
                    return

                halopath = self.main.headertab.parentsimpath + 'RockstarData'
                halodata = RSDataReader.RSDataReader(halopath,63,digits=2)
                allhalos = halodata.get_hosts()
                idhalo = int(self.haloidselect)
                idcand = getcandidatelist(self.candidatefiledir + self.candidatefilename)
                idcand = idcand[:,0]
                for index in xrange(0,len(idcand)):
                    if idcand[index] == idhalo:
                        nhalo = index
        
                rvircand = allhalos.ix[idhalo]['rvir']
                mvircand = allhalos.ix[idhalo]['mvir']
                posXcand = allhalos.ix[idhalo]['posX']
                posYcand = allhalos.ix[idhalo]['posY']
                posZcand = allhalos.ix[idhalo]['posZ']
        
                ext = "/512Parent/outputs/snapdir_063/snap_063"
                header=rsHD.snapshot_header(self.main.headertab.parentsimpath+ext)
        
                print "------------------------------------------------"
                print "Rockstar ID inside parent simulation: ",idhalo
                print "------------------------------------------------"
                print "            Index:",nhalo
                print "            x-pos:",'{:.2f}'.format(float(allhalos.ix[idhalo]['posX'])), "   \ [Mpc/h]"
                print "            y-pos:",'{:.2f}'.format(float(allhalos.ix[idhalo]['posY'])), "   \ [Mpc/h]"
                print "            z-pos:",'{:.2f}'.format(float(allhalos.ix[idhalo]['posZ'])), "   \ [Mpc/h]"
                print "      virial mass:",'{0:.2e}'.format(float(allhalos.ix[idhalo]['mvir'])/header.hubble),"\ [Msol]"
                print "    virial radius:",'{:.2f}'.format(float(allhalos.ix[idhalo]['rvir'])),"  \ [kpc]"
                print "------------------------------------------------"

                self.rockstarhaloid = idhalo
                self.haloposx = '{:.2f}'.format(float(allhalos.ix[idhalo]['posX']))
                self.haloposy = '{:.2f}'.format(float(allhalos.ix[idhalo]['posY']))
                self.haloposz = '{:.2f}'.format(float(allhalos.ix[idhalo]['posZ']))
                self.halomvir = '{0:.2e}'.format(float(allhalos.ix[idhalo]['mvir'])/header.hubble)
                self.halorvir = '{:.2f}'.format(float(allhalos.ix[idhalo]['rvir']))

                for Nrvir in self.nrvir:
                    print 'Constructing: H' + str(self.haloidselect) + 'NRVIR' + str(int(Nrvir))
                    Nrvir = float(Nrvir)
                    ext = "/512Parent/outputs/snapdir_063/snap_063"
                    snapPOS = rsHD.read_block(self.main.headertab.parentsimpath+ext,"POS ")
                    dx = allhalos.ix[idhalo]['posX'] - snapPOS[:,0]
                    dy = allhalos.ix[idhalo]['posY'] - snapPOS[:,1]
                    dz = allhalos.ix[idhalo]['posZ'] - snapPOS[:,2]
                    R = np.sqrt(dx**2. + dy**2. + dz**2.)
                    Rindex = np.where(R < Nrvir*rvircand/1000)
                    currentpos = snapPOS[Rindex[0]]
                    del snapPOS, dx, dy, dz
                
                    snapIDS=rsHD.read_block(self.main.headertab.parentsimpath+ext,"ID  ")
                    regionIDS = snapIDS[Rindex[0]]
                    del snapIDS
    
                    extics = "/512Parent/ics/ics"
                    snapIDSlagr = rs.read_block(self.main.headertab.parentsimpath+extics,"ID  ",doubleprec=False)
                    mask = np.in1d(snapIDSlagr,regionIDS,assume_unique=True)
                    del snapIDSlagr
                    snapPOSlagr = rs.read_block(self.main.headertab.parentsimpath+extics,"POS ",doubleprec=False)
                    lagrPos=snapPOSlagr[mask]
                    del mask, regionIDS
    
                    CorrectPos(lagrPos[:,0],header.boxsize)
                    CorrectPos(lagrPos[:,1],header.boxsize)
                    CorrectPos(lagrPos[:,2],header.boxsize)
                    comV=COM(lagrPos[:,0],lagrPos[:,1],lagrPos[:,2])
                    self.centx=comV[0]/header.boxsize
                    self.centy=comV[1]/header.boxsize
                    self.centz=comV[2]/header.boxsize
                    dx=max(abs(lagrPos[:,0]-comV[0]))
                    dy=max(abs(lagrPos[:,1]-comV[1]))
                    dz=max(abs(lagrPos[:,2]-comV[2]))
                    self.extx=2.0*dx*1.12/header.boxsize
                    self.exty=2.0*dy*1.12/header.boxsize
                    self.extz=2.0*dz*1.12/header.boxsize
    
                    if len(self.nrvir) == 1:
                        print "Visualising:", 'HALO' + str(self.haloidselect) + 'NRVIR' + str(int(self.nrvir[0]))
                        figure = self.main.display
                        figure.clear()
                        ax = figure.add_subplot(111)

                        self.xpos = lagrPos[:,0]
                        self.ypos = lagrPos[:,1]
                        self.zpos = lagrPos[:,2]

                        if self.projopt == 'xy':
                            xbox = self.centx - 0.5*self.extx
                            ybox = self.centy - 0.5*self.exty
                            xext = self.extx
                            yext = self.exty
                            xtmp = self.xpos
                            ytmp = self.ypos
                            xlabel = 'x-pos'
                            ylabel = 'y-pos'
                            
                        if self.projopt == 'xz':
                            xbox = self.centx - 0.5*self.extx
                            ybox = self.centz - 0.5*self.extz
                            xext = self.extx
                            yext = self.extz
                            xtmp = self.xpos
                            ytmp = self.zpos
                            xlabel = 'x-pos'
                            ylabel = 'z-pos'
                
                        if self.projopt == 'yz':
                            xbox = self.centy - 0.5*self.exty
                            ybox = self.centz - 0.5*self.extz
                            xext = self.exty
                            yext = self.extz
                            xtmp = self.ypos
                            ytmp = self.zpos
                            xlabel = 'y-pos'
                            ylabel = 'z-pos'
                
                        ax = self.main.display.axes[0]
                        self.lagrnpart = len(lagrPos[:,1])
                        self.lagrvol = self.extx*self.exty*self.extz
                        ax.add_patch(patches.Rectangle((xbox,ybox),xext,yext,facecolor='none',
                                                                            edgecolor=self.main.markercolor,
                                                                            linestyle='dashed'))
                        ax.plot(xtmp,ytmp,color=self.main.markercolor,
                                         marker=self.main.markerstyle,
                                         markersize=self.main.markersize,
                                         markeredgewidth=0.0,
                                         linestyle='None')
                        ax.set_xlim(xtmp.min()*0.9,xtmp.max()*1.1)
                        ax.set_ylim(ytmp.min()*0.9,ytmp.max()*1.1)
                        ax.set_xlabel(xlabel)
                        ax.set_ylabel(ylabel)
                        wx.CallAfter(self.main.display.canvas.draw)

                        self.xpos = lagrPos[:,0]
                        self.ypos = lagrPos[:,1]
                        self.zpos = lagrPos[:,2]

                    if self.writelagrfile == True:
                        headerfilename = self.lagroutputdir + '/H' + str(self.haloidselect) + 'NRVIR' + str(int(Nrvir)) + '.head'
                        f1=open(headerfilename,'w')
                        f1.write('#' + str(self.centx) + '\n')
                        f1.write('#' + str(self.centy) + '\n')
                        f1.write('#' + str(self.centz) + '\n')
                        f1.write('#' + str(self.extx) + '\n')
                        f1.write('#' + str(self.exty) + '\n')
                        f1.write('#' + str(self.extz) + '\n')
                        f1.close()

                        filename = self.lagroutputdir + '/H' + str(self.haloidselect) + 'NRVIR' + str(int(Nrvir))
                        f2=open(filename,'w')
                        for iv in xrange(0,len(lagrPos[:,0])):
                            f2.write(str(lagrPos[iv,0]/header.boxsize)+' '+str(lagrPos[iv,1]/header.boxsize)+' '+ str(lagrPos[iv,2]/header.boxsize)+'\n')                
                        f2.close()
    
                        print "Region constructed!"


    def __init__(self, main, **kwargs):
        HasTraits.__init__(self)
        self.main = main
        self.musicpath = self.main.headertab.musicpath
        self.haloid = self.main.candidatestab.haloid

        self.candidatefiledir = self.main.headertab.datamasterpath
        self.candidatefilename = 'candidates.dat'

        self.toplagr = 'lagr'
        self.lagroutputdir = self.main.headertab.datamasterpath + 'ics/' + self.toplagr

        self.accuracy = 0.00001
        self.fftfine = True
        self.pre_smooth = 3
        self.post_smooth = 3
        self.smoother = 'gs'
        self.projopt = 'xy'
        self.tranfunc = ['eisenstein']
        self.cosmologylist = ['PLANCK']
        self.laplaceorder = 6
        self.grad_order = 6
        self.lagroutput = str(self.main.headertab.masterpath) + '/' + str(self.toplagr) + '/H' + str(self.haloidselect) + 'NRVIR' + str(self.nrvir)
        self.resimlagrdir = str(self.main.headertab.datamasterpath)
        self.resimlagrfile = '/' + str(self.toplagr) + '/H' + str(self.haloidselect) + 'NRVIR' + str(self.nrvir)
        self.masterpath = self.main.headertab.masterpath
        self.outfilename = 'ics'
        self.parenticpath = self.main.headertab.parentsimpath + 'RockstarData/ics/'
        self.outpath = str(self.main.headertab.datamasterpath)
        self.refx = 0.5
        self.refy = 0.5
        self.refz = 0.5
        self.extentx = 0.2
        self.extenty = 0.2
        self.extentz = 0.2
        self.padding = ['7']
        self.overlap = ['4']
        self.lmax = ['10']
        self.gradorder = 6
        self.noutput = 4
        #self.parentsimconf = 'ics_example.conf'
        self.parentsimpath = self.main.headertab.parentsimpath + '512Parent/ics/'
        self.parentsimconf = os.path.basename(glob(self.parentsimpath + "*.conf")[0])
        self.resimdir = str(self.main.headertab.datamasterpath) + str(self.toplagr) + 'H' + str(self.haloidselect) + 'NRVIR' + str(self.nrvir)
        filename = self.parentsimpath + self.parentsimconf
        self.parentseedlevel = 9
        self.parentseednum = 34567

        try:
            with open(filename):
                self.parentconfstatus = "Proceed"
        except IOError:
           self.parentconfstatus = "Cannot locate file."

def constructresimconf(confname,boxlength,zstart,lmin,lTF,lmax,padding,overlap,refcentx,refcenty,refcentz, \
                        refextx,refexty,refextz,align,baryons,use2LPT,useLLA,omegam,omegal,omegab,hubble, \
                        sigma8,nspec,transfer,seednum,seedlevel,outformat,icfilename,fftfine,accuracy,presmooth,postsmooth, \
                        smoother,laplaceorder,gradorder,boxlevel,periodicTFstr,pointfile,boxtype,noutput):

    f = open(confname,'w')
    f.write('[setup]' + '\n')
    f.write('boxlength            = ' + str(boxlength) + '\n')
    f.write('zstart               = ' + str(zstart) + '\n')
    f.write('levelmin             = ' + str(lmin) + '\n')
    f.write('levelmin_TF          = ' + str(lTF) + '\n')
    f.write('levelmax             = ' + str(lmax) + '\n')
    f.write('padding              = ' + str(padding) + '\n')
    f.write('overlap              = ' + str(overlap) + '\n')
    f.write('region               = ' + str(boxtype) + '\n')

    if boxtype == 'box':
        f.write('ref_center           = ' + str(refcentx) + ', ' + str(refcenty) + ', ' + str(refcentz) + '\n')
        f.write('ref_extent           = ' + str(refextx) + ', ' + str(refexty) + ', ' + str(refextz) + '\n')

    f.write('region_point_file    = ' + str(pointfile) + '\n')
    f.write('align_top            = ' + str(align) + '\n')
    f.write('baryons              = ' + str(baryons) + '\n')
    f.write('use_2LPT             = ' + str(use2LPT) + '\n')
    f.write('use_2LLA             = ' + str(useLLA) + '\n')
    f.write('periodic_TF          = ' + str(periodicTFstr) + '\n')
    f.write('\n')
    f.write('[cosmology]'+ '\n')
    f.write('Omega_m              = ' + str(omegam) + '\n')
    f.write('Omega_L              = ' + str(omegal) + '\n')
    f.write('Omega_b              = ' + str(omegab) + '\n')
    f.write('H0                   = ' + str(hubble) + '\n')
    f.write('sigma_8              = ' + str(sigma8) + '\n')
    f.write('nspec                = ' + str(nspec) + '\n')
    f.write('transfer             = ' + str(transfer) + '\n')
    f.write('\n')
    f.write('[random]' + '\n')

    diff = int(lmax)+1 - int(lmin)
    print diff
    print int(lmax),int(lmin)
    seednumnew = random.sample(range(1000,9999), diff)

    seedi = 0
    for level in range(int(lmin),int(lmax)+1):
        if level != seedlevel:
            seeduse = seednumnew[seedi]
            f.write('seed[' + str(level) + ']              = ' + str(seeduse) + '\n')
            seedi += 1
    
    f.write('seed[' + str(seedlevel) + ']              = ' + str(seednum) + '\n')

    f.write('\n')
    f.write('[output]' + '\n')

    if outformat == 'music':
        outformat = 'generic'

    if outformat == 'gadget':
        outformat = 'gadget2'

    f.write('format               = ' + str(outformat) + '\n')
    f.write('filename             = ' + str(icfilename) + '\n')
    f.write('gadget_num_files     = ' + str(noutput) + '\n')
    f.write('\n')
    f.write('[poisson]' + '\n')
    f.write('fft_fine             = ' + str(fftfine) + '\n')
    f.write('accuracy             = ' + str(accuracy) + '\n')
    f.write('pre_smooth           = ' + str(presmooth) + '\n')
    f.write('post_smooth          = ' + str(postsmooth) + '\n')
    f.write('smoother             = ' + str(smoother)  + '\n')
    f.write('laplace_order        = ' + str(laplaceorder) + '\n')
    f.write('grad_order           = ' + str(gradorder) + '\n')
    f.close()

def constructparentconf(confname,boxlength,zinit,lTF,padding,overlap,refcentx,refcenty,refcentz, \
                         refextx,refexty,refextz,align,baryons,use2LPT,useLLA,omegam,omegal,omegab,hubble, \
                         sigma8,nspec,transfer,seed,outformat,icfilename,fftfine,accuracy,presmooth,postsmooth, \
                         smoother,laplaceorder,gradorder,boxlevel,periodicTFstr,noutput):
    
    f = open(confname,'w')
    f.write('[setup]' + '\n')
    f.write('boxlength            = ' + str(boxlength) + '\n')
    f.write('zstart               = ' + str(zinit) + '\n')
    f.write('levelmin             = ' + str(boxlevel) + '\n')
    f.write('levelmin_TF          = ' + str(lTF) + '\n')
    f.write('levelmax             = ' + str(boxlevel) + '\n')
    f.write('padding              = ' + str(padding) + '\n')
    f.write('overlap              = ' + str(overlap) + '\n')
    f.write('ref_center           = ' + str(refcentx) + ', ' + str(refcenty) + ', ' + str(refcentz) + '\n')
    f.write('ref_extent           = ' + str(refextx) + ', ' + str(refexty) + ', ' + str(refextz) + '\n')
    f.write('align_top            = ' + str(align) + '\n')
    f.write('baryons              = ' + str(baryons) + '\n')
    f.write('use_2LPT             = ' + str(use2LPT) + '\n')
    f.write('use_2LLA             = ' + str(useLLA) + '\n')
    f.write('periodic_TF          = ' + str(periodicTFstr) + '\n')
    f.write('\n')
    f.write('[cosmology]'+ '\n')
    f.write('Omega_m              = ' + str(omegam) + '\n')
    f.write('Omega_L              = ' + str(omegal) + '\n')
    f.write('Omega_b              = ' + str(omegab) + '\n')
    f.write('H0                   = ' + str(hubble) + '\n')
    f.write('sigma_8              = ' + str(sigma8) + '\n')
    f.write('nspec                = ' + str(nspec) + '\n')
    f.write('transfer             = ' + str(transfer) + '\n')
    f.write('\n')
    f.write('[random]' + '\n')
    f.write('seed[' + str(boxlevel) + ']              = ' + str(seed) + '\n')

    f.write('\n')
    f.write('[output]' + '\n')

    if outformat == 'music':
        outformat = 'generic'

    if outformat == 'gadget':
        outformat = 'gadget2'

    f.write('format               = ' + str(outformat) + '\n')
    f.write('filename             = ' + str(icfilename) + '\n')
    f.write('gadget_num_files     = ' + str(noutput) + '\n')
    f.write('\n')
    f.write('[poisson]' + '\n')
    f.write('fft_fine             = ' + str(fftfine) + '\n')
    f.write('accuracy             = ' + str(accuracy) + '\n')
    f.write('pre_smooth           = ' + str(presmooth) + '\n')
    f.write('post_smooth          = ' + str(postsmooth) + '\n')
    f.write('smoother             = ' + str(smoother)  + '\n')
    f.write('laplace_order        = ' + str(laplaceorder) + '\n')
    f.write('grad_order           = ' + str(gradorder) + '\n')
    f.close()

def determineboolstr(boolean):
    if boolean == True:
        returnstr = 'yes'
    elif boolean == False:
        returnstr = 'no'

    return returnstr

