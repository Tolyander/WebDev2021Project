import { Component, OnInit } from '@angular/core';
import { NgModel } from '@angular/forms';
import { Category, Product } from '../models';
import { ProductComponent } from '../product/product.component';
import { CATEGORIES, PRODUCTS } from '../products';
import { ProductService } from '../_services/product.service';

export class Phone {
  constructor(public title: string, 
              public price: number, 
              public company: string)
  { }
}

@Component({
  selector: 'app-add-product',
  templateUrl: './add-product.component.html',
  styleUrls: ['./add-product.component.css']
})
export class AddProductComponent implements OnInit {

  // categories : Category[] = [];
  // products : Product[] = [];

  phone: Phone = new Phone("", 0, "");
    companies: string[] = ["Apple", "Huawei", "Xiaomi", "Samsung", "LG", "Motorola", "Alcatel"];
     
    addPhone(title:NgModel, price: NgModel, comp: NgModel){
        console.log(title);
        console.log(price);
        console.log(comp);
    }
  

  constructor(private productService: ProductService) { }

  ngOnInit(): void {
    // this.categories = CATEGORIES;
    // this.products = PRODUCTS;
  }


}
