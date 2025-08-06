import { useState } from "react";
import Game from "./Game";

export default function JoinRoom() {
  const [room, setRoom] = useState("");
  const [joined, setJoined] = useState(false);

  return joined ? (
    <Game roomCode={room} />
  ) : (
    <div className="p-10">
      <h1 className="text-3xl font-bold mb-4">Join Poker Room</h1>
      <input
        className="border p-2 mr-2"
        placeholder="Enter Room Code"
        value={room}
        onChange={(e) => setRoom(e.target.value)}
      />
      <button className="btn" onClick={() => setJoined(true)}>
        Join
      </button>
    </div>
  );
}
