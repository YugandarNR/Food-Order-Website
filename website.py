{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="Stylesheet" href="{% static 'styles/styles.css' %}">
    <title>Hotel Reservation System - User Home</title>
</head>

<body>
    <header>
        Hotel Reservation System
        {% if user.is_authenticated %}
        <button class="register-button">{{user.first_name}}</button>
        <button class="login-button" onclick="window.location.href='logout'">Logout</button>
        {% else %}
        <button class="register-button" onclick="window.location.href='register'">Register</button>
        <button class="login-button" onclick="window.location.href='login'">Login</button>
        {% endif %}
    </header>
    <div class="user-container">
        <h2>Select a Hotel</h2>
        <div class="room-options">
            {% for hotel in hotels %}
            <div class="room-card">
                <img src="{{hotel.hotelImage.url}}" alt="">
                <div class="room-details">
                    <h3 class="room-title">{{hotel.hotelTitle}}</h3>
                    <div class="room-description">
                        <p>{{hotel.hotelDescription}}
                        </p>
                    </div>
                </div>
                <form action="home" method="post">
                    {% csrf_token %}
                    <input type="hidden" name="hotelId" value={{hotel.hotelId}}>
                    <input type="hidden" name="itemTitle" value={{hotel.hotelTitle}}>
                    <input type="hidden" name="itemPrice" value={{hotel.hotelTitle}}>
                    <input type="submit" name="room" class="room-price-button" value="Book Rooms From $ {{hotel.hotelPrice}}">
                </form>
            </div>
            {% endfor %}
        </div>
        <hr>   
    </div>
    <footer>
        <div>
            How can we Help?
            <button>Request for Call</button>
        </div>
        <p>Terms and Conditions | &copy; 2023 Hotel Reservation System</p>
    </footer>
</body>

</html>