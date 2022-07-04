from algorithmanalysis import Algorithm, CASES
from algorithmanalysis.algorithms import merge_sort


Algorithm.analyze(merge_sort, case=CASES.WORST, size=10000)
