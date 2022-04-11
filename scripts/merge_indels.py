import sys
import pandas as pd
indels = sys.argv[2]
metadata = sys.argv[1]
of = sys.argv[3]
metadata_d = pd.read_csv(metadata, sep = "\t")
indels_d = pd.read_csv(indels)

metadata_d.merge(indels_d, on = 'strain', how = 'left').to_csv(of, sep = "\t", index=False)
