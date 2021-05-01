import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ProductService } from '../_services/product.service';
import { CategoryService } from '../category.service';
import { Category, Product} from '../models';
import { NgModel } from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  categories : Category[] = [];
  products : Product[] = [];

  constructor(private categoryService: CategoryService,
    private router: Router) { }

  ngOnInit(): void {
    this.getCategories();
    
  }
  getCategories() {
    this.categoryService.getCategories().subscribe((data) => {
      this.products = data;
    });
  }

  addProduct(title:NgModel, price: NgModel, cat: NgModel) {
    console.log(title);
    console.log(price);
    console.log(cat);
  }
  
}
