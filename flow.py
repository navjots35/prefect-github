from prefect import flow


@flow(log_prints=True)
def hello():
    print("HAHAHAHAHAAHAHHHHHAHHH! this is github actions again")


if __name__ == "__main__":
    hello.deploy(
        name="github-deploy-actions",
        work_pool_name="github-pool",
        image="kevingrismoreprefect/cicd-example:latest",
    )
