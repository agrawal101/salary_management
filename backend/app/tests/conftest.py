import builtins
import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from backend.app.main import app


builtins.client = TestClient(app)
