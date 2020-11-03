# Tutorial on SLIPO: Scalable Data Integration for Points of Interest

Teaching material for POI data integration &amp; analytics with the SLIPO Workbench, the SLIPO API, and LOCI.

## Overview

Points of Interest (POIs) are nowadays indispensable to various location-based applications and services. 

Yet, integrating POI data from heterogeneous sources with diverse schemas and formats remains a painstaking, costly, and error-prone task. 

In this tutorial:

- We first exhibit current limitations, gaps, and challenges in the POI data integration lifecycle. As no specialized software exists to address these specific challenges, we have implemented the open-source [SLIPO](https://github.com/SLIPO-EU/) system, which harnesses Linked Data technologies ([RDF](https://www.w3.org/RDF/), [OWL](https://www.w3.org/OWL/), [GeoSPARQL](https://www.opengeospatial.org/standards/geosparql)) to handle the inherent geospatial, thematic, and semantic ambiguities of POIs.

- Then, we showcase the [SLIPO Workbench](https://github.com/SLIPO-EU/workbench), our open-source web application that orchestrates and executes POI data integration workflows ([transformation](https://github.com/SLIPO-EU/TripleGeo), [interlinking](https://github.com/SLIPO-EU/LIMES), [fusion](https://github.com/SLIPO-EU/FAGI), [enrichment](https://github.com/SLIPO-EU/deer)) in a user-friendly, interactive, semi-automated, scalable, and quality-assured fashion. 

- Finally, we use [Jupyter notebooks](notebooks) to manage all stages of the integration process via the [SLIPO API](https://app.dev.slipo.eu/docs/webapp-api/index.html), and then explore, mine, and visualize POI data assets using [LOCI](https://github.com/SLIPO-EU/loci), our spatial analytics software.

## Audience

This tutorial mainly targets data scientists, professionals, and GIS enthusiasts with particular interest in POI data management and integration.

Data scientists will learn how to exploit SLIPO to quickly deploy efficient, large-scale, and quality-assured POI data integration workflows. 

Industrial stakeholders could see the significant gains from SLIPO in productivity, cost, and added value without disrupting, but instead complementing their existing workflows.

The tutorial requires no particular knowledge of POI data concepts and practices; skills in data management, GIS, and statistics would enable users to get easily familiar with the executed tasks.


## Interacting with SLIPO at HELIX Lab

We can provide free access to [HELIX Lab](https://lab.hellenicdataservice.gr/) for 15 days to interested users, so they can avoid deploying notebooks in their own systems and ensuring that all required libraries for SLIPO are in place. 

Once connected to HELIX Lab, users can submit requests concerning POI data integration with the [SLIPO API](https://app.dev.slipo.eu/docs/webapp-api/index.html) and spatial analytics with [LOCI](https://github.com/SLIPO-EU/loci). We have prepared several Jupyter [notebooks](notebooks) to showcase the provided functionality with a wide range of examples.

Follow these [instructions](https://drive.google.com/file/d/1dIoz97eBScDDx9P0aMh7chIbmqJxJwBa/view?usp=sharing) if you wish to get your free registration to HELIX Lab. Once your account is confirmed, you can start interacting with SLIPO via Jupyter notebooks even with your own POI data.

## Local installation

Please consult these [instructions](https://github.com/SLIPO-EU/workbench/blob/master/INSTALL.md) if you wish to install and launch SLIPO in your own infrastructure.


## Publications

- S. Athanasiou, M. Alexakis, G. Giannopoulos, N. Karagiannakis, Y. Kouvaras, P. Mitropoulos, K. Patroumpas, and D. Skoutas. [SLIPO: large-scale data integration for Points of Interest](https://openproceedings.org/2019/conf/edbt/EDBT19_paper_280.pdf). In EDBT, pages 574–577, 2019.

- S. Athanasiou, G. Giannopoulos, D. Graux, N. Karagiannakis, J. Lehmann, A. N. Ngomo, K. Patroumpas, M. A. Sherif, and D. Skoutas. [Big POI data integration with Linked Data technologies](https://openproceedings.org/2019/conf/edbt/EDBT19_paper_377.pdf). In EDBT, pages 477–488, 2019.

- K. Patroumpas, D. Skoutas, G. M. Mandilaras, G. Giannopoulos, and S. Athanasiou. [Exposing Points of Interest as Linked Geospatial Data](https://dl.acm.org/doi/10.1145/3340964.3340976). In SSTD, pages 21–30, 2019.

## License

The contents of this tutorial are licensed under the [Apache License 2.0](https://github.com/smartdatalake/simsearch/blob/master/LICENSE).

## Acknowledgement

This software has been developed in the context of the [SLIPO](http://slipo.eu/) project. The project has received funding from the European Union’s [Horizon 2020 research and innovation programme](https://ec.europa.eu/programmes/horizon2020/en) under grant agreement No 731581.
