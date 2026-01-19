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




function simpleClamp(e) {
    const changed = e.target;
    const h = parseInt(herbe.value, 10) || 0;
    const l = parseInt(loup.value, 10) || 0;
    const m = parseInt(mouton.value, 10) || 0;
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
mouton.addEventListener('input', simpleClamp);
