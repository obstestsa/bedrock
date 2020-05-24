import axios from 'axios';
import JwtService from './jwt.service';

const ApiClient = axios.create({
  baseURL: '/api',
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
    return ApiClient.get(`${resource}/${slug}`, {
      headers: {
        Authorization: '',
      },
    });
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

export const SorApiService = {
  get(resource, slug = '') {
    return ApiService.get(`sor/${resource}`, slug);
  },
  post(resource, params) {
    return ApiService.post(`sor/${resource}`, params);
  },
  update(resource, slug, params) {
    return ApiService.put(`sor/${resource}/${slug}`, params);
  },
  put(resource, params) {
    return ApiService.put(`sor/${resource}`, params);
  },
  delete(resource) {
    return ApiService.delete(`sor/${resource}`);
  },
};
