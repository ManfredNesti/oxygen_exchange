#!/bin/bash
## ---------------------------------------------------------------------
## Copyright (C) 2021 by the lifex authors.
##
## This file is part of lifex.
##
## lifex is free software; you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## lifex is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## Lesser General Public License for more details.
##
## You should have received a copy of the GNU Lesser General Public License
## along with lifex.  If not, see <http://www.gnu.org/licenses/>.
## ---------------------------------------------------------------------

# Author: Pasquale Claudio Africa <pasqualeclaudio.africa@polimi.it>.

############################
### Resource allocation. ###
############################

# No. nodes to allocate.
TORQUE_N_NODES=1

# Total no. processors per node to allocate.
TORQUE_PPN=56

# Walltime, in hh:mm:ss.
TORQUE_WALLTIME=120:00:00

# Torque resource properties specifier.
TORQUE_RESOURCE_PROPERTIES=:big

##########################
### Job configuration. ###
##########################

# Torque partition.
TORQUE_JOB_PARTITION=gigatlong


# Executable name.
TORQUE_EXEC_NAME=./lifex_example_perfusion_heart

# Executable command-line arguments.
TORQUE_EXEC_ARGS="-f OE.prm -o OE"

# Slurm job name.
TORQUE_JOB_NAME=OE


#################################
### Output and notifications. ###
#################################

# Standard output/error log files.
TORQUE_FILENAME_OUTPUT=${TORQUE_JOB_NAME}_output.log
TORQUE_FILENAME_ERROR=${TORQUE_JOB_NAME}_error.log

# Email notification type.
# Valid values are:
# a: job aborts
# b: job begins
# e: job exits
TORQUE_MAIL_TYPE=abe

# User email.
TORQUE_MAIL_ADDRESS=manfred.nesti@mail.polimi.it
