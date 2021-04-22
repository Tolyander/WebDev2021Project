import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ProductService } from '../service/product.service';

import { products } from '../products';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  products = products;

  constructor(private productService: ProductService,
    private router: Router) { }

    
  // надо подключить бд
  ngOnInit(): void {
    // this.getProducts();
  // }
  // getProducts() {
  //   this.productService.getAllProducts()
  //     .subscribe(products => this.products = products);
    
  // }
  }

  
}

// this.productService.getAllProducts().subscribe((prods: {count: Number, products: any[]}) => {
//   this.products = prods.products;
//   console.log(this.products);
// }); 

// selectProduct(id: Number) {
//   this.router.navigate(['/product', id]).then();
// }