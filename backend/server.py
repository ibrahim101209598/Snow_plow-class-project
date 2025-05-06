from flask import Flask, jsonify
from flask_cors import CORS
import serial
import threading

app = Flask(__name__)
CORS(app)

SERIAL_PORT = 'COM3'  # Change to your Arduino's port
BAUDRATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)
latest_data = {}

def read_serial():
    global latest_data
    while True:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line:
                parts = line.split(',')
                if len(parts) == 6:
                    latest_data = {
                        'leftDistance': float(parts[0]),
                        'middleDistance': float(parts[1]),
                        'rightDistance': float(parts[2]),
                        'leftLine': int(parts[3]),
                        'middleLine': int(parts[4]),
                        'rightLine': int(parts[5])
                    }
        except Exception:
            continue

@app.route('/api/sensors')
def get_sensors():
    if latest_data:
        return jsonify(latest_data)
    else:
        return jsonify({'error': 'No data'}), 500

if __name__ == '__main__':
    t = threading.Thread(target=read_serial, daemon=True)
    t.start()
    app.run(debug=True) 