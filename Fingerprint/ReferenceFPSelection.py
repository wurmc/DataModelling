#  Copyright (c) 2019. Clara Wurm
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of
#  this software and associated documentation files (the "Software"), to deal in
#  the Software without restriction, including without limitation the rights to use,
#  copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
#  Software, and to permit persons to whom the Software is furnished to do so,
#  subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
#  FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHOR OR
#  COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
#  IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#  CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# functionality to select one reference fp out of given set of fingerprints

from Fingerprint import Fingerprint
from Distance import FingerprintRestoration
from Fingerprint import AvgFPBuild
from Distance import DistanceCalculation
from Fingerprint import FingerprintStorage


# managing of reference fp selection
def select_reference_fp():
    ref_fp = Fingerprint.Fingerprint()
    # restore fingerprints from saved csv
    arr_fps = FingerprintRestoration.restore_fp()

    # call avg fp build with arr_fps in avg_fp
    avg_fp = AvgFPBuild.build_avg_fp(arr_fps)

    # call distance calc with avg_fp and arr_fps in arr_dist
    arr_dist = []
    arr_index = []
    for o_fp in arr_fps:
        arr_dist.append(DistanceCalculation.calculate_distance(avg_fp, o_fp))
        arr_index.append(arr_fps.index(o_fp))

    # find minimal distance of arr_dist including index of original fp, set reference fp with original fp
    min_dist = min(arr_dist)
    ind = arr_dist.index(min_dist)
    ref_fp = arr_fps[ind]

    # save original fp as reference fp in csv file
    tmp_arr_fp = []
    tmp_arr_fp.append(ref_fp)
    FingerprintStorage.store_fingerprint(tmp_arr_fp)
