GWB Documentation
===================
Use this documentation to get more in-depth information about the GWB objects and container objects.

The GWB Object
--------------------------

In this documentation, we assume that a GWB object named *wb* has already been created.

To open up a PowerWorld case, use the ``wb.open_pwb()`` function:

.. py:function:: wb.open_pwb(fileName = None)

   Open up a PowerWorld case.

   :param fileName: Directory to the PowerWorld case.
   :type kind: str
   :return: None
   :rtype: None

To read in a PowerWorld case, use the ``wb.pwb_read_all()`` function. Make sure the PowerWorld case has been opened before using this function.

.. py:function:: wb.pwb_read_all(hush = False)

   Read in a PowerWorld case.

   :param hush: A control to turn on or off the default printout after reading in the case. Set to True to turn off printout-it's set to False by default. Recommended to set hush to True if calling this function many times to avoid cluttered printout.
   :type kind: bool
   :return: None
   :rtype: None

To send changes to the local PowerWorld case being used, use the ``wb.pwb_write_all()`` function.

.. py:function:: wb.pwb_write_all()

   Send changes to local PowerWorld case.

   :return: None
   :rtype: None


To save changes to the local PowerWorld case, use the ``wb.esa.SaveCase()`` function.

.. py:function:: wb.esa.SaveCase(fname)

   Save a copy of the local PowerWorld case.

   :param fname: The directory to the new PowerWorld case.
   :type kind: str
   :return: None
   :rtype: None

To close a PowerWorld case, use the ``wb.close_pwb()`` function. After closing a PowerWorld case, a new one can be opened in the same script.

.. py:function:: wb.close_pwb()

   Close the current PowerWorld case.

   :return: None
   :rtype: None

**The following sections give more information about the container objects in GWB.** To see the hierarchy of the objects, check out :ref:`this <container>` section in the :doc:`tutorial` for more information.

.. note::

   In this documentation, when referring to objects in a power system, such as buses, substations, or generators, we refer to their GWB container objects.

.. _region:

Region Objects
----------------------

A region is a very large portion of the power system. Most grids will only have one region. Regions can be accessed by their number or iterated over using the GWB object.

Here are some of the fields that area objects have:

* areas - all areas contained in the region
* branches - all branches contained in the region
* buses - all buses contained in the region
* gens - all generators contained in the region
* loads - all loads contained in the region
* number - the region's number
* shunts - all shunts contained in the region
* subs - all substations contained in the region
* wb - the GWB object

.. _area:

Area Objects
--------------------

Area objects comprise a large part of the power system, but are smaller than regions. They can be accessed by their number, through the workbench object, or through a region object.

Here are some of the fields that areas objects have:

* branches - all branches contained in the area
* buses - all buses contained in the area
* gens - all generators contained in the area
* loads - all loads contained in the area
* number - the area's number
* region - the region that contains the area
* shunts - all shunts contained in the area
* subs - all substations contained in the area
* wb - the GWB object

.. _sub:

Substation Objects
----------------------------

Substation objects represent substations in the power grid. They can be accessed by their number, through their containing area, or through the workbench object.

Here are some of the fields that substation objects have:

* area - the area that contains the substation
* branches - all branches contained in the substation
* buses - all buses contained in the substation
* gens - all generators contained in the substation
* latitude - the substation's latitude (substations do not necessarily have a latitude and a longitude)
* longitude - the substation's longitude
* name - the substation's name
* number - the substation's number
* region - the region that contains the substation
* shunts - all shunts contained in the substation
* wb - the GWB object

.. _bus:

Bus Objects
------------------

Buses represent electrical points in a power system, and can hold other grid objects.

Here are some of the fields that bus objects have:

* area - the area that contains the bus
* branches - all branches contained in the bus
* gens - all generator objects contained in the bus
* loads - all load objects contained in the bus
* nominal_kv - the nominal voltage of the bus in kilovolts
* name - the bus' name
* number - the bus' number
* region - the region that contains the bus
* shunts - all shunts contained in the bus
* sub - the substation that contains the bus
* vang - the bus' voltage angle in degrees
* vpu - the bus' per-unit voltage
* wb - the GWB object
* zone_number - zone number of the bus

.. _gen:

Generator Objects
---------------------------

Generator objects represent generators in a power system.

Here are some of the fields that generators have:

* bus - the bus containing the generator
* fuel_type - the type of generation (wind, solar, etc)
* id - the generator's ID
* p - real power of the generator
* pmax - maximum real power of the generator
* pmin - minimum real power of the generator
* q - reactive power of the generator
* qmax - maximum reactive power of the generator
* qmin - minimum reactive power of the generator
* sbase - the apparent power base of the generator
* status - status of the generator (open or closed)

.. _load:

Load Objects
--------------------

Load objects represent loads in a power system.

Here are some of the fields that loads have:

* bus - the bus containing the load
* id - the load's ID
* p - the load's real power
* ps - constant power portion of MW load
* q - the load's reactive power
* qs - constant power portion of MVAR load
* status - the status of the load (open or closed)
* benefit - the load's benefit (to be used for optimization)


.. _shunt:

Shunt Objects
--------------------

Shunt objects represent shunts in a power system.

Here are some of the fields that shunts have:

* bus - the bus that contains the shunt
* id - the shunt's ID
* q - reactive power of the shunt
* qnom - nominal reactive power of the shunt
* status - the status of the shunt (open or closed)

.. _branch:

Branch Objects
----------------------

Branch objects represent two-node objects such as transmission lines and transformers.

Here are some of the fields that branches have:

* MVA_Limit_A - limit set A
* MVA_Limit_B - limit set B
* MVA_Limit_C - limit set C
* B - per-unit susceptance
* G - per-unit conductance
* R - per-unit resistance
* X - per-unit reactance
* branch_device_type - the branch device type (transformer or transmission line)
* connected - whether or not the branch is part of the case (has a value of False when the branch is not included in the PowerWorld case)
* from_bus - the bus on the "from" side of the branch
* to_bus - the bus on the "to" side of the branch
* id - the branch's circuit number
* length - straight-line distance between "from" and "to" buses in miles
