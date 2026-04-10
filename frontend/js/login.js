document.getElementById("loginForm").addEventListener("submit", async function(e){
    e.preventDefault();

    const formData = new FormData(this);

    const res = await fetch("http://127.0.0.1:8000/login", {
        method: "POST",
        body: formData
    });

    const data = await res.json();

    if(data.status === "success"){
        localStorage.setItem("token", data.token);
        localStorage.setItem("user", JSON.stringify(data));

        window.location.href = "profile.html";
    } else {
        alert("Invalid login");
    }
});