# racecontrol-core

Frontend Streamlit UI for the RaceControl F1 dashboard.

- Uses `racecontrol-client` for all data & computation
- No pandas in this layer: only Streamlit + Plotly + Python dicts/lists

Run locally:

```bash
pip install -e .
streamlit run app.py
---

### `racecontrol_core/__init__.py`

```python
from .ui import *
from .services import *
from .utils import *

__all__ = ["ui", "services", "utils"]