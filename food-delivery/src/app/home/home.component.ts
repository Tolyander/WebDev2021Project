import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ProductService } from '../service/product.service';

import { CATEGORIES, PRODUCTS } from '../products';
import { Category, Product } from '../models';
import { NgModel } from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  categories : Category[] = [];
  products : Product[] = [];

  constructor(private productService: ProductService,
    private router: Router) { }

    
  // надо подключить бд
  ngOnInit(): void {
    this.categories = CATEGORIES;
    this.products = PRODUCTS;
    // this.getProducts();
  // }
  // getProducts() {
  //   this.productService.getAllProducts()
  //     .subscribe(products => this.products = products);
    
  // }
  }
  addProduct(title:NgModel, price: NgModel, cat: NgModel) {
    console.log(title);
    console.log(price);
    console.log(cat);
  }
  
}

// this.productService.getAllProducts().subscribe((prods: {count: Number, products: any[]}) => {
//   this.products = prods.products;
//   console.log(this.products);
// }); 

// selectProduct(id: Number) {
//   this.router.navigate(['/product', id]).then();
// }