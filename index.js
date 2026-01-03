const nome = 'Gabriel'
let xp = 10000
let nivel = "";

if (xp<=1000) {
    nivel = 'Ferro';}
else if (xp>=1001 && xp<=2000) {
    nivel = 'Bronze'}
else if (xp>=2001 && xp<=4000) {
    nivel = 'Prata'}
else if (xp>=4001 && xp<=6000) {
    nivel = 'Ouro'}
else if (xp>=6001 && xp<=8000) {
    nivel = 'Platina'}
else if (xp>=8001 && xp<=9000) {
    nivel = 'Ascendente'}
else if (xp>=9001 && xp<=10000) {
    nivel = 'Imortal'}
else { nivel = 'Radiante' ; }

console.log(O Herói de nome ${nome} está no nível de ${nivel});

