from Common import *

class InitialConditions(HasTraits):

    icdir = Directory
    resimdir = Directory

    cosmologylist = List( editor = CheckListEditor(values = ['WMAP1','WMAP3','WMAP5','wMAP7','WMAP9','PLANCK'],cols   = 3) )

    boxlength = List(editor = CheckListEditor(values = ['5','10','25','50','75','100','250','500'],cols= 4))
    
    zinit = Range(0,127,127)
    
    padding = List(editor = CheckListEditor(values = ['5','6','7','8','9','10'],cols=6) )

    lmin = List(editor = CheckListEditor(values = ['5','6','7','8','9','10','11','12','13','14','15'],cols=11))

    lmax = List(editor = CheckListEditor(values = ['5','6','7','8','9','10','11','12','13','14','15'],cols=11))

    overlap = List(editor = CheckListEditor(values = ['1','2','3','4','5','6'],cols=6) )

    baryons = Bool(False)
    use2LPT = Bool(False)
    use2LPT = Bool(False)
    useLLA = Bool(False)
    periodicTF = Bool(False)

    uniformbox = Bool(False)
    resimbox = Bool(False)

    refx = Float
    refy = Float
    refz = Float
    extentx = Float
    extenty = Float
    extentz = Float

    boxtype = List( editor = CheckListEditor(values = ['Ellipsoid','Box'],cols=2))
    tranfunc = List( editor = CheckListEditor(values = ['Eisenstein'],cols=1))
    
    haloid = Str
    #haloid = Int(0)

    #OUTPUT
    outformat = List(editor = CheckListEditor(values = ['Gadget','Enzo','Grafic2','Generic','TIPSY'], cols = 5) )
    outfilename = Str

    noutput = Int

    #POISSON
    fftfine = Bool(False)
    accuracy = Float
    presmooth = 3
    postsmooth = 3
    smoother = Str
    laplaceorder = Int
    gradorder = Int
    align = Bool(False)

    generate_button = Button("Generate ICs!")
#
    view = View(Item(name='icdir',label='Directory'),
                 Tabbed(
                      Group(HGroup(Item(name='uniformbox',show_label=False),
                                Group(Group(Group(HGroup(Item(name='refx',label='ref_centerx'),
                                                         Item(name='refy',label='ref_centery'),
                                                         Item(name='refz',label='ref_centerz')),

                                                  HGroup(Item(name='extentx',label='ref_extentx'),
                                                         Item(name='extenty',label='ref_extenty'),
                                                         Item(name='extentz',label='ref_extentz'))
                                                  ,enabled_when='uniformbox==True')
                                                  ,enabled_when='resimbox==False')
                                                  ,show_border=True,label='Uniform Box')),
 #width=-50
                            HGroup(Item(name='resimbox',show_label=False),Group(
                                   Group(HGroup(Group(Item(name='resimdir',label='Pointer File'),
                                                      Item(name='haloid',label='HaloID'))
                                       ,enabled_when='resimbox==True'),enabled_when='uniformbox==False')
                                       ,show_border=True,label='Re-simulation')),

                            Group(Item(name='boxtype'        ,label='Box Type',style='custom'),
                                  Item(name='cosmologylist'  ,label='Cosmology'     ,style='custom'),
                                  Item(name='boxlength'      ,label='Box Length',style='custom'),
                                  Item(name='zinit'          ,label='zinit'),
                                  Item(name='lmin'           ,label='Level Min'      ,style='custom'),
                                  Item(name='lmax'           ,label='Level Max'      ,style='custom'),
                                  Item(name='padding'        ,label='Padding'        ,style='custom',springy=False),
                                  Item(name='overlap'        ,label='Overlap',style='custom'),show_border=True,label='Iterative Components'),

                            Group(HGroup(Item(name='baryons'        ,label='Baryons'),
                                         Item(name='use2LPT'        ,label='use_2LPT'),
                                         Item(name='useLLA'         ,label='use_LLA'),
                                         Item(name='tranfunc'       ,label='Trans. Func.')),
                                         HGroup(Item(name='periodicTF'     ,label='periodicTF'),
                                         Item(name='align'          ,label='align_top')),show_border=True,label='Extra Options')
                            ,label='Setup'),

                            Group(Item(name='fftfine' ,label='fft_fine'),
                                  Item(name='accuracy'       ,label='accuracy'),
                                  Item(name='presmooth'      ,label='pre_smooth'),
                                  Item(name='postsmooth'     ,label='post_smooth'),
                                  Item(name='smoother',label='smoother'),
                                  Item(name='laplaceorder'   ,label='laplace_order'),
                                  Item(name='gradorder'      ,label='grad_order'),label='Poisson'),

                            Group(Item(name='outformat',show_label=False,style='custom'),
                                  Item(name='noutput',label='# outputs'),
                                  Item(name='outfilename',label='Filename'),
                                  Item(name='generate_button',show_label=False),label='Output')))
    
    def _uniformbox_changed(self):
        if self.uniformbox == True:
            self.resimbox = False

    def _resimbox_changed(self):
        if self.resimbox == True:
            self.uniformbox = False

    def _generate_button_fired(self):
        if self.uniformbox == True:
            for cosmi in self.cosmologylist:
                for boxlengthi in self.boxlength:
                    for boxtypei in self.boxtype:
                        for paddingi in self.padding:
                            for lmini in self.lmin:
                                for lmaxi in self.lmax:
                                    foldername = cosmi + \
                                                '_L' + str(boxlengthi) + \
                                                '_B' + str(boxtypei[0].upper()) + \
                                                '_Z' + str(self.zinit) + \
                                                '_P' + str(paddingi) + \
                                                '_LMIN' + str(lmini) + \
                                                '_LMAX' + str(lmaxi)
                                    
                                    print foldername
        else:
            for boxlengthi in self.boxlength:
                for boxtypei in self.boxtype:
                    for paddingi in self.padding:
                        for lmini in self.lmin:
                            for lmaxi in self.lmax:
                                foldername = 'HALO' + str(self.haloid) + \
                                            '_L' + str(boxlengthi) + \
                                            '_B' + str(boxtypei[0].upper()) + \
                                            '_Z' + str(self.zinit) + \
                                            '_P' + str(paddingi) + \
                                            '_LMIN' + str(lmini) + \
                                            '_LMAX' + str(lmaxi)
                                
                                print foldername


    def __init__(self, main, **kwargs):
        HasTraits.__init__(self)
        self.main = main
        self.haloid = self.main.existencetab.haloid 
        self.resimbox = True
        self.accuracy = 0.00001
        self.fftfine = True
        self.pre_smooth = 3
        self.post_smooth = 3
        self.smoother = 'gs'
        self.laplaceorder = 6
        self.grad_order = 6
        self.icdir = self.main.headertab.basepath + 'ics'
        self.refx = 0.5
        self.refy = 0.5
        self.refz = 0.5
        self.extentx = 0.2
        self.extenty = 0.2
        self.extentz = 0.2

        #self.outfilename = 'ic'
    