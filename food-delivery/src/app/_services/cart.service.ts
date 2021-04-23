import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { PRODUCTS } from '../products';
import { ProductService } from './product.service';

@Injectable({
  providedIn: 'root'
})
export class CartService {
  items = [];
  products = PRODUCTS;

  constructor(private http: HttpClient,
    private router: Router,
    private productService: ProductService) { }

}