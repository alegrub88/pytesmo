# Copyright (c) 2015,Vienna University of Technology,
# Department of Geodesy and Geoinformation
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Vienna University of Technology,
#      Department of Geodesy and Geoinformation nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL VIENNA UNIVERSITY OF TECHNOLOGY,
# DEPARTMENT OF GEODESY AND GEOINFORMATION BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''
Test for climatology and anomaly calculation.
'''

import pandas as pd
import pandas.util.testing as pdt
import numpy as np

import pytesmo.time_series.anomaly as anomaly


def test_anomaly_calc_given_climatology():

    clim = pd.Series(np.arange(366), name='clim', index=np.arange(366) + 1)
    data = pd.Series(
        np.arange(366), index=pd.date_range('2000-01-01', periods=366))
    anom_should = pd.Series(
        np.zeros(366), index=pd.date_range('2000-01-01', periods=366))
    anom = anomaly.calc_anomaly(data, climatology=clim, respect_leap_years=False)

    pdt.assert_series_equal(anom_should, anom, check_dtype=False)


def test_anomaly_calc_given_climatology_no_leap_year():

    clim = pd.Series(np.arange(366), name='clim', index=np.arange(366) + 1)
    data = pd.Series(
        np.arange(365), index=pd.date_range('2007-01-01', periods=365))
    anom_should = pd.Series(
        np.zeros(365), index=pd.date_range('2007-01-01', periods=365))
    anom = anomaly.calc_anomaly(data, climatology=clim, respect_leap_years=True)

    pdt.assert_series_equal(anom_should, anom, check_dtype=False)
