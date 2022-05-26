from collections import namedtuple
import pandas as pd

def useNamedTuple(n, colmnNames, data):
    col = colmnNames.split()
    student = namedtuple('student', col)
    total = 0
    for i in range(n):
        # fields could be in different orders
        field1, field2, field3, field4 = data[i].split()

        row = student(field1, field2, field3, field4)
        total += int(row.MARKS)
    print('{:.2f}'.format(total/n))


def usePandas(n, colmnNames, data):
    col = colmnNames.split()
    def item_looper():
        for i in range(n):
            # fields could be in different orders
            field1, field2, field3, field4 = data[i].split()
            yield field1, field2, field3, field4

    df_list = [item_info for item_info in item_looper()]
    df = pd.DataFrame(df_list, columns=col)
    df = df.astype({'MARKS': 'int', 'CLASS': 'long', 'NAME': 'string', 'ID': 'long'})
    df.set_index('ID', inplace=True)
    print('{:.2f}'.format(df['MARKS'].mean(axis=0)))

useNamedTuple(5, "MARKS      CLASS      NAME       ID",
              ["92         2          Calum      1",
               "82         5          Scott      2",
               "94         2          Jason      3",
               "55         8          Glenn      4",
               "82         2          Fergus     5"])

usePandas(5, "MARKS      CLASS      NAME       ID",
          ["92         2          Calum      1",
           "82         5          Scott      2",
           "94         2          Jason      3",
           "55         8          Glenn      4",
           "82         2          Fergus     5"])