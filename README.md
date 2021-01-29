# project1-mb865
Webpage served on `/` that randomly displays song information from a list of random my favorite artists. This information is dynamically fetched via Spotify API.

## Installation Guide

## Technologies Used
### Flask
Flask is a python framework that is used here to serve the main webpage for the application. After importing the library in `app.py`, the instance is created as `app`. The route decorator is then used to determine what happens when the `/` endpoint is called upon the server.

### Spotipy
Spotipy is a python library that allows you to create a spotipy instance. This instance lets you interact with the Spotify API easily when provided with the right credentials. In my project I use it to obtain the top 10 tracks from each artist on my list of artists. This list of tracks is then parsed for the required information for my webpage.
### Miscellaneous
* `https://getbootstrap.com/docs/4.0/getting-started/introduction/` is used for easy styling.
* `https://fonts.google.com/` is used to select a font family.
* `https://uigradients.com/` is used to obtain the css code for the gradient background.

## Discoveries
### a. What are at least 3 technical issues you encountered with your project? How did you fix them?
### b. What are known problems, if any, with your project?
### c. What would you do to improve your project in the future?
