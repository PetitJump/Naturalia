const herbe = document.getElementById("herbe");
const qherbe = document.getElementById("qherbe");

const loup = document.getElementById("loup");
const qloup = document.getElementById("qloup");

const mouton = document.getElementById("mouton");
const qmouton = document.getElementById("qmouton");

function majh() {
    qherbe.textContent = herbe.value;
}
herbe.addEventListener("input", majh);

function majl() {
    qloup.textContent = loup.value;
}
loup.addEventListener("input", majl);

function majm() {
    qmouton.textContent = mouton.value;
}
mouton.addEventListener("input", majm);

majm();
majl();
majh();