#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

""" Defines IEC 61970 CIM.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api import \
    HasTraits, String, Int, Float, List, Trait, Instance, Bool, Range, \
    Property, Enum, Any, Delegate, Tuple, Array, Disallow, cached_property

#------------------------------------------------------------------------------
#  "IEC61970" class:
#------------------------------------------------------------------------------

class IEC61970(HasTraits):
    """ Defines IEC 61970 CIM.
    """

    # This package is responsible for modeling the energy consumers and the
    # system load as curves and associated curve data. Special circumstances
    # that may affect the load, such as seasons and daytypes, are also
    # included here.
    #
    # This information is used by Load Forecasting and Load Management.
    loadmodel = List(Instance(HasTraits), desc="""package is responsible for
        modeling the energy consumers and the system load as curves and
        associated curve data.""")


    generation = List(Instance(HasTraits), desc="""packages that have
        information for Unit Commitment and Economic Dispatch of Hydro and
        Thermal Generating Units, Load Forecasting, Automatic Generation
        Control, and Unit Modeling for Dynamic Training Simulator""")

# EOF -------------------------------------------------------------------------
