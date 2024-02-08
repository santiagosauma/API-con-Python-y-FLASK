# Flask REST API

¡Bienvenido a la API REST sencilla construida con Flask y Python!

Esta API te permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre recursos específicos a través de solicitudes HTTP.

## Funcionalidades

- **Crear**: Agrega nuevos recursos a la base de datos.
- **Leer**: Recupera información de recursos específicos o de todos los recursos disponibles.
- **Actualizar**: Modifica la información de recursos existentes.
- **Eliminar**: Elimina recursos específicos de la base de datos.

## Tecnologías utilizadas

- **Flask**: Un framework web ligero para Python que facilita la creación de aplicaciones web.
- **Python**: Un lenguaje de programación versátil y potente.
- **HTML**: Utilizado para las pruebas funcionales.
- **Postman**: Una herramienta colaborativa de desarrollo de API que permite realizar pruebas y documentar APIs fácilmente.
- **MySQL**: Un sistema de gestión de bases de datos relacional utilizado para almacenar datos.

## Guía de instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias utilizando el comando `pip install -r requirements.txt`.
3. Configura la base de datos MySQL con las credenciales adecuadas.
4. Ejecuta la aplicación utilizando el comando `python app.py`.
5. Abre tu navegador y accede a `http://localhost:5000` para interactuar con la API.

## Endpoints

- **GET /items**: Obtiene todos los recursos disponibles.
- **POST /items**: Crea un nuevo recurso.
- **PUT /items/{id}**: Actualiza un recurso existente.
- **DELETE /items/{id}**: Elimina un recurso específico.

## Pruebas funcionales

Puedes realizar pruebas funcionales utilizando Postman siguiendo estos pasos:

1. Descarga e instala [Postman](https://www.postman.com/downloads/).
2. Importa la colección de pruebas funcionales ubicada en `tests/Flask_REST_API.postman_collection.json`.
3. Ejecuta las pruebas y verifica que todas las solicitudes HTTP se completen correctamente.

## Contribución

¡Siéntete libre de contribuir a este proyecto! Puedes abrir problemas (issues) o enviar solicitudes de extracción (pull requests) para sugerir mejoras, corregir errores o agregar nuevas funcionalidades.

## Licencia

Este proyecto está bajo la Licencia [MIT](LICENSE).
