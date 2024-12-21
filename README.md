# AlivianaWindows

**Versión: 1.2**

Desarrollado por **Iván Ayub**

**AlivianaWindows** es una herramienta todo en uno diseñada para optimizar el rendimiento y la salud de los sistemas Windows. Combina comandos esenciales de mantenimiento con una interfaz basada en consola fácil de usar, para simplificar el cuidado y la gestión del sistema.

[Haz clic aquí para descargar la aplicación desde Google Drive (.zip)](https://drive.google.com/file/d/1rH1N3V4qNefDXG0qIn2aAW1EDLhYPMH7/view?usp=drive_link)

Para consultas o comentarios, contáctame en: [sellocasadenubes@gmail.com](sellocasadenubes@gmail.com).

---
![Ícono NextMask FFmpeg](assets/AlivianaWindows.jpg)

## Descripción

**AlivianaWindows** proporciona una lista categorizada de comandos esenciales para mantener tu sistema Windows en óptimas condiciones. Es ideal para usuarios que buscan mejorar la estabilidad del sistema, resolver problemas y mantener el rendimiento con el menor esfuerzo posible.

---

## Características

### **Mantenimiento del Sistema:**

- Escanea y repara archivos del sistema.
- Verifica y repara discos duros.
- Desfragmenta discos para mejorar el rendimiento.

### **Administración de Red:**

- Muestra configuraciones de red.
- Limpia la caché de DNS.
- Verifica la conectividad de red con ping.

### **Gestión de Procesos:**

- Muestra los procesos en ejecución.
- Termina procesos innecesarios.

### **Reparación de Arranque:**

- Repara el Master Boot Record (MBR).
- Reconstruye el BCD (Boot Configuration Data).

### **Herramientas Variadas:**

- Restablece la Microsoft Store.
- Habilita o deshabilita la hibernación.

### **Interfaz Interactiva:**

- Comandos categorizados para una fácil navegación.
- Indicaciones claras para ejecutar tareas.

---

## Instrucciones de Uso

1. **Ejecuta el programa** como administrador.
2. **Selecciona una categoría** desde el menú.
3. **Ingresa el número del comando** para ejecutarlo.
4. **Sigue las instrucciones en pantalla** y revisa los resultados.
5. Escribe `exit` para cerrar el programa.

### Ejemplo de Escenario

¿Quieres asegurarte de que tus archivos del sistema estén en óptimas condiciones?
Abre AlivianaWindows, selecciona "Mantenimiento del Sistema" y ejecuta el comando "sfc /scannow" para escanear y reparar archivos corruptos.

---

## Estructura de la Aplicación

### **Interfaz de Usuario (UI):**

La interfaz utiliza un enfoque basado en texto con colores y arte ASCII para mejorar la legibilidad, utilizando las librerías **`pyfiglet`** y **`termcolor`**.

### **Módulos Principales:**

1. **Ejecución de Comandos:** Ejecuta comandos de mantenimiento del sistema utilizando subprocess.
2. **Navegación del Menú:** Organiza los comandos en categorías intuitivas.
3. **Manejador de Errores:** Muestra mensajes informativos sobre ejecuciones exitosas o fallidas.

---

## Requisitos del Sistema

- **Sistema Operativo:** Windows 10 o posterior
- **Dependencias:**
  - Python 3.10+
  - `pyfiglet`
  - `termcolor`

---

## Capturas
![Captura de la Aplicación](assets/SS1AlivianaWindows1.2.png)
![Captura de la Aplicación](assets/SS2AlivianaWindows1.2.png)
---

## Desarrollo y Contribución

### **Créditos:**

Este software utiliza las siguientes bibliotecas:

- **`pyfiglet`**: Para arte de texto en ASCII.
- **`termcolor`**: Para colorear texto en terminal.

Agradecimientos especiales a Microsoft por proporcionar documentación oficial sobre los comandos del sistema.

### **Contribuciones:**

¡Te damos la bienvenida para que contribuyas! Para hacerlo:

1. Haz un fork del repositorio.
2. Realiza tus cambios.
3. Envía un pull request.

---

¡Disfruta usando **AlivianaWindows**! Tu retroalimentación es invaluable y nos ayuda a mejorar continuamente.

--- 

¡Espero que te sirva!
