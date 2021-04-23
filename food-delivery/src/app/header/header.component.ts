import { Component, OnInit } from '@angular/core';
import { NgModel } from '@angular/forms';
import { Category, Product } from '../models';
import { CATEGORIES, PRODUCTS } from '../products';
import { ProductService } from '../service/product.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  categories : Category[] = [];
  products : Product[] = [];

  constructor() { }

  ngOnInit(): void {
    this.categories = CATEGORIES;
    this.products = PRODUCTS;
  }

  addProduct(title:NgModel, price: NgModel, cat: NgModel) {
    console.log(title);
    console.log(price);
    console.log(cat);
  }

}
