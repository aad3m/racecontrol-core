# 🏁 racecontrol-core  
### Streamlit Frontend for Interactive Dashboards, Analytics, and Tools

`racecontrol-core` is the **application layer** of the project.  
It provides the user interface, interactive controls, visualizations, and
end-to-end experience built on top of the backend client package
`racecontrol-client`.

This separation ensures the core app stays lean, modular, and easy for
contributors to extend.

---

## ✨ Features

- 🎨 Clean Streamlit UI with reusable components  
- 📊 Dynamic visualizations powered by Plotly  
- 🔌 Fully decoupled from data layer via `racecontrol-client`  
- 🧠 Supports rich analytics, scoring models, and custom logic  
- 🌐 Ready for deployment, dashboards, or embedding  

---

## 📁 Project Structure
```
racecontrol-core/
├─ app.py                 → Main application entrypoint
├─ project_core/
│   ├─ ui/                → UI components, layouts, charts
│   ├─ services/          → App-specific helpers
│   ├─ utils/             → Formatting, small helpers
│   └─ init.py
└─ README.md
```
This structure enforces a clear separation of **UI**, **client logic**, and
**application behavior**.

---

## 🚀 Getting Started

### Install dependencies:
```bash
pip install -r requirements.txt
```
### Install the client library (required):
```bash
pip install ../racecontrol-client
```
### Run the app:
```bash
streamlit run app.py
```

## 🧩 Using the Client Library
Inside the core app, you import backend functionality like this:
```python
from racecontrolClient import (
    get_schedule,
    get_driver_standings,
    get_fantasy_scores,
)
```
This ensures the core app does zero business logic —
all computation lives in the client library.

## ⚙️ Sidebar Controls
The app supports interactive inputs such as:
- Selecting seasons
- Adjusting scoring weights
- Toggling display modes
- Refreshing data

These controls dynamically update visualizations using Streamlit state.

## 🎨 UI Components
All UI elements are modularized in ui/, such as:
- render_header()
- render_kpis()
- render_tabs()
- Charts + layout components

Contributors can add new components without touching core logic.

## 🧠 App Philosophy
- Keep UI simple and clean
- Keep logic in the client library
- Allow contributors to build new tabs, charts, or features easily
- Make the app framework-agnostic so the backend works everywhere

## 🤝 Contributing
We welcome contributions!
Please see:
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [ARCHITECTURE.md](ARCHITECTURE.md)

Before opening a pull request.

Good contributions include:
- New UI components
- Improved visualizations
- New tabs or analytics
- Better documentation
- Bug fixes or refactors

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.