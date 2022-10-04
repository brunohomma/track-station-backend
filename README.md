# DartSaurs API Backend

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Introduction

This project defines the backend of our solution. With it we are able to perform communications with other API's like [Where the ISS API](https://wheretheiss.at/w/developer) and others (coming soon).

**NOTE**: This Documentation is currently being updated

## Technologies

[COMMING SOON]

## Installation

The API was developed using Django and Django REST framework. The project was developed using Python version 3.9.5, Django version 3.2.2 and DRF version 3.12.4.

For the Django installation:

```sh
pip install Django==3.2.2
```
**NOTE**: You must have the pip installer configured on your machine.

For the Django REST framework installation:
```sh
pip install djangorestframework==3.12.4
```

## Features

- Performs requests for data collection from the ISS space station
- COMING SOON...

## Endpoints

| Plugin | README |
| ------ | ------ |
| Track By Where The ISS At API | `/tracks/track_by_where_the_iss_at` |
| Track By TLE API | `/tracks/track_by_tle_api` |

- `[GET] /tracks/track_by_where_the_iss_at`: captures the coordinates (latitude, longitude and altitude), as well as its moving speed (km/h) using the information collected from the [Where the ISS API](https://wheretheiss.at/w/developer) and send data in JSON format.
- `[GET] /tracks/track_by_tle_api`: returns the position of the space station in coordinates (latitude, longitude and altitude) by processing the TLE data sent by [CelesTrack](https://celestrak.org/) and from this TLE we calculate the coordinates in JSON format **(in development)**.

## Run Application

To run the application server follow the instructions below:

First: You need to set Environment variables

``` 
(copy this content in local.env file)

WHERETHEISS_API=https://api.wheretheiss.at/v1
TLE_API=http://tle.ivanstanojevic.me
```
