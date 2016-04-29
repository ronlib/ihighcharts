import datetime
from IPython import display
import pandas as pd
import numpy as np

def display_chart(events):
    # TODO: remove

    x = pd.date_range(datetime.date.today(), periods=10)
    y = pd.DataFrame(np.zeros([10,2]), index=x, columns=['A', 'B'])
    y['B']=y['A']=range(10)
    y['C']=np.random.choice(['red','blue'],size=10)
    y['B'] = y['B']+1



    pass
