GWB Documentation
===================

The GWB Object
--------------------------

In this tutorial, we assume that a GWB object named *wb* has already been created.

To open up a PowerWorld case, use the ``wb.open_pwb()`` function:

.. py:function:: wb.open_pwb(fileName = None)

   Open up a PowerWorld case.

   :param fileName: directory to the PowerWorld case.
   :type kind: str
   :return: None
   :rtype: None

To read in a PowerWorld case, use the ``wb.pwb_read_all()`` function. Make sure the PowerWorld case has been opened before using this function.

.. py:function:: wb.pwb_read_all(hush = False)

   Read in a PowerWorld case.

   :param hush: a control to turn on or off default printout after reading in the case. set to True to turn off printout-it's set to False by default. Recommended to set to True if calling this function many times to avoid cluttered printout.
   :type kind: bool
   :return: None
   :rtype: None

