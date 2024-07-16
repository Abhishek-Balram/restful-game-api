const API_BASE_URL = 'http://localhost:5001';       //change this to the server's actual address in production

async function addPlayer() {
    const playerData = document.getElementById('newPlayerData').value;
    try {
        const response = await axios.post(`${API_BASE_URL}/players`, `data=${playerData}`);
        alert(`Player added with ID: ${Object.keys(response.data)[0]}`);
        getPlayerList();
    } catch (error) {
        alert('Error adding player');
    }
}

async function getPlayer() {
    const playerId = document.getElementById('getPlayerId').value;
    try {
        const response = await axios.get(`${API_BASE_URL}/players/${playerId}`);
        document.getElementById('playerDetails').innerHTML = `
            <h3>Player Details</h3>
            <p>ID: ${playerId}</p>
            <p>Data: ${response.data[playerId]}</p>
        `;
    } catch (error) {
        alert('Error getting player');
    }
}

async function updateScore() {
    const playerId = document.getElementById('updatePlayerId').value;
    const score = document.getElementById('updatePlayerScore').value;
    try {
        await axios.put(`${API_BASE_URL}/scores/${playerId}`, `score=${score}`);
        alert('Score updated successfully');
        getPlayerScore(playerId);
    } catch (error) {
        alert('Error updating score');
    }
}

async function getPlayerScore(playerId) {
    try {
        const response = await axios.get(`${API_BASE_URL}/scores/${playerId}`);
        document.getElementById('scoreDetails').innerHTML = `
            <h3>Player Score</h3>
            <p>ID: ${playerId}</p>
            <p>Score: ${response.data[playerId]}</p>
        `;
    } catch (error) {
        alert('Error getting player score');
    }
}

async function getPlayerList() {
    try {
        const response = await axios.get(`${API_BASE_URL}/players`);
        const playerListHtml = Object.entries(response.data).map(([id, data]) => `
            <p>ID: ${id}, Data: ${data}</p>
        `).join('');
        document.getElementById('playerList').innerHTML = `
            <h3>Player List</h3>
            ${playerListHtml}
        `;
    } catch (error) {
        alert('Error getting player list');
        console.log(error)
    }
}

// Initialize player list on page load
document.addEventListener('DOMContentLoaded', getPlayerList);