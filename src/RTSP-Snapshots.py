import os, subprocess, time, yaml
from pathlib import Path
from datetime import datetime

CONFIG = os.path.join(os.path.dirname(__file__), "..", "config.yaml")

def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def ensure_dir(p): Path(p).mkdir(parents=True, exist_ok=True)

def grab_with_ffmpeg(rtsp, out_path, timeout_sec=15):
    cmd = [
        "ffmpeg",
        "-rtsp_transport", "tcp",
        "-stimeout", str(timeout_sec * 1000000),  # micros
        "-y",
        "-i", rtsp,
        "-frames:v", "1",
        out_path,
    ]
    try:
        subprocess.run(cmd, check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False

def main():
    cfg = load_config(CONFIG)
    cams = cfg.get("cameras", [])
    snap_cfg = cfg.get("snapshots", {})
    out_base = Path(snap_cfg.get("output_dir", "./data/snapshots"))
    for cam in cams:
        name = cam["name"].replace(" ", "_")
        rtsp = cam["rtsp"]
        day = datetime.now().strftime("%Y-%m-%d")
        cam_dir = out_base / name / day
        ensure_dir(cam_dir)
        ts = int(time.time())
        out_path = str(cam_dir / f"img_{ts}.jpg")
        print(f"[INFO] Capturando {name} via FFmpeg…")
        if grab_with_ffmpeg(rtsp, out_path):
            print(f"[OK] Snapshot salvo: {out_path}")
        else:
            print("[ERR] Falha ao capturar snapshot desta câmera.")

if __name__ == "__main__":
    main()
