# DartSaurs API Backend

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Introduction

This project defines the backend of our solution. With it we are able to perform communications with other API's like [Where the ISS API](https://wheretheiss.at/w/developer) and others (coming soon).

## Technologies

COMMING SOON

## Installation

The API was developed using Django and Django REST framework. The project was developed using Python version 3.9.5, Django version 3.2.2 and DRF version 3.12.4. We use libraries such as Astropy and SGP4 to get the coordinates of the ISS. We use Redis to prevent the API from identifying the requests as mm denial of service attacks, so we store the relevant information in RAM and use it to get the ISS positions.

For the Django installation and dependencies:

```sh
pip install Django==3.2.2
pip install django-cors-headers==3.5.0
pip install django-environ==0.4.5
pip install django-filter==2.4.0
pip install django-guardian==2.3.0
pip install django-versatileimagefield==2.0
```
**NOTE**: You must have the pip installer configured on your machine.

For the Django REST framework installation:
```sh
pip install djangorestframework==3.12.4
```
For important libraries used in the API:
```sh
pip install requests==2.26.0
pip install astropy==5.1
pip install sgp4==2.21
```

For the Redis library installation:
```sh
pip install redis==4.1.1
```

**NOTE**: You must have Redis installed!!!

### How to install Redis on Windows

Acess the link bellow to installation instructions in Windows:
https://redis.io/docs/getting-started/installation/install-redis-on-windows/

### How to install Redis on Linux

Acess the link bellow to installation instructions in Linux:
https://redis.io/docs/getting-started/installation/install-redis-on-linux/

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

First: Set Environment variables

In Windows:

To set persistent environment variables at the command line, we will use `setx.exe`. It became part of Windows as of Vista/Windows Server 2008. Prior to that, it was part of the Windows Resource Kit. If you need the Windows Resource Kit, see Resources at the bottom of the page.  
`setx.exe` does not set the environment variable in the current command prompt, but it will be available in subsequent command prompts.
```
setx WHERETHEISS_API "https://api.wheretheiss.at/v1"
```
```
setx TLE_API "http://tle.ivanstanojevic.me"
```
To check if the variables have been set:

In command prompt (cmd):
```
echo %WHERETHEISS_API%
```
In powershell:
```
echo $Env:WHERETHEISS_API
```
Output:
```
https://api.wheretheiss.at/v1
```

In Linux:

We have two options for setting the environment variables:

one a one:
```
export WHERETHEISS_API=https://api.wheretheiss.at/v1
export TLE_API=http://tle.ivanstanojevic.me
```
single set:

1. copy the content bellow in a local.env file in current directory;
``` 
WHERETHEISS_API=https://api.wheretheiss.at/v1
TLE_API=http://tle.ivanstanojevic.me
```
2. In the current directory, run this command:
```
export $(cat local.env)
```

Output:
Following either way, we will get the same output. Run this command bellow:
```
echo $WHERETHEISS_API
```
And the result will be:
```
https://api.wheretheiss.at/v1
```
**NOTE**: test the same for the variable `TLE_API`

## License

MIT License
Copyright (c) [2022] [DartSaurs Team]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
