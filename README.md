# Watchlist

A REST API for a movie-watching platform inspired by IMDB.

## Introduction
The `watchlist` repository is a REST API platform for movie enthusiasts to come together and share their thoughts and opinions on a wide range of movies. The platform allows administrators to add movies to the site, while registered users can leave reviews for these movies and rank them on a scale from 1 to 5. The overall movie rating is calculated and displayed on each movie's detail page. Token authentication is used for user authentication, ensuring user security.

## Features
- Movie adding by administrators
- Movie ranking and reviewing by users
- User token authentication
- Overall rating calculation
- Throttling for API requests

## Technologies Used
This project was built using a combination of technologies, including:
- Python
- Django
- Django Rest Framework

These technologies were chosen for their versatility, reliability, and ease of use, and were used to create a modern and user-friendly movie-watching platform.

## Getting Started
To get started with the `watchlist` project, you will need to clone the repository to your local machine. You will also need to set up a virtual environment, install the required dependencies, and configure the database. Once these steps have been completed, you will be ready to run the development server and access the site.

## Throttling
The `watchlist` API has been configured with throttling to limit the number of requests made by users. Anonymous users are allowed to use the API only three times per day, while logged in users can make GET requests without any restrictions. However, there are still some restrictions in place for methods like POST and PUT.

## Contributions
If you're interested in contributing to the `watchlist` project, feel free to submit a pull request. The repository's maintainers will be happy to review and merge your changes.

## Conclusion
The `watchlist` project is an excellent resource for anyone looking to create a movie-watching platform similar to IMDB. Whether you're a programmer looking to learn more about building similar projects or a movie enthusiast looking to share your thoughts and opinions on your favorite movies, the `watchlist` project is a great starting point. Get started with the project today and create your own movie-watching community!
