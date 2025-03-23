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

In ``./src/main.py``, tests are integrated for the following three products:
  - WISE-2410
  - WISE-4610
  - WISE-2200-M

To run the tests, execute the following command:
 
.. code-block:: shell

    pipenv run python ./src/main.py

After running, the downlink commands for each product will be output sequentially, for example:
 
.. code-block:: shell

    === WISE-2410 Tests ===
    Generated WISE-2410 FFT Command: [command output]
    Generated WISE-2410 TimeSync Command: [command output]
    Generated WISE-2410 Uplink Interval Command: [command output]
    
    === WISE-4610 Tests ===
    Generated WISE-4610 TimeSync Command: [command output]
    Generated WISE-4610 Uplink Interval Command: [command output]
    
    === WISE-2200-M Tests ===
    Generated WISE-2200-M TimeSync Command: [command output]
    Generated WISE-2200-M Uplink Interval Command: [command output]
    Generated WISE-2200-M Transparent Command: [command output]

*For further information on the supported functions of this repository, please refer to the last section of this document.*

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