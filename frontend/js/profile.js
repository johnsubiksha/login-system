const user = JSON.parse(localStorage.getItem("user"));

if(!user){
    window.location.href = "login.html";
}

// show basic info
document.getElementById("name").innerText = user.name;
document.getElementById("email").innerText = user.email;

// fetch profile
fetch(`http://127.0.0.1:8000/profile-data?email=${user.email}`)
.then(res => res.json())
.then(data => {
    document.querySelector("[name=nickname]").value = data.nickname || "";
    document.querySelector("[name=gender]").value = data.gender || "";
    document.querySelector("[name=country]").value = data.country || "";
    document.querySelector("[name=language]").value = data.language || "";
    document.querySelector("[name=timezone]").value = data.timezone || "";
});

// enable edit
function enableEdit(){
    document.querySelectorAll("input").forEach(i => i.disabled = false);
    document.getElementById("saveBtn").style.display = "block";
}

// save update
document.getElementById("profileForm").addEventListener("submit", async function(e){
    e.preventDefault();

    const formData = new FormData(this);
    formData.append("email", user.email);

    await fetch("http://127.0.0.1:8000/update-profile", {
        method: "POST",
        body: formData
    });

    alert("Profile Updated ✅");
    location.reload();
});

// logout
function logout(){
    localStorage.removeItem("user");
    window.location.href = "login.html";
}