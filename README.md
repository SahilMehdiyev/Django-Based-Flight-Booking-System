# Django Based Flight Reservation System

This project covers the development of a Django-based backend API for a flight reservation system. This system offers users functions such as searching for flights, making reservations, making payments and viewing reservation details. It works integrated with an external flight API and manages flight information, prices and reservation status.

## Features

- **Flight Search:** Users can search for flights based on certain criteria.
- **Making a Reservation:** Users can book flights of their choice.
- **Payment Transactions:** Online payment transactions are made for reservations.
- **Reservation Details:** Users can view the details of the reservations they have made.
- **API Integration:** Updated flight information is provided by integrating with an external flight API.

## Setup

Follow the steps below to run this project in your local environment.

### Requirements

-Python 3.x
- Django
- Django REST Framework

### Steps

1. Clone this project to your local machine:
 ```bash
 git clone https://github.com/username/proje-name.git
 ```
2. Go to the project directory:
 ```bash
 cd project-name
 ```
3. Create a virtual environment:
 ```bash
 python -m venv venv
 ```
4. Activate the virtual environment:
 ```bash
 #Windows
 venv\Scripts\activate

 # MacOS/Linux
 source venv/bin/activate
 ```
5. Install the required dependencies:
 ```bash
 pip install -r requirements.txt
 ```
6. Run database migrations:
 ```bash
 python manage.py migrate
 ```
7. Start the development server:
 ```bash
 python manage.py runserver
 ```

## Use

- Flight search: `/api/flights/search`
- Making reservations: `/api/reservations`
- Payment transactions: `/api/payments`
- Reservation details: `/api/reservations/{reservation_id}`
