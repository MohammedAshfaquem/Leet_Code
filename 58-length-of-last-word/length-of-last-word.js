/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    const arrayword = s.trim().split(' ');
    const lastword = arrayword[arrayword.length -1].length
   return lastword
};
