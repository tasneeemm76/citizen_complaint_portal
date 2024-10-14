Citizen_Complain_Portal
Citizen_Complain_Portal is a web application designed to help citizens report and track issues related to public services and infrastructure. Users can log complaints about issues like road damage, garbage disposal, water supply problems, and more. The application promotes better city management by providing a platform for citizens to raise concerns that require government attention.

Key Features
Users can submit complaints by specifying the type of issue, subtype, a detailed description, and the location.
Complaints are categorized based on district and pincode for easier tracking.
The application uses latitude and longitude to mark the exact location of reported issues.
A dashboard displays complaint data using bar graphs and heatmaps for easy visualization and analysis.
Admins can monitor complaints and address areas with the most reported problems.
Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Python (Django) and PHP
Database: MySQL
Data Visualization: Python libraries like Pandas and Matplotlib
Location Mapping: Google Maps API for geolocation features
Prerequisites
Python 3.x
Django 3.x
MySQL
Google Maps API Key
Required Python libraries (Pandas, Matplotlib)
Database Structure
The application uses a MySQL database with the following table:

reported_issues
issue_id: Auto-incrementing ID for each issue.
issue_type: The type of issue, such as Infrastructure, Sanitation, Water Supply, or Power.
issue_subtype: Further classification of the issue, like Road, Garbage, Leakage, or Street Light.
issue_description: A text field to describe the issue in detail.
district: The district where the issue is reported, such as Shivajinagar or Kothrud.
pincode: The pincode of the area where the issue is located.
latitude: The latitude of the issue's location.
longitude: The longitude of the issue's location.
submission_date: The date and time when the issue was submitted.
How to Run the Project
Clone this repository to your local machine.
Install the required dependencies using the command: pip install -r requirements.txt.
Set up the MySQL database using the provided SQL script.
Obtain and configure your Google Maps API key.
Run the Django development server with python manage.py runserver.
