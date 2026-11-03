const monitor = "/monitor"
const apiBase = "http://127.0.0.1:8000"

async function getData() {
    try 
    {
        const response = await fetch(apiBase + monitor);

        const result = await response.json();

        console.log(result);
        setValues(result);
    }
    
    catch (error) 
    {
        console.error("Fetch-Fehler:", error);
    }
}

async function setValues(data) {
    if (data == null)
        return;

    // RAM
    document.getElementById("ram_free").textContent = `RAM Free: ${data.ram_free}`;
    document.getElementById("ram_total").textContent = `RAM Total: ${data.ram_total}`;
    document.getElementById("ram_used").textContent = `RAM Used: ${data.ram_used}`;

    // DISK
    document.getElementById("disk_free").textContent = `Disk Free: ${data.disk_free}`;
    document.getElementById("disk_percent").textContent = `Disk Percent: ${data.disk_percent}`;
    document.getElementById("disk_total").textContent = `Disk Total: ${data.disk_total}`;
    document.getElementById("disk_usage").textContent = `Disk Usage: ${data.disk_usage}`;

    // UPTIME
    document.getElementById("uptime").textContent = `Uptime Seconds: ${data.uptime}`;

    // NETWORK
    document.getElementById("upload_speed").textContent = `Upload Speed: ${data.upload_speed}`;
    document.getElementById("download_speed").textContent = `Download Speed: ${data.download_speed}`;
}

getData();