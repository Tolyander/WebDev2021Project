import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class OrderService {

  // private products: ProductRespo[] = [];
  // private serverURL = environment.SERVER_URL;

  constructor(private http: HttpClient) { 
    // getSingleOrder(orderId: Number) {
    //   return this.http.get<ProductResponseModel[]>(`${this.serverURL}orders/${orderId}`).toPromise();
    // }
  }
}
