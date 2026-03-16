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




function simpleClamp(e) {
    const changed = e.target;
    const h = parseInt(herbe.value, 10) || 0;
    const l = parseInt(loup.value, 10) || 0;
    const m = parseInt(cerf.value, 10) || 0;
    const sum = h + l + m;
    if (sum > 20) {
        const excess = sum - 20;
        changed.value = Math.max(0, parseInt(changed.value, 10) - excess);
    }
    if (changed === herbe) majh();
    else if (changed === loup) majl();
    else majm();
}

herbe.addEventListener('input', simpleClamp);
loup.addEventListener('input', simpleClamp);
cerf.addEventListener('input', simpleClamp);
