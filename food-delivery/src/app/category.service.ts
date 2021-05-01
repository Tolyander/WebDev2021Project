import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Category, Product} from './models';

@Injectable({
  providedIn: 'root'
})
export class CategoryService {

  BASE_URL = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  getCategories(): Observable <Product[]>{
    return this.http.get<Product[]>(`${this.BASE_URL}/api/products/`);
  }

  getCategories2(): Observable <Product[]>{
    return this.http.get<Product[]>(`${this.BASE_URL}/api/products/laptop/`);
  }

  getCategories3(): Observable <Product[]>{
    return this.http.get<Product[]>(`${this.BASE_URL}/api/products/phone/`);
  }

  getCategories4(): Observable <Product[]>{
    return this.http.get<Product[]>(`${this.BASE_URL}/api/products/accessory/`);
  }
}
