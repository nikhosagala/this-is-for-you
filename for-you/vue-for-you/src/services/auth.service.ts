import axios from 'axios';
import { BaseService } from './base.service';

class AuthService extends BaseService {
    constructor() {
        super();
    }

    register(email: string, password: string) {
        const data = {
            "email": email,
            "password": password
        };
        return this.service.post('/users/', data);
    }

    login(email: string, password: string) {
        const data = {
            "email": email,
            "password": password
        };
        return this.service.post('/auth/login', data);
    }

    getProfile() {
        const token = this.getToken();
        return this.service.get('/users/me/');
    }

    setToken(token: string) {
        localStorage.setItem(this.authKey, token);
    }

    getToken() {
        return localStorage.getItem(this.authKey);
    }

    removeToken() {
        localStorage.removeItem(this.authKey);
    }
}

export const authService = new AuthService();
