from prefect import flow


@flow
def hello_world():
  print('Hello from prefect!!')

hello_world()