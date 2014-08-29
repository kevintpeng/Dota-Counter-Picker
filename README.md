Dota Counter Picker
===================
Introduction
-------------------
This program is designed to aid Dota 2 players during the drafting process. Using massive sample sizes from stat website [Dotabuff][1], we can evaluate general effectiveness of specific heroes against a given enemy team. To run the counter picker, run main.py to launch the GUI. The interface is super simple to navigate. There are five combo boxes that let you specify any heroes the opposing team has picked. Press "Calculate" to find the best counter based on pub stats. The output is in the console.
  [1]: http://www.dotabuff.com/

Installing
-------------------
Dota Counter Picker requires at least [python 2.7][2] and [pyQt4][3], and all associated libraries. Follow the pyQt4 installation guide. Everything else should work without additional installations. For full functionality, make sure HeroList.txt is up to date. If you make a change to the HeroList, delete data.csv and update the data by clicking File>Update Data (should take about 2 minutes to update depending on internet speeds).
  [2]: https://www.python.org/download/releases/2.7/
  [3]: http://pyqt.sourceforge.net/Docs/PyQt4/installation.html

