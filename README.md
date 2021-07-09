# Gieß-den-Kiez Open Data
*This repos purpose is to run a GitHub action to automatically generate open datasets about the usage of the Gieß-den-Kiez website. The action executes a python script that makes a request to the database on the first day of every month.
The datasets generated on this way are located in the daten-folder and the metadata is published at [Open Data Portal Berlin](https://daten.berlin.de/datensaetze).*

### Description

Gieß den Kiez is a project by CityLAB Berlin that aims to protect Berlin's urban trees from drying out. More than 625,000 street and park trees in Berlin are visualised on a map. With the help of the web app, trees can be explored, adopted and watered at www.giessdenkiez.de, thus recording and improving the coordination of the city's watering efforts.

Here you can find data about the usage of the giessdenkiez.de website. These are on the one hand the KPI's (Key-Performance-Indicators) such as the number of users, the number of trees adopted and others, but also data on all waterings recorded via the website. During the growing season (01.03. to 30.09.), the data is regularly updated at the beginning of each month. Gieß den Kiez went online at the end of May 2020.

All tree points visualised in the app come from the official [tree dataset of the city of Berlin](https://daten.berlin.de/datensaetze/baumbestand-berlin-straßenbäume-wfs). This dataset is published annually in the Open Data Portal by the responsible office, the Green Space Information System (GRIS), based on the surveys of the twelve district green space offices, and uniquely identifies each tree via the unique ID's "Technischer Schlüssel". The data published here has this same ID as a key attribute, so that the trees of Gieß-den-Kiez can be clearly assigned to the trees in the tree dataset in order to obtain more information about the trees.

