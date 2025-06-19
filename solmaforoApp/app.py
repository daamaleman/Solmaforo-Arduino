from flask import Flask, render_template
from flask_socketio import SocketIO
import serial
import re
import threading
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app, async_mode='threading')

# Serial port configuration (adjust port as needed, e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux)
SERIAL_PORT = 'COM3'  # Update this to your Arduino's serial port
BAUD_RATE = 9600
ser = None

# Global variable to store latest UV data
uv_data = {'uv_index': 0.00, 'danger_level': 'N/A', 'color': 'gray'}

def get_color_for_uv(uv_index):
    """Determine background color based on UV index, matching Arduino relay logic."""
    if uv_index < 3:
        return 'green'
    elif uv_index < 6:
        return 'yellow'
    elif uv_index < 8:
        return 'orange'
    elif uv_index < 11:
        return 'red'
    else:
        return 'purple'

def read_serial():
    """Background thread to read serial data and emit updates."""
    global uv_data
    ser = None  # Inicializa ser como None
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"Connected to {SERIAL_PORT}")
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                print("Linea recibida:", line)  # Mostrar siempre la línea cruda
                # Parse serial output like "UV Index: 5.23, Voltaje: 3.45, Nivel: MEDIO"
                match = re.match(r'UV Index: (\d+\.\d+), Voltaje: (\d+\.\d+), Nivel: (\w+)', line)
                if match:
                    uv_index = round(float(match.group(1)), 2)
                    voltage = round(float(match.group(2)), 2)
                    danger_level = match.group(3)
                    color = get_color_for_uv(uv_index)
                    uv_data = {
                        'uv_index': uv_index,
                        'voltage': voltage,
                        'danger_level': danger_level,
                        'color': color
                    }
                    print("Enviando datos:", uv_data)
                    socketio.emit('uv_update', uv_data)
                else:
                    # Si no hay match, envía el dato crudo para debug
                    print("No match, enviando crudo a web:", line)
                    socketio.emit('uv_update', {'uv_index': 0, 'voltage': 0, 'danger_level': 'N/A', 'color': 'gray', 'raw': line})
            time.sleep(0.1)  # Small delay to prevent CPU overuse
    except serial.SerialException as e:
        print(f"Serial error: {e}")
        uv_data = {'uv_index': 0.00, 'danger_level': 'ERROR', 'color': 'gray', 'voltage': 0.0}
        print("Enviando datos:", uv_data)
        socketio.emit('uv_update', uv_data)
    finally:
        if ser is not None and ser.is_open:
            ser.close()

@app.route('/')
def index():
    """Serve the main web page."""
    return render_template('index.html')

@app.route('/graphs')
def graphs():
    return render_template('graphs.html')

@socketio.on('connect')
def handle_connect():
    """Send initial UV data to newly connected clients."""
    socketio.emit('uv_update', uv_data)

if __name__ == '__main__':
    # Start the serial reading thread
    serial_thread = threading.Thread(target=read_serial, daemon=True)
    serial_thread.start()
    # Run the Flask-SocketIO app
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, use_reloader=False)