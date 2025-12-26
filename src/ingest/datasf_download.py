from pathlib import Path
import requests

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

def download_csv(url: str, out_path: Path) -> None:
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    out_path.write_bytes(r.content)
    print(f"Saved: {out_path} ({out_path.stat().st_size:,} bytes)")

def download_geojson(url: str, out_path: Path) -> None:
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    out_path.write_bytes(r.content)
    print(f"Saved: {out_path} ({out_path.stat().st_size:,} bytes)")

def main():
    # DataSF (Socrata) dataset IDs:
    evictions_url = "https://data.sfgov.org/resource/5cei-gny5.csv?$limit=1000000"
    download_csv(evictions_url, DATA_DIR / "evictions.csv")

    # SF Find Neighborhood
    neighborhoods_url = "https://data.sfgov.org/resource/pty2-tcw4.geojson?$limit=50000"
    download_geojson(neighborhoods_url, DATA_DIR / "neighborhoods.geojson")

if __name__ == "__main__":
    main()
