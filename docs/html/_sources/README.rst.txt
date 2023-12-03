Making Changes to GWB Documentation
=====================================

Making changes to GWB is not simple. You cannot just edit the files in github: the changes will not be reflected in the webpage.

This documentation was created using Sphinx documentation and is written in reStructuredText. It could be very helpful to check out the `Sphinx Documentation Tutorial <https://www.sphinx-doc.org/en/master/tutorial/getting-started.html>`_ and `reStructuredText Documentation <https://docutils.sourceforge.io/rst.html#user-documentation/>`_ to help you understand how to make edits to the documentation.

GWB documentation is edited by doing the following:

#. Download the file you want to change locally (ex: download the examples.rst file if you want to change the "examples" page)
#. Setup Spinx
#. Setup for making changes
#. Make changes to the file
#. Rebuild the project / Implement Changes
#. Send changes to GitHub

Setting Up Sphinx
---------------------------

Make a new folder to store the documentation. Then, open the command line terminal (this could also be done in the terminal if you have PyCharm). Then, cd into the folder that you just created and run the following commands:

.. code-block:: console

    > python-m .venv .venv
    > activate
    > python -m pip install sphinx
    > sphinx-quickstart docs

You will presented a series of questions to create the basic directory and configuration layout for your project inside the docs folder. To proceed, answer each questions as follows:

* Separate source and build directories (y/n) [n]: Write “y” (without quotes) and press Enter.
* Project name: Write “GridWorkbench” (without quotes) and press Enter.
* Author name(s): Write “Joshua Xia” (without quotes) followed by a comma and a space, and your name. Then press Enter.
* Project release []: Write “0.1” (without quotes) and press Enter.
* Project language [en]: Leave it empty (the default, English) and press Enter.

Run the following line of code to create an html page:

.. code-block:: console

    > sphinx-build -M html docs/source/ docs/build/

Consult `Sphinx Documentation Tutorial <https://www.sphinx-doc.org/en/master/tutorial/getting-started.html>`_ for more information on setting up Sphinx.

Setting Up to Make Changes
----------------------------------------

The following steps must be done before making changes to files:

* Download the docs folder from GitHub to your computer.
* Delete everything in the source folder of the project except for the static folder, the templates folder, and conf.py.
* Transfer all rst files and pictures from the rst folder from the Github page to the local source folder. Do the same with the local rst folder.
* Delete all files in the local project's doctrees folder and replace the files with the files from the GitHub doctrees folder.
* Delete all files in the local html folder in the build folder and replace with the html folder from GitHub.


Making Changes to Files
------------------------------------

Before making any changes to the desired file, put the file to be edited in the "source" folder. Then, open up index.rst, and under *.. toctree::*, add the name of the file that you just added. For example, if you wanted to make changes to "examples.rst", then under the toctree section, add a new line with the text "examples". More information on how to do this can be found here: `Narrative Documentation in Sphinx <https://www.sphinx-doc.org/en/master/tutorial/narrative-documentation.html>`_

The toctree section should look similar to the following:

.. code-block:: console

   .. toctree::
      tutorial
      examples

Then, open up the file to be edited and make changes. Again, you may find `Sphinx Documentation Tutorial <https://www.sphinx-doc.org/en/master/tutorial/getting-started.html>`_ useful for formatting the webpage and for other help.


Rebuilding the Project / Implementing Changes
---------------------------------------------------------------------

Once you've edited the file, go to the terminal and cd to the "docs" folder. Run the following line of code to implement your changes:

.. code-block:: console

   > .\make html

Anytime you want to implement the changes you make, cd into the docs folder and rebuild the project (using the code from above).

Sending Changes To Github
-----------------------------------------

To send the changes to Github, do the following in the GridWorkbench folder in your GitHub desktop folder:

* Empty the doctrees folder in the GitHub desktop folder, and replace with the local doctrees folder under "build."
* Empty the html folder in the GitHub desktop folder, and replace with the local html folder under "build."
* Empty the rst folder in the GitHub desktop folder, and replace with the local "source" folder. Also copy the makefile from the local docs folder to the GitHub rst folder.
* Commit and publish changes using GitHub desktop.