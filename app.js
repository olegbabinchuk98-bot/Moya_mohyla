const T={uk:{grave:'Моя могила',dig:'Копати',inventory:'Інвентар',crypt:'Склеп',avatar:'Аватар',clan:'Клан'},ru:{grave:'Моя могила',dig:'Копать',inventory:'Инвентарь',crypt:'Склеп',avatar:'Аватар',clan:'Клан'},en:{grave:'My Grave',dig:'Dig',inventory:'Inventory',crypt:'Crypt',avatar:'Avatar',clan:'Clan'}};
let lang='uk';
function setLang(l){lang=l;document.querySelectorAll('[data-i18n]').forEach(e=>e.textContent=T[l][e.dataset.i18n]);localStorage.lang=l}
setLang(localStorage.lang||'uk');
