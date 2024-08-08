from setuptools import setup, find_packages

setup(
    name="clipllm",
    version="0.1",
    author="Peyton, HKUSTGZ",
    description="automatically process input from clipboard",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=["numpy", "numba", "joblib"],
    test_suite="tests",
)
