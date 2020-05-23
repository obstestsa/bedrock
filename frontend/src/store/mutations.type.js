// common mutation types
export const FETCH_PENDING = 'fetchPending';
export const RESET_STATE = 'resetModuleState';
export const SET_ERROR = 'setError';

// sor mutation types
export const SET_RESOURCES = 'setResources';
export const SET_RESOURCE = 'setResource';
export const RESOURCE_ADD = 'addResource';
export const RESOURCE_EDIT = 'editResource';
export const RESOURCE_REMOVE = 'removeResource';

// snack bar mutation types
export const SET_SNACKBAR = 'setSnackBar';

// auth mutation types
export const SET_AUTH = 'setUser';
export const PURGE_AUTH = 'logOut';

export default {
  FETCH_PENDING,
  RESET_STATE,
  SET_ERROR,
  SET_RESOURCES,
  SET_RESOURCE,
  RESOURCE_ADD,
  RESOURCE_EDIT,
  RESOURCE_REMOVE,
  SET_SNACKBAR,
  SET_AUTH,
  PURGE_AUTH,
};
