// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Determines how long it takes to prepare a certain juice.
 *
 * @param {string} name
 * @returns {number} time in minutes
 */
export function timeToMixJuice(name) {
  switch(name){
    case 'Pure Strawberry Joy':
      return .5
    case 'Energizer':
      return 1.5
    case 'Green Garden':
      return 1.5
    case 'Tropical Island':
      return 3
    case 'All or Nothing':
      return 5
    default:
      return 2.5
  };
}

/**
 * Calculates the number of limes that need to be cut
 * to reach a certain supply.
 *
 * @param {number} wedgesNeeded
 * @param {string[]} limes
 * @returns {number} number of limes cut
 */
export function limesToCut(wedgesNeeded, limes) {
  var totalCut = 0;
  var totalLimes = 0;
  while (totalCut < wedgesNeeded && limes.length > 0) {  
    if(limes[0] === 'small'){
      totalCut += 6;
    } 
    else if(limes[0] === 'medium'){
      totalCut += 8;
    }
    else if(limes[0] === 'large'){
      totalCut += 10;
  }
    totalLimes += 1;
    limes.shift();
  }
  return totalLimes
}

/**
 * Determines which juices still need to be prepared after the end of the shift.
 *
 * @param {number} timeLeft
 * @param {string[]} orders
 * @returns {string[]} remaining orders after the time is up
 */
export function remainingOrders(timeLeft, orders) {
  var clockingOut = timeLeft;
  while(clockingOut > 0){
    if (orders.length === 0){
      return [];
    } else{
    let orderTime = 0;
    orderTime = timeToMixJuice(orders[0]);
    clockingOut -= orderTime;
    orders.shift();}
  }
  return orders;
}
