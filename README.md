# Cursor AI Map Project

This is a Python Flask application that allows users to look up an address and view a static map image of that location, along with travel times to nearby points of interest.

## Features

- Address lookup
- Display of static map image for the entered address
- Identification of nearby points of interest (Supermarket, Cafe, Park, Fitness)
- Display of walking, transit, and driving times to each point of interest

## Prerequisites

- Python 3.10+
- Google Cloud Platform account with Maps API enabled

## Setup

Install the required packages:

```
pip install -r requirements.txt
```

Set up your Google Cloud API key:

- Go to the Google Cloud Console and create a new project (or select an existing one)
- Enable the Maps JavaScript API and the Directions API for your project
- Create an API key with access to these APIs
- Set the API key as an environment variable:

  ```
  export GOOGLE_CLOUD_API_KEY=your_api_key_here
  ```

## Running the Application

1. Start the Flask server:

   ```
   python server.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Enter an address in the search box and click "Search" to view the map and nearby points of interest

## Project Structure

- `server.py`: Main Flask application
- `src/`:
  - `main.py`: Command-line interface for the application
  - `map_utils.py`: Utility functions for map-related operations
  - `place_description.py`: Data class for describing places of interest
  - `point_of_interest.py`: Data class for storing information about points of interest
- `templates/`:
  - `index.html`: Home page with address input form
  - `map.html`: Results page displaying map and points of interest

## Architecture

The application follows a simple client-server architecture:

1. The user interacts with the frontend (HTML templates)
2. The Flask server handles requests and communicates with the Google Maps API
3. The server processes the data and renders the results using the HTML templates
