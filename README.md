**Geo Base** Geo Base is a web application for managing and visualising geospatial data.
It uses a Django backend and a JavaScript frontend, with support for PostGIS-enabled PostgreSQL databases.

## Features

- **Interactive Maps**: Visualize geospatial data using dynamic maps.
- **User Management**: Handle user authentication and authorization.
- **Data Dashboard**: Access and manage geospatial datasets through a user-friendly dashboard.

## Project Structure

The repository is organized as follows:

- `backend/`: Contains Django backend code.
- `frontend/`: Contains JavaScript frontend code.
- `config/`: Configuration files for the project.
- `dashboard/`: Dashboard-related components and views.
- `members/`: User management components.
- `static/`: Static files such as CSS, JavaScript, and images.
- `templates/`: HTML templates for rendering views.
- `media/`: Directory for user-uploaded media files.
- `woodland/`: Additional app or module related to geospatial data.

## Requirements

- Python 3.x
- Django
- PostgreSQL with PostGIS extension
- Node.js and npm (for frontend development)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/bendamian/geo_base.git
   cd geo_base
