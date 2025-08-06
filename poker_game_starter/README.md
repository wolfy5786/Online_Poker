# Poker Game Starter Project

## Overview
This project implements a simple multiplayer poker game using:
- Backend: Django + Channels + Redis
- Frontend: React + Tailwind CSS
- Communication: WebSockets

## Requirements
- Docker and Docker Compose installed

## How to run

1. Build and start all containers:

```bash
docker-compose up --build
```

2. Backend will be available on `http://localhost:8000`
3. Frontend will be available on `http://localhost:3000`

## Usage

- Open multiple browser tabs/windows and join the same room code.
- Click **Start Game** to shuffle and deal cards.
- Use **Next Turn** to move the turn to next player.
- Players can **Fold** to exit.
- The game ends when only one player remains.

## WebSocket API

WebSocket endpoint:

```
ws://localhost:8000/ws/game/<room_code>/
```

### Messages from client:

| Action   | Description                 |
|----------|-----------------------------|
| start    | Start the game, deal cards   |
| next     | Move to next player turn     |
| fold     | Fold and leave the game      |

### Messages from server:

- **update**: game state update

```json
{
  "action": "update",
  "players": [...],
  "your_hand": [...],
  "community_cards": [...],
  "turn": 0
}
```

- **game_over**: game ended, winner announced

```json
{
  "action": "game_over",
  "winner": "player_id"
}
```
