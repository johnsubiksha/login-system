document.getElementById("registerForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    const password = formData.get("password");

    // password rules
    if (password.length < 6) {
        alert("Password must be at least 6 characters");
        return;
    }

    if (!/[A-Z]/.test(password)) {
        alert("Password must contain at least 1 uppercase letter");
        return;
    }

    if (!/[0-9]/.test(password)) {
        alert("Password must contain at least 1 number");
        return;
    }
    
    try {
        const res = await fetch("http://127.0.0.1:8000/register", {
            method: "POST",
            body: formData
        });

        const data = await res.json();

        if (data.status === "registered") {
            alert("Registered Successfully ✅");
            window.location.href = "login.html";
        }
        else if (data.status === "exists") {
            alert("Email already registered ❌");
        } else {
            alert("Registration Failed ❌");
        }
    } catch (error) {
        alert("Server Error ❌");
        console.error(error);
    }
});