import axios, { AxiosInstance } from 'axios';

export class BaseService {
    api: string;
    service: AxiosInstance;
    protected authKey = "auth.token";

    constructor() {
        this.api = "/api";

        if (process.env.NODE_ENV === 'development') {
            this.api = "/api";
        }
        this.service = axios.create({
            baseURL: this.api,
            headers: this.buildHeaders()
        });
        console.log('creating base service for api:', this.api);
    }

    public isLoggedIn(): boolean {
        return !!localStorage.getItem(this.authKey);
    }

    protected buildHeaders() {
        let h = {};
        if (this.isLoggedIn()) {
            const currentToken = localStorage.getItem(this.authKey);
            h = { "Authorization": `JWT ${currentToken}` };
        }
        return h;
    }
}
