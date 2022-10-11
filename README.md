<h1 align="center">
  <br>
  <a href="http://68.183.26.243/dartsaurs/"><img src="https://drive.google.com/uc?export=view&id=1u6rsZHnae_r0B6LIpGbJczVpDDM5kbOs" alt="Markdownify" width="200"></a>
  <br>
  DartSaurs API Backend
  <br>
</h1>

<h4 align="center">A project of <a href="https://2022.spaceappschallenge.org/challenges/2022-challenges/track-the-iss/details" target="_blank">NASA International Space Apps Challenge 2022</a></h4>

<p align="center">
  <!--<a href="https://badge.fury.io/js/electron-markdownify">
    <img src="https://badge.fury.io/js/electron-markdownify.svg"
         alt="Gitter">
  </a>
   <a href="https://gitter.im/amitmerchant1990/electron-markdownify"><img src="https://badges.gitter.im/amitmerchant1990/electron-markdownify.svg"></a>
  <a href="https://saythanks.io/to/bullredeyes@gmail.com">
      <img src="https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg">
  </a>
  <a href="https://www.paypal.me/AmitMerchant">
    <img src="https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&amp;style=flat">
  </a>-->
</p>

<p align="center">
  <a href="#team">Team</a> •
  <a href="#technologies">Technologies</a> •
  <a href="#installation">Installation</a> •
  <a href="#features">Features</a> •
  <a href="#endpoints">Endpoints</a> •
  <a href="#run-application">Run Application</a> •
  <a href="#license">License</a>
</p>

## Introduction

This project was created from one of the 23 challenges offered in the NASA International Space Apps Challenge 2022. Our challenge was to develop a responsive web platform for us to track the International Space Station (ISS) in a 3D modeling. Using some resources offered by NASA, our team elaborated this project with a lot of dedication and focus. I hope you enjoy it and see when the ISS will pass over your heads.

by: DartSaurs Team

## Team

| Photo | Data |
| ------ | ------ |
 <img src="https://drive.google.com/uc?export=view&id=17HGgIWZvfUmxcKWObBA0B3UK7S7ouW_u" width="100"> | **Bruno Mitsuo Homma** <br> Software Engeneer /  Backend Developer <br> social media: <a href="https://www.linkedin.com/in/bruno-mitsuo-homma-432100169/"><img src="https://raw.githubusercontent.com/yushi1007/yushi1007/1f3f3e189376e20a38857f06c588eaae182998ab/images/linkedin.svg" alt="icon" width="21px"/></a> <a href="https://www.instagram.com/bruno.homma/"><img src="https://raw.githubusercontent.com/yushi1007/yushi1007/1f3f3e189376e20a38857f06c588eaae182998ab/images/instagram.svg" alt="icon" width="21px"/></a> |
| <img src="https://drive.google.com/uc?export=view&id=1j5qWlcc2wk1x91yDBg1DQ43Yh2LolT8a" width="100"> | **Bruno Rampim** <br> Biologist <br> Master's student in Agronomy (Genetics and Plant Breeding) at Universidade Estadual Paulista - UNESP  |
| <img src="https://drive.google.com/uc?export=view&id=1Z243MrnAXiM4Subf5v1UcqjUQ2XI9cVD" width="100"> | **Cesar Augusto Nascimento** <br> Biologist <br> PhD in Genetics and Molecular Biology at Universidade Estadual de Campinas - Unicamp  |
| <img src="https://drive.google.com/uc?export=view&id=1yUM5Ff6OuxkiA20o8d2Moriu-U1a5MdD" width="100"> | **Everton da Silva** <br> Measurement and Technology Analyst Senior <br> Study and application of algorithms for automatic recomposition of electricity distribution networks  <br> social media: <a href="https://www.linkedin.com/in/everton-silva-tom-62a9b429"><img src="https://raw.githubusercontent.com/yushi1007/yushi1007/1f3f3e189376e20a38857f06c588eaae182998ab/images/linkedin.svg" alt="icon" width="21px"/></a> |
| <img src="https://drive.google.com/uc?export=view&id=1TDOGSiy5rEoWvty3Np4axIy3w-OLMaS1" width="100"> | **Lucas Nascimento** <br> Agronomist Engineer <br> Master's student in Genetics and Molecular Biology at Universidade Estadual de Campinas - Unicamp  |
| <img src="https://drive.google.com/uc?export=view&id=1f-si8P7bMpeE8uT0N4SUxZ5Umw91MRlT" width="100"> | **Paulo Henrique da Costa** <br> Graduating in Mechanical Engineering from Faculdade de Engenharia de Piracicaba - EEP  <br> social media: <a href="https://www.linkedin.com/in/paulo-h-c/"><img src="https://raw.githubusercontent.com/yushi1007/yushi1007/1f3f3e189376e20a38857f06c588eaae182998ab/images/linkedin.svg" alt="icon" width="21px"/></a> |

## Technologies

[COMMING SOON]

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

#### or

### Direct Requirements Installation

You can make the installation requirements from a .txt file. First you need to create a file called `requirements.txt`, and copy the content bellow into this file:
```sh
# Django
Django==3.2.2
django-cors-headers==3.5.0
django-environ==0.4.5
django-filter==2.4.0
django-guardian==2.3.0
django-versatileimagefield==2.0

# Django REST Framework (DRF)
djangorestframework==3.12.4

# Redis
redis==4.1.1

# Request lib for API communications
requests==2.26.0

# For Coordenates Satellite Calculations
astropy==5.1
sgp4==2.21
```

After that, in the same directory as the requirements.txt file, run the command bellow:
```sh
pip install -r requirements.txt
```

Then you will install all the necessary requirements at once.

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

After that, you need to run:
```
python manage.py runserver
```

**NOTE**: Ignore all migrations warnings because we don't use database, so it's not need to run migrations

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
