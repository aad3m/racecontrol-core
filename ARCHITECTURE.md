# 📐 Project Architecture

This project follows a **two-layer architecture** designed for clarity,
scalability, and clean separation of responsibilities.

```
+———————–+      +—————————+
|  racecontrol-client    |      |     racecontrol-core       |
|  (Backend Library)    | —> |  (Frontend Application)    |
+———————–+      +—————————+
```
---

# 🟦 1. Backend Library — `racecontrol-client`

The backend library is an installable Python package that contains:

- **Data fetching** (`data/`)
- **Business logic** and transformations (`services/`)
- **Utility helpers** (`utils/`)
- **A clean public API** (`__init__.py`)

### 📁 Folder Structure
```
racecontrol-client/
├─ data/         → fetch data, API wrappers
├─ services/     → scoring, analytics, form calculations
├─ utils/        → config, constants, HTTP helpers
└─ init.py   → defines public API
```

### 🧠 Design Principles
- Pure Python — no UI logic  
- All transformations done here  
- Public API returns **JSON-like data structures**  
- Semantic versioning controls breaking changes  
- Reusable in dashboards, servers, scripts, and CLI tools

---

# 🟩 2. Core Application — `racecontrol-core`

The core app is typically a **Streamlit** or **UI/UX layer** that imports
`racecontrol-client` and renders:

- Tables  
- Charts  
- KPIs  
- Interactive controls  

### 📁 Folder Structure
```
project_core/
├─ ui/          → layout, visualization, components
├─ services/    → app-specific helpers
├─ utils/       → formatting, UI helpers
└─ init.py
```

### 🎨 Design Principles
- No business logic — only UI & presentation  
- Calls backend functions for all real calculations  
- Supports multiple tabs, visualizations, and layouts  
- Easy to extend with new UI components

---

# 🧩 3. Data Flow Between Layers
```
User → Core App (UI) → racecontrol-client (data access + logic) → External API
↑
└── returns clean dict/list structures
```

- Core app never directly fetches external data  
- All calculations come from `racecontrol-client`  
- Core app focuses purely on visualization and user interaction  

---

# 🧪 4. Testing Strategy

### Client Library
- Unit tests for services
- Integration tests for API wrappers
- Mock external requests when necessary

### Core App
- Light UI testing
- Prefer manual or snapshot testing for visual components

---

# 🧱 5. Versioning Strategy

### Client Library
- Follows SemVer (`MAJOR.MINOR.PATCH`)
- API changes require version bump
- Releases align with feature milestones

### Core App
- Independently versioned
- UI changes do not affect the library version
- Tied loosely to backend versions

---

# 🚀 6. Deployment & Distribution

### racecontrol-client:
- Install locally (`pip install -e .`)
- Future: publish to PyPI

### racecontrol-core:
- Can be deployed on:
  - Streamlit Cloud
  - Render
  - HuggingFace Spaces
  - Dockerized environments

---

# 📝 Summary

| Component            | Purpose | Contains | Should Not Contain |
|----------------------|---------|----------|---------------------|
| `racecontrol-client` | Backend logic | Data, services, utils | UI, Streamlit, app logic |
| `racecontrol-core`   | Frontend UI | Layouts, components | Business logic, heavy computation |

This architecture makes the project:
- Easy to scale  
- Easy to maintain  
- Easy to contribute to  
- Clear for onboarding new developers  

---

# 🙌 Thanks for building with this architecture!