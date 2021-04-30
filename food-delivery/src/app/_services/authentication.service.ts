import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { AuthToken } from '../models';
import { User } from '../models/user.model';
import { map } from "rxjs/operators";

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  SERVER_URL = 'http://localhost:8000';

  constructor(private http: HttpClient) { 

  }

  login(username: any, password: any): Observable<AuthToken> {
    return this.http.post<AuthToken>(`${this.SERVER_URL}/api/login/`, {
      username,
      password
    });
  }
  
}

