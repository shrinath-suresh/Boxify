from setuptools import setup, find_packages


setup(
    name="boxify",
    version="0.1.0",
    description="Package for format conversion and drawing bounding boxes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    # Require MLflow as a dependency of the plugin, so that plugin users can simply install
    # the plugin & then immediately use it with MLflow
    # install_requires=["torchserve", "torch-model-archiver", "mlflow"],
    # entry_points={"mlflow.deployments": "torchserve=mlflow_torchserve"},
)