#!/bin/sh

#
# Description:
# We expect to have the CrabTestPackage directory under CMSSW_X_Y_Z/src directory,
# Under CMSSW_X_Y_Z/src, run
# bash CrabTestPackage/make_tarball.sh
# which will create a tarball two directory above just outside CMSSW_X_Y_Z
#

#tar czvf ../../Tutorial.tgz Tutorial/tutorial.py Tutorial/crab_tutorial.cfg 
#tar czvf ../../Globus.tgz Globus/MyTest Globus/setup.sh 

tar czvf ../../CrabTestPackage.tgz CrabTestPackage/cmsDriver_commands.sh CrabTestPackage/make_tarball.sh CrabTestPackage/*.cfg CrabTestPackage/slurp.py
