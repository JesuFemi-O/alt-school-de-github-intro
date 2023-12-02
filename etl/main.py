"""
This script serves as an entrypoint to our data pipeline
for orchestrating the Alt school DE Project.

"""

def run_raw_pipeline():
    print("Starting etl on raw daatabase pipeline...")

def run_services_pipeline():
    print("Starting etl on services database pipeline...")

def run():
    print("starting etl pipeline..")
    run_raw_pipeline()
    run_services_pipeline()


if __name__ == "__main__":
    run()