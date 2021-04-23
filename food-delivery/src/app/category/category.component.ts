import { HttpRequest, HttpResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Product } from '../models';
import { PRODUCTS } from '../products';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit {

  // products = products;
  products : Product[] = [];
  category! : string;
  PRODUCTS = PRODUCTS;

  constructor(
    private route: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    this.getProducts();
  }
  getProducts() {
    this.category = this.router.url.split("/")[this.router.url.split("/").length-1];
    // console.log(this.category);
    this.products = this.PRODUCTS.filter((x) => x.category === this.category);
  }

}
