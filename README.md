## Data Science Project


import dagshub
dagshub.init(repo_owner='Rohitwagh1406', repo_name='ML_project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)