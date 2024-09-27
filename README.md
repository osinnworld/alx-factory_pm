# Factory Project Management System

## Overview

The Factory Project Management System is a comprehensive web application designed to streamline production line management, report creation, and issue tracking in factory settings. Built with Django, this system offers an intuitive interface for managing factory operations efficiently.

## Features

- **Production Line Management**: Create, update, and monitor production lines.
- **Report Creation and Tracking**: Generate and manage detailed production reports.
- **Problem Reporting**: Report and categorize issues for quick resolution.
- **Performance Dashboard**: View key performance indicators and overall factory efficiency.
- **User Authentication**: Secure login system with role-based access control.

## Technology Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Database**: SQLite (default), easily configurable for PostgreSQL or MySQL
- **Authentication**: Django's built-in authentication system

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/factory-project-management.git
   cd factory-project-management
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the application at `http://localhost:8080`

## Usage

1. Log in with your superuser credentials.
2. Set up production lines, products, and user profiles through the admin interface.
3. Create production reports and track performance through the main application interface.
4. Use the dashboard to get an overview of factory performance.

## Project Structure

- `accounts/`: User authentication and profile management
- `areas/`: Production line management
- `products/`: Product catalog management
- `reports/`: Production reporting and problem tracking
- `templates/`: HTML templates for the application
- `static/`: CSS, JavaScript, and other static files

## Contributing

We welcome contributions to the Factory Project Management System. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

shemogata@gmail.com

Project Link: COMING SOON!!
