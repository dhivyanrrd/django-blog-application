# Django Blog Application

A full-stack blog application built using Django and MySQL. This project supports user authentication, blog post management, image uploads, and secure configuration using environment variables.

## Features
- User registration and login
- Role-based dashboard (Editors)
- Create, edit, delete, and publish blog posts
- Image upload for posts
- Categories and pagination
- Password reset via email
- Contact form
- Secure session handling

## Screens Implemented
- Home page with latest posts
- Post detail page
- User dashboard
- Create / edit post pages
- About page
- Contact page

## Tech Stack
- Backend: Django (Python)
- Database: MySQL
- Frontend: HTML, CSS, Bootstrap
- Authentication: Django Authentication System
- Version Control: Git & GitHub
- Configuration Management: Environment variables (.env)

## Database Design
The application uses a relational MySQL database with normalized tables for users, posts, categories, sessions, and authentication data.

## Security
- Sensitive credentials are stored using environment variables
- `.env` file is excluded from version control
- Django’s built-in authentication and session framework is used

## Setup Instructions
1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies using `requirements.txt`
4. Configure environment variables in a `.env` file
5. Run migrations
6. Start the development server

## Project Status
This project is completed and intended for learning, portfolio presentation, and interview demonstration.
