from setuptools import setup, find_packages


setup(
    name="microscope_esp32_controller_serial",
    version="1.0",
    packages=find_packages("microscope_esp32_controller_serial"),
    scripts=['scripts/microscope-esp32-controller-serial']
)
