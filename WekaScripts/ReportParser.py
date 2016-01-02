"""
The report parser takes reports generated by weka and returns
its values
"""

import sys
import re


def get_correctly_classified_instances(report):
    """
    @param report: The weka report
    @type report: String
    """
    o = re.compile("Correctly Classified Instances[\s]*[0-9]*[\s]*([0-9]*.[0-9]*) \%", report)

    
def demo():
    """
    works on a sample string.
    """
    report = """
Number of Leaves  : 	22004

Size of the tree : 	44007


Time taken to build model: 696.34 seconds

=== Stratified cross-validation ===
=== Summary ===

Correctly Classified Instances      198879               69.7733 %
Incorrectly Classified Instances     86157               30.2267 %
Kappa statistic                          0.5342
Mean absolute error                      0.2062
Root mean squared error                  0.4356
Relative absolute error                 47.6479 %
Root relative squared error             93.6432 %
Total Number of Instances           285036
"""


if __name__ == "__main__":
    demo()

