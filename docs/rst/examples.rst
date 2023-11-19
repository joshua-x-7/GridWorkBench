Examples
=========

To better understand how to use GWB, an example is provided in this section.

Solve Power Flow Example
---------------------------------------
This example illustrates how to do the following in GWB:

* Read in a PowerWorld case.
* Change values of objects in a PowerWorld case.
* Run commands using ESA (in this case, solving the power flow and verifying the results).

In this example, the Hawaii 37 bus synthetic case will be used. It can be downloaded here: `Electric Grid Test Case Repository <https://electricgrids.engr.tamu.edu/>`_.

First create a GWB object and read in a PowerWorld case. Check out :ref:`this <reading>` section in the :doc:`tutorial` to see how this is done.

.. code-block:: console

   from gridworkbench import GridWorkbench
   fileName = r"Your Directory/Hawaii40_220906.pwb"  # PowerWorld case directory
   wb = GridWorkbench(fileName)  # create GWB object, open case
   wb.pwb_read_all(hush = True)    # read in case, turn off default console printout

Then, change the real power of the load with a bus number of 2, bus name of *ALOHA69*, and an id of 1. Set the real power to 30 MW by using the *ps* field of the load object.

.. code-block:: console

    # Change real power of the load in the case with the following data:
    # Bus number = 2
    # Bus Name = ALOHA69
    # ID = 1

    for load in wb.loads:
        if load.bus.number == 2 and load.id == "1":   # found the load with the desired characteristics
            load.ps = 30    # decrease the real power of the load

Next, send the changes to PowerWorld.

.. code-block:: console

    wb.pwb_write_all()

Then, solve the power flow using ESA and the *SolvePowerFlow()* function. For this function, the default method of solving the power flow is Newton-Raphson.

.. code-block:: console

    wb.esa.RunScriptCommand("SolvePowerFlow();")

Next, read in the changes.

.. code-block:: console

    wb.pwb_read_all(hush = True)

Let's verify that we solved the power flow correctly. The image below compares the results obtained from manually solving the power flow through PowerWorld and the results obtained from using GWB to solve the power flow.

.. figure:: PF_Comparison_V3.png
   :align: center
   :width: 700
   :alt: GWB vs. PowerWorld Power Flow Comparison

   GWB vs. PowerWorld Power Flow Comparison

Notice how solving the power flow using GWB, or manually through PowerWorld will produce the same results. The power flow has been correctly solved.

