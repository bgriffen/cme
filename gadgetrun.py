from Common import *
import mergertrees.MTCatalogue as MT

class GadgetRun(HasTraits):

#--------------------------------------- Basic operation mode of code
  PERIODIC = Bool(True)
  COOLING = Bool(False)
  SFR = Bool(False)
  SINKS = Bool(False)
  UNEQUALSOFTENINGS = Bool(True)
  
#--------------------------------------- Kernel Options
  QUINTIC_KERNEL = Bool(False)  # Implementation of the Morris 1996 quintic spline kernel, requires (3/2)^3 more neighbours !
  TWODIMS = Bool(False)         # Switch for 2D test problems
  ONEDIM = Bool(False)          # Switch for 1D test problems
#--------------------------------------- TreePM Options

  PMGRID = Int(512)
  GRIDBOOST = Int(2)
  PLACEHIGHRESREGION = Int(2)
  ENLARGEREGION = Float(1.2)
  
#--------------------------------------- Multi-Domain and Top-Level Tree options
  MULTIPLEDOMANS = Int(8)
  TOPNODEFACTOR = Int(3)
  KD_HMAX_ESTIMATE = 1.2

#--------------------------------------- Things that are always recommended

  PEANOHILBERT = Bool(True)
  WALLCLOCK = Bool(True)
  MYSORT = Bool(True)
  AUTO_SWAP_ENDIAN_READIC = Bool(False)
  WRITE_KEY_FILES = Bool(False)
  WRITE_INFO_BLOCK = Bool(False)
  PERMUTATAION_OPTIMIZATION = Bool(False)
  PROCESS_TIMES_OF_OUTPUTLIST  = Bool(False)
  SYNCRONIZ_OUTPUT = Bool(False)

#---------------------------------------- Single/Double Precision
  DOUBLEPRECISION = Bool(True)
  DOUBLEPRECISION_FFTW = Bool(True)
  OUTPUT_IN_DOUBLEPRECISION = Bool(False)
  INPUT_IN_DOUBLEPRECISION = Bool(False)

#---------------------------------------- Invariance Tes
  INVARIANCETEST = Bool(False)
  INVARIANCETEST_SIZE1 = Int(2)
  INVARIANCETEST_SIZE2 = Int(6)
  FLTROUNDOFFREDUCTION = Bool(False)
  SOFTDOUBLEDOUBLE = Bool(False)

#---------------------------------------- On the fly FOF groupfinder
  FOF = Bool(False)
  FOF_PRIMARY_LINK_TYPES = Int(2)         # 2^type for the primary dark matter type      
  FOF_SECONDARY_LINK_TYPES=4+8+16+32      # 2^type for the types linked to nearest primaries
  FOF_GROUP_MIN_LEN = Int(32)             # default is 32       
  SUBFIND = Bool(False)
  DENSITY_SPLIT_BY_TYPE=1+2+16+32         # 2^type for whch the densities should be calculated seperately
  MAX_NGB_CHECK = Int(3)                  # Max numbers of neighbours for sattlepoint detection (default = 2)
  SAVE_MASS_TAB = Bool(False)             # Saves the an additional array with the masses of the different components                   
  SUBFINDSAVE_PARTICLELISTS = Bool(False) # Saves also phase-space and type variables parallel to IDs     
  SO_VEL_DISPERSIONS = Bool(False)        # computes velocity dispersions for as part of FOF SO-properties      
  ORDER_SNAPSHOTS_BY_ID = Bool(False)   
  SAVE_HSML_IN_IC_ORDER = Bool(False)      # will store the hsml-values in the order of the particles in the IC file
  ONLY_PRODUCE_HSML_FILES = Bool(False)    # only carries out density estimate          
  KEEP_HSML_AS_GUESS = Bool(False)         # keep using hsml for gas particles in subfind_density              
  LINKLENGTH = Float(0.16)                 # Linkinglength for FoF (default=0.2)         
  NO_GAS_CLOUDS = Bool(False)              # Do not accept pure gaseous substructures           
  WRITE_SUB_IN_SNAP_FORMAT = Bool(False)   # Save subfind results in snap format           
  LT_ADD_GAL_TO_SUB = Int(12)              # Adds optical luminosities in 6 bands to subhalos  
  DUSTATT = Int(11)                        # Includes dust attenuation into the luminosity calculation (using 11 radial bins)   
  OBSERVER_FRAME = Bool(False)             # If defined, use CB07 Observer Frame Luminosities, otherwise CB07 Rest Frame Luminosities           
  SO_BAR_INFO = Bool(False)                # Adds temperature, Lx, bfrac, etc to Groups       
  FSUBFINDCOUNT_BIG_HALOS = Float(1e4)     # Adds extra blocks for Halos with M_TopHat > SUBFIND_COUNT_BIG_HALOS
  KD_CHOOSE_PSUBFIND_LIMIT = Bool(False)   # Increases the limit for the parallel subfind to the maximum possible   
  KD_ALTERNATIVE_GROUP_SORT = Bool(False)  # Alternative way to sort the Groups/SubGroupe before writing 
  KD_CHOOSE_LINKING_LENGTH = Bool(False)   # Special way to estimate the linking length          
  SUBFINDREAD_FOF = Bool(False)   
  SUBFINDCOLLECTIVE_STAGE1 = Bool(False)   
  SUBFINDCOLLECTIVE_STAGE2 = Bool(False)   
  SUBFINDALTERNATIVE_COLLECTIVE = Bool(False)   
  SUBFINDRESHUFFLE_CATALOGUE = Bool(False)   
  SUBFINDRESHUFFLE_CATALOGUE_WITH_VORONOI = Bool(False)   
  SUBFINDRESHUFFLE_AND_POTENTIAL = Bool(False)       #needs -DSUBFIND_RESHUFFLE_CATALOGUE and COMPUTE_POTENTIAL_ENERGY
  SUBFINDDENSITY_AND_POTENTIAL = Bool(False)         #only calculated density and potential and write them into snapshot
  
#--------------------------------------- Adaptive Gravitational Softening (F. Iannuzzi)
  ADAPTGRAVSOFT = Bool(False)
  AGS_UPDATEALLPARTICLES = Bool(False)
  AGS_NOCORRECTION = Bool(False)
  AGS_OUTPUTGRAVSOFT = Bool(False)
  AGS_OUTPUTGRAVNUMDENS = Bool(False)
  AGS_OUTPUTZETA = Bool(False)
  AGS_OUTPUTOMEGA = Bool(False)
  AGS_OUTPUTCORR = Bool(False)
  AGS_OUTPUTNGBS = Bool(False)
  AGS_MAXSOFT=Float(1000)
  AGS_MINSOFT=Float(0.001)

#-------------------------------------- Mofified Gravity
  MODGRAV = Bool(False)               # modified gravity master switch
  MODGRAV_DGP = Bool(False)           # DGP cosmology
  MODGRAV_FORCETEST = Bool(False)     # for testing the Poisson solver for the scalar fiel
  
#--------------------------------------- SFR/feedback model
  GENERATIONS=Int(1)           # the number of stars a gas particle may spawn
  SOFTEREQS = Bool(False)
  MOREPARAMS = Bool(False)
  METALS = Bool(False)
  STELLARAGE = Bool(False)
  WINDS = Bool(False)
  VARIABLE_WINDS = Bool(False)
  QUICK_LYALPHA = Bool(False)
  ISOTROPICWINDS = Bool(False)
  MHM = Bool(False)
  MODIFIED_SFR = Bool(False)
  ALTERNATIVE_SFR = Bool(False)

  #-------------------------------------- AGN stuff
  BLACK_HOLES = Bool(False)             # enables Black-Holes (master switch)
  BONDI = Bool(False)                   # Bondi-Hoyle style accretion model
  BH_VARIABLE_ACCRETION_FACTOR = Bool(False)   # variable-alpha model as in Booth&Schaye 2009
  ENFORCE_EDDINGTON_LIMIT = Bool(False) # put a hard limit on the maximum accretion rate
  BH_THERMALFEEDBACK = Bool(False)      # couple a fraction of the BH luminosity into surrounding gas
  BH_DRAG = Bool(False)                 # Drag on black-holes due to accretion
  SWALLOWGAS = Bool(False)              # Enables stochastic accretion of gas particles consistent with growth rate of hole
  EVALPOTENTIAL = Bool(False)           # computes gravitational potential
  REPOSITION_ON_POTMIN = Bool(False)    # repositions hole on potential minimum (requires EVALPOTENTIAL)
  BH_COUNTPROGS = Bool(False)        # carries a counter for each BH that gives the total number of seeds that merged into it
  BH_USE_GASVEL_IN_BONDI = Bool(False)  # only when this is enabled, the surrounding gas velocity is used in addition to the sounds speed in the Bon$
  CSND_FRAC_BH_MERGE=Float(0.5)  # Relative levocity fraction (in units of soundspeed) for merging blackholes, default=0.5
  DETACH_BLACK_HOLES = Bool(False)      # Insert an independent data structure for BHs (currently exlicitly depends on LT_STELLAREVOLUTION)
  
  #-------------------------------------- Some use-full adds
  KD_BHSEED_ON_POTMIN = Bool(False)             # Seed in minimal potential instead of max density
  KD_SEED_STAR_MASS_FRACTION=Float(0.02) # minimum star mass fraction for BH seeding
  KD_FRICTION = Bool(False)                     # Turns on dynamical friction for BHs
  KD_FRICTION_DYNAMIC = Bool(False)             # Calculates environment dependent terms dynamically
  KD_IGNORE_ACCRETED_GAS_MOMENTUM = Bool(False) # Do not transfer momentum for swallowed gas, but follow momentum for swallowed BHs
  KD_TAKE_CENTER_OF_MASS_FOR_BH_MERGER = Bool(False)   # Do preserve center of mass when swallowing
  
  #-------------------------------------- AGN-Bubble feedback
  BUBBLES = Bool(False)                 # generation of hot bubbles in an isolated halo or the the biggest halo in the run
  MULTI_BUBBLES = Bool(False)        # hot bubbles in all haloes above certain mass threshold (works only with FOF and without BUBBLES)
  EBUB_PROPTO_BHAR = Bool(False)        # Energy content of the bubbles with cosmic time evolves as an integrated BHAR(z) over a Salpeter time (Di M$
  
  BH_BUBBLES = Bool(False)              # calculate bubble energy directly from
                                        # the black hole accretion rate
  
  UNIFIED_FEEDBACK = Bool(False)        # activates BH_THERMALFEEDBACK at high
                                        # Mdot and BH_BUBBLES FEEDBACK al low Mdot
  
  #------------------------------------ # [options from LT and DF]
  LT_BH_ACCRETE_SLICES = Bool(False)
  LT_BH_GUESSHSML = Bool(False)
  LT_DF_BH = Bool(False)
  LT_DF_BH_BHAR_SWITCH=Int(4)         # switch feedback by BHAR
  
  #-------------------------------------- Viscous gas treatment
  NAVIERSTOKES = Bool(False)            # Braginskii-Spitzer parametrization of the shear viscosity: mu = f x T^{5/2}
  NAVIERSTOKES_CONSTANT = Bool(False)   # Shear viscosity set constant for all gas particles
  NAVIERSTOKES_BULK = Bool(False)       # Bulk viscosity set constant for all gas particles. To run with bulk visocity only one has to set shear vis$
  VISCOSITY_SATURATION = Bool(False)    # Both shear and bulk viscosities are saturated, so that unphysical accelerations and entropy increases are $
  NS_TIMESTEP = Bool(False)             # Enables timestep criterion based on entropy increase due to internal friction forces
  OUTPUTSTRESS = Bool(False)            # Outputs diagonal and offdiagonal components of viscous shear stress tensor
  OUTPUTBULKSTRESS = Bool(False)        # Outputs viscous bulk stress tensor
  OUTPUTSHEARCOEFF = Bool(False)        # Outputs variable shear viscosity coefficient in internal code units
  
  #-------------------------------------------- Things for special behaviour
  WINDTUNNEL = Bool(False)
  POWERSPEC_ON_OUTPUT = Bool(False)
  POWERSPEC_ON_OUTPUT_EACH_TYPE = Bool(False)
  DO_NOT_CREATE_STAR_PARTICLES = Bool(False)
  TRADITIONAL_SPH_FORMULATION = Bool(False)
  NOTEST_FOR_IDUNIQUENESS = Bool(False)
  SNIA_HEATING = Bool(False)
  RADIAL_TREE = Bool(False)                   #make tree forces exact radial (only implemented in tree, not TreePM)
  FIXEDTIMEINFIRSTPHASE=Int(1000)
  NO_ISEND_IRECV_IN_DOMAIN = Bool(True)   
  FIX_PATHSCALE_MPI_STATUS_IGNORE_BUG = Bool(True)   
  MPISENDRECV_SIZELIMIT=Int(100)
  MPISENDRECV_CHECKSUM = Bool(False)
  NOGRAVITY = Bool(False)
  NOACCEL = Bool(False)
  NOISMPRESSURE = Bool(False)
  NOVISCOSITYLIMITER = Bool(False)
  NOTREERND = Bool(False)
  NOTYPEPREFIX_FFTW = Bool(False)
  ISOTHERM=Int(200)                  # adds potential of an isothermal sphere
  COMPUTE_POTENTIAL_ENERGY = Bool(True)   
  ALLOWEXTRAPARAMS = Bool(False)
  LONGIDS = Bool(False)
  ENLARGE_DYNAMIC_RANGE_IN_TIME = Bool(False)  # NOT TESTED !!!
  ASSIGN_NEW_IDS = Bool(False)
  INHOMOG_GASDISTR_HINT = Bool(False)         # if the gas is distributed very different from collisionless particles, this can helps to avoid probl$
  LONG_X=Int(140)
  LONG_Y=Int(1)
  LONG_Z=Int(1)
  SPH_BND_PARTICLES = Bool(False)
  NEW_RATES = Bool(False)                     # switches in updated cooling rates from Naoki
  RADIATIVE_RATES = Bool(False)               # used in non-equilibrium chemistry model
  READ_HSML = Bool(False)                     # reads hsml from IC file
  ADAPTIVE_GRAVSOFT_FORGAS = Bool(False)      # allows variable softening length for gas particles (requires UNEQUALSOFTENINGLENGTH)
  ADAPTIVE_GRAVSOFT_FORGAS_HSML = Bool(False) # this sets the gravitational softening for SPH particles equal to the SPH smoothing (requires ADAPTIV$
  GENERATE_GAS_IN_ICS = Bool(False)
  SPLIT_PARTICLE_TYPE=Str('4+8')
  NEUTRINOS = Bool(False)                     # Option for special integration of light neutrino species
  OMIT_NEUTRINOS_IN_SNAPS = Bool(False)
  KSPACE_NEUTRINOS = Bool(False)
  START_WITH_EXTRA_NGBDEV = Bool(False)        # Uses special MaxNumNgbDeviation for starting
  ISOTHERM_EQS = Bool(False)                  # isothermal equation of state
  NO_UTHERM_IN_IC_FILE = Bool(False)
  SPECIAL_GAS_TREATMENT_IN_HIGHRESREGION = Bool(False)
  DONOTUSENODELIST = Bool(False)
  MAXHSML = Bool(False)
  SUB_TURB_DRIVING = Bool(False)
  ADJ_BOX_POWERSPEC = Bool(False)         # compiles in a code module that allows via restart-flag 6 the calculation of a gas velocity power spectru$
  
  #---------------------------------------- New shockfinding method
  AB_SHOCK=Float(0.85)                  # Shock- and Machfinder
  AB_SHOCK_SHOCKFLAG=Float(0.40)        # Mark particles that clearly belong to a shock front
  AB_SHOCK_SPEEDUP=Float(0.01)          # Shockflag calculation only depends on a mach number criteron for faster execution
  AB_SHOCK_MAGNETIC = Bool(False)              # Account for Alfvenwaves in signal velocity
  AB_SHOCK_EXPANSION=Float(1.0)         # Account for expansion of space in signal velocity
  AB_SHOCK_CORRECTION=Float(1.045)      # Correction factor for mach number
  AB_SHOCK_STATISTICS = Bool(False)            # Outputs additional statistics in a text file
  AB_SHOCK_STATISTICS_SIMPLE = Bool(False)     # General mach statistics. Useable without shockfinder
  
  
  #---------------------------------------- Imports from L-Gadget3 (testing phase, do not use)
  SORT_FROM_L3 = Bool(False)                   # Uses L-Gadget3 version of sort
  PM_FROM_L3 = Bool(False)                     # Uses L-Gadget3 cersion of sort
  
  FFTW3 = Bool(False)
  FFTW3_THREADS = Bool(False)
  FFTW2_THREADS = Bool(False)
  
  OPENMP=Int(4)                       # Masterswitch for explicit OpenMP implementation
  OMP_MYSORT = Bool(False)                     # Uses a OpenMP version of the self-written mergesort
  OMP_SORT=Int(2000)                  # Replaces standard quicksort with a self-written version with OpenMP support
  
  
  #--------------------------------------- Time integration options
  ALTERNATIVE_VISCOUS_TIMESTEP = Bool(False)
  NOSTOP_WHEN_BELOW_MINTIMESTEP = Bool(False)
  NOWINDTIMESTEPPING = Bool(False)            # Disable wind reducing timestep (not recommended)
  NOPMSTEPADJUSTMENT = Bool(False)
  FORCE_EQUAL_TIMESTEPS = Bool(False)
  
  #--------------------------------------- Output/Input options
  OUTPUTPOTENTIAL = Bool(True)   
  RECOMPUTE_POTENTIAL_ON_OUTPUT = Bool(True)    # update potential every output even it EVALPOTENTIAL is set
  OUTPUTACCELERATION = Bool(True)   
  OUTPUTCHANGEOFENTROPY = Bool(False)
  OUTPUT_DIV_CURL = Bool(False)
  OUTPUT_VORTICITY = Bool(False)              # outputs the vorticity vector
  OUTPUTTIMESTEP = Bool(True)   
  OUTPUTCOOLRATE = Bool(False)                   # outputs cooling rate, and conduction rate if enabled
  HAVE_HDF5 = Bool(True)                        # needed when HDF5 I/O support is desired
  OUTPUTBSMOOTH = Bool(False)
  OUTPUTDENSNORM = Bool(False)
  XXLINFO = Bool(False)                       # Enables additional output for viscosityand bfield
  OUTPUTLINEOFSIGHT = Bool(False)             # enables on-the-fly output of Ly-alpha absorption spectra
  OUTPUTLINEOFSIGHT_SPECTRUM = Bool(False)
  OUTPUTLINEOFSIGHT_PARTICLES = Bool(False)
  
  #--------------------------------------- Testing and Debugging options
  FORCETEST=0.1
  DEBUG = Bool(True)                   # enables core-dumps and FPU exceptions
  PARTICLE_DEBUG = Bool(False)            # auxiliary communication of IDs
  VERBOSE = Bool(False)
  CHECKSUM_DEBUG = Bool(False)



  view = View(Group(HGroup(Group(Item('PERIODIC',label='PERIODIC'),
              Item('COOLING',label='COOLING'),
              Item('SFR',label='SFR'),
              Item('SINKS',label='SINKS'),
              Item('UNEQUALSOFTENINGS',label='UNEQUALSOFTENINGS')),

              Group(Item('QUINTIC_KERNEL',label='QUINTIC_KERNEL'),
              Item('TWODIMS',label='TWODIMS'),
              Item('ONEDIM',label='ONEDIM'))),

              Item('PMGRID',label='PMGRID'),
              Item('GRIDBOOST',label='GRIDBOOST'),
              Item('PLACEHIGHRESREGION',label='PLACEHIGHRESREGION'),
              Item('ENLARGEREGION',label='ENLARGEREGION'),
              
              Item('MULTIPLEDOMANS',label='MULTIPLEDOMANS'),
              Item('TOPNODEFACTOR',label='TOPNODEFACTOR'),
              Item('KD_HMAX_ESTIMATE',label='KD_HMAX_ESTIMATE'),

              HGroup(Group(Item('PEANOHILBERT',label='PEANOHILBERT'),
                           Item('WALLCLOCK',label='WALLCLOCK'),
                           Item('MYSORT',label='MYSORT'),
                           Item('AUTO_SWAP_ENDIAN_READIC',label='AUTO_SWAP_ENDIAN_READIC'),
                           Item('WRITE_KEY_FILES',label='WRITE_KEY_FILES'),
                           Item('WRITE_INFO_BLOCK',label='WRITE_INFO_BLOCK'),
                           Item('PERMUTATAION_OPTIMIZATION',label='PERMUTATAION_OPTIMIZATION'),
                           Item('PROCESS_TIMES_OF_OUTPUTLIST',label='PROCESS_TIMES_OF_OUTPUTLIST'),
                           Item('SYNCRONIZ_OUTPUT',label='SYNCRONIZ_OUTPUT')),
             
                     Group(Item('DOUBLEPRECISION',label='DOUBLEPRECISION'),
                           Item('DOUBLEPRECISION_FFTW',label='DOUBLEPRECISION_FFTW'),
                           Item('OUTPUT_IN_DOUBLEPRECISION',label='OUTPUT_IN_DOUBLEPRECISION'),
                           Item('INPUT_IN_DOUBLEPRECISION',label='INPUT_IN_DOUBLEPRECISION'),
             
                           Item('INVARIANCETEST',label='INVARIANCETEST'),
                           Item('INVARIANCETEST_SIZE1',label='INVARIANCETEST_SIZE1'),
                           Item('INVARIANCETEST_SIZE2',label='INVARIANCETEST_SIZE2'),
                           Item('FLTROUNDOFFREDUCTION',label='FLTROUNDOFFREDUCTION'),
                           Item('SOFTDOUBLEDOUBLE',label='SOFTDOUBLEDOUBLE'))),label='Mode'),

              Group(Item('FOF',label='FOF'),
              Item('FOF_PRIMARY_LINK_TYPES',label='FOF_PRIMARY_LINK_TYPES'),
              Item('FOF_SECONDARY_LINK_TYPES',label='FOF_SECONDARY_LINK_TYPES'),
              Item('FOF_GROUP_MIN_LEN',label='FOF_GROUP_MIN_LEN'),
              Item('SUBFIND',label='SUBFIND'),
              Item('DENSITY_SPLIT_BY_TYPE',label='DENSITY_SPLIT_BY_TYPE'),
              Item('MAX_NGB_CHECK',label='MAX_NGB_CHECK'),
              Item('SAVE_MASS_TAB',label='SAVE_MASS_TAB'),
              Item('SUBFINDSAVE_PARTICLELISTS',label='SUBFINDSAVE_PARTICLELISTS'),
              Item('SO_VEL_DISPERSIONS',label='SO_VEL_DISPERSIONS'),
              Item('ORDER_SNAPSHOTS_BY_ID',label='ORDER_SNAPSHOTS_BY_ID'),
              Item('SAVE_HSML_IN_IC_ORDER',label='SAVE_HSML_IN_IC_ORDER'),
              Item('ONLY_PRODUCE_HSML_FILES',label='ONLY_PRODUCE_HSML_FILES'),
              Item('KEEP_HSML_AS_GUESS',label='KEEP_HSML_AS_GUESS'),
              Item('LINKLENGTH',label='LINKLENGTH'),
              Item('NO_GAS_CLOUDS',label='NO_GAS_CLOUDS'),
              Item('WRITE_SUB_IN_SNAP_FORMAT',label='WRITE_SUB_IN_SNAP_FORMAT'),
              Item('LT_ADD_GAL_TO_SUB',label='LT_ADD_GAL_TO_SUB'),
              Item('DUSTATT',label='DUSTATT'),
              Item('OBSERVER_FRAME',label='OBSERVER_FRAME'),
              Item('SO_BAR_INFO',label='SO_BAR_INFO'),
              Item('FSUBFINDCOUNT_BIG_HALOS',label='FSUBFINDCOUNT_BIG_HALOS'),label='SUB'),

              Group(Item('KD_CHOOSE_PSUBFIND_LIMIT',label='KD_CHOOSE_PSUBFIND_LIMIT'),
              Item('KD_ALTERNATIVE_GROUP_SORT',label='KD_ALTERNATIVE_GROUP_SORT'),
              Item('KD_CHOOSE_LINKING_LENGTH',label='KD_CHOOSE_LINKING_LENGTH'),
              Item('SUBFINDREAD_FOF',label='SUBFINDREAD_FOF'),
              Item('SUBFINDCOLLECTIVE_STAGE1',label='SUBFINDCOLLECTIVE_STAGE1'),
              Item('SUBFINDCOLLECTIVE_STAGE2',label='SUBFINDCOLLECTIVE_STAGE2'),
              Item('SUBFINDALTERNATIVE_COLLECTIVE',label='SUBFINDALTERNATIVE_COLLECTIVE'),
              Item('SUBFINDRESHUFFLE_CATALOGUE',label='SUBFINDRESHUFFLE_CATALOGUE'),
              Item('SUBFINDRESHUFFLE_CATALOGUE_WITH_VORONOI',label='SUBFINDRESHUFFLE_CATALOGUE_WITH_VORONOI'),
              Item('SUBFINDRESHUFFLE_AND_POTENTIAL',label='SUBFINDRESHUFFLE_AND_POTENTIAL'),
              Item('SUBFINDDENSITY_AND_POTENTIAL',label='SUBFINDDENSITY_AND_POTENTIAL'),

              Item('ADAPTGRAVSOFT',label='ADAPTGRAVSOFT'),
              Item('AGS_UPDATEALLPARTICLES',label='AGS_UPDATEALLPARTICLES'),
              Item('AGS_NOCORRECTION',label='AGS_NOCORRECTION'),
              Item('AGS_OUTPUTGRAVSOFT',label='AGS_OUTPUTGRAVSOFT'),
              Item('AGS_OUTPUTGRAVNUMDENS',label='AGS_OUTPUTGRAVNUMDENS'),
              Item('AGS_OUTPUTZETA',label='AGS_OUTPUTZETA'),
              Item('AGS_OUTPUTOMEGA',label='AGS_OUTPUTOMEGA'),
              Item('AGS_OUTPUTCORR',label='AGS_OUTPUTCORR'),
              Item('AGS_OUTPUTNGBS',label='AGS_OUTPUTNGBS'),
              Item('AGS_MAXSOFT',label='AGS_MAXSOFT'),
              Item('AGS_MINSOFT',label='AGS_MINSOFT'),label='Add-ons'),

              Group(Item('MODGRAV',label='MODGRAV'),
              Item('MODGRAV_DGP',label='MODGRAV_DGP'),
              Item('MODGRAV_FORCETEST',label='MODGRAV_FORCETEST'),

              Item('GENERATIONS',label='GENERATIONS'),
              Item('SOFTEREQS',label='SOFTEREQS'),
              Item('MOREPARAMS',label='MOREPARAMS'),
              Item('METALS',label='METALS'),
              Item('STELLARAGE',label='STELLARAGE'),
              Item('WINDS',label='WINDS'),
              Item('VARIABLE_WINDS',label='VARIABLE_WINDS'),
              Item('QUICK_LYALPHA',label='QUICK_LYALPHA'),
              Item('ISOTROPICWINDS',label='ISOTROPICWINDS'),
              Item('MHM',label='MHM'),
              Item('MODIFIED_SFR',label='MODIFIED_SFR'),
              Item('ALTERNATIVE_SFR',label='ALTERNATIVE_SFR'),label='MG & SF'),

              Group(Item('BLACK_HOLES',label='BLACK_HOLES'),
              Item('BONDI',label='BONDI'),
              Item('BH_VARIABLE_ACCRETION_FACTOR',label='BH_VARIABLE_ACCRETION_FACTOR'),
              Item('ENFORCE_EDDINGTON_LIMIT',label='ENFORCE_EDDINGTON_LIMIT'),
              Item('BH_THERMALFEEDBACK',label='BH_THERMALFEEDBACK'),
              Item('BH_DRAG',label='BH_DRAG'),
              Item('SWALLOWGAS',label='SWALLOWGAS'),
              Item('EVALPOTENTIAL',label='EVALPOTENTIAL'),
              Item('REPOSITION_ON_POTMIN',label='REPOSITION_ON_POTMIN'),
              Item('BH_COUNTPROGS',label='BH_COUNTPROGS'),
              Item('BH_USE_GASVEL_IN_BONDI',label='BH_USE_GASVEL_IN_BONDI'),
              Item('CSND_FRAC_BH_MERGE',label='CSND_FRAC_BH_MERGE'),
              Item('DETACH_BLACK_HOLES',label='DETACH_BLACK_HOLES'),
              Item('KD_BHSEED_ON_POTMIN',label='KD_BHSEED_ON_POTMIN'),
              Item('KD_SEED_STAR_MASS_FRACTION',label='KD_SEED_STAR_MASS_FRACTION'),
              Item('KD_FRICTION',label='KD_FRICTION'),
              Item('KD_FRICTION_DYNAMIC',label='KD_FRICTION_DYNAMIC'),
              Item('KD_IGNORE_ACCRETED_GAS_MOMENTUM',label='KD_IGNORE_ACCRETED_GAS_MOMENTUM'),
              Item('KD_TAKE_CENTER_OF_MASS_FOR_BH_MERGER',label='KD_TAKE_CENTER_OF_MASS_FOR_BH_MERGER'),label='BH'),

              Group(Item('BUBBLES',label='BUBBLES'),
              Item('MULTI_BUBBLES',label='MULTI_BUBBLES'),
              Item('EBUB_PROPTO_BHAR',label='EBUB_PROPTO_BHAR'),
              Item('BH_BUBBLES',label='BH_BUBBLES'),
              Item('UNIFIED_FEEDBACK',label='UNIFIED_FEEDBACK'),

              Item('LT_BH_ACCRETE_SLICES',label='LT_BH_ACCRETE_SLICES'),
              Item('LT_BH_GUESSHSML',label='LT_BH_GUESSHSML'),
              Item('LT_DF_BH',label='LT_DF_BH'),
              Item('LT_DF_BH_BHAR_SWITCH',label='LT_DF_BH_BHAR_SWITCH'),

              Item('NAVIERSTOKES',label='NAVIERSTOKES'),
              Item('NAVIERSTOKES_CONSTANT',label='NAVIERSTOKES_CONSTANT'),
              Item('NAVIERSTOKES_BULK',label='NAVIERSTOKES_BULK'),
              Item('VISCOSITY_SATURATION',label='VISCOSITY_SATURATION'),
              Item('NS_TIMESTEP',label='NS_TIMESTEP'),
              Item('OUTPUTSTRESS',label='OUTPUTSTRESS'),
              Item('OUTPUTBULKSTRESS',label='OUTPUTBULKSTRESS'),
              Item('OUTPUTSHEARCOEFF',label='OUTPUTSHEARCOEFF'),
              Item('WINDTUNNEL',label='WINDTUNNEL'),label='AGN & Gas'),

              Group(HGroup(Group(Item('POWERSPEC_ON_OUTPUT',label='POWERSPEC_ON_OUTPUT'),
              Item('POWERSPEC_ON_OUTPUT_EACH_TYPE',label='POWERSPEC_ON_OUTPUT_EACH_TYPE'),
              Item('DO_NOT_CREATE_STAR_PARTICLES',label='DO_NOT_CREATE_STAR_PARTICLES'),
              Item('TRADITIONAL_SPH_FORMULATION',label='TRADITIONAL_SPH_FORMULATION')),
              Group(Item('NOTEST_FOR_IDUNIQUENESS',label='NOTEST_FOR_IDUNIQUENESS'),
              Item('SNIA_HEATING',label='SNIA_HEATING'),
              Item('RADIAL_TREE',label='RADIAL_TREE'))),
              Item('FIXEDTIMEINFIRSTPHASE',label='FIXEDTIMEINFIRSTPHASE'),
              HGroup(Item('NO_ISEND_IRECV_IN_DOMAIN',label='NO_ISEND_IRECV_IN_DOMAIN'),
              Item('FIX_PATHSCALE_MPI_STATUS_IGNORE_BUG',label='FIX_PATHSCALE_MPI_STATUS_IGNORE_BUG')),
              Item('MPISENDRECV_SIZELIMIT',label='MPISENDRECV_SIZELIMIT'),
              HGroup(Group(Item('MPISENDRECV_CHECKSUM',label='MPISENDRECV_CHECKSUM'),
              Item('NOGRAVITY',label='NOGRAVITY'),
              Item('NOACCEL',label='NOACCEL'),
              Item('NOISMPRESSURE',label='NOISMPRESSURE')),
              Group(Item('NOVISCOSITYLIMITER',label='NOVISCOSITYLIMITER'),
              Item('NOTREERND',label='NOTREERND'),
              Item('NOTYPEPREFIX_FFTW',label='NOTYPEPREFIX_FFTW'))),
              Item('ISOTHERM',label='ISOTHERM'),
              HGroup(Group(Item('COMPUTE_POTENTIAL_ENERGY',label='COMPUTE_POTENTIAL_ENERGY'),
              Item('ALLOWEXTRAPARAMS',label='ALLOWEXTRAPARAMS'),
              Item('LONGIDS',label='LONGIDS')),
              Group(Item('ENLARGE_DYNAMIC_RANGE_IN_TIME',label='ENLARGE_DYNAMIC_RANGE_IN_TIME'),
              Item('ASSIGN_NEW_IDS',label='ASSIGN_NEW_IDS'),
              Item('INHOMOG_GASDISTR_HINT',label='INHOMOG_GASDISTR_HINT'))),
              HGroup(Item('LONG_X',label='LONG_X'),
              Item('LONG_Y',label='LONG_Y'),
              Item('LONG_Z',label='LONG_Z'))),
              
              Group(Item('SPH_BND_PARTICLES',label='SPH_BND_PARTICLES'),
              Item('NEW_RATES',label='NEW_RATES'),
              Item('RADIATIVE_RATES',label='RADIATIVE_RATES'),
              Item('READ_HSML',label='READ_HSML'),
              Item('ADAPTIVE_GRAVSOFT_FORGAS',label='ADAPTIVE_GRAVSOFT_FORGAS'),
              Item('ADAPTIVE_GRAVSOFT_FORGAS_HSML',label='ADAPTIVE_GRAVSOFT_FORGAS_HSML'),
              Item('GENERATE_GAS_IN_ICS',label='GENERATE_GAS_IN_ICS'),
              Item('SPLIT_PARTICLE_TYPE',label='SPLIT_PARTICLE_TYPE'),
              Item('NEUTRINOS',label='NEUTRINOS'),
              Item('OMIT_NEUTRINOS_IN_SNAPS',label='OMIT_NEUTRINOS_IN_SNAPS'),
              Item('KSPACE_NEUTRINOS',label='KSPACE_NEUTRINOS'),
              Item('START_WITH_EXTRA_NGBDEV',label='START_WITH_EXTRA_NGBDEV'),
              Item('ISOTHERM_EQS',label='ISOTHERM_EQS'),
              Item('NO_UTHERM_IN_IC_FILE',label='NO_UTHERM_IN_IC_FILE'),
              Item('SPECIAL_GAS_TREATMENT_IN_HIGHRESREGION',label='SPECIAL_GAS_TREATMENT_IN_HIGHRESREGION'),
              Item('DONOTUSENODELIST',label='DONOTUSENODELIST'),
              Item('MAXHSML',label='MAXHSML'),
              Item('SUB_TURB_DRIVING',label='SUB_TURB_DRIVING'),
              Item('ADJ_BOX_POWERSPEC',label='ADJ_BOX_POWERSPEC')),

              Group(Item('AB_SHOCK',label='AB_SHOCK'),
              Item('AB_SHOCK_SHOCKFLAG',label='AB_SHOCK_SHOCKFLAG'),
              Item('AB_SHOCK_SPEEDUP',label='AB_SHOCK_SPEEDUP'),
              Item('AB_SHOCK_MAGNETIC',label='AB_SHOCK_MAGNETIC'),
              Item('AB_SHOCK_EXPANSION',label='AB_SHOCK_EXPANSION'),
              Item('AB_SHOCK_CORRECTION',label='AB_SHOCK_CORRECTION'),
              HGroup(Group(Item('AB_SHOCK_STATISTICS',label='AB_SHOCK_STATISTICS'),
              Item('AB_SHOCK_STATISTICS_SIMPLE',label='AB_SHOCK_STATISTICS_SIMPLE'),
              Item('SORT_FROM_L3',label='SORT_FROM_L3'),
              Item('PM_FROM_L3',label='PM_FROM_L3')),
              Group(Item('FFTW3',label='FFTW3'),
              Item('FFTW3_THREADS',label='FFTW3_THREADS'),
              Item('FFTW2_THREADS',label='FFTW2_THREADS'))),
              Item('OPENMP',label='OPENMP'),
              Item('OMP_MYSORT',label='OMP_MYSORT'),
              Item('OMP_SORT',label='OMP_SORT'),

              HGroup(Group(Item('ALTERNATIVE_VISCOUS_TIMESTEP',label='ALTERNATIVE_VISCOUS_TIMESTEP'),
                           Item('NOSTOP_WHEN_BELOW_MINTIMESTEP',label='NOSTOP_WHEN_BELOW_MINTIMESTEP'),
                           Item('NOWINDTIMESTEPPING',label='NOWINDTIMESTEPPING'),
                           Item('NOPMSTEPADJUSTMENT',label='NOPMSTEPADJUSTMENT'),
                           Item('FORCE_EQUAL_TIMESTEPS',label='FORCE_EQUAL_TIMESTEPS'),
                           Item('OUTPUTPOTENTIAL',label='OUTPUTPOTENTIAL')),
                     Group(Item('RECOMPUTE_POTENTIAL_ON_OUTPUT',label='RECOMPUTE_POTENTIAL_ON_OUTPUT'),
                           Item('OUTPUTACCELERATION',label='OUTPUTACCELERATION'),
                           Item('OUTPUTCHANGEOFENTROPY',label='OUTPUTCHANGEOFENTROPY'),
                           Item('OUTPUT_DIV_CURL',label='OUTPUT_DIV_CURL'),
                           Item('OUTPUT_VORTICITY',label='OUTPUT_VORTICITY')))),

              Group(HGroup(Group(Item('OUTPUTTIMESTEP',label='OUTPUTTIMESTEP'),
              Item('OUTPUTCOOLRATE',label='OUTPUTCOOLRATE'),
              Item('HAVE_HDF5',label='HAVE_HDF5'),
              Item('OUTPUTBSMOOTH',label='OUTPUTBSMOOTH'),
              Item('OUTPUTDENSNORM',label='OUTPUTDENSNORM')),
              Group(Item('XXLINFO',label='XXLINFO'),
              Item('OUTPUTLINEOFSIGHT',label='OUTPUTLINEOFSIGHT'),
              Item('OUTPUTLINEOFSIGHT_SPECTRUM',label='OUTPUTLINEOFSIGHT_SPECTRUM'),
              Item('OUTPUTLINEOFSIGHT_PARTICLES',label='OUTPUTLINEOFSIGHT_PARTICLES'))),

              Item('FORCETEST',label='FORCETEST'),

              HGroup(Group(Item('DEBUG',label='DEBUG'),
                           Item('PARTICLE_DEBUG',label='PARTICLE_DEBUG')),
                     Group(Item('VERBOSE',label='VERBOSE'),
                           Item('CHECKSUM_DEBUG',label='CHECKSUM_DEBUG')))),label='Output')

  def __init__(self, main, **kwargs):
      HasTraits.__init__(self)
      self.main = main
        
def outvar(variable)

    