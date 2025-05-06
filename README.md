# Auto-Snowplow

A project to read sensor data from an Arduino-powered snowplow and display it in real-time on a web dashboard.

---

## Project Structure

```
arduino/Final.ino           # Arduino code for sensors and motors
backend/server.py           # Flask backend to read serial and serve API
backend/requirements.txt    # Python dependencies
frontend/sensor-dashboard/  # React frontend for dashboard
```

---

## Getting Started

### 1. Arduino

- Upload `Final.ino` to your Arduino board.
- Ensure the board is connected to your PC and note the COM port.

### 2. Backend (Flask)

- Install Python dependencies:
  ```bash
  cd backend
  pip install -r requirements.txt
  ```
- Edit `server.py` and set the correct `SERIAL_PORT` for your Arduino.
- Start the server:
  ```bash
  python server.py
  ```

### 3. Frontend (React)

- Install Node dependencies:
  ```bash
  cd frontend/sensor-dashboard
  npm install
  ```
- Start the React app:
  ```bash
  npm start
  ```
- Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## Features

- Real-time display of ultrasonic and line sensor data.
- Simple, modern dashboard UI.
- Easily extensible for more sensors or controls.

---

## License

This project is for educational purposes. 