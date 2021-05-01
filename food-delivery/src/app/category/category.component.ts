import { HttpRequest, HttpResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Product } from '../models';
import { CategoryService } from '../category.service';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit {

  // products = products;
  products : Product[] = [];
  products1 : Product[] = [];
  category! : string;

  constructor(
    private categoryService: CategoryService,
    private route: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    this.getProducts();
  }

  getProducts() {
    this.category = this.router.url.split("/")[this.router.url.split("/").length-1];
    if (this.category === "laptops"){
      this.categoryService.getCategories2().subscribe((data) => {
        this.products = data;
      });
    } else if(this.category === "phones"){
      this.categoryService.getCategories3().subscribe((data) => {
        this.products = data;
      });
    } else if(this.category === "accessories"){
      this.categoryService.getCategories4().subscribe((data) => {
        this.products = data;
      });
    }
  }

}
