
# SQLAlchemy Challenge

## Project Overview
This project conducts a detailed analysis of climate data from Hawaii using SQLAlchemy ORM, Pandas, and Matplotlib in Python. The objective is to provide insights for trip planning by analyzing historical weather trends. A Flask API is also implemented to serve the data analysis results through a set of HTTP endpoints.

## Data Source
- **Database**: `hawaii.sqlite` - Contains historical climate data from various stations across Hawaii.

## Tools Used
- **Python Libraries**: SQLAlchemy, Pandas, Matplotlib, Numpy
- **Web Framework**: Flask

## Visualizations
The project generates several visualizations to effectively communicate climate trends:
- **Precipitation Levels**: Displays precipitation trends over time in Hawaii, aiding in understanding the best times to visit.

![3f475a76-610a-44d7-ad91-a5a1318b21da](https://github.com/user-attachments/assets/9734fc87-a6fa-4ca1-bcac-1ddc6b1bdac2)


- **Station Histogram**: Shows frequency of temperature observations at most active station. Important for identifying preferred travel periods.

![annual tobs most activestation](https://github.com/user-attachments/assets/33a37f26-4c4f-4abc-bfa0-57d119aca69d)


## Flask API Endpoints
The Flask application provides several endpoints to access climate data:

- **Home Page (`/`)**:
  - Lists all available routes.
 <img width="553" alt="Screenshot 2024-08-21 at 1 02 40 PM" src="https://github.com/user-attachments/assets/62667d24-5a27-4c69-a91a-bee48bc47907">

    

- **Precipitation Data (`/api/v1.0/precipitation`)**:
  - Converts precipitation data into a dictionary using the date as the key.
  - Returns a JSON representation of the dictionary.
  
<img width="277" alt="Screenshot 2024-08-21 at 1 04 21 PM" src="https://github.com/user-attachments/assets/066b2543-8798-4852-a06c-6f6593d387fc">

- **Station List (`/api/v1.0/stations`)**:
  - Returns a JSON list of stations from the dataset.
 
    
<img width="375" alt="Screenshot 2024-08-21 at 1 07 05 PM" src="https://github.com/user-attachments/assets/7df8f329-ade9-43f0-aa72-216e8f8d6b29">

- **Temperature Observations (`/api/v1.0/tobs`)**:
  - Retrieves temperature observations from the last year of the dataset.
  - Returns a JSON list of temperature observations for that year.
 <img width="506" alt="Screenshot 2024-08-21 at 1 06 16 PM" src="https://github.com/user-attachments/assets/b4001217-2d53-40c0-a996-837eb975a13f">

  

- **Temperature Range (`/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`)**:
  - Returns a JSON list of the minimum, average, and maximum temperatures for a given start or start-end date range.
  - If only the start date is provided, it returns data for all dates greater than and equal to the start date.
  - If both start and end dates are provided, it returns data for the range inclusive of both dates.
 
  

## Installation and Setup
To run this project, clone the repository and ensure you have Python installed along with the required libraries. You will also need Flask installed to run the API.

1. Install the required Python packages:
   ```bash
   pip install SQLAlchemy pandas matplotlib flask
   ```
2. To start the Flask server, navigate to the directory containing `app.py` and run:
   ```bash
   flask run
   ```

Navigate to `http://127.0.0.1:5000/` in your web browser to view the API endpoints and interact with the platform, accessing detailed climate information crucial for planning a trip to Hawaii.

