const monitor = "/monitor";
const config = "/config";
const apiBase = "http://127.0.0.1:8000";

async function getData() {
    try 
    {
        const response = await fetch(apiBase + monitor);

        const result = await response.json();

        console.log(result);
        setValues(result);
        handleErrors(result);
    }
    catch (error) 
    {
        console.error("Fetch-Fehler:", error);
    }
}

async function setStatus(statusText, color) {
    const status = document.getElementById("status");

    status.style.color = color;
    status.textContent = statusText   
}


async function setValues(data) {

    if (data == null)
        return;
    // RAM
    document.getElementById("ram_free").textContent = `RAM: ${data.ram_used}GB used of ${data.ram_total}GB`;
    document.getElementById("ram_used").textContent = `${data.ram_free}GB Free - ${data.ram_used} GB Used`;

    // DISK
    const remainingPercent = ((data.disk_free / data.disk_total) * 100).toFixed(2);
    document.getElementById("disk_free").textContent = `Storage: ${data.disk_usage}GB used of ${data.disk_total}GB`;
    document.getElementById("disk_percent").textContent = `${remainingPercent}% Available`;
    document.getElementById("disk_usage").textContent = `${data.disk_free} GB Free - ${data.disk_usage} GB Used`;
    
    // UPTIME
    document.getElementById("uptime").textContent = `Uptime Seconds: ${data.uptime}`;

    // NETWORK
    document.getElementById("upload_speed").textContent = `Upload Speed: ${data.upload_speed}MB/s`;
    document.getElementById("download_speed").textContent = `Download Speed: ${data.download_speed}MB/s`;
    document.getElementById("private_ip").textContent = `Private IP: ${data.private_ip}`;
    document.getElementById("public_ip").textContent = `Public IP ${data.public_ip}`;
    
    // CPU
    document.getElementById("cpu_usage").textContent =  `CPU Usage: ${data.cpu_usage}%`;
}

async function getConfig() {
    try {
        const response = await fetch(apiBase + config);

        if (!response.ok) {
            throw new Error("HTTP Error: " + response.status);
        }

        const result = await response.json();
        return result;

    } catch (error) {
        console.error("Fetch-Fehler:", error);
        return null;
    }
}

function setDesign(id,text,color)
{
    const element = document.getElementById(id);

    element.style.color = color;
    element.textContent = text;
}

async function handleErrors(data)
{
    if (data == null)
    {
        setDesign("warnings", "Server offline 🔴","red")
        return;
    }
    
    const result = await getConfig();
    
    if (!result) return;
    
    let messages = [];
    
    // CPU
    if (data.cpu_usage >= 95)
        messages.push("🔴 CPU kritisch ausgelastet!");
    else if (data.cpu_usage >= 80)
        messages.push("🟠 CPU stark ausgelastet!");
    else if (data.cpu_usage >= 60)
        messages.push("🟡 CPU-Auslastung erhöht!");

    // RAM
    if (data.ram_used > result.critical_ram_usage)
        messages.push("🔴 RAM kritisch ausgelastet!");
    else if (data.ram_used > result.high_ram_usage)
        messages.push("🟠 RAM stark ausgelastet!");
    else if (data.ram_used > result.medium_ram_usage)
        messages.push("🟡 RAM-Auslastung erhöht!");
    if (messages.length > 0)
    {
        setDesign("warnings",messages,"green");
    }
}
getData();
setInterval(getData, 5000);