document.getElementById("registerForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const formData = new FormData(this);

    try {
        const res = await fetch("http://127.0.0.1:8000/register", {
            method: "POST",
            body: formData
        });

        const data = await res.json();

        if (data.status === "registered") {
            alert("Registered Successfully ✅");
            window.location.href = "login.html";
        } else {
            alert("Registration Failed ❌");
        }
    } catch (error) {
        alert("Server Error ❌");
        console.error(error);
    }
});