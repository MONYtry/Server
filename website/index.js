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
    document.getElementById("ram_free").textContent = `RAM: ${data.ram_used}GB used of ${data.ram_total}GB`;
    document.getElementById("ram_used").textContent = `${data.ram_free}GB Free · ${data.ram_used} GB Used`;

    // DISK
    const remainingPercent = ((data.disk_free / data.disk_total) * 100).toFixed(2);
    document.getElementById("disk_free").textContent = `Storage: ${data.disk_usage}GB used of ${data.disk_total}GB`;
    document.getElementById("disk_percent").textContent = `${remainingPercent}% Available`;
    document.getElementById("disk_usage").textContent = `${data.disk_free} GB Free · ${data.disk_usage} GB Used`;

    // UPTIME
    document.getElementById("uptime").textContent = `Uptime Seconds: ${data.uptime}`;

    // NETWORK
    document.getElementById("upload_speed").textContent = `Upload Speed: ${data.upload_speed}MB/s`;
    document.getElementById("download_speed").textContent = `Download Speed: ${data.download_speed}MB/s`;
}

getData();
setInterval(getData(), 5000);