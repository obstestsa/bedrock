module.exports = {
  transpileDependencies: ['vuetify'],
  // Proxy conifg for api server
  devServer: {
    proxy: {
      '^/api/': {
        target: 'http://localhost:8081/',
      },
    },
  },
  // outputDir must be added to Django's TEMPLATE_DIRS
  outputDir: './dist/',
  // assetsDir must match Django's STATIC_URL
  assetsDir: 'static',
};
