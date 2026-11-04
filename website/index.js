const monitor = "/monitor";
const config = "/config";
const apiBase = "http://127.0.0.1:8000";


let messages = [];

async function getData() {
    try 
    {
        const response = await fetch(apiBase + monitor);

        const result = await response.json();
        
        messages = [];

        console.log(result);
        setValues(result);

        displayBar(result.cpu_usage,"bar_cpu", "cpu");
    }
    catch (error) 
    {
        console.error("Fetch-Fehler:", error);
        const div = document.getElementById("warnings");
        // Alte Warnungen entfernen
        div.replaceChildren();

        div.className = "report";
    
        div.textContent = "Server offline 🔴";
        div.style.color = "red";

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
    const usedPercentRam = ((data.ram_used / data.ram_total) * 100).toFixed(2);
    displayBar(usedPercentRam, "bar_ram","ram");


    document.getElementById("ram_free").textContent = `RAM: ${data.ram_used}GB used of ${data.ram_total}GB`;
    document.getElementById("ram_used").textContent = `${data.ram_free}GB Free - ${data.ram_used} GB Used`;

    // DISK
    const usedPercentDisk =((data.disk_usage / data.disk_total) * 100).toFixed(2);    
    displayBar(usedPercentDisk, "bar_disk", "disk");
    
    document.getElementById("disk_free").textContent = `Storage: ${data.disk_usage}GB used of ${data.disk_total}GB`;
    document.getElementById("disk_percent").textContent = `${usedPercentDisk}% Used`;
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




function displayBar(dataToCheck, bar_id, type) {
    // Null-Reference Handler
    if (dataToCheck == null || bar_id == null)
    {
        console.log("Fehler bei der Übergabe der Werte, bitte überprüfe diese!");
        return;
    }

    // Holt sich das Bar-Element
    const bar = document.getElementById(bar_id);
    if (!bar) return;
    
    // Entfernt alte Classes
    bar.classList.remove("green", "yellow", "red");
    
    // Holt sich das Parent-Element
    const parent = bar.parentElement;
    
    // Alles hier ist in %-Angaben
    if (dataToCheck <= 20)
    {
        bar.classList.add("green");
        parent.parentElement.classList.add("card-normal");
        messages.push({component: type, status: "normal", value: dataToCheck });
    }

    else if (dataToCheck <= 40)
    {
        bar.classList.add("yellow");
        parent.parentElement.classList.add("card-warning");
        messages.push({ component: type, status: "warning", value: dataToCheck });
    }
    else
    {
        bar.classList.add("red");
        parent.parentElement.classList.add("card-critical");
        messages.push({ component: type, status: "critical", value: dataToCheck });
    }

    let progress = dataToCheck;
    bar.style.width = progress + "%";
}



getData();
setInterval(getData, 5000);