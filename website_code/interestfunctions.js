/**
 * Returns the amount plus interest earnt over a given number of payments, given AER rate and a number of yearly payments
 * @param {*} aer - Annual Equivalent interest rate, as a percentage (e.g. 5%)
 * @param {*} payments - Number of payments made (i.e. days until account matures)
 * @param {*} yearlyPayments - Number of payments that would be made in a year (usually 365)
 * @returns 
 */
function interest(aer, payments, yearlyPayments){
  return (aer/100 + 1)**(payments/yearlyPayments);
}

/**
 * Returns the new expected return value for an account given its original value, AER, days left in year and a new amount added to the account
 * @param {*} currentReturn The amount currently predicted to be in the account when it matures (including interest)
 * @param {*} AER Annual Equivalent interest rate, as a percentage (e.g. 5%)
 * @param {*} daysleftinyear Number of days left until account matures (number of payments)
 * @param {*} amountAdded Amount of money added in this payment
 * @returns 
 */
function addMoney(currentReturn, AER, daysleftinyear, amountAdded){
  return currentReturn + amountAdded * interest(AER, daysleftinyear, 365);
}

/**
 * Returns the new expected return value for an account given its original value, AER, days left in year and an amount removed from the account
 * @param {*} currentReturn The amount currently predicted to be in the account when it matures (including interest)
 * @param {*} AER Annual Equivalent interest rate, as a percentage (e.g. 5%)
 * @param {*} daysleftinyear Number of days left until account matures (number of payments)
 * @param {*} amountAdded Amount of money removed in this payment
 * @returns 
 */
function removeMoney(currentReturn, AER, daysleftinyear, amountRemoved){
  return currentReturn - amountAdded * interest(AER, daysleftinyear, 365);
}