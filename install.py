from Common import *

class InstallFiles(HasTraits):

    view = View(VGroup( HGroup(Item('libpath',show_label=False,springy=True),
                                Item('makelibdir_button',show_label=False,springy=True)),
                        HGroup(Item('fftw2dir',show_label=False,springy=True),
                            Item('installfftw2_button',show_label=False,springy=True)),
                        HGroup(Item('fftw3dir',show_label=False,springy=True),
                            Item('installfftw3_button',show_label=False,springy=True)),
                        HGroup(Item('hdf5dir',show_label=False,springy=True),
                            Item('installhdf5_button',show_label=False,springy=True)),
    	                HGroup(Item('gsldir',show_label=False,springy=True),
                            Item('installgsl_button',show_label=False,springy=True)),
    	                HGroup(Item('zlibdir',show_label=False,springy=True),
                            Item('installzlib_button',show_label=False,springy=True)),
                        HGroup(Item('szipdir',show_label=False,springy=True),
                            Item('installszip_button',show_label=False,springy=True))))

    libpath = Directory
    fftw2dir = Directory
    fftw3dir = Directory
    gsldir = Directory
    zlibdir = Directory
    hdf5dir = Directory
    szipdir = Directory
    
    installfftw2_button = Button('Install FFTW2')
    installfftw3_button = Button('Install FFTW3')
    installhdf5_button = Button('Install HDF5')
    installgsl_button = Button('Install GSL')
    installzlib_button = Button('Install ZLIB')
    installszip_button = Button('Install SZIP')
    makelibdir_button = Button('Make Directory')

    def _libpath_changed(self):
        self.fftw2dir = self.libpath + '/fftw2'
        self.fftw3dir = self.libpath + '/fftw3'
        self.hdf5dir = self.libpath + '/hdf5'
        self.gsldir = self.libpath + '/gsl'
        self.zlibdir = self.libpath + '/zlib'
        self.szipdir = self.libpath + '/szip'

    def _makelibdir_button_fired(self):
        if not os.path.exists(str(self.libpath)):
            os.makedirs(str(self.libpath))

    def _installfftw2_button_fired(self):
        tmplibpath = './lib/installs/fftw-2.1.5/'
        print "Installing:",tmplibpath

        flagstr = '--enable-type-prefix --enable-mpi'
        tmpdir = os.getcwd()
        os.chdir(tmplibpath)
        os.system("make clean")
        os.system("./configure --prefix=%s %s" % (str(self.fftw2dir),flagstr))
        os.system("make")
        os.system("make install")
        os.system("make clean")
        os.chdir(tmpdir)

        flagstr = '--enable-float --enable-type-prefix --enable-mpi'
        tmpdir = os.getcwd()
        os.chdir(tmplibpath)
        os.system("make clean")
        os.system("./configure --prefix=%s %s" % (str(self.fftw2dir),flagstr))
        os.system("make")
        os.system("make install")
        os.system("make clean")
        os.chdir(tmpdir)

        flagstr = '--enable-mpi'
        tmpdir = os.getcwd()
        os.chdir(tmplibpath)
        os.system("make clean")
        os.system("./configure --prefix=%s %s" % (str(self.fftw2dir),flagstr))
        os.system("make")
        os.system("make install")
        os.system("make clean")
        os.chdir(tmpdir)

        flagstr = '--enable-float --enable-mpi'
        tmpdir = os.getcwd()
        os.chdir(tmplibpath)
        os.system("make clean")
        os.system("./configure --prefix=%s %s" % (str(self.fftw2dir),flagstr))
        os.system("make")
        os.system("make install")
        os.system("make clean")
        os.chdir(tmpdir)

        print "FFTW2 INSTALLED:",str(self.fftw2dir)

    def _installfftw3_button_fired(self):
        tmplibpath = './lib/installs/fftw-3.3.3/'
        print "Installing:",tmplibpath

        flagstr = '--enable-threads  --enable-float'
        tmpdir = os.getcwd()
        os.chdir(tmplibpath)
        os.system("make clean")
        os.system("./configure --prefix=%s %s" % (str(self.fftw3dir),flagstr))
        os.system("make")
        os.system("make install")
        os.system("make clean")
        os.chdir(tmpdir)

        flagstr = '--enable-threads'
        tmpdir = os.getcwd()
        os.chdir(tmplibpath)
        os.system("make clean")
        os.system("./configure --prefix=%s %s" % (str(self.fftw3dir),flagstr))
        os.system("make")
        os.system("make install")
        os.system("make clean")
        os.chdir(tmpdir)

        flagstr = '--enable-type-prefix --enable-threads --enable-float '
        tmpdir = os.getcwd()
        os.chdir(tmplibpath)
        os.system("make clean")
        os.system("./configure --prefix=%s %s" % (str(self.fftw3dir),flagstr))
        os.system("make")
        os.system("make install")
        os.system("make clean")
        os.chdir(tmpdir)

        flagstr = '--enable-type-prefix --enable-threads '
        tmpdir = os.getcwd()
        os.chdir(tmplibpath)
        os.system("make clean")
        os.system("./configure --prefix=%s %s" % (str(self.fftw3dir),flagstr))
        os.system("make")
        os.system("make install")
        os.system("make clean")
        os.chdir(tmpdir)

        print "FFTW3 INSTALLED:",str(self.fftw3dir)

    def _installhdf5_button_fired(self):
        tmplibpath = './lib/installs/hdf5-1.8.10/'
        print "Installing:",tmplibpath
        #(/home/bgriffen/lib/szip,/home/bgriffen/lib/zlib/include,/home/bgriffen/lib/zlib/lib)
        #flagstr = '--enable-fortran --enable-cxx --with-szlib=%s --with-zlib=%s,%s'
        flagstr = '--enable-fortran --enable-cxx'
        tmpdir = os.getcwd()
        os.chdir(tmplibpath)
        os.system("make clean")
        os.system("./configure --prefix=%s %s" % (str(self.hdf5dir),flagstr))
        os.system("make")
        os.system("make install")
        os.system("make clean")
        os.chdir(tmpdir)
        print "HDF5 INSTALLED:",str(self.hdf5dir)
        
    def _installgsl_button_fired(self):
        tmplibpath = './lib/installs/gsl-1.9/'
        print "Installing:",tmplibpath
        tmpdir = os.getcwd()
        os.chdir(tmplibpath)
        os.system("make clean")
        os.system("./configure --prefix=%s" % str(self.gsldir))
        os.system("make")
        os.system("make install")
        os.system("make clean")
        os.chdir(tmpdir)
        print "GSL INSTALLED:",str(self.gsldir)

    def _installszip_button_fired(self):
        tmplibpath = './lib/installs/szip-2.1/'
        print "Installing:",tmplibpath
        tmpdir = os.getcwd()
        os.chdir(tmplibpath)
        os.system("make clean")
        flagstr = '--enable-shared=no --enable-static=yes'
        os.system("./configure --prefix=%s %s" % (str(self.szipdir),flagstr))
        os.system("make")
        os.system("make install")
        os.system("make clean")
        os.chdir(tmpdir)
        print "SZIP INSTALLED:",str(self.szipdir)

    def _installzlib_button_fired(self):
        tmplibpath = './lib/installs/zlib-1.2.8/'
        print "Installing:",tmplibpath
        tmpdir = os.getcwd()
        os.chdir(tmplibpath)
        os.system("make clean")
        os.system("./configure --prefix=%s" % str(self.zlibdir))
        os.system("make")
        os.system("make install")
        os.system("make clean")
        os.chdir(tmpdir)
        print "ZLIB INSTALLED:",str(self.zlibdir)

    def __init__(self, main, **kwargs):
        HasTraits.__init__(self)
        self.main = main
        self.libpath = self.main.headertab.masterpath + '/lib'
        self.fftw2dir = self.libpath + '/fftw2'
        self.fftw3dir = self.libpath + '/fftw3'
        self.hdf5dir = self.libpath + '/hdf5'
        self.gsldir = self.libpath + '/gsl'
        self.zlibdir = self.libpath + '/zlib'
        