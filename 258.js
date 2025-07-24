var addDigits = function(num) {
let total = num.toString().split('').map(Number);
let sum = 0;
let finalvalue = 0;
var lastvalue = 0
for(let i=0;i<total.length;i++){
   sum += total[i]
}

let sumsplit = sum.toString().split('').map(Number);
for(let i=0;i<sumsplit.length;i++){
   finalvalue += sumsplit[i]
}

if(finalvalue.toString().length > 1){
let finalvaluesplit = finalvalue.toString().split('').map(Number);
   for(let i=0;i<finalvaluesplit.length;i++){
   lastvalue += finalvaluesplit[i];
}
return lastvalue
}
return finalvalue
};


