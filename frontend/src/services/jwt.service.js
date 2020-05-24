const ID_ACCESS_TOKEN = 'id_access_token';
const ID_REFRESH_TOKEN = 'id_refresh_token';

export const getToken = (type = ID_ACCESS_TOKEN) => {
  return window.localStorage.getItem(type);
};

export const setToken = ({ access, refresh }) => {
  if (access !== undefined)
    window.localStorage.setItem(ID_ACCESS_TOKEN, access);
  if (refresh !== undefined)
    window.localStorage.setItem(ID_REFRESH_TOKEN, refresh);
};

export const removeToken = () => {
  window.localStorage.removeItem(ID_ACCESS_TOKEN);
  window.localStorage.removeItem(ID_REFRESH_TOKEN);
};

export default {
  ID_ACCESS_TOKEN,
  ID_REFRESH_TOKEN,
  getToken,
  setToken,
  removeToken,
};
