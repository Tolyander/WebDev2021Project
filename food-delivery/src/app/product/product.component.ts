import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { PRODUCTS } from '../products';
import { CartService } from '../_services/cart.service';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {
  products: any;

  constructor(
    private route: ActivatedRoute,
    private cartService: CartService
  ) { }

  // addToCart(product: any) {
  //   this.cartService.addToCart(product);
  //   window.alert('Your product has been added to the cart!');
  // }

  ngOnInit(): void {
    const routeParams = this.route.snapshot.paramMap;
    // console.log(routeParams);
    const productIdFromRoute = Number(routeParams.get('productId'));
    this.products = PRODUCTS.find(product => product.id === productIdFromRoute);
  }

    // tslint:disable-next-line:typedef
  shareTelegram(url: string, name: string) {
    const l = 'https://t.me/share/url?url=' + url + '&text='  + name;
    window.open(l, '_blank');
  }
  // <a href="https://www.facebook.com/sharer/sharer.php?u=#url" target="_blank">Share</a>
  shareFacebook(url: string, name: string) {
    const l = 'https://www.facebook.com/sharer/sharer.php?u=' + url + '&text='  + name;
    window.open(l, '_blank');
  }

  // http://twitter.com/share?text=text goes here&url=http://url goes here&hashtags=hashtag1,hashtag2,hashtag3
  shareTwitter(url: string, name: string) {
    const l = '"https://twitter.com/intent/tweet?url=' + url + '&text='  + name;
    window.open(l, '_blank');
  }
  
  shareOnGoogle(url: string){
    var url = "https://plus.google.com/share?url=" + url;
    window.open(url, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=550,width=780');
    return false;
}

}
