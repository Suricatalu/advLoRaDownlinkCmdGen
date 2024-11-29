Advantech LoRa Product Downlink Command Generator
=================================================

*(Not Advantech Official Repo)*

Advantech offers a comprehensive range of LoRa-related products, including the WISE-2410, WISE-4610, and WISE-2200-M series. Notably, the downlink command, which is frequently utilized by users for controlling LoRa nodes, is a key component of these products. To address the need for users who require the generation of downlink commands in Python, the repository provides a solution. Subsequently, these commands can be transmitted to LoRa nodes via the WISE-6610v2 device.

Installation & Activate Project
-------------------------------

Pyenv & Pipenv
~~~~~~~~~~~~~~

The environment is developed using pyenv and pipenv. Please install these two tools first.

On macOS
^^^^^^^^

1. **Install pyenv & pipenv**

   Follow the instructions from the official documentation to install `pyenv` and `pipenv`.

2. **Spawn a subshell and activate the virtual environment**

   In the root of the repository, input the below command to activate the pipenv environment:

   .. code-block:: shell

       pipenv shell

Quick Start
-----------

In the ``./main.py`` file, the code responsible for generating time synchronization commands is presented below:

The user has the ability to modify the ``./main.py`` file to generate the other downlink commands for other devices.

*For further information on the supported functions of this repository, please refer to the last section of this document.*

.. code-block:: python

    import shared.downlinkFields as DWHDR
    from products.WISE2410 import WISE2410

    def wise2410testtimesync():
        device = WISE2410()

        cmd = device.time_sync(
            type=DWHDR.TIMESYNC_TYPE_I,
            fcnt=0,
            timestamp="2020-06-23T10:16:07+08:00",
            version=0
        )

        print(f"Generated WISE-2410 Command: {cmd}")

    def main():
        wise2410testtimesync()

    if __name__ == "__main__":
        main()

Then, the user can execute the below command to generate the downlink command.

.. code-block:: shell

    pipenv run python ./src/main.py 
    # Output: Generated WISE-2410 Command: 80001d611b02323032302d30362d32335431303a31363a30372b30383a30300066

Supported Function
------------------

- WISE-2410

    * Time Sychronization (Unix Time or ISO 8601)
    * Change Uplink Interval
    * FFT Command (Log Index or Log Index with Timestamp)

- WISE-4610

    * Time Sychronization (Unix Time or ISO 8601)
    * Change Uplink Interval

- WISE-2200-M

    * Time Sychronization (Unix Time or ISO 8601)
    * Change Uplink Interval
    * Transparent