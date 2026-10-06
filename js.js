const cor = document.querySelector(".btn-cor");

// Quando a página abrir, verifica se o modo escuro estava ativado
if (localStorage.getItem("modo") === "escuro") {
    document.body.classList.add("dark-mode");
    cor.querySelector("button").textContent = "🌒";
}

cor.addEventListener("click", function() {

    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {
        localStorage.setItem("modo", "escuro");
        cor.querySelector("button").textContent = "🌒";
    } else {
        localStorage.setItem("modo", "claro");
        cor.querySelector("button").textContent = "☀️";
    }

});

const login = document.querySelector(".btn-entrar");
login.addEventListener("click", function(){
    modal.style.display = "flex"
})

const funciona = document.querySelector(".bt-sobre");
funciona.addEventListener("click", function(){
    window.location.href = "funcionamento.html"
})

const modal = document.querySelector(".modal-login");

const fechar = document.querySelector(".fechar");
fechar.addEventListener("click", function(){
    modal.style.display = "none"
})

const img = document.getElementById("animaçao")
img.addEventListener("click", function(){
    const confete = document.createElement("div");
    confete.classList.add("confete");
    document.body.appendChild(confete);

})
