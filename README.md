# IP Insight

A web-based IPv4 subnet calculator built with Python and Flask.

**[Try IP Insight](https://ipinsight.onrender.com)**

## About

IP Insight is a learning project built to practise Python programming and networking fundamentals. It helps users calculate information about IPv4 addresses and their associated subnets through a web interface.

The project uses Python's built-in `ipaddress` module for IP address and subnet calculations.

## Features

- IPv4 address validation
- Network address calculation
- Broadcast address calculation
- Wildcard Mask Calculation
- Usable host range calculation
- Usable host count calculation

## Technologies Used

- **Python** - application logic
- **Flask** - web framework
- **`ipaddress`** - IP address and subnet calculations
- **HTML and CSS** - user interface

## How to Use

1. Open the [IP Insight live demo](https://ipinsight.onrender.com).
2. Enter the IPv4 address you want to calculate information for.
3. Enter the corresponding subnet mask.
4. Submit the form to view the calculated network information.

Invalid IP addresses or subnet masks should be corrected before submitting again.

## Project Structure

```text
ip-subnet-calculator/
├── app.py
├── calculator.py
├── requirements.txt
├── templates/
├── static/
└── README.md
```

- `app.py` - Flask routes and request handling
- `calculator.py` - IP address and subnet calculation logic
- `requirements.txt` - Python dependencies
- `templates/` - HTML templates
- `static/` - static assets, including CSS

## What I Learned

Building IP Insight gave me an opportunity to practise Python programming, IPv4 subnetting, input validation, and building a web application with Flask.

## Limitations

- The application focuses on IPv4 calculations.
- The project is intended as a learning project and may not cover every feature available in more advanced subnet calculators.
