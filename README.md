CME Caterpillar Made Easy
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

The packaged utilizes a number of suites which come with EPD distribution (e.g. Traits, Pandas) which is required for the package to work. A number of read modules are not included for Gadget files and the Rockstar halo catalogues. 

Please contact [brendan.f.griffen@gmail.com](mailto:brendan.f.griffen) if you would like to use this software for your simulation suites.

*Screeshots:*

Candidate Selection
![candidate selection](http://bgriffen.scripts.mit.edu/www/wp-content/uploads/2014/01/candidateselection.png)

Inspect & Generate Lagrangian Regions
![inspect lagrangian region](http://bgriffen.scripts.mit.edu/www/wp-content/uploads/2014/01/lagrangianinspection.png)

Inspect Merger Trees
![inspect lagrangian region](http://bgriffen.scripts.mit.edu/www/wp-content/uploads/2014/01/mergertreeinspection.png)

Examing Halo Distributions Interactively  (via in-line Mayavi)
![Examing Halo Distributions Interactively](http://bgriffen.scripts.mit.edu/www/wp-content/uploads/2014/01/FOFviz.png)

Examing Halo Velocity Field Interactively (via in-line Mayavi)
![Examing Halo Velocity Field Interactively](http://bgriffen.scripts.mit.edu/www/wp-content/uploads/2014/01/velocityhaloinspection.png)

Examine Contatmination Quality
![Examine Contatmination Quality](http://bgriffen.scripts.mit.edu/www/wp-content/uploads/2014/01/contaminationradial.png)

Specify All Gadget Parameters (temporal resolution etc.)
![Specify All Gadget Parameters](http://bgriffen.scripts.mit.edu/www/wp-content/uploads/2014/01/specifysnapshotoutput.png)

Investigate inter-halo relations from Rockstar halo catalogue
![Investigate inter-halo relations](http://bgriffen.scripts.mit.edu/www/wp-content/uploads/2014/01/inspectparams.png)

Run full suites with varied initial conditions (e.g. to determine how resolution effects contamination rate)
![Run full suites with varying initial conditions](http://bgriffen.scripts.mit.edu/www/wp-content/uploads/2014/01/existencecheck.png)
