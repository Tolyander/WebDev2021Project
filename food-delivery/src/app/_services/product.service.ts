import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { ProductModelServer, serverResponse } from '../models/product.model';
import { PRODUCTS } from '../products';
import { AuthToken, Phone, Category, Product} from '../models';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  products = PRODUCTS

  private SERVER_URL = environment.SERVER_URL;
  constructor(private http: HttpClient,
    private router: Router
     ) { }

  getProducts(category:string): Observable<Product[]>{
    return this.http.get<Product[]>(`${this.SERVER_URL}/category/${category}`);
  }

  getProduct(category:string, product_id:number): Observable<Product>{
    return this.http.get<Product>(`${this.SERVER_URL}/categories/${category}/${product_id}`);
  }
}