#------------------------------------------------------------------------------
# Copyright (C) 2008 Richard W. Lincoln
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

""" Defines the load element """

#------------------------------------------------------------------------------
#  "Load" class:
#------------------------------------------------------------------------------

class Load(PowerConversionElement):
    """ The load is assumed balanced over the no. of phases defined.  To model
    unbalanced loads, define separate single-phase loads.

    If you do not specify load shapes defaults are:
        Yearly:  Defaults to No variation or Daily when Daily is defined
        Daily:   Defaults to No variation  (i.e. multiplier = 1.0 always)
        Dutycycle: Defaults to Daily shape
        Growth: Circuit default growth factor


    A Load is a complicated Power Conversion element that is at the heart of
    many analyses.  It is basically defined by its nominal kW and PF or its kW
    and kvar.  Then it may be modified by a number of multipliers, including
    the global circuit load multiplier, yearly load shape, daily load shape,
    and a dutycycle load shape.

    The default is for the load to be a current injection source.  Thus, its
    primitive Y matrix contains only the impedance that might exist from the
    neutral of a wye-connected load to ground.  However, if the load model is
    switched to Admittance from PowerFlow (see Set LoadModel command), the load
    is converted to an admittance and included in the system Y matrix.  This
    would be the model used for fault studies where convergence might not be
    achieved because of low voltages.

    Loads are assumed balanced for the number of phases specified.  If you
    would like unbalanced loads, enter separate single-phase loads.

    There are three legal ways to specify the base load:
        1.kW, PF
        2.kw, kvar
        3.kVA, PF

    If you sent these properties in the order shown, the definition should
    work. If you deviate from these procedures, the result may or may not be
    what you want.  (To determine if it has accomplished the desired effect,
    execute the Dump command for the desired load(s) and observe the settings.)

    """

    # Name of bus to which the load is connected.  Include node definitions if
    # the terminal conductors are connected abnormally.  3-phase Wye-connected
    # loads have 4 conductors; Delta-connected have 3.  Wye-connected loads, in
    # general, have one more conductor than phases.  1-phase Delta has 2
    # conductors; 2-phase has 3.  The remaining Delta, or line-line,
    # connections have the same number of conductors as phases.
    bus_1 = None

    # Number of Phases, this load.  Load is evenly divided among phases.
    n_phases = 3

    # Nominal rated (1.0 per unit) voltage, kV, for load. For 2- and 3-phase
    # loads, specify phase-phase kV.  Otherwise, specify actual kV across each
    # branch of the load.  If wye (star), specify phase-neutral kV.  If delta
    # or phase-phase connected, specify phase-phase kV.
    kv = 12.47

    # Total base kW for the load.  Normally, you would enter the maximum kW for
    # the load for the first year and allow it to be adjusted by the load
    # shapes, growth shapes, and global load multiplier.
    # Legal ways to define base load:
    #    kW, PF
    #    kW, kvar
    #    kVA, PF
    kw = 10

    # Load power factor.  Enter negative for leading powerfactor (when kW and
    # kvar have opposite signs.)
    pf = 0.88

    # Integer code for the model to use for load variation with voltage.
    # Valid values are:
    # 1:Standard constant P+jQ load. (Default)
    # 2:Constant impedance load.
    # 3:Const P, Quadratic Q (like a motor).
    # 4:Nominal Linear P, Quadratic Q (feeder mix). Use this with CVRfactor.
    # 5:Constant Current Magnitude
    # 6:Const P, Fixed Q
    # 7:Const P, Fixed Impedance Q
    # For Types 6 and 7, only the P is modified by load multipliers.
    model = 1

    # Load shape to use for yearly simulations.  Must be previously defined
    # as a Loadshape object. Defaults to Daily load shape when Daily is
    # defined.  The daily load shape is repeated in this case. Otherwise, the
    # default is no variation.
    yearly = ""

    # Load shape to use for daily simulations.  Must be previously defined
    # as a Loadshape object of 24 hrs, typically. Default is no variation
    # (constant) if not defined. Side effect: Sets Yearly load shape if not
    # already defined.
    daily = ""

    # Load shape to use for duty cycle simulations.  Must be previously defined
    # as a Loadshape object.  Typically would have time intervals less than
    # 1 hr. Designate the number of points to solve using the Set Number=xxxx
    # command. If there are fewer points in the actual shape, the shape is
    # assumed to repeat. Defaults to Daily curve If not specified.
    duty = ""

    # Characteristic  to use for growth factors by years.  Must be previously
    # defined as a Growthshape object. Defaults to circuit default growth
    # factor
    growth = ""

    # {wye or LN | delta or LL}.
    conn = "wye"

    # Specify the base kvar for specifying load as kW & kvar.  Assumes kW has
    # been already defined.  Alternative to specifying the power factor.  Side
    # effect: the power factor and kVA is altered to agree.
    kvar = 5

    # Neutral resistance of wye (star)-connected load in actual ohms. If
    # entered as a negative value, the neutral is assumed to be open, or
    # floating.
    r_neut = -1

    # Neutral reactance of wye(star)-connected load in actual ohms.  May be
    # + or -.
    x_neut = 0

    # {Variable | Fixed | Exempt}.  Default is variable. If Fixed, no load
    # multipliers apply;  however, growth multipliers do apply.  All
    # multipliers apply to Variable loads.  Exempt loads are not modified by
    # the global load multiplier, such as in load duration curves, etc.  Daily
    # multipliers do apply, so this is a good way to represent industrial load
    # that stays the same for the period study.
    status = "variable"

    # An arbitrary integer number representing the class of load so that load
    # values may be segregated by load value. Default is 1; not used
    # internally.
    klass = 1

    # Minimum per unit voltage for which the MODEL is assumed to apply.
    # Below this value, the load model reverts to a constant impedance model.
    v_min_pu = 0.95

    # Maximum per unit voltage for which the MODEL is assumed to apply.
    # Above this value, the load model reverts to a constant impedance model.
    v_max_pu = 1.05

    # Minimum per unit voltage for load EEN evaluations, Normal limit.
    # Default = 0, which defaults to system "vminnorm" property (see Set
    # Command under Executive).  If this property is specified, it ALWAYS
    # overrides the system specification. This allows you to have different
    # criteria for different loads. Set to zero to revert to the default system
    # value.
    v_min_norm = 0.0

    # Minimum per unit voltage for load UE evaluations, Emergency limit.
    # Default = 0, which defaults to system "vminemerg" property (see Set
    # Command under Executive).  If this property is specified, it ALWAYS
    # overrides the system specification. This allows you to have different
    # criteria for different loads.  Set to zero to revert to the default
    # system value.
    v_min_emerg = 0.0

    # Rated kVA of service transformer for allocating loads based on connected
    # kVA at a bus. Side effect:  kW, PF, and kvar are modified.
    xf_kva = 0.0

    # Allocation factor for allocating loads based on connected kVA at a bus.
    # Side effect:  kW, PF, and kvar are modified by multiplying this factor
    # times the XFKVA (if > 0).
    allocation_factor = 0.5

    # Specify base Load in kVA (and power factor).  This is intended to be used
    # in combination with the power factor (PF) to determine the actual load.
    kva = 11.3636

    # Percent mean value for load to use for monte carlo studies if no
    # loadshape is assigned to this load.
    pct_mean = 50

    # Percent Std deviation value for load to use for monte carlo studies if no
    # loadshape is assigned to this load.
    pct_std_dev = 10

    # Percent reduction in active power (watts) per 1% reduction in voltage
    # from 100% rated. Typical values range from 0.4 to 0.8. Applies to Model=4
    # only. Intended to represent conservation voltage reduction or voltage
    # optimization measures.
    cvr_watts = 1

    # Percent reduction in reactive power (vars) per 1% reduction in voltage
    # from 100% rated. Typical values range from 2 to 3. Applies to Model=4
    # only. Intended to represent conservation voltage reduction or voltage
    # optimization measures.
    cvr_vars = 2

# EOF -------------------------------------------------------------------------