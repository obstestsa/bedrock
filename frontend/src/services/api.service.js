import axios from 'axios';
import JwtService from './jwt.service';

const ApiClient = axios.create({
  baseURL: 'http://localhost:8081',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
  timeout: 10000,
});

const ApiService = {
  setHeader() {
    ApiClient.defaults.headers.common[
      'Authorization'
    ] = `Bearer ${JwtService.getToken()}`;
  },
  get(resource, slug = '') {
    return ApiClient.get(`${resource}/${slug}`);
  },
  post(resource, params) {
    return ApiClient.post(`${resource}`, params);
  },
  update(resource, slug, params) {
    return ApiClient.put(`${resource}/${slug}`, params);
  },
  put(resource, params) {
    return ApiClient.put(`${resource}`, params);
  },
  delete(resource) {
    return ApiClient.delete(`${resource}`);
  },
};

export default ApiService;
