// ES. 1

function isTrue(a){
    if(a == "Y" || a == "yes" || a == "y"){
        return true
    }else
    return false
}

console.log("ES: 1: " + isTrue("y"))

// ES. 2

function isSQRT(num){
    return Math.sqrt(num)
}

console.log("ES: 2: " + isSQRT(55))

// ES. 3 

function StringToArray(){
    pers = 'Pietro, Marco, Luca'
    pers = pers.replace(/ /g,'')
    return pers.split(',')
}
console.log("ES: 3: " + StringToArray())

// ES. 4 
var array = ["A","B","N","N","B","L"];

function removeDuplicates(array) {
    var unique = [];
    for(i=0; i < array.length; i++){  
        if(unique.indexOf(array[i]) === -1) {  
            unique.push(array[i]);  
        }  
    }
    return unique;
}
console.log("ES: 4: " + removeDuplicates(array));

// ES. 5

var arr = [1,3,5,8,9,8,7];
var num = 8

function findNum(arr){
    return arr.indexOf(num)
}
console.log("ES: 5: " + findNum(arr));

// ES. 6

var arr = [1,3,5,8,9,8,7];
var num = 8

function findMin(arr){
    num = arr.sort()
    min = arr[0]
    max = arr[arr.length-1]
    return min
}

function findMax(arr){
    num = arr.sort()
    max = arr[arr.length-1]
    return max
}

console.log("ES: 6: " + findMin(arr),findMax(arr));

// ES. 7

var arr1 = [1,3,5,8,9,8,7];
var arr2 = [5,8,7,8,8,9,6];
var arr3 = [];

function uniqueArray(){
    for(let i=0;i<arr1.length;i++){
        if(arr3.indexOf(arr1[i]) == -1)
        arr3.push(arr1[i])
      }

    for(let i=0;i<arr2.length;i++){
        if(arr3.indexOf(arr2[i]) == -1)
        arr3.push(arr2[i])
      }

    return arr3.sort();
}
console.log("ES: 7: " + uniqueArray());

//ES. 8
var arr = [3,2,5,1,4];

function toSort(){
    return arr.sort();
}
console.log("ES: 8: " + toSort());

//ES. 9

function myMail(){
    var email = "matt.giuriato@gmail.com";
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
          
    if (email.match(validRegex)) {
        return true;
    }
    else{
        return false;
    }
            
}
console.log("ES: 9: " + myMail());

//ES. 10

str = "Ciao bello!"
function reverseString(str){
    var splitString = str.split("");
    var reverseArray = splitString.reverse();
    var joinArray = reverseArray.join("");

    return joinArray;
}
console.log("ES: 10: " + reverseString(str));

//ES. 11

num = 123456

function reverseNum(num) {
    num = num.toString();
    var splitString = num.split("");
    var reverseArray = splitString.reverse();
    var joinArray = reverseArray.join("");

    return joinArray;
}

console.log("ES: 11: " + reverseNum(num));
