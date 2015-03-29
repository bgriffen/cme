CME: Caterpillar Made Easy
===

Interactive suite to do the following tasks for the Caterpillar Project being carried out at MIT/Harvard:

* generate list of candidates based on tunable isolation and merger history criteria
* inspect lagrangian region properties (e.g. size, volume, morphology)
* contruct initial conditions for cosmological simulations using MUSIC (Hahn & Abel 2010).
* run cosmological simulations using P-Gadget3.
* examine contamination of low-resolution particles in resimulation across suite
* create heatmaps of contamination in every projection
* do 3D visualisations of halo and particle velocity field and positions
* submit job via both PBS and SLURM submission systems.

Not a single line of code is required by the user. 

The packaged utilizes a number of suites which come with EPD distribution (e.g. Traits, Pandas) which is required for the package to work. A number of read modules are not included for Gadget files and the Rockstar halo catalogues. Although it is for the *Caterpillar Project*, it can in principle work on any cosmological simulation suite. 

Please contact [brendan.f.griffen@gmail.com](mailto:brendan.f.griffen) if you would like to use this software for your simulation suites.

## Examples

#### Candidate Selection
![candidate selection](http://brendangriffen.com/assets/cme/candidateselection.png)

#### Inspect & Generate Lagrangian Regions
![inspect lagrangian region](http://brendangriffen.com/assets/cme/lagrangianinspection.png)

#### Inspect Merger Trees
![inspect lagrangian region](http://brendangriffen.com/assets/cme/mergertreeinspection.png)

#### Examing Halo Distributions Interactively  (via Mayavi)
![Examing Halo Distributions Interactively](http://brendangriffen.com/assets/cme/FOFviz.png)

#### Examing Halo Velocity Field Interactively (via Mayavi)
![Examing Halo Velocity Field Interactively](http://brendangriffen.com/assets/cme/velocityhaloinspection.png)

#### Examine Contamination Quality
![Examine Contatmination Quality](http://brendangriffen.com/assets/cme/contaminationradial.png)

#### Examine Contamination Quality (via heatmap)
![Examine Contatmination Heatmaps](http://brendangriffen.com/assets/cme/contaminationheatmap.png)

#### Specify All Gadget Parameters (temporal resolution etc.)
![Specify All Gadget Parameters](http://brendangriffen.com/assets/cme/specifysnapshotoutput.png)

#### Investigate inter-halo relations from Rockstar halo catalogue
![Investigate inter-halo relations](http://brendangriffen.com/assets/cme/inspectparams.png)

#### Run full suites with varied initial conditions 
##### (e.g. to determine how resolution effects contamination rate)
![Run full suites with varying initial conditions](http://brendangriffen.com/assets/cme/existencecheck.png)

#### Submit jobs to cluster via PBS or SLURM
![Submit jobs](http://brendangriffen.com/assets/cme/submitjob.png)
