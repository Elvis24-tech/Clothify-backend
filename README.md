# M-Pesa Backend (Django REST API)

This is the backend for a clothing shop application, built with Django and Django REST Framework. It provides RESTful APIs for managing products, orders, and M-Pesa STK Push payments.

## Table of Contents

* [Features](#features)
* [Tech Stack](#tech-stack)
* [Setup Instructions](#setup-instructions)
* [Environment Variables](#environment-variables)
* [API Endpoints](#api-endpoints)
* [Testing](#testing)
* [License](#license)

---

## Features

* User authentication and authorization
* Product listing and management
* Shopping cart and checkout functionality
* M-Pesa STK Push integration for payments
* Admin routes for order and product management

---

## Tech Stack

* Python 3.11+
* Django 5.2+
* Django REST Framework
* SQLite (default, can be replaced with PostgreSQL)
* M-Pesa Daraja API (sandbox)

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone <repository_url>
cd mpesa_backend
```

2. **Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate  
venv\Scripts\activate     
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the root directory and add the following:

```env
DJANGO_SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

MPESA_CONSUMER_KEY=your_mpesa_consumer_key
MPESA_CONSUMER_SECRET=your_mpesa_consumer_secret
MPESA_SHORTCODE=your_mpesa_shortcode
MPESA_PASSKEY=your_mpesa_passkey
MPESA_BASE_URL=https://sandbox.safaricom.co.ke
```

5. **Run migrations**

```bash
python manage.py migrate
```

6. **Run the development server**

```bash
python manage.py runserver
```

Your API should now be running at `http://127.0.0.1:8000/`.

---

## API Endpoints

### Products

* `GET /products/` - List all products
* `GET /products/:id/` - Retrieve a single product
* `POST /products/` - Create a new product (admin only)
* `PUT /products/:id/` - Update a product (admin only)
* `DELETE /products/:id/` - Delete a product (admin only)

### Orders

* `GET /orders/` - List orders (admin only)
* `POST /orders/` - Create an order
* `GET /orders/:id/` - Retrieve a specific order

### M-Pesa STK Push

* `POST /mpesa/stkpush/` - Initiate payment request
* `POST /mpesa/callback/` - M-Pesa payment callback

---

## Testing

Use Postman or a similar tool to test endpoints. Example payload for STK Push:

```json
{
  "name": "John Doe",
  "phone_number": "254712345678",
  "amount": 1500
}
```

---

## License

This project is licensed under the MIT License.
