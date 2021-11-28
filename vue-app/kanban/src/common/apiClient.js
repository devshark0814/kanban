import $axios from "axios";

const apiClient = $axios.create({
    baseURL: 'http://localhost:3000',
    headers: { 'Content-Type': 'application/json' },
    timeout: 5000, // milliseconds
});

export default apiClient;