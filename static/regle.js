// Boutton pour les prédateurs

const nbpa1 = document.getElementById('nb_bebe_predateur1')
const nbpa2 = document.getElementById('nb_bebe_predateur2')

function majnbpa2(){
    nbpa2.disabled = false
    nbpa2.min = Number(nbpa1.value)
}

nbpa1.addEventListener('change', majnbpa2)

const nbjpa1 = document.getElementById('nb_bebe_tout_les_preda')
const nbjpa2 = document.getElementById('nb_bebe_tout_les_preda2')

function majnbjpa2(){
    nbjpa2.disabled = false
    nbjpa2.min = Number(nbjpa1.value)
}

nbjpa1.addEventListener('change', majnbjpa2)


// boutton pour les proies

const nbpo1 = document.getElementById('nb_bebe_proie1')
const nbpo2 = document.getElementById('nb_bebe_proie2')

function majnbpo2(){
    nbpo2.disabled = false
    nbpo2.min = Number(nbpo1.value)
}

nbpo1.addEventListener('change', majnbpo2)

const nbjpo1 = document.getElementById('nb_bebe_tout_les_proie')
const nbjpo2 = document.getElementById('nb_bebe_tout_les_proie2')

function majnbjpo2(){
    nbjpo2.disabled = false
    nbjpo2.min = Number(nbjpo1.value)
}

nbjpo1.addEventListener('change', majnbjpo2)
