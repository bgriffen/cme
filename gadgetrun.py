from Common import *
import mergertrees.MTCatalogue as MT

class GadgetRun(HasTraits):
  #clusteropt = List()
  
  PBSncores = Range(0,64,8)
  PBSnnodes = Range(0,10,8)
  PBSuser = Str("bgriffen")
  PBSemail = Str("bgriffen@space.mit.edu")
  PBSjobname = Str()
  PBSqueue = Str("default")
  PBSoutputfile = Str("OUTPUT")
  PBSerrorfile = Str("ERROR")
  PBSextraflags = Str("#PBS -be ")
  PBSextralines = Str(". /opt/torque/etc/openmpi-setup.sh")
  PBSexecute = Str()
  compilegadopt = Bool(False)
  InitCondFile = Str()
  OutputDir = Str()
  EnergyFile = Str()
  InfoFile  = Str()
  TimingsFile = Str()
  CpuFile = Str()
  RestartFile = Str()
  SnapshotFileBase = Str()
  OutputListFilename = Str()
  TimebinFile = Str()
  ICFormat = Int()
  SnapFormat = Int()
  TimeLimitCPU = Int()
  CpuTimeBetRestartFile = Int()
  ResubmitOn = Int()
  ResubmitCommand = Str()
  MaxMemSize = Int()
  PartAllocFactor = Float()
  BufferSize = Int()
  TimeBegin = Float()
  TimeMax = Float()
  ComovingIntegrationOn = Int()
  PeriodicBoundariesOn = Int()
  CoolingOn = Int()
  StarformationOn = Int()
  Omega0 = Float()
  OmegaLambda = Float()
  OmegaBaryon = Float()
  HubbleParam = Float()
  BoxSize = Float()
  OutputListOn = Int()
  TimeBetSnapshot = Float()
  TimeOfFirstSnapshot = Float()
  TimeBetStatistics = Float()
  NumFilesPerSnapshot = Int()
  NumFilesWrittenInParallel = Int()
  TypeOfTimestepCriterion = Int()
  ErrTolIntAccuracy = Float()
  CourantFac = Float()
  MaxRMSDisplacementFac = Float()
  MaxSizeTimestep = Float()
  MinSizeTimestep = Float()
  InitGasTemp = Float()
  MinGasTemp = Float()
  TypeOfOpeningCriterion = Int()
  ErrTolTheta = Float()
  ErrTolForceAcc = Float()
  TreeDomainUpdateFrequency = Float()
  DesNumNgb = Int()
  MaxNumNgbDeviation = Int()
  UnitLength_in_cm = Float()
  UnitMass_in_g = Float()
  UnitVelocity_in_cm_per_s = Float()
  GravityConstantInternal = Int()
  MinGasHsmlFractional = Float()
  SofteningGas = Float()
  SofteningHalo = Float()
  SofteningDisk = Float()
  SofteningBulge = Float()
  SofteningStars = Float()
  SofteningBndry = Float()
  SofteningGasMaxPhys = Float()
  SofteningHaloMaxPhys = Float()
  SofteningDiskMaxPhys = Float()
  SofteningBulgeMaxPhys = Float()
  SofteningStarsMaxPhys = Float()
  SofteningBndryMaxPhys = Float()
  ArtBulkViscConst  = Float()
  levelmaxuse = Int(12)
  ErrTolThetaSubfind = Float
  DesLinkNgb = Int
  ExpansionListArr = Array

  PMGRID = Int(512)
  ENABLE_SUBFIND = Bool(False)
  FOF_SECONDARY_LINK_TYPES = Str()

  gadpath = Directory
  checkexistence_button = Button("Check Existence")
  createconfig_button = Button("Make and distribute gadget!")
  padding = List(editor = CheckListEditor(values = ['5','6','7','8','9','10'],cols=6) )
  lmin = Enum(['7','8','9','10','11','12','13','14','15'])
  lmax = List(editor = CheckListEditor(values = ['7','8','9','10','11','12','13','14'],cols=9))
  overlap = List(editor = CheckListEditor(values = ['1','2','3','4','5','6'],cols=6) )
  nrvir = List(editor = CheckListEditor(values = ['1','2','3','4','5','6','7','8','9'],cols=11))
  cosmologylist = List( editor = CheckListEditor(values = ['WMAP1','WMAP3','WMAP5','WMAP7','WMAP9','PLANCK'],cols   = 6) )
  boxtype = List( editor = CheckListEditor(values = ['ellipsoid','box'],cols=2))
  haloid = Int()
  haloidlist = List(Int)
  zinit = Range(0,127,127)
  redshifti = Float()
  expfacti = Float()
  nintervals = Enum(['32','64','128','258','512','1024'])
  snapshotlist = Str()
  alloutputopt = Bool(True)
  PBSstring = Str()
  vizexpz_button = Button("Inspect/Update List")
  subscript_button = Button("Create Submission Script")

  view = View(Group(Group(Group(
                    Item('gadpath',label='Base Path'),
                    Item(name='haloid',label='Halo ID'),
                    Item(name='nrvir',label='Nvir',style='custom'),
                    HGroup(Item(name='boxtype',label='Box Type',style='custom'),Item(name='lmin',label='Level Min'),Item(name='zinit',label='zinit')),
                    Item(name='cosmologylist',label='Cosmology',style='custom'),
                    Item(name='lmax',label='Level Max',style='custom'),
                    Item(name='padding',label='Padding',style='custom'),
                    Item(name='overlap',label='Overlap',style='custom')),
                    Group(Item('checkexistence_button',show_label=False)),
              Group(Item(name='haloidlist',show_label=False,style='readonly',editor=ListEditor(style='readonly',columns=6,rows=4)),label='Halo Sample',show_border=True)),label='Existence'),

              Group(
              Item('levelmaxuse',label='Level Max'),
              Item('InitCondFile',label='InitCondFile'),
              Item('OutputDir',label='OutputDir'),
              Item('EnergyFile',label='EnergyFile'),
              Item('InfoFile' ,label='InfoFile '),
              Item('TimingsFile',label='TimingsFile'),
              Item('CpuFile',label='CpuFile'),
              Item('RestartFile',label='RestartFile'),
              Item('SnapshotFileBase',label='SnapshotFileBase'),
              Item('OutputListFilename',label='OutputListFilename'),
              Item('TimebinFile',label='TimebinFile'),
              Item('ICFormat',label='ICFormat'),
              Item('SnapFormat',label='SnapFormat'),
              Item('TimeLimitCPU',label='TimeLimitCPU'),
              Item('CpuTimeBetRestartFile',label='CpuTimeBetRestartFile'),
              Item('ResubmitOn',label='ResubmitOn'),
              Item('ResubmitCommand',label='ResubmitCommand'),
              Item('MaxMemSize',label='MaxMemSize'),
              Item('PartAllocFactor',label='PartAllocFactor'),
              Item('BufferSize',label='BufferSize'),
              Item('TimeBegin',label='TimeBegin'),
              Item('TimeMax',label='TimeMax'),label='Format'),
              
              Group(Item('ComovingIntegrationOn',label='ComovingIntegrationOn'),
              Item('PeriodicBoundariesOn',label='PeriodicBoundariesOn'),
              Item('CoolingOn',label='CoolingOn'),
              Item('StarformationOn',label='StarformationOn'),
              Item('Omega0',label='Omega0'),
              Item('OmegaLambda',label='OmegaLambda'),
              Item('OmegaBaryon',label='OmegaBaryon'),
              Item('HubbleParam',label='HubbleParam'),
              Item('BoxSize',label='BoxSize'),
              Item('OutputListOn',label='OutputListOn'),
              Item('TimeBetSnapshot',label='TimeBetSnapshot'),
              Item('TimeOfFirstSnapshot',label='TimeOfFirstSnapshot'),
              Item('TimeBetStatistics',label='TimeBetStatistics'),
              Item('NumFilesPerSnapshot',label='NumFilesPerSnapshot'),
              Item('NumFilesWrittenInParallel',label='NumFilesWrittenInParallel'),
              Item('TypeOfTimestepCriterion',label='TypeOfTimestepCriterion'),
              Item('ErrTolIntAccuracy',label='ErrTolIntAccuracy'),
              Item('CourantFac',label='CourantFac'),
              Item('MaxRMSDisplacementFac',label='MaxRMSDisplacementFac'),
              Item('MaxSizeTimestep',label='MaxSizeTimestep'),
              Item('MinSizeTimestep',label='MinSizeTimestep'),
              Item('InitGasTemp',label='InitGasTemp'),
              Item('MinGasTemp',label='MinGasTemp'),label='Cosmology & Timestep'),

              Group(Item('TypeOfOpeningCriterion',label='TypeOfOpeningCriterion'),
              HGroup(Item('ErrTolTheta',label='ErrTolTheta'),
              Item('ErrTolForceAcc',label='ErrTolForceAcc')),
              Item('TreeDomainUpdateFrequency',label='TreeDomainUpdateFrequency'),
              Item('DesNumNgb',label='DesNumNgb'),
              Item('MaxNumNgbDeviation',label='MaxNumNgbDeviation'),
              Item('UnitLength_in_cm',label='UnitLength_in_cm'),
              Item('UnitMass_in_g',label='UnitMass_in_g'),
              Item('UnitVelocity_in_cm_per_s',label='UnitVelocity_in_cm_per_s'),
              Item('GravityConstantInternal',label='GravityConstantInternal'),
              
              Item('MinGasHsmlFractional',label='MinGasHsmlFractional'),
              Item('SofteningGas',label='SofteningGas'),
              Item('SofteningHalo',label='SofteningHalo'),
              Item('SofteningDisk',label='SofteningDisk'),
              Item('SofteningBulge',label='SofteningBulge'),
              Item('SofteningStars',label='SofteningStars'),
              Item('SofteningBndry',label='SofteningBndry'),
              Item('SofteningGasMaxPhys',label='SofteningGasMaxPhys'),
              Item('SofteningHaloMaxPhys',label='SofteningHaloMaxPhys'),
              Item('SofteningDiskMaxPhys',label='SofteningDiskMaxPhys'),
              Item('SofteningBulgeMaxPhys',label='SofteningBulgeMaxPhys'),
              Item('SofteningStarsMaxPhys',label='SofteningStarsMaxPhys'),
              Item('SofteningBndryMaxPhys',label='SofteningBndryMaxPhys'),
              Item('ArtBulkViscConst' ,label='ArtBulkViscConst '),label='Softening'),

              Group(HGroup(Item('redshifti',label='Starting Output Redshift'),Item('expfacti',label='Expansion Factor')),
                    Item('nintervals',label='Number Of Outputs',style='custom'),
                    HGroup(Item('alloutputopt',label='Output Every Snapshot?'),Group(Item('snapshotlist',label='Only Specific Snapshots (csv)',springy=True),springy=True,enabled_when='alloutputopt == False')),
                    Group(Item('vizexpz_button',show_label=False),enabled_when='haloid in haloidlist'),
                    Heading('ExpansionList Output (last two columns)'),
                    Item('ExpansionListArr',show_label = False,
                                       editor= ArrayViewEditor(titles = [ 'snapshot','redshift','exp. fact.', ' I/O' ],
                                                                    format = '%2.5e',
                                                                    show_index = False
                                                                   )),label='Exp.'),

              Group(HGroup(Item('PMGRID',label='PMGRID'),
                    Item('ENABLE_SUBFIND',label='Subfind'),
                    Group(Item('FOF_SECONDARY_LINK_TYPES',label='FOF_SECONDARY_LINK_TYPES'),enabled_when='ENABLE_SUBFIND==True',springy=True)),
                    Group(Item('createconfig_button',show_label=False),enabled_when='haloid in haloidlist'),
                    Item('_'),
                    Group(Item('clusteropt',label='Cluster',style='readonly'),
                    Item('PBSncores',label='# Cores'),
                    Item('PBSnnodes',label='# Nodes'),
                    Item('PBSuser',label='Username'),
                    Item('PBSemail',label='Email'),
                    #Item('PBSjobname',label='Job Name'),
                    Item('PBSqueue',label='Queue'),
                    Item('PBSoutputfile',label='Output File'),
                    Item('PBSerrorfile',label='Error File'),
                    Item('PBSextraflags',label='Extra Flag'),
                    Item('PBSextralines',label='Extra Lines'),
                    Item('PBSexecute',label='Execute Line')),
                    HGroup(Item('compilegadopt',label='Compile Gadget?'),Item('subscript_button',show_label=False)),
                    label='Write & Submit Job')
              )

  def _subscript_button_fired(self):
    for boxtypei in self.boxtype:
          for nrviri in self.nrvir:
              for paddingi in self.padding:
                  for lmini in self.lmin:
                      for lmaxi in self.lmax:
                          for overlapi in self.overlap:
                              foldername = 'H' + str(self.haloid) + \
                                          '_B' + str(boxtypei.upper())[0] + \
                                          '_Z' + str(self.zinit) + \
                                          '_P' + str(paddingi) + \
                                          '_LN' + str(lmini) + \
                                          '_LX' + str(lmaxi) + \
                                          '_O' + str(overlapi) + \
                                          '_NV' + str(nrviri)

                              jobname = 'H' + str(self.haloid)[0:2] + \
                                        str(boxtypei.upper())[0] + \
                                        'P' + str(paddingi) + \
                                        'L' + str(lmaxi) + \
                                        'N' + str(nrviri)

                              filepath = self.gadpath + 'halos/H' + str(self.haloid) + '/' + foldername

                              f = open(filepath + "/runscript",'w')
                              f.write("#!/bin/sh" + "\n")
                              f.write("#PBS -l nodes=" + str(self.PBSnnodes) + ":ppn=" + str(self.PBSncores) + "\n")
                              f.write("#PBS -N " + jobname + "\n")
                              f.write("#PBS -u " + self.PBSuser + "\n")
                              f.write("#PBS -q " + self.PBSqueue + "\n")
                              f.write(self.PBSextraflags + "\n")
                              f.write("\n")
                              f.write(self.PBSextralines + "\n")
                              f.write("\n")
                              f.write(self.PBSexecute)
      
                              f.close()

                              if compilegadopt == True:
                                #CONSTRUCT CONFIG FILE & RUN GADGET COMPILER
                                pass

  def _PBSncores_changed(self):
      self.PBSexecute = "mpirun -np " + str(int(self.PBSncores*self.PBSnnodes)) + " ./P-Gadget3 ./param.txt 1>" + self.PBSoutputfile + " 2>" + self.PBSerrorfile

  def _PBSnnodes_changed(self):
      self.PBSexecute = "mpirun -np " + str(int(self.PBSncores*self.PBSnnodes)) + " ./P-Gadget3 ./param.txt 1>" + self.PBSoutputfile + " 2>" + self.PBSerrorfile

  def _PBSoutputfile_changed(self):
      self.PBSexecute = "mpirun -np " + str(int(self.PBSncores*self.PBSnnodes)) + " ./P-Gadget3 ./param.txt 1>" + self.PBSoutputfile + " 2>" + self.PBSerrorfile

  def _PBSoutputfile_changed(self):
      self.PBSexecute = "mpirun -np " + str(int(self.PBSncores*self.PBSnnodes)) + " ./P-Gadget3 ./param.txt 1>" + self.PBSoutputfile + " 2>" + self.PBSerrorfile

  def _vizexpz_button_fired(self):
      figure = self.main.display
      figure.clear()
      ax = figure.add_subplot(111)
      ax = self.main.display.axes[0]

      snapshots = range(0,int(self.nintervals))
      expfact = np.linspace(self.expfacti,1,int(self.nintervals))

      ax.set_xlabel('Snapshot')
      ax.set_ylabel('Expansion Factor')
      redall = np.float64(1./expfact - 1)
    
      if self.alloutputopt == True:
          self.ExpansionListArr = np.zeros(shape=(len(snapshots),4))
          self.ExpansionListArr[:,0] = snapshots
          self.ExpansionListArr[:,1] = redall
          self.ExpansionListArr[:,2] = expfact
          self.ExpansionListArr[:,3] = np.array(len(expfact)*[1])
          self.display_points = ax.plot(snapshots,expfact,'bo')

      else:
          listin = str(self.snapshotlist)
          snapshotin = np.array(listin.split(','))
          listcomp = np.array(self.ExpansionListArr[:,0])
          self.ExpansionListArr[:,3] = np.array(len(expfact)*[0])
          for i in xrange(0,len(listcomp)):
              for j in xrange(0,len(snapshotin)):
                  if int(listcomp[i]) ==  int(snapshotin[j]):
                      self.ExpansionListArr[i,3] = 1

      self.display_points = ax.plot(snapshots,expfact,'b-')
      wx.CallAfter(self.main.display.canvas.draw)

    #      listin = str(self.specificredshift)
    #      redshiftlist =listin.split(',')
    #      io1 = []
    #      io2 = []
    #      io3 = []
    #      io4 = []
    #      for redshift in redshiftlist:
    #          redshift = float(redshift)
    #          exptmp = np.float64(1./(1+redshift))
    #          foundexp = min(range(len(expfact)), key=lambda i: abs(np.float64(expfact[i])-exptmp))
    #          ax.plot(snapshots[foundexp],expfact[foundexp],'bo')
    #          io1.append(snapshots[foundexp])
    #          io2.append(float(redshift))
    #          io3.append(expfact[foundexp])
    #          io4.append(1)

          #self.ExpansionListArr = []
     #     self.ExpansionListArr = np.zeros(shape=(len(io1),4))
     #     self.ExpansionListArr[:,0] = io1
     #     self.ExpansionListArr[:,1] = io2
     #     self.ExpansionListArr[:,2] = io3
     #     self.ExpansionListArr[:,3] = io4

      

  def _expfacti_changed(self):
    self.redshifti = 1./self.expfacti - 1

  def _redshifti_changed(self):
    self.expfacti = 1./(1 + self.redshifti)

  def _BoxSize_changed(self):
      self.SofteningGas = 0.0
      self.SofteningHalo = self.BoxSize/2**float(self.levelmaxuse)/40.
      self.SofteningDisk = 2*self.SofteningHalo 
      self.SofteningBulge = 2*self.SofteningDisk 
      self.SofteningStars = 2*self.SofteningBulge 
      self.SofteningBndry = 2*self.SofteningStars 
      self.SofteningGasMaxPhys = 0.0
      self.SofteningHaloMaxPhys = self.BoxSize/2**float(self.levelmaxuse)/40.
      self.SofteningDiskMaxPhys = 2*self.SofteningHaloMaxPhys 
      self.SofteningBulgeMaxPhys = 2*self.SofteningDiskMaxPhys 
      self.SofteningStarsMaxPhys = 2*self.SofteningBulgeMaxPhys 
      self.SofteningBndryMaxPhys = 2*self.SofteningStarsMaxPhys 

  def _levelmaxuse_changed(self):
      self.SofteningGas = 0.0
      self.SofteningHalo = self.BoxSize/2**float(self.levelmaxuse)/40.
      self.SofteningDisk = 2*self.SofteningHalo 
      self.SofteningBulge = 2*self.SofteningDisk 
      self.SofteningStars = 2*self.SofteningBulge 
      self.SofteningBndry = 2*self.SofteningStars 
      self.SofteningGasMaxPhys = 0.0
      self.SofteningHaloMaxPhys = self.BoxSize/2**float(self.levelmaxuse)/40.
      self.SofteningDiskMaxPhys = 2*self.SofteningHaloMaxPhys 
      self.SofteningBulgeMaxPhys = 2*self.SofteningDiskMaxPhys 
      self.SofteningStarsMaxPhys = 2*self.SofteningBulgeMaxPhys 
      self.SofteningBndryMaxPhys = 2*self.SofteningStarsMaxPhys 

  def makeparam(self,filename,ext,includesub):
      snapshots = range(0,int(self.nintervals))
      expfact = np.linspace(self.expfacti,1,int(self.nintervals))
      expfilename = ext + '/' + self.OutputListFilename
      f = open(expfilename,'w')

      for i in xrange(0,len(self.ExpansionListArr[:,0])):  
          f.write(str(np.float64(self.ExpansionListArr[i,2])) + ' ' + str(int(self.ExpansionListArr[i,3])) + '\n')
      
      f.close()

      f = open(filename,'w')
      f.write('%----  Relevant files' + '\n')
      f.write('InitCondFile               ' + str(self.InitCondFile) + '\n')
      f.write('OutputDir                  ' + str(self.OutputDir) + '\n')
      f.write('EnergyFile                 ' + str(self.EnergyFile) + '\n')
      f.write('InfoFile                   ' + str(self.InfoFile) + '\n')
      f.write('TimingsFile                ' + str(self.TimingsFile) + '\n')
      f.write('CpuFile                    ' + str(self.CpuFile) + '\n')
      f.write('RestartFile                ' + str(self.RestartFile) + '\n')
      f.write('SnapshotFileBase           ' + str(self.SnapshotFileBase) + '\n')
      f.write('OutputListFilename         ' + str(self.OutputListFilename) + '\n')
      f.write('TimebinFile                ' + str(self.TimebinFile) + '\n')
      f.write('\n')
      f.write('%---- File formats' + '\n')
      f.write('ICFormat                   ' + str(self.ICFormat) + '\n')
      f.write('SnapFormat                 ' + str(self.SnapFormat) + '\n')
      f.write('\n')
      f.write('%---- CPU-time limits' + '\n')
      f.write('TimeLimitCPU               ' + str(self.TimeLimitCPU) + '\n')
      f.write('CpuTimeBetRestartFile      ' + str(self.CpuTimeBetRestartFile) + '\n')
      f.write('ResubmitOn                 ' + str(self.ResubmitOn) + '\n')
      f.write('ResubmitCommand            ' + str(self.ResubmitCommand) + '\n')
      f.write('\n')
      f.write('%----- Memory alloction' + '\n')
      f.write('MaxMemSize                 ' + str(self.MaxMemSize) + '\n')
      f.write('PartAllocFactor            ' + str(self.PartAllocFactor) + '\n')
      f.write('BufferSize                 ' + str(self.BufferSize) + '\n')
      f.write('\n')
      f.write('%---- Caracteristics of run' + '\n')                                  
      f.write('TimeBegin                  ' + str(self.TimeBegin) + '\n')
      f.write('TimeMax                    ' + str(self.TimeMax) + '\n')
      f.write('\n')
      f.write('%---- Basic code options that set the type of simulation' + '\n')
      f.write('ComovingIntegrationOn      ' + str(self.ComovingIntegrationOn) + '\n')
      f.write('PeriodicBoundariesOn       ' + str(self.PeriodicBoundariesOn) + '\n')
      f.write('CoolingOn                  ' + str(self.CoolingOn) + '\n')
      f.write('StarformationOn            ' + str(self.StarformationOn) + '\n')
      f.write('\n')
      f.write('%---- Cosmological parameters' + '\n')                                  
      f.write('Omega0                     ' + str(self.Omega0) + '\n')
      f.write('OmegaLambda                ' + str(self.OmegaLambda) + '\n')
      f.write('OmegaBaryon                ' + str(self.OmegaBaryon) + '\n')
      f.write('HubbleParam                ' + str(self.HubbleParam/100) + '\n')
      f.write('BoxSize                    ' + str(self.BoxSize) + '\n')
      f.write('\n')
      f.write('%---- Tree algorithm, force accuracy, domain update frequency' + '\n')
      f.write('OutputListOn               ' + str(self.OutputListOn) + '\n')
      f.write('TimeBetSnapshot            ' + str(self.TimeBetSnapshot) + '\n')
      f.write('TimeOfFirstSnapshot        ' + str(self.TimeOfFirstSnapshot) + '\n')
      f.write('TimeBetStatistics          ' + str(self.TimeBetStatistics) + '\n')
      f.write('NumFilesPerSnapshot        ' + str(self.NumFilesPerSnapshot) + '\n')
      f.write('NumFilesWrittenInParallel  ' + str(self.NumFilesWrittenInParallel) + '\n')
      f.write('\n')
      f.write('%---- Accuracy of time integration' + '\n')
      f.write('TypeOfTimestepCriterion    ' + str(self.TypeOfTimestepCriterion) + '\n')
      f.write('ErrTolIntAccuracy          ' + str(self.ErrTolIntAccuracy) + '\n')
      f.write('CourantFac                 ' + str(self.CourantFac) + '\n')
      f.write('MaxRMSDisplacementFac      ' + str(self.MaxRMSDisplacementFac) + '\n')
      f.write('MaxSizeTimestep            ' + str(self.MaxSizeTimestep) + '\n')
      f.write('MinSizeTimestep            ' + str(self.MinSizeTimestep) + '\n')
      f.write('\n')
      #f.write('%---- Accuracy of time integration')
      f.write('InitGasTemp                ' + str(self.InitGasTemp) + '\n')
      f.write('MinGasTemp                 ' + str(self.MinGasTemp) + '\n')
      f.write('\n')
      f.write('%---- Tree algorithm, force accuracy, domain update frequency' + '\n')
      f.write('TypeOfOpeningCriterion     ' + str(self.TypeOfOpeningCriterion) + '\n')
      f.write('ErrTolTheta                ' + str(self.ErrTolTheta) + '\n')
      f.write('ErrTolForceAcc             ' + str(self.ErrTolForceAcc) + '\n')
      f.write('TreeDomainUpdateFrequency  ' + str(self.TreeDomainUpdateFrequency) + '\n')
      f.write('\n')
      f.write('%---- Initial density estimate' + '\n')
      f.write('DesNumNgb                  ' + str(self.DesNumNgb) + '\n')
      f.write('MaxNumNgbDeviation         ' + str(self.MaxNumNgbDeviation) + '\n')
      f.write('\n')
      f.write('%---- System of units' + '\n')
      f.write('UnitLength_in_cm           ' + str(self.UnitLength_in_cm) + '\n')
      f.write('UnitMass_in_g              ' + str(self.UnitMass_in_g) + '\n')
      f.write('UnitVelocity_in_cm_per_s   ' + str(self.UnitVelocity_in_cm_per_s) + '\n')
      f.write('GravityConstantInternal    ' + str(self.GravityConstantInternal) + '\n')
      f.write('\n')
      f.write('%---- Gravitational softening lengths' + '\n')
      f.write('MinGasHsmlFractional       ' + str(self.MinGasHsmlFractional) + '\n')
      f.write('\n')
      f.write('SofteningGas               ' + str(self.SofteningGas) + '\n')
      f.write('SofteningHalo              ' + str(self.SofteningHalo) + '\n')
      f.write('SofteningDisk              ' + str(self.SofteningDisk) + '\n')
      f.write('SofteningBulge             ' + str(self.SofteningBulge) + '\n')
      f.write('SofteningStars             ' + str(self.SofteningStars) + '\n')
      f.write('SofteningBndry             ' + str(self.SofteningBndry) + '\n')
      f.write('\n')
      f.write('SofteningGasMaxPhys        ' + str(self.SofteningGasMaxPhys) + '\n')
      f.write('SofteningHaloMaxPhys       ' + str(self.SofteningHaloMaxPhys) + '\n')
      f.write('SofteningDiskMaxPhys       ' + str(self.SofteningDiskMaxPhys) + '\n')
      f.write('SofteningBulgeMaxPhys      ' + str(self.SofteningBulgeMaxPhys) + '\n')
      f.write('SofteningStarsMaxPhys      ' + str(self.SofteningStarsMaxPhys) + '\n')
      f.write('SofteningBndryMaxPhys      ' + str(self.SofteningBndryMaxPhys) + '\n')
      f.write('\n')
      f.write('%---- non-common' + '\n')
      f.write('ArtBulkViscConst           ' + str(self.ArtBulkViscConst) + '\n')
                                    
      if includesub == True:
          f.write('ErrTolThetaSubfind         ' + str(self.ErrTolThetaSubfind) + '\n')
          f.write('DesLinkNgb                 ' + str(self.DesLinkNgb) + '\n')
                                    
      f.close()

  def _createconfig_button_fired(self):
      for cosmi in self.cosmologylist:
          for boxtypei in self.boxtype:
              for nrviri in self.nrvir:
                  for paddingi in self.padding:
                      for lmini in self.lmin:
                          for lmaxi in self.lmax:
                              for overlapi in self.overlap:
                                  foldername = 'H' + str(self.haloid) + \
                                              '_B' + str(boxtypei.upper())[0] + \
                                              '_Z' + str(self.zinit) + \
                                              '_P' + str(paddingi) + \
                                              '_LN' + str(lmini) + \
                                              '_LX' + str(lmaxi) + \
                                              '_O' + str(overlapi) + \
                                              '_NV' + str(nrviri)
                                  
                                  filepath = self.gadpath + 'halos/H' + str(self.haloid) + '/' + foldername
                                 
                                  if not os.path.exists(filepath):
                                      print "PATH NOT FOUND:",filepath
                                  else:
                                      print "PATH FOUND:",filepath

                                      self.levelmaxuse = int(lmaxi)
                                      #self.HubbleParam = 0.6711
                                      self.Omega0,self.OmegaLambda,self.OmegaBaryon,self.HubbleParam,sigma8,nspec = cosmoconstant(cosmi)
                                      #makeparam('param.txt',ENABLE_SUBFIND)
                                      ext = self.gadpath + 'halos/H' + str(self.haloid) + '/' + foldername
                                      if self.ENABLE_SUBFIND == True:
                                          self.makeparam('param.txt',ext,includesub=False)
                                          self.makeparam('param_sub.txt',ext,includesub=True)
                                          mving = "mv param.txt " + filepath
                                          print "Moving..."
                                          print mving
                                          subprocess.call([mving], shell=True)
                                          mving = "mv param_sub.txt " + filepath
                                          print "Moving..."
                                          print mving
                                          subprocess.call([mving], shell=True)
                                      else:
                                          self.makeparam('param.txt',ext,includesub=False)
                                          mving = "mv param.txt " + filepath
                                          print "Moving..."
                                          print mving
                                          subprocess.call([mving], shell=True)
                                      
                                      mkdirs = "mkdir -p outputs"
                                      subprocess.call([mkdirs], shell=True)

  def _checkexistence_button_fired(self):

      figure = self.main.display
      figure.clear()
      ax = figure.add_subplot(111)
    
      ax = self.main.display.axes[0]
      ax.set_xticks([])
      ax.set_yticks([])

      titlestr = 'HALO    BOXTYPE    PAD    LMIN    LMAX    NVIR    ICS    GADGET    HALOS'

      placenormtext(ax,0.03, 0.98,'HALO',10)
      placenormtext(ax,0.15, 0.98,'BOXTYPE',10)
      placenormtext(ax,0.60, 0.98,'PAD',10)
      placenormtext(ax,0.40, 0.98,'LMIN',10)
      placenormtext(ax,0.50, 0.98,'LMAX',10)
      placenormtext(ax,0.31, 0.98,'NVIR',10)
      placenormtext(ax,0.70, 0.98,'ICS',10)
      placenormtext(ax,0.77, 0.98,'GADGET',10)
      placenormtext(ax,0.91, 0.98,'HALOS',10)
      txtdisplace = 0.0
      for boxtypei in self.boxtype:
          for nrviri in self.nrvir:
              for paddingi in self.padding:
                  for lmini in self.lmin:
                      for lmaxi in self.lmax:
                          for overlapi in self.overlap:
                              foldername = 'H' + str(self.haloid) + \
                                          '_B' + str(boxtypei.upper())[0] + \
                                          '_Z' + str(self.zinit) + \
                                          '_P' + str(paddingi) + \
                                          '_LN' + str(lmini) + \
                                          '_LX' + str(lmaxi) + \
                                          '_O' + str(overlapi) + \
                                          '_NV' + str(nrviri)

                              filepath = self.gadpath + 'halos/H' + str(self.haloid) + '/' + foldername
                              
                              #print filepath
                              #print filepath + '/ics.0'
                              #print filepath + '/outputs/snapdir_064'
                              #print filepath + '/outputs/groups_064'

                              try:
                                 with open(filepath + '/ics.0'):
                                     icfound = '+'
                              except IOError:
                                 icfound = '-'

                              if os.path.exists(filepath + '/outputs/snapdir_063'):
                                   gadfound = '+'
                              else:
                                   gadfound = '-'
                        
                              if os.path.exists(filepath + '/outputs/groups_063'):
                                   halosfound = '+'
                              else:
                                   halosfound = '-'
                             
                              txtdisplace += 0.03
                              placenormtext(ax,0.02, 0.98 - txtdisplace,str(self.haloid),10)
                              placenormtext(ax,0.14, 0.98 - txtdisplace,str(boxtypei.upper()),10)
                              placenormtext(ax,0.615, 0.98 - txtdisplace,str(paddingi),10)
                              placenormtext(ax,0.42, 0.98 - txtdisplace,str(lmini),10)
                              placenormtext(ax,0.52, 0.98 - txtdisplace,str(lmaxi),10)
                              placenormtext(ax,0.325, 0.98 - txtdisplace,str(nrviri),10)
                              placenormtext(ax,0.71, 0.98 - txtdisplace,str(icfound),10)
                              placenormtext(ax,0.81, 0.98 - txtdisplace,str(gadfound),10)
                              placenormtext(ax,0.94, 0.98 - txtdisplace,str(halosfound),10)
                            
      wx.CallAfter(self.main.display.canvas.draw)                                

  def __init__(self, main, **kwargs):
      HasTraits.__init__(self)
      self.main = main
      self.nvir = ['3','4','5','6','7','8','9']
      self.padding = ['7','8','9','10']
      self.overlap = ['4']
      self.lmax = ['11']
      self.cosmologylist = ['PLANCK']
      self.haloidlist = self.main.candidatestab.haloid
      self.gadpath = self.main.headertab.datamasterpath
      self.nintervals = '64'
      self.redshifti = 46.
      self.expfacti = 1./(1.+self.redshifti)
      self.InitCondFile =        './ics_rewrite'
      self.OutputDir =           './outputs'
      self.EnergyFile =          'energy.txt'
      self.InfoFile =            'info.txt'
      self.TimingsFile =         'timings.txt'
      self.CpuFile =             'cpu.txt'
      self.RestartFile =         'restart'
      self.SnapshotFileBase =    'snap'
      self.OutputListFilename =  'ExpansionList'
      self.TimebinFile =         'timebin'
      self.ICFormat =           1
      self.SnapFormat =         1
      self.TimeLimitCPU =              340000 # in seconds
      self.CpuTimeBetRestartFile =     43200    # in seconds
      self.ResubmitOn =        0
      self.ResubmitCommand =   'my-scriptfile'
      self.MaxMemSize =        3500      # sets maximum memory use in MByte
      self.PartAllocFactor =   2.5
      self.BufferSize =        100       # in MByte
      self.TimeBegin =           0.0078125   #%z=127
      self.TimeMax =             1.0
      self.ComovingIntegrationOn =    1
      self.PeriodicBoundariesOn =     1
      self.CoolingOn =                0
      self.StarformationOn =          0
      self.Omega0 =                0.3175 # 0.276
      self.OmegaLambda =           0.6825 # 0.724
      self.OmegaBaryon =           0.0
      self.HubbleParam =           0.6711 # 0.703
      self.BoxSize =               100.0
      self.OutputListOn =              1
      self.TimeBetSnapshot =           0.0
      self.TimeOfFirstSnapshot =       0.0
      self.TimeBetStatistics =         0.01
      self.NumFilesPerSnapshot =       4
      self.NumFilesWrittenInParallel = 4
      self.TypeOfTimestepCriterion =  0
      self.ErrTolIntAccuracy =        0.012
      self.CourantFac =               0.15
      self.MaxRMSDisplacementFac =    0.125
      self.MaxSizeTimestep =          0.005
      self.MinSizeTimestep =          0.0
      self.InitGasTemp =            1000.0
      self.MinGasTemp =             5.0
      self.TypeOfOpeningCriterion =       1
      self.ErrTolTheta =                  0.6
      self.ErrTolForceAcc =               0.0025
      self.TreeDomainUpdateFrequency =    0.01
      self.DesNumNgb =              64
      self.MaxNumNgbDeviation =     1
      self.UnitLength_in_cm =         3.085678e24        #  1.0 Mpc
      self.UnitMass_in_g =            1.989e43           #  1.0e10 solar masses
      self.UnitVelocity_in_cm_per_s = 1e5                #  1 km/sec
      self.GravityConstantInternal =  0
      self.MinGasHsmlFractional = 0.25
      self.SofteningGas =    0.0
      self.SofteningHalo =   0.000610352
      self.SofteningDisk =   0.001220703
      self.SofteningBulge =  0.002441406
      self.SofteningStars =  0.004882813
      self.SofteningBndry =  0.009765625
      self.SofteningGasMaxPhys =     0.0
      self.SofteningHaloMaxPhys =    0.000610352
      self.SofteningDiskMaxPhys =    0.001220703
      self.SofteningBulgeMaxPhys =   0.002441406
      self.SofteningStarsMaxPhys =   0.004882813
      self.SofteningBndryMaxPhys =   0.009765625
      self.ArtBulkViscConst = 1.0
      self.ErrTolThetaSubfind = 0.7
      self.DesLinkNgb = 20
      self.FOF_SECONDARY_LINK_TYPES = '4+8+16+32'
      self.ExpansionListArr = np.zeros(shape=(1,4))
      self.clusteropt = self.main.headertab.clusteropt
      self.PBSexecute = "mpirun -np " + str(int(self.PBSncores*self.PBSnnodes)) + " ./P-Gadget3 ./param.txt 1>" + self.PBSoutputfile + " 2>" + self.PBSerrorfile


      #self.PBSstring = \
      #"#!/bin/sh \n#PBS -l nodes=3:ppn=8 \n#PBS -N H190897LX9N1 \n#PBS -m be \n. /opt/torque/etc/openmpi-setup.sh \ncd /spacebase/data/AnnaGroup/caterpillar/halos/H190897/H190897_BE_Z127_P7_LN7_LX9_O4_NV1 \nmpirun -np 24 ./P-Gadget3 ./param.txt 1>OUTPUT 2>ERROR"


   