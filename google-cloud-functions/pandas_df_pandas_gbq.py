"""import pandas
import pandas_gbq
import os
from datetime import datetime"""


def bq_load(request):
  # TODO: Set project_id to your Google Cloud Platform project ID.
  project_id = os.environ.get('PROJECT_ID')

  # TODO: Set table_id to the full destination table ID (including the
  #       dataset ID).
  table_id = os.environ.get('TABLE_ID')
  now_ts = datetime.today()

  df = pandas.DataFrame(
      {
          "letters": ["a", "b", "c"],
          "integers": [1, 2, 3],
          "floats": [4.0, 5.0, 6.0],
          "bool1": [True, False, True],
          "bool2": [False, True, False],
          "dates": pandas.date_range("now", periods=3),
      }
  )
  print(df.head(1))

  pandas_gbq.to_gbq(df, table_id, project_id=project_id, if_exists='replace')
  return 'OK ' + str(now_ts)
