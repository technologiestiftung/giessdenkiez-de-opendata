![](https://img.shields.io/badge/Built%20with%20%E2%9D%A4%EF%B8%8F-at%20Technologiestiftung%20Berlin-blue)

# Gieß den Kiez Open Data

_This repos purpose is to run a GitHub action to automatically generate open datasets about the usage of the Gieß-den-Kiez website. The action executes a python script that makes a request to the database on the first day of every month.
The datasets generated on this way are located in the daten-folder and the metadata is published at [Open Data Portal Berlin](https://daten.berlin.de/datensaetze)._

### Description

Gieß den Kiez is a project by CityLAB Berlin that aims to protect Berlin's urban trees from drying out. More than 625,000 street and park trees in Berlin are visualised on a map. With the help of the web app, trees can be explored, adopted and watered at www.giessdenkiez.de, thus recording and improving the coordination of the city's watering efforts.

Here you can find data about the usage of the giessdenkiez.de website. These are on the one hand the KPI's (Key-Performance-Indicators) such as the number of users, the number of trees adopted and others, but also data on all waterings recorded via the website. During the growing season (01.03. to 30.09.), the data is regularly updated at the beginning of each month. Gieß den Kiez went online at the end of May 2020.

All tree points visualised in the app come from the official [tree dataset of the city of Berlin](https://daten.berlin.de/datensaetze/baumbestand-berlin-straßenbäume-wfs). This dataset is published annually in the Open Data Portal by the responsible office, the Green Space Information System (GRIS), based on the surveys of the twelve district green space offices, and uniquely identifies each tree via the unique ID's "Technischer Schlüssel". The data published here has this same ID as a key attribute, so that the trees of Gieß-den-Kiez can be clearly assigned to the trees in the tree dataset in order to obtain more information about the trees.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/julizet"><img src="https://avatars.githubusercontent.com/u/52455010?v=4?s=64" width="64px;" alt=""/><br /><sub><b>Julia Zet</b></sub></a><br /><a href="https://github.com/technologiestiftung/giessdenkiez-de-opendata/commits?author=julizet" title="Code">💻</a> <a href="https://github.com/technologiestiftung/giessdenkiez-de-opendata/commits?author=julizet" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/Lisa-Stubert"><img src="https://avatars.githubusercontent.com/u/61182572?v=4?s=64" width="64px;" alt=""/><br /><sub><b>Lisa-Stubert</b></sub></a><br /><a href="https://github.com/technologiestiftung/giessdenkiez-de-opendata/commits?author=Lisa-Stubert" title="Code">💻</a> <a href="https://github.com/technologiestiftung/giessdenkiez-de-opendata/commits?author=Lisa-Stubert" title="Documentation">📖</a></td>
    <td align="center"><a href="https://fabianmoronzirfas.me/"><img src="https://avatars.githubusercontent.com/u/315106?v=4?s=64" width="64px;" alt=""/><br /><sub><b>Fabian Morón Zirfas</b></sub></a><br /><a href="#maintenance-ff6347" title="Maintenance">🚧</a></td>
    <td align="center"><a href="https://github.com/vogelino"><img src="https://avatars.githubusercontent.com/u/2759340?v=4?s=64" width="64px;" alt=""/><br /><sub><b>Lucas Vogel</b></sub></a><br /><a href="https://github.com/technologiestiftung/giessdenkiez-de-opendata/commits?author=vogelino" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Credits

<table>
  <tr>
    <td>
      <a src="https://citylab-berlin.org/en/start/">
        <br />
        <br />
        <img width="200" src="https://logos.citylab-berlin.org/logo-citylab-berlin.svg" />
      </a>
    </td>
    <td>
      A project by: <a src="https://www.technologiestiftung-berlin.de/en/">
        <br />
        <br />
        <img width="150" src="https://logos.citylab-berlin.org/logo-technologiestiftung-berlin-en.svg" />
      </a>
    </td>
    <td>
      Supported by:
      <br />
      <br />
      <img width="120" src="https://logos.citylab-berlin.org/logo-berlin.svg" />
    </td>
  </tr>
</table>

<!-- bump -->