import json
import subprocess
from pathlib import Path
from datetime import datetime

RESULTS_DIR = Path(__file__).parent.parent / "results"
RESULTS_DIR.mkdir(exist_ok=True)

def run_and_time(cmd, outfile):
    """Run spark-submit in a subprocess and dump timing JSON."""
    start = datetime.utcnow()
    proc = subprocess.run(cmd, check=True)
    end = datetime.utcnow()
    elapsed = (end - start).total_seconds()

    out = RESULTS_DIR / outfile
    out.write_text(json.dumps({
        "cmd": cmd,
        "utc_start": start.isoformat() + "Z",
        "utc_end": end.isoformat() + "Z",
        "elapsed_s": elapsed
    }, indent=2))
    print(f"📝  Wrote timing to {out}")
