Citizen_Complain_Portal is a web-based application that allows citizens to report and track complaints about public infrastructure and services in their local area. The platform empowers citizens to raise issues such as road damage, garbage disposal, water supply problems, and more, contributing to better city management and sustainability.
Features
Users can submit complaints specifying the type of issue, subtype, description, and location.
Complaints are categorized by district and pincode.
Integration of latitude and longitude for precise location mapping of the reported issues.
A dashboard displays complaint trends with data visualization tools like bar graphs and heatmaps.
Admins can track and analyze complaints based on districts and types to identify priority areas for resolution.
Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: PHP, Python (Django), SQL
Database: MySQL
Visualization: Data science techniques for creating graphs and heatmaps
Mapping: Google Maps API (for geolocation features)
Prerequisites
Python 3.x
Django 3.x
MySQL
Google Maps API Key
Data Science Libraries (Pandas, Matplotlib)
Database Tables
1. reported_issues
Column Name	Data Type	Description
issue_id	INT (Primary Key, Auto Increment)	Unique identifier for each issue.
issue_type	VARCHAR(100)	Type of issue (e.g., Infrastructure, Sanitation)
issue_subtype	VARCHAR(100)	Subtype of issue (e.g., Road, Garbage)
issue_description	TEXT	Description of the issue reported.
district	VARCHAR(100)	District where the issue is reported.
pincode	VARCHAR(10)	Pincode for location identification.
latitude	DECIMAL(10,8)	Latitude of the issue location.
longitude	DECIMAL(11,8)	Longitude of the issue location.
submission_date	TIMESTAMP	Date and time when the issue was reported.
How to Run the Project
Clone the repository.
Install the required dependencies using pip install -r requirements.txt.
Set up the database using the provided SQL scripts.
Run the Django development server using python manage.py runserver.
