import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from '../_services/authentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  logged = false;
  username = '';
  password = '';


  constructor(private authenticationService: AuthenticationService) {}

  login(){
    this.authenticationService.login(this.username, this.password).subscribe((data) => {
      // console.log(data);

      localStorage.setItem('token', data.token);

      this.logged = true;

      this.username = '';
      this.password = '';
    });
  }

  logout(){
    this.logged = false;
    localStorage.removeItem('token');
  }

  ngOnInit(): void {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
  }
}
