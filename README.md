Little Lemon Backend Project

Este proyecto es una API backend para el restaurante Little Lemon usando Django y Django REST Framework.

La aplicación permite gestionar el menú del restaurante y las reservas de mesas. También incluye autenticación basada en tokens para proteger ciertas rutas.

Tecnologías utilizadas:
- Python
- Django
- Django REST Framework
- SQLite / MySQL (según configuración del proyecto)
- Insomnia para pruebas de API

Endpoints principales:

Menu API:
GET /restaurant/menu/
POST /restaurant/menu/
GET /restaurant/menu/<id>/
PUT /restaurant/menu/<id>/
DELETE /restaurant/menu/<id>/

Booking API:
GET /restaurant/booking/
POST /restaurant/booking/
GET /restaurant/booking/<id>/
PUT /restaurant/booking/<id>/
DELETE /restaurant/booking/<id>/

Autenticación:
POST /api-token-auth/

Uso de autenticación:
Para acceder a rutas protegidas, se debe enviar el token en el header:
Authorization: Token <your_token>

Notas:
- Las pruebas de la API se realizaron usando Insomnia.
- El acceso a Booking API está protegido con autenticación por token.
