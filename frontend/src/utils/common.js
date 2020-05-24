/**
 * Utitlity function that return the color based on status
 * @param {string} status
 */
export function getStatusColor(status) {
  if (status === 'ACTIVE') return 'green';
  else if (status === 'INACTIVE') return 'orange';
  else return 'red';
}
