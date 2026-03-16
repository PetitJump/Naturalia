// Active le deuxième champ de chaque fourchette quand le premier est rempli
const paires = [
  ['nb_bebe_predateur1', 'nb_bebe_predateur2'],
  ['nb_bebe_proie1',     'nb_bebe_proie2'],
];
paires.forEach(([id1, id2]) => {
  const el1 = document.getElementById(id1);
  const el2 = document.getElementById(id2);
  if (!el1 || !el2) return;
  el1.addEventListener('input', () => {
    el2.min = el1.value;
    if (parseInt(el2.value) < parseInt(el1.value)) el2.value = el1.value;
  });
});
