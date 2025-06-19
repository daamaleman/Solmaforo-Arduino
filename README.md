# 🌞 Solmáforo con Arduino para Monitoreo de Radiación UV 🌞

![Solmáforo Logo](/images/solmaforo.jpg) <!-- Placeholder para logo -->

---

## 📋 Descripción del Proyecto

**Solmáforo** es un proyecto innovador que monitorea en tiempo real los niveles de radiación ultravioleta (UV) ☀️ utilizando un sensor **VEML6075** conectado a una placa **Arduino**. Incluye una interfaz web moderna 🌐 con gráficos dinámicos 📊 y alertas visuales 🚨 basadas en la escala de la **Organización Mundial de la Salud (OMS)**. Este prototipo busca proteger a los usuarios de los riesgos de la exposición solar, especialmente en regiones de alta incidencia solar como Nicaragua 🇳🇮.

**Autores**: Diedereich Alemán, Gabriel Lacayo  
**Versión**: 1.0.0  
**Licencia**: [MIT](LICENSE) 📜

---

## 🎯 Objetivos

### **Objetivo General**
Diseñar e implementar un prototipo funcional de **Solmáforo** que detecte en tiempo real los niveles de radiación UV utilizando Arduino y el sensor VEML6075 🔍.

### **Objetivos Específicos**
- 🔬 Investigar el impacto de la radiación UV en la salud humana.
- 🛠️ Integrar el sensor VEML6075 con Arduino para medir radiación UV.
- 💻 Programar la lógica para activar indicadores visuales según los niveles UV.
- 🔧 Ensamblar un prototipo con una interfaz visual clara y accesible.
- 🌍 Evaluar el dispositivo en condiciones reales dentro del campus universitario.

---

## ✨ Funcionalidades Principales

- **Monitoreo en Tiempo Real** ⏱️: Muestra el índice UV actual, nivel de peligro y una barra de progreso coloreada según el riesgo (verde, amarillo, naranja, rojo, violeta).
- **Gráficos Dinámicos** 📈: Visualización de datos de índice UV y voltaje en gráficos de líneas actualizados en tiempo real.
- **Interfaz Web Intuitiva** 🖥️:
  - `index.html`: Panel de monitoreo con índice UV, nivel de peligro y barra de progreso.
  - `graphs.html`: Gráficos en tiempo real para índice UV y voltaje.
- **Comunicación en Tiempo Real** ⚡️: Utiliza **WebSockets** (Socket.IO) para transmitir datos desde el Arduino al navegador.
- **Indicadores Visuales** 💡: Cambia el color de fondo y activa LEDs según la escala OMS:
  - **0–2 (Bajo)**: 🟢 Verde
  - **3–5 (Moderado)**: 🟡 Amarillo
  - **6–7 (Alto)**: 🟠 Naranja
  - **8–10 (Muy Alto)**: 🔴 Rojo
  - **11+ (Extremadamente Alto)**: 🟣 Violeta

---

## 🛠️ Tecnologías Utilizadas

### **Hardware** 🔩
- **Arduino** con sensor **VEML6075** 📡.
- **Bujias LEDs** para indicadores visuales de niveles de riesgo 💡.

### **Software** 💾
- **Frontend**:
  - **HTML5**, **Tailwind CSS** (estilos modernos) 🎨, **Chart.js** (gráficos dinámicos) 📊.
  - **Socket.IO** (comunicación en tiempo real) ⚡️.
  - Fuentes: **Montserrat** (Google Fonts) ✍️.
- **Backend**:
  - **Flask** (servidor web ligero) 🐍.
  - **Flask-SocketIO** (gestión de WebSockets) 🌐.
  - **Python** con `pyserial` para comunicación serial 🔌.
- **Comunicación**:
  - Puerto serial para datos del Arduino 🔗.
  - WebSockets para transmisión al cliente 📡.

---

## 🚀 Instalación y Configuración

### **Requisitos Previos**
- 🐍 **Python 3.8** o superior.
- 🛠️ **Arduino** con sensor VEML6075 conectado a un puerto serial (ej. `COM3` o `/dev/ttyUSB0`).
- 🌐 Navegador web moderno (Chrome, Firefox, Edge).
- 📦 Dependencias de Python especificadas en `requirements.txt`:

### **Pasos de Instalación**
1. **Clonar el repositorio** 📥:
   ```bash
   git clone https://github.com/daamaleman/Solmaforo-Arduino.git
   ```
2. **Instalar dependencias de Python** 📦:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configurar el puerto serial** ⚙️:
   - Editar la variable `SERIAL_PORT` en `app.py` según el puerto de tu Arduino (ej. `COM3` o `/dev/ttyUSB0`).
4. **Programar el Arduino** 🖥️:
   - Cargar el código en el Arduino para enviar datos en el formato: `UV Index: X.XX, Voltaje: Y.YY, Nivel: ZZZ`.
   - Ejemplo: `UV Index: 5.23, Voltaje: 3.45, Nivel: MEDIO`.
5. **Ejecutar el servidor** 🚀:
   ```bash
   python app.py
   ```
6. **Acceder a la interfaz web** 🌐:
   - Monitoreo: `http://localhost:5000`
   - Gráficos: `http://localhost:5000/graphs`

---

## 📂 Estructura del Proyecto

```plaintext
solmaforo/
├── app.py                # 🐍 Servidor Flask con lógica de comunicación serial y WebSockets
├── templates/
│   ├── index.html        # 🖥️ Panel de monitoreo con índice UV y barra de progreso
│   └── graphs.html       # 📊 Gráficos en tiempo real de índice UV y voltaje
├── README.md             # 📜 Documentación del proyecto
└── requirements.txt      # 📋 Lista de dependencias de Python
```

---

## 🛡️ Problemas y Soluciones

| **Problema** 😕 | **Solución** ✅ |
|-----------------|----------------|
| **Calibración del sensor**: La señal analógica no correspondía a los niveles UV. | Se realizaron pruebas empíricas y ajustes en el código para mapear correctamente los valores. 🔧 |
| **Interferencias ambientales**: Luces artificiales o sombras afectaban las lecturas. | Se diseñó una carcasa protectora y se ubicó el sensor en un lugar con luz solar directa. 🛡️ |
| **Estabilidad de datos**: Pérdida temporal de conexión serial. | Se implementó un sistema de detección de errores que muestra alertas si no se reciben datos en 5 segundos. 🚨 |

---

## 📊 Resultados

- **Prototipo funcional** ✅: Responde correctamente a variaciones de radiación UV, con LEDs y colores en la interfaz web alineados con la escala OMS.
- **Precisión** 🎯: Las lecturas calibradas coinciden con fuentes meteorológicas locales.
- **Interfaz intuitiva** 🌟: La interfaz web es clara, moderna y fácil de usar, con actualizaciones en tiempo real.

---

## 🌍 Aplicaciones en la Vida Real

- 🏫 **Espacios públicos**: Instalación en escuelas, parques o centros deportivos para prevenir daños por exposición solar.
- 📚 **Educación**: Uso en campañas de concienciación sobre los riesgos de la radiación UV.
- 🩺 **Salud pública**: Implementación en instituciones que promuevan la protección solar y el bienestar.

---

## 🏁 Conclusiones

El **Solmáforo** demuestra que es posible desarrollar un sistema económico, confiable y visualmente accesible para monitorear la radiación ultravioleta ☀️. La integración de hardware (**Arduino**, sensor VEML6075) y software (**Flask**, **Socket.IO**, **Chart.js**) ofrece una solución práctica para la prevención de riesgos solares, con un gran potencial para aplicaciones educativas y de salud pública.

**Innovación**:
- 🔗 Conexión entre teoría científica (radiación UV) y tecnología práctica.
- 🎨 Importancia del diseño visual para comunicar datos ambientales.
- 🌟 Versatilidad de Arduino en proyectos de impacto social.

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! 🚀 Para colaborar:
1. Haz un *fork* del repositorio 🍴.
2. Crea una rama para tu cambio (`git checkout -b feature/nueva-funcionalidad`) 🌿.
3. Realiza tus cambios y haz *commit* (`git commit -m 'Añadir nueva funcionalidad'`) 💾.
4. Sube los cambios (`git push origin feature/nueva-funcionalidad`) 🚀.
5. Crea un *pull request* en GitHub 📬.

---

## 📜 Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE). Consulta el archivo `LICENSE` para más detalles.

---

## 📧 Contacto

Para preguntas o sugerencias, contacta a los autores:
- **Diedereich Alemán**: [diedereicha@uamv.edu.ni](diedereicha@uamv.edu.ni) 📧
- **Gabriel Lacayo**: [gnolacayo@uamv.edu.ni](gnolacayo@uamv.edu.ni) 📧

---

🌟 *Desarrollado con pasión en Nicaragua para un futuro más seguro bajo el sol.* 🌟