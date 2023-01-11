// -------
// -------
// 
//      Tipologie
//      VARIABILI
// 
// -------
// -------

var nome1 = 'Pietra'; // Variabile
let nome2; // Variabile locale
const NOME3 = ''; // Constanti in maiuscolo

/*
for(let i; i<10; i++){ 
    Funziona sono qui dentro
}
*/

console.log(nome1)

// -------
// -------
// 
//      Tipologia
//      OGGETTI
// 
// -------
// -------

var stringa1 = 'matteo';
var stringa2 = "Antonio";

var boolean = true;
var integer = 12;
var a = null;

var array = [];
var object= {};

// -------
// -------
// 
//    Conversione
// 
// -------
// -------

var anni = 'anni';
var anni2 = 18;

var anniC = parseInt(anni);
var anniC1 = parseFloat(anni); // Numeri con virgola

console.log(anniC);
console.log(anniC1);

// Numeri non confertiti restituisce nan

var a = 'anni';
var aC = parseInt(a);

console.log(aC);
console.log(isNaN(aC));

// -------
// -------
// 
//    Ritorno
//    Valore
// 
// -------
// -------

var intero = "23";
console.log(typeof(intero));

// -------
// -------
// 
//    Concatenazione   
//    Stringhe e numeri
// 
// -------
// -------

var a = '37';
var b = 7;

a = parseInt(a)

console.log(a + b)

// -------
// -------
// 
//    Ritorno
//    Valore e comparazioni
// 
// -------
// -------

var a = '37';
var b = 37;

console.log(a == b)
console.log(a !== b)
console.log(a === b)

// -------
// -------
// 
//    Array
// 
// -------
// -------

var dati = ['matteo', 35, 'Prova', true];

console.log(dati[2]);

// -------
// -------
// 
//    Swith (IF else)
// 
// -------
// -------

var user = 'Matteo';
var role = 'editor';

switch(user){
    case 'Matteo':
        role = 'Admin';
        break;

    case 'Marco':
        role = 'Builder';
        break;

    default:
        role = 'user';
}

// -------
// -------
// 
//    FOR
// 
// -------
// -------
var nomi = ['pietro','gigi','rose','john']

for(let i = 0; i < nomi.length ; i++){
    if(nomi[i] != 'rose') continue;
        console.log('Ciao ' + nomi[i])
}

for(element of nomi){
    console.log(element)
}