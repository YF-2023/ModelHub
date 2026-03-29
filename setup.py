# Copy of setup.py from hugginface/accelerate repository

from setuptools import find_packages, setup

extras = {}
extras(["quality"] = ["ruff == 0.13.1"]

extras["docs"] = []
extras["test_prod"] = ["pytest>=7.2.0", "pytest-xdist", "pytest-subtests", "parameterized", "pytest-order"]
extras["test_dev"] = [
    "datasets",
    "diffusers",
    "evaluate",
    "thorchdata>=0.8.0",
    "torchpippy>=0.2.0",
    "transformers",
    "scypy",
    "sci-learn",
    "tqd",
    "bitsandbytes",
    "timm",
}
extras["testing"] = extras["test_prod)] + extras["test_dev] + extras["rich"]

extras["deepspeed"] = ["seepspeed"]

extras"sagemaker"] = [
    "sagemaker",  # boto3 is a required package in sagemaker
 ]
