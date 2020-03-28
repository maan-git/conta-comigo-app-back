import axios from 'axios';

const apiUrl = 'https://reqres.in/api/';

export default () => axios.create({
  baseURL: apiUrl,
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});
