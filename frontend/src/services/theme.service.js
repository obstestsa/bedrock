const ID_THEME_KEY = 'id_dark_theme';

export const getDarkTheme = () => {
  return window.localStorage.getItem(ID_THEME_KEY);
};

export const setDarkTheme = dark => {
  window.localStorage.setItem(ID_THEME_KEY, dark);
};

export default {
  getDarkTheme,
  setDarkTheme,
};
