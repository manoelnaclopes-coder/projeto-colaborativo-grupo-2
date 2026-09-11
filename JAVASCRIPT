document.getElementById("txt-1").innerHTML = "mudei informação <b></b>";  //inserir coisas no html pelo id

function eventoclick() {
    if (document.body.style.backgroundColor == "dark") {
        document.body.style.setProperty("white-mode", "#f2f2f2");
    } else {
        document.body.style.setProperty("dark-mode", "#000000");
    }
}

const cor = document.querySelector(".btn-cor");
cor.addEventListener("click", function(){
    document.body.classList.toggle("dark-mode");
    if(document.body.classList.contains("dark-mode")){
        cor.textContent = "🌒";
    }else{
        cor.textContent = "☀️ ";
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

