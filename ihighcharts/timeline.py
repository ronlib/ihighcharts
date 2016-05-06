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

    base_dict = {
        'chart': {
            'type': 'line',
            },
        'series': [],
        'xAxis': {
            'gridLineWidth': 1,
            'type': 'datetime',
            'plotBands': [{
                u'color': u'#FCFFC5',
                # u'from': 4.5,
                u'id': u'plotband-1',
                # u'to': 7.5
                }]
            }

        }

    x = pd.read_csv('/home/ron/notebooks/data.csv')
    data = x[["date", "bank_status"]].to_dict('split')
    data.pop('columns', None)
    data.pop('index', None)

    base_dict['series'].append(data)




    # base_dict = \
    #   {u'series': [
    #       {u'data':
    #            [29.9,
    #                 71.5,
    #                 106.4,
    #                 129.2,
    #                 144,
    #                 176,
    #                 135.6,
    #                 148.5,
    #                 216.4,
    #                 194.1,
    #                 95.6,
    #            54.4]}],
    #            u'xAxis':
    #            {u'categories':
    #                 [u'Jan',
    #                      u'Feb',
    #                      u'Mar',
    #                      u'Apr',
    #                      u'May',
    #                      u'Jun',
    #                      u'Jul',
    #                      u'Aug',
    #                      u'Sep',
    #                      u'Oct',
    #                      u'Nov',
    #                 u'Dec'],
    #                 u'plotBands':
    #                 [{u'color': u'#FCFFC5',
    #                       u'from': 4.5,
    #                       u'id': u'plotband-1',
    #                       u'to': 7.5}]}}



    # pass
