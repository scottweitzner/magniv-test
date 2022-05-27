from magniv import task

@task(schedule="@daily", description="Daily hello world!", key="hello world")
def hello_world():
    print("hello world")
