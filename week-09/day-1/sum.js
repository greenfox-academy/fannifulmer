// Create a sum method in your class which has a list of integers as parameter
// It should return the sum of the elements in the list
// Follow these steps:
// Add a new test case
// Instantiate your class
// create a list of integers
// use the t.equal to test the result of the created sum method
// Run it
// Create different tests where you
// test your method with an empyt list
// with a list with one element in it
// with multiple elements in it
// with a null
// with a string
// Run them
// Fix your code if needed


// var counter = {
//     sum: 0,
//     
//     sumAdder: function(numberArray){
//         for (var i = 0; i < numberArray.length; i++){
//             this.sum += numberArray[i];
//         }
//         return this.sum;
//     }
// }
// 
// // counter.sumAdder([1, 2]);



var counter = function() {
    this.sum = 0;
    
    this.sumAdder = function(numberArray){
        for (var i = 0; i < numberArray.length; i++){
            if (typeof numberArray[i] === 'number'){
            this.sum += numberArray[i];
            } else {
            return 'The list should only contain numbers'
            }
        }
        return this.sum;
    }
}

module.exports = counter;

var obj = new counter();
console.log(obj.sumAdder([2, 5]));

