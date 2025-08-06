# ♠️ Poker Game - Multiplayer WebSocket App

A real-time multiplayer poker game built with **Django**, **Channels**, **Redis**, and **React**. This project showcases WebSocket-based communication for real-time game state updates and is fully containerized using Docker.

---

## 🛠️ Tech Stack

### 💻 Backend
- **Python 3.11**
- **Django** – Core backend framework
- **Channels** – WebSocket support via ASGI
- **Redis** – In-memory pub/sub and channel layer for real-time communication
- **Daphne** – ASGI server for Django/Channels

### 🎨 Frontend
- **React 18**
- **Vite** – Fast modern frontend tooling
- **TailwindCSS** – Utility-first CSS framework

### 🐳 DevOps
- **Docker** – Containerized full-stack setup
- **Docker Compose** – Multi-container orchestration

---

## 🎯 Features

- ♠️ Real-time multiplayer poker table
- 📡 WebSocket communication (no page reloads)
- 🔄 Game state updates broadcast instantly
- ⚙️ Redis-backed channel layer for performance
- 🧱 Modular backend and frontend codebases
- 🐳 Fully Dockerized for easy deployment

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/poker-game.git
cd poker-game
```

### 2. Run the app with Docker

```bash
docker-compose up --build
```

This command builds and starts:

- `backend` on [http://localhost:8000](http://localhost:8000)
- `frontend` on [http://localhost:5173](http://localhost:5173)
- `redis` on port `6379`

---

## 📁 Project Structure

```
poker_game_starter/
│
├── poker_game/           # Django backend
│   ├── poker_game/       # Django project settings
│   └── game/             # Game logic app
│
├── poker-ui/             # React frontend
│   ├── src/
│   └── tailwind.config.js
│
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
└── README.md
```

---

## 📦 Docker Containers

| Service   | Description                   | Port     |
|-----------|-------------------------------|----------|
| backend   | Django + Channels + Daphne    | 8000     |
| frontend  | React + Vite + Tailwind       | 5173     |
| redis     | Pub/Sub + channel layer       | 6379     |

---

## 🔧 TODO / Future Improvements

- ✅ Player login and authentication
- ⏳ Matchmaking or lobby system
- ⏳ Poker hand evaluation logic
- ⏳ Game replays / logs
- ✅ Tailwind styling polish


