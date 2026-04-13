from flask import Flask, render_template, jsonify
import glob
import psutil
import os

app = Flask(__name__)

def get_temp():
    try:
        temps = psutil.sensors_temperatures()
        if temps:
            for entries in temps.values():
                for entry in entries:
                    if entry.current is not None:
                        return round(entry.current, 1)
    except Exception:
        pass

    for path in sorted(glob.glob("/sys/class/thermal/thermal_zone*/temp")):
        try:
            with open(path, "r") as f:
                raw = f.read().strip()
            temp = int(raw)
            if temp > 1000:
                temp = temp / 1000.0
            return round(temp, 1)
        except Exception:
            continue

    return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stats")
def stats():
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return jsonify({
        "cpu": psutil.cpu_percent(),
        "ram": {
            "used": round(mem.used / (1024**2), 1),
            "total": round(mem.total / (1024**2), 1),
            "percent": mem.percent
        },
        "disk": {
            "free": round(disk.free / (1024**3), 2),
            "percent": disk.percent
        },
        "temp": get_temp()
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host="0.0.0.0", port=port)