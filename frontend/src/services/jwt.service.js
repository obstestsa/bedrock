const ID_TOKEN_KEY = 'id_access_token';

export const getToken = () => {
  return window.localStorage.getItem(ID_TOKEN_KEY);
};

export const setToken = token => {
  window.localStorage.setItem(ID_TOKEN_KEY, token);
};

export const removeToken = () => {
  window.localStorage.removeItem(ID_TOKEN_KEY);
};

export default {
  getToken,
  setToken,
  removeToken,
};
