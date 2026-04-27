async function getClimate() {
    const city = document.getElementById("city").value;

    const response = await fetch(`http://127.0.0.1:5000/climate?city=${city}`);
    const data = await response.json();

    document.getElementById("result").innerHTML = `
        <h3>${data.city}</h3>
        <p>🌡 Temp: ${data.current_temp}°C</p>
        <p>💧 Humidity: ${data.humidity}%</p>
        <p>🔮 Predicted Temp: ${data.predicted_temp}°C</p>
    `;
}
