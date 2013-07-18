# This script read in ICs and shifts lower resolution particles from all being type 5

import numpy as np
import readsnap as rs
import os

def getBlocks(path):

    #pathname = '/n/home01/bgriffen/data/caterpillar/ics/halo80609/l12/p' + padding + '/nvir' + nvir + '/ics'
    pathname = path + '/ics'

    # defining header blocks:
    nall=np.zeros(6,dtype=np.int32)
    massarr=np.zeros(6,dtype=np.float64)
    fill=np.zeros(24,dtype=np.int32)
    
    header=rs.snapshot_header(pathname+'.0')
    nall[1]=header.nall[1]
    massarr[1]=header.massarr[1]
    count=0

    # first find break down of nall

    for i in xrange(0,header.filenum):

        header=rs.snapshot_header(pathname+'.'+str(i))

        if (header.npart[5]>0)&(header.massarr[5]==0.0):

            if count==0:
                datM=rs.read_block(pathname+'.'+str(i), "MASS",parttype=5,doubleprec=False,mult=False)
                count = count+1
            else:
                datM=np.concatenate((datM,rs.read_block(pathname+'.'+str(i), "MASS",parttype=5,doubleprec=False,mult=False)))
                
    mass=np.unique(datM)

    type5Tot=0
    for j in xrange(0,len(mass)):

        mask=datM==mass[j]
        print "Mass|Num", mass[j], mask.sum()

        if (j<3) | (len(mass)==4) :
            nall[j+2]=mask.sum()
            massarr[j+2]=mass[j]
        else:
            type5Tot=type5Tot+mask.sum()

    if type5Tot>0:
        nall[5]=type5Tot
        
    print nall
    print massarr

    print (header.nall).sum(), nall.sum()

    # now have info. go through each snapshot file and rewrite
    
    for i in xrange(0,header.filenum):

        header=rs.snapshot_header(pathname+'.'+str(i))

        ids1=rs.read_block(pathname+'.'+str(i), "ID  ",parttype=1,mult=False)
        pos1=rs.read_block(pathname+'.'+str(i), "POS ",parttype=1,doubleprec=False,mult=False)
        vel1=rs.read_block(pathname+'.'+str(i), "VEL ",parttype=1,doubleprec=False,mult=False,physical_velocities=False)

        ids5=rs.read_block(pathname+'.'+str(i), "ID  ",parttype=5,mult=False)
        pos5=rs.read_block(pathname+'.'+str(i), "POS ",parttype=5,doubleprec=False,mult=False)
        vel5=rs.read_block(pathname+'.'+str(i), "VEL ",parttype=5,doubleprec=False,mult=False,physical_velocities=False)

        npart=np.zeros(6,dtype=np.int32)
        npart[1]=header.npart[1]
        
        if (header.npart[5]>0)&(header.massarr[5]==0.0):

            #ids5=rs.read_block(pathname+'.'+str(i), "ID  ",parttype=5,mult=False)
            #pos5=rs.read_block(pathname+'.'+str(i), "POS ",parttype=5,doubleprec=False,mult=False)
            #vel5=rs.read_block(pathname+'.'+str(i), "VEL ",parttype=5,doubleprec=False,mult=False,physical_velocities=False)
            datM=rs.read_block(pathname+'.'+str(i), "MASS",parttype=5,doubleprec=False,mult=False)

            type5Tot=0
            for j in xrange(0,len(mass)):

                mask=datM==mass[j]
                #print "Mass|Num", mass[j], mask.sum()

                if (j<3) | (len(mass)==4) :
                    npart[j+2]=mask.sum()
                else:
                    type5Tot=type5Tot+mask.sum()
                    
            if type5Tot>0:
                npart[5]=type5Tot
                    
        #testing
        print "Snapshot:",i, (header.npart).sum()==npart.sum()
            
        # now start outputting
        
        f=open(pathname+'_rewrite.'+str(i),'w')

        # header
        sz=np.int32(256)
        sz.tofile(f)
        npart.tofile(f)
        massarr.tofile(f)
        (header.time).tofile(f)
        (header.redshift).tofile(f)
        (header.sfr).tofile(f)
        (header.feedback).tofile(f)
        nall.tofile(f)
        (header.cooling).tofile(f)
        (header.filenum).tofile(f)
        (header.boxsize).tofile(f)
        (header.omega_m).tofile(f)
        (header.omega_l).tofile(f)
        (header.hubble).tofile(f)
        fill.tofile(f)
        sz.tofile(f)

        # positions
        sz=np.int32((header.npart).sum()*3*4)
        sz.tofile(f)
        pos1.tofile(f)

        if (header.npart[5]>0):
            for j in xrange(0,len(mass)):
                mask=datM==mass[j]
                temp=pos5[mask]
                temp.tofile(f)
        sz.tofile(f)

        # velocities
        sz=np.int32((header.npart).sum()*3*4)
        sz.tofile(f)
        vel1.tofile(f)

        if (header.npart[5]>0):
            for j in xrange(0,len(mass)):
                mask=datM==mass[j]
                temp=vel5[mask]
                temp.tofile(f)
        sz.tofile(f)

        #ids
        sz=np.int32((header.npart).sum()*4)
        sz.tofile(f)
        ids1.tofile(f)

        if (header.npart[5]>0):
            for j in xrange(0,len(mass)):
                mask=datM==mass[j]
                temp=ids5[mask]
                temp.tofile(f)
        sz.tofile(f)

        # mass block (if necessary)
        if (massarr[5]==0.0)&(npart[5]>0):
            sz=np.int32(npart[5]*4)
            sz.tofile(f)
            for j in xrange(3,len(mass)):
                mask=datM==mass[j]
                temp=datM[mask]
                temp.tofile(f)
            sz.tofile(f)
        f.close()

    # now smoothing length calculation
    mtot=3.0*header.omega_m*10000.0/8.0/np.pi/43.0118*header.boxsize*header.boxsize*header.boxsize

    soft=header.boxsize/((mtot/massarr)**(1.0/3.0))/40.0
    print "mass", massarr
    print "softening", soft

    soft=header.boxsize/((mtot/mass)**(1.0/3.0))/40.0
    print "mass", mass
    print "softening", soft

    

if __name__ == "__main__":
    import sys
    getBlocks()            

