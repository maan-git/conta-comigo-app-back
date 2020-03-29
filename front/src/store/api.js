import axios from 'axios';

// const apiUrl = 'https://reqres.in/api/';
const apiUrl = 'https://conta-comigo-ap.herokuapp.com/app/';

export default () => axios.create({
  baseURL: apiUrl,
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});
