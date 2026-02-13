const herbe = document.getElementById("herbe");
const qherbe = document.getElementById("qherbe");

const loup = document.getElementById("loup");
const qloup = document.getElementById("qloup");

const cerf = document.getElementById("cerf");
const qcerf = document.getElementById("qcerf");

function majh() {
    qherbe.textContent = herbe.value;
}
herbe.addEventListener("input", majh);

function majl() {
    qloup.textContent = loup.value;
}
loup.addEventListener("input", majl);

function majm() {
    qcerf.textContent = cerf.value;
}
cerf.addEventListener("input", majm);

majm();
majl();
majh();
